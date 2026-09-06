# 🌍 AI-Powered Disaster Risk Prediction & Assessment System

An interactive **Machine Learning-based Disaster Risk Assessment Platform** built with Python and Streamlit. The system analyzes disaster-related datasets and provides prediction, risk assessment, historical analysis, interactive visualizations, and ML model insights.

The platform is designed to help users understand the potential disaster risks associated with a geographic location using historical and geographic information.

## 🚀 Live Demo

👉 **[Open the LIVE DEMO](https://drive.google.com/file/d/1K417oEo4Nzf8Ad5dv3-8FD6z0X3aKXWp/view?usp=sharing)**

---

## 📌 Project Overview

Natural disasters such as **earthquakes, floods, and cyclones** can cause significant damage to people, infrastructure, and the environment.

This project uses **Machine Learning, data analysis, and geospatial visualization** to build an interactive disaster intelligence platform.

Users can explore historical disaster data and, where the available data supports it, enter a **latitude and longitude** to obtain a location-based disaster risk assessment.

The system provides:

* 🌍 Location-based risk assessment
* 🌎 Disaster type analysis
* 🚦 LOW / MEDIUM / HIGH risk classification
* 📊 Disaster probability/risk scores
* 🗺️ Interactive geographic visualizations
* 📈 Historical disaster trends
* 🤖 Machine Learning predictions
* 🔍 Model performance comparison
* 💡 Feature importance / explainable AI
* 🛡️ General disaster safety recommendations

---

# ✨ Key Features

## 📍 1. Location-Based Disaster Risk Assessment

Users can provide:

```text
Latitude
Longitude
```

The system analyzes available historical and geographic information associated with the location and estimates relevant disaster risks.

Example:

```text
Location: 28.6139° N, 77.2090° E

Earthquake Risk → HIGH
Flood Risk      → MEDIUM
Cyclone Risk    → LOW

Overall Risk Score → 74/100
```

The exact outputs are generated from the project's available data and ML models rather than hard-coded geographic rules.

---

## 🌋 2. Earthquake Risk Analysis

The earthquake module analyzes earthquake-related data and provides insights based on available features such as:

* Latitude
* Longitude
* Magnitude
* Geographic distribution
* Historical earthquake activity

### Visualizations

* Earthquake distribution map
* Magnitude distribution
* Historical earthquake trends
* Geographic concentration of events

---

## 🌊 3. Flood Risk Prediction

The flood module uses Machine Learning to assess flood risk using relevant environmental and geographic features available in the dataset.

The system provides:

* Flood-risk prediction
* Risk category
* Probability/confidence where supported
* Feature analysis
* Historical trends
* Visualizations

Risk categories:

🟢 **LOW**

🟡 **MEDIUM**

🔴 **HIGH**

---

## 🌀 4. Cyclone Analysis

The cyclone module analyzes historical cyclone data from the Pacific dataset.

It provides:

* Cyclone frequency
* Intensity analysis
* Geographic distribution
* Historical trends
* Year-wise analysis
* Interactive visualizations

---

# 🗺️ 5. Interactive Disaster Map

The application provides geographic visualization of disaster events.

Users can explore:

* Disaster locations
* Severity/intensity
* Geographic concentration
* Historical events
* Selected locations

Interactive features include:

* Zoom
* Pan
* Hover information
* Disaster filtering
* Severity-based analysis

---

# 🤖 6. Machine Learning Models

Multiple Machine Learning algorithms are explored and evaluated.

### Classification Models

* Logistic Regression
* Random Forest
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)
* Gradient Boosting
* XGBoost

### Regression Models

* Random Forest Regressor
* Support Vector Regression (SVR)
* Ridge Regression
* Lasso Regression
* XGBoost Regressor

The best-performing model is selected based on appropriate evaluation metrics rather than assuming one algorithm is always superior.

---

# 🧠 7. Machine Learning Pipeline

The project follows a complete ML workflow:

```text
Raw Disaster Data
        ↓
Data Cleaning
        ↓
Missing Value Handling
        ↓
Outlier Detection
        ↓
Feature Engineering
        ↓
Feature Selection
        ↓
Encoding
        ↓
Feature Scaling
        ↓
Class Imbalance Handling
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Prediction
        ↓
Risk Assessment
        ↓
Interactive Visualization
```

---

# ⚖️ 8. Handling Class Imbalance

For datasets with imbalanced classes, the project uses **SMOTE (Synthetic Minority Over-sampling Technique)** where appropriate.

SMOTE is applied to training data to reduce bias toward majority classes.

Care is taken to avoid data leakage between training and testing data.

---

# 🔧 9. Hyperparameter Optimization

The project uses techniques such as:

* GridSearchCV
* Cross-validation
* Model comparison

to identify suitable model configurations.

---

# 🔍 10. Explainable AI

The project aims to make ML predictions more understandable.

The system can provide insights into important features contributing to a prediction using techniques such as:

* Feature importance
* Permutation importance
* SHAP, where practical

Instead of only displaying:

