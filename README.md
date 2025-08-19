# Laptop Price Predictor (My personal project)
Live Demo: https://my-laptop-price-predictor.streamlit.app/

**Type:** Web App  
**Purpose:** Predict laptop prices based on hardware and configuration attributes (RAM, CPU, GPU, storage, display, etc.) to help users estimate cost before purchase.

---

## Pipeline

The project follows this pipeline:

1. **Framing the problem**  
2. **Gathering Data**  
3. **Data Cleaning & Preprocessing**  
4. **Exploratory Data Analysis (EDA)**  
5. **Feature Engineering**  
6. **Modeling**  
7. **Cross-validation & Hyperparameter Tuning**  
8. **Model Serving (Website/App)**  
9. **Deployment**  

---
![Image](https://github.com/user-attachments/assets/4d467f4f-7a6a-4966-aa83-d08e56cdffd9)
---
## PACE Workflow

**1. Plan**  
- Framing the problem  
- Gathering Data  

**2. Analyze**  
- Data Cleaning & Preprocessing  
- EDA (Univariate Analysis, Feature Selection, Transformation, Extraction)  

**3. Construction**  
- Modeling (Linear Regression, Random Forest)  
- Cross-validation & Hyperparameter Tuning  

**4. Execute**  
- Model Serving (Web/App)  
- Deployment  
---

## Model Training & Results

**1. Linear Regression (Baseline)**  
- R² Score: 0.8247  
- MAE: 0.1991

**2. Random Forest Regression**  
- **Default Parameters:**  
  - Training R²: 0.9076  
  - MAE: 0.1454  
  - Avg CV R²: 0.8715  

- **Hyperparameter-Tuned:**  
  - Training R²: 0.9135  
  - MAE: 0.1368  
  - Avg CV R²: 0.8756  

**Conclusion:** Random Forest outperforms Linear Regression and provides robust, accurate predictions.

---

## Tools & Libraries

- Python, Streamlit  
- pandas, numpy, scikit-learn, matplotlib, seaborn  
- Random Forest Regressor, Linear Regression, RandomizedSearchCV 
- Deployment: Hugging Face Space (previously Heroku)

---

#### Note: Documentation for each phase can be found in the **doc** directory. 
---
