🌾 Crop Recommendation System

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

📌 Overview

The Crop Recommendation System is a machine learning project that helps farmers select the most suitable crop based on soil nutrient levels and environmental conditions. By analyzing soil composition (N, P, K), temperature, humidity, pH, and rainfall, the system recommends one of 22 possible crops with high accuracy.

This project compares 9 different classification algorithms and selects the best-performing model for crop prediction.

---

🎯 Problem Statement

Choosing the right crop for a given piece of land is critical for maximizing yield and minimizing crop failure. Farmers often rely on traditional knowledge or trial-and-error methods. This project provides a **data-driven solution** by using machine learning to recommend crops based on scientific parameters.

---

📊 Dataset

The dataset used in this project is available on Kaggle.

Features (7 Inputs)

N - Nitrogen content in soil (mg/kg)
P - Phosphorus content in soil (mg/kg)
K - Potassium content in soil (mg/kg)
temperature - Atmospheric temperature (°C)
humidity - Relative humidity (%)
ph - Soil pH value (pH units)
rainfall - Rainfall amount (mm)

Target (22 Crop Classes)

rice, maize, chickpea, kidneybeans, pigeonpeas, mothbeans, mungbean, blackgram, lentil, pomegranate, banana, mango, grapes, watermelon, muskmelon, apple, orange, papaya, coconut, cotton, jute, coffee

### 📥 Download Dataset

[Click here to download the dataset from Kaggle](https://www.kaggle.com/datasets/ankitakhutwad/crop-recommendation-dataset)

> **Note:** The dataset is not included in this repository due to file size limits. Please download it from the link above and place it in the `data/` folder.

---

🧠 Algorithms Used

The project trains and evaluates 9 different classification algorithms:

| Algorithm | Status |
|-----------|--------|
| Logistic Regression | ✅ |
| Decision Tree Classifier | ✅ |
| AdaBoost Classifier | ✅ |
| Gradient Boosting Classifier | ✅ |
| Random Forest Classifier | ✅ |
| Extra Trees Classifier | ✅ |
| Support Vector Classifier (SVC) | ✅ |
| K-Nearest Neighbors (KNN) | ✅ |
| Gaussian Naive Bayes | ✅ |

Best Performing Model: Random Forest Classifier

---

## 📁 Project Structure
