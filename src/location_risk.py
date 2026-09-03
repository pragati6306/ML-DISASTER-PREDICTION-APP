"""Data-driven location risk features for the available disaster datasets."""

from __future__ import annotations

from typing import Any

import numpy as np
import pandas as pd

SUPPORTED_DISASTERS = ("earthquake", "flood", "cyclone")


def haversine_km(latitude: float, longitude: float, latitudes: pd.Series, longitudes: pd.Series) -> pd.Series:
    """Return great-circle distance from one point to many points in kilometres."""
    earth_radius_km = 6371.0088
    lat1 = np.radians(latitude)
    lon1 = np.radians(longitude)
    lat2 = np.radians(pd.to_numeric(latitudes, errors="coerce"))
    lon2 = np.radians(pd.to_numeric(longitudes, errors="coerce"))
    delta_lat = lat2 - lat1
    delta_lon = lon2 - lon1
    haversine = np.sin(delta_lat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(delta_lon / 2) ** 2
    return pd.Series(2 * earth_radius_km * np.arcsin(np.sqrt(np.clip(haversine, 0, 1))), index=latitudes.index)


def _historical_score(events: pd.DataFrame, total_records: int, radius_km: float) -> float:
    """Score observed local activity relative to the loaded dataset, not a fixed map lookup."""
    if events.empty or total_records == 0:
        return 0.0
    count_signal = min(len(events) / max(total_records * 0.02, 1), 1.0)
    intensity = pd.to_numeric(events["mag"], errors="coerce").dropna()
    if intensity.empty:
        intensity_signal = 0.0
    else:
        global_min = float(pd.to_numeric(events["mag"], errors="coerce").min())
        global_max = float(pd.to_numeric(events["mag"], errors="coerce").max())
        intensity_signal = (float(intensity.mean()) - global_min) / max(global_max - global_min, 1e-9)
    distance_signal = float(np.exp(-float(events["distance_km"].min()) / max(radius_km, 1)))
    return round(float(100 * (0.45 * count_signal + 0.35 * intensity_signal + 0.20 * distance_signal)), 1)


def extract_location_features(
    latitude: float,
    longitude: float,
    datasets: dict[str, pd.DataFrame],
    radius_km: float = 100.0,
) -> dict[str, Any]:
    """Extract nearby historical features for each supported disaster type."""
    features: dict[str, Any] = {
        "latitude": float(latitude),
        "longitude": float(longitude),
        "radius_km": float(radius_km),
        "disasters": {},
    }
    for disaster in SUPPORTED_DISASTERS:
        dataset = datasets.get(disaster, pd.DataFrame()).copy()
        required = {"latitude", "longitude", "mag"}
        if dataset.empty or not required.issubset(dataset.columns):
            features["disasters"][disaster] = {
                "available": False,
                "event_count": 0,
                "risk_score": 0.0,
                "nearest_event_km": None,
                "average_intensity": None,
                "maximum_intensity": None,
                "events": pd.DataFrame(),
            }
            continue
        dataset["distance_km"] = haversine_km(latitude, longitude, dataset["latitude"], dataset["longitude"])
        nearby = dataset[dataset["distance_km"] <= radius_km].sort_values("distance_km").copy()
        intensities = pd.to_numeric(nearby["mag"], errors="coerce").dropna()
        features["disasters"][disaster] = {
            "available": True,
            "event_count": int(len(nearby)),
            "risk_score": _historical_score(nearby, len(dataset), radius_km),
            "nearest_event_km": round(float(nearby["distance_km"].min()), 1) if not nearby.empty else None,
            "average_intensity": round(float(intensities.mean()), 2) if not intensities.empty else None,
            "maximum_intensity": round(float(intensities.max()), 2) if not intensities.empty else None,
            "events": nearby,
        }
    return features


def predict_disaster_risk(
    latitude: float,
    longitude: float,
    datasets: dict[str, pd.DataFrame],
    radius_km: float = 100.0,
    model_probabilities: dict[str, float] | None = None,
) -> dict[str, Any]:
    """Assess location risk from historical evidence and optional fitted model probabilities."""
    result = extract_location_features(latitude, longitude, datasets, radius_km)
    risks: dict[str, dict[str, Any]] = {}
    for disaster, details in result["disasters"].items():
        historical_score = float(details["risk_score"])
        model_score = None if model_probabilities is None else model_probabilities.get(disaster)
        if model_score is None:
            score = historical_score
            source = "historical evidence"
        else:
            score = round(0.6 * historical_score + 0.4 * float(model_score) * 100, 1)
            source = "historical evidence + fitted classifier probability"
        severity = "HIGH" if score >= 70 else "MEDIUM" if score >= 40 else "LOW"
        risks[disaster] = {**details, "risk_score": score, "severity": severity, "evidence_source": source}
    scores = [item["risk_score"] for item in risks.values()]
    overall_score = round(float(100 * (1 - np.prod([1 - score / 100 for score in scores]))), 1) if scores else 0.0
    result["risks"] = risks
    result["overall_score"] = overall_score
    result["overall_level"] = "HIGH" if overall_score >= 70 else "MEDIUM" if overall_score >= 40 else "LOW"
    result["historical_event_count"] = sum(item["event_count"] for item in risks.values())
    nearest = [item["nearest_event_km"] for item in risks.values() if item["nearest_event_km"] is not None]
    result["nearest_event_km"] = min(nearest) if nearest else None
    return result