> "HIGH RISK"

the application attempts to explain:

> "Which factors contributed to this assessment?"

This makes the prediction system more transparent and useful for analysis.

---

# 📊 11. Model Evaluation

Models are evaluated using appropriate metrics.

### Classification Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC
* Confusion Matrix

### Regression Metrics

* MAE
* MSE
* RMSE
* R² Score

Model performance is visualized using charts and comparison tables.

---

# 📈 12. Disaster Analytics

The analytics dashboard provides insights such as:

* Total disaster records
* Disaster distribution
* Average earthquake magnitude
* Maximum magnitude
* Disaster frequency
* Year-wise trends
* Geographic distribution
* Severity distribution

Interactive Plotly visualizations are used wherever appropriate.

---

# 🚦 13. Risk Classification

The platform categorizes assessed risk into three levels:

| Level     | Meaning                                           |
| --------- | ------------------------------------------------- |
| 🟢 LOW    | Relatively lower assessed risk                    |
| 🟡 MEDIUM | Moderate assessed risk requiring awareness        |
| 🔴 HIGH   | Higher assessed risk requiring greater precaution |

Risk categories are derived from the project's model/data methodology and should not be interpreted as official emergency warnings.

---

# 🛡️ 14. Safety Recommendations

Based on the assessed disaster risk, the application can provide general precautionary guidance.

For example:

### High Flood Risk

* Monitor official weather alerts
* Avoid low-lying areas
* Keep emergency supplies ready
* Follow local evacuation instructions

### High Earthquake Risk

* Identify safe areas
* Secure heavy objects
* Keep emergency supplies available
* Follow official emergency guidance

### Cyclone Risk

* Monitor official cyclone warnings
* Secure loose objects
* Stay informed about evacuation instructions
* Keep emergency contacts available

> **Disclaimer:** Safety recommendations provided by this application are general educational guidance and should not replace instructions from official disaster-management authorities.

---

# 📂 Datasets

The project currently works with disaster datasets including:

```text
earthquakeUSCS.csv
flood_risk_dataset_india.csv
pacific.csv
```

### Earthquake Dataset

Used for:

* Earthquake distribution
* Magnitude analysis
* Geographic analysis
* Historical earthquake patterns

### Flood Dataset

Used for:

* Flood-risk prediction
* Classification
* Environmental feature analysis

### Pacific Cyclone Dataset

Used for:

* Cyclone analysis
* Historical cyclone trends
* Geographic visualization
* Intensity analysis

---

# 🛠️ Tech Stack

### Programming Language

🐍 Python

### Machine Learning

* Scikit-learn
* XGBoost
* Imbalanced-learn
* Joblib

### Data Processing

* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib

### Web Application

* Streamlit

### Development

* Git
* GitHub
* VS Code

---


## Project Structure

```text
code8.py                       Streamlit UI, preprocessing, models, and charts
src/location_risk.py           Haversine-based location risk features
code7.py                       Optional XGBoost availability check
earthquakeUSCS.csv             Earthquake data
flood_risk_dataset_india.csv   Flood-risk data
pacific.csv                    Pacific cyclone data
requirements.txt               Python dependencies


> The exact structure may vary depending on the current implementation.

---

# ⚙️ Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Move into the project directory:

```bash
cd Disaster-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

---

# ☁️ Deployment

The application can be deployed using **Streamlit Community Cloud**.

Basic deployment process:

```text
GitHub Repository
        ↓
Streamlit Community Cloud
        ↓
requirements.txt
        ↓
Streamlit Application
        ↓
Live Web App
```

Live application:

👉 **[Launch Disaster Prediction App](YOUR_STREAMLIT_APP_LINK_HERE)**

---

# 🔮 Future Enhancements

Potential future improvements include:

* Real-time weather data integration
* Real-time earthquake feeds
* Real-time cyclone alerts
* Satellite/weather data integration
* Advanced geospatial ML
* SHAP-based explanations
* Automated risk reports
* Location comparison
* Disaster-risk heatmaps
* Mobile-friendly interface
* Real-time notification system
* More disaster categories such as landslides, droughts, and wildfires
* Model monitoring and periodic retraining

---

# 🎯 Project Highlights

This project demonstrates practical experience with:

* Machine Learning
* Classification & Regression
* Feature Engineering
* Data Preprocessing
* SMOTE
* Hyperparameter Tuning
* Cross-validation
* Model Evaluation
* Explainable AI
* Geospatial Analysis
* Interactive Data Visualization
* Streamlit Application Development
* ML Model Deployment

---

# ⚠️ Disclaimer

This application is an **educational and analytical Machine Learning project**.

Its predictions and risk assessments are based on the available historical/geographic data and trained models. They should **not be considered official disaster forecasts, emergency warnings, or replacements for information from government or disaster-management authorities.**

---

# 👩‍💻 Author

**Pragati Pandey**

B.Tech — Computer Science & Information Technology


---

## ⭐ If you find this project useful

Consider giving the repository a ⭐ on GitHub!
