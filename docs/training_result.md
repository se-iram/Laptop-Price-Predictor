## Models & Results

### 1. Linear Regression

**Results:**
- **R² Score:** `0.8247`  
- **Mean Absolute Error (MAE):** `0.1991`  

**🔎 Analysis**
- The model explains about **82.5% of the variance** in laptop prices.  
- Predictions deviate on average by about **0.20 units**.  
- While performance is fairly good, **Linear Regression may not fully capture complex, non-linear relationships** in the dataset.  

---

### 2. Random Forest Regression

#### First Attempt (Default/Initial Parameters)

**Results:**
- **Training R² Score:** `0.9076`  
- **MAE:** `0.1454`  
- **Cross-Validation R² Scores:** `[0.8546, 0.9097, 0.8924, 0.8291, 0.8718]`  
- **Average CV R²:** `0.8715`  

---

#### Hyperparameter-Tuned Version (Best parameters by RandomizedSearchCV)

**Results:**
- **Training R² Score:** `0.9135`  
- **MAE:** `0.1368`  
- **Cross-Validation R² Scores:** `[0.8547, 0.9102, 0.8969, 0.8365, 0.8799]`  
- **Average CV R²:** `0.8756`  

---

**🔎 Analysis**
- **Random Forest outperforms Linear Regression** in both R² and MAE.  
- The **tuned version** improves slightly over the default, showing **better generalization across folds**.  
- Predictions are more accurate (**lower MAE**), indicating the model effectively captures laptop pricing patterns.  
- Cross-validation results are **stable**, confirming robustness.  

---

## 4. Conclusion
- Linear Regression serves as a solid **baseline** model.  
- Random Forest demonstrates **superior performance**, both in accuracy and robustness.  
- Future work may include:
  - Testing other ensemble methods (e.g., Gradient Boosting, XGBoost).  
  - Incorporating additional feature engineering for improved accuracy.  

---