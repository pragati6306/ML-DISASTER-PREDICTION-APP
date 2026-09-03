# Disaster Intelligence Dashboard

A Streamlit-based disaster risk assessment application that combines real earthquake, flood, and Pacific cyclone records with machine-learning classification, regression, interactive geographic visualizations, model comparison, and prediction guidance.

## Highlights

- Schema-aware loading for the three supplied CSV datasets
- Hemisphere-aware parsing of cyclone coordinates such as `20.2N` and `106.3W`
- Coordinate-based disaster-type classification
- Magnitude/intensity regression and risk-level interpretation
- Model comparison for classification and regression
- Interactive Plotly geographic and historical analytics
- Model confidence and fitted-model signal insights
- Joblib/pickle-compatible model persistence through the Streamlit UI
- Clear handling for missing files and unavailable models

## Run Locally

```text
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open `http://localhost:8501` in a browser. Load the data from the sidebar, then train the models. Quick Mode reduces the hyperparameter search for demonstrations.

## Data

The application expects these files beside `app.py`:

- `earthquakeUSCS.csv`: USGS-style earthquake records, including latitude, longitude, and magnitude
- `flood_risk_dataset_india.csv`: Indian flood-risk observations and the `Flood Occurred` target
- `pacific.csv`: Pacific cyclone records with date, location, wind, and pressure fields

Paths are resolved relative to the application file, so launching Streamlit from another working directory is supported.

## Machine Learning Notes

The current shared model uses latitude and longitude as features so it can provide a common coordinate-based demonstration across all disaster types. SMOTE is applied only to the classification training split. The flood dataset does not provide a magnitude field, so the current regression view uses a deterministic 1/5 intensity proxy derived from `Flood Occurred`; this is a demonstration target, not a physical flood-intensity measurement.

Predicted probabilities are model outputs from the selected classifier. Risk labels are heuristic interpretations for demonstration and must not replace official emergency warnings, local authorities, or professional hazard assessments.

## Project Structure

```text
app.py                         Streamlit UI, preprocessing, models, and charts
code7.py                       Optional XGBoost availability check
earthquakeUSCS.csv             Earthquake data
flood_risk_dataset_india.csv   Flood-risk data
pacific.csv                    Pacific cyclone data
requirements.txt               Python dependencies
```

## Future Improvements

- Train separate disaster-specific models using the full feature sets available in each source dataset
- Persist versioned pipelines and evaluation metadata under a dedicated `models/` directory
- Add temporal validation and spatial holdout evaluation
- Add SHAP or permutation explanations for models with suitable feature coverage
- Connect predictions to official warning services only after validating the operational data contract
