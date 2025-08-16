# Plan Phase

This document captures the decisions made in the **Plan** stage of the PACE workflow for the *Laptop Price Prediction* project.

---

## 1) What is the purpose of this model?
The goal is to develop a machine learning model that predicts laptop prices based on hardware and configuration attributes (e.g., RAM, CPU type, storage, display size, GPU). This will help users estimate the expected cost of a laptop before purchase and support sellers, e-commerce platforms, and manufacturers in price benchmarking.

---

## 2) How will its predictions be used?
- **Consumers:** to estimate whether a laptop with specific specifications fits within their budget. 
- **Retailers & E-commerce platforms:** to benchmark prices of new or existing stock, ensuring competitive pricing strategies. 
- **Manufacturers:** to analyze market alignment of their pricing concerning hardware features.

---

## 3) Who is affected?
- **End-users (buyers)**: students, professionals, general consumers.
- **Retailers & e-commerce platforms**: listing and selling laptops.
- **Manufacturers (indirectly)**: pricing insights can influence demand and perception.

---

## 4) How significant could the effects be?
**Positive impacts**
Provides transparency for buyers, competitive advantage for sellers, and improved decision-making for inventory managers.

**Potential risks**
Misleading predictions due to outdated or biased data may negatively influence buyer decisions or seller pricing strategies.

---

## 5) What types of results are needed?
The model should output a continuous numerical value representing the predicted price of a laptop given its configuration. Accuracy, interpretability, and generalization ability are important to ensure reliable predictions.

---

## 6) What type of model will you need?
- **Learning paradigm**: **Supervised** (labeled dataset with target = price).
- **Task**: **Regression** (continuous output).
- **Candidate algorithms** (baseline → advanced):
  - Linear Regression / Regularized (Ridge/Lasso/Elastic Net)
  - Decision Tree Regressor
  - Random Forest Regressor
  - Gradient Boosting (XGBoost/LightGBM/CatBoost)
  - SVR (if feature scaling and kernel choice fit)
  - (Optional) Shallow Neural Network for larger datasets

---

## 7) Online Learning or Offline (Batch) Learning?
- **Decision**: **Offline (Batch) Learning** — current dataset is small and relatively static.
- **Plan**: retrain periodically (e.g., monthly/quarterly) or when drift is detected.

---

## 8) Instance-based Learning or Model-based Learning?
- **Decision**: **Model-based Learning** for fast inference and good generalization.
- Rationale: instance-based methods (e.g., KNN) are memory-heavy and slow at prediction time. KNN may be used **only as a sanity-check baseline**.

---

## 9) What tools will be required?
- **Data processing**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`
- **Modeling**: `scikit-learn` (baselines), `XGBoost`/`LightGBM` (boosting)
- **Web app**: `Streamlit`
- **Deployment**: `Heroku` (alternatives: AWS/GCP/Azure)
- **Versioning & docs**: `Git/GitHub`, Markdown docs

---

## (Optional) Success metrics & acceptance criteria
- **Primary metric**: RMSE (target: ≤ 15% of the median price; refine after baseline).
- **Secondary**: MAE, MAPE (for interpretability), and R².
- **Operational**: P95 latency of prediction ≤ 200 ms in the web app.

---

## Decisions Summary (Plan Phase)

| Topic                                    | Decision                             |
|------------------------------------------|--------------------------------------|
| Learning approach                         | **Offline (Batch)**                  |
| Learning method                           | **Model-based**                      |
| ML paradigm                               | **Supervised**                       |
| Task type                                 | **Regression**                       |
| Output                                    | **Numeric price**                    |
| Algorithms                                | Linear/Ridge/Lasso → RF/GBM/XGB/LGBM |
| Tooling                                   | pandas, numpy, sklearn, XGBoost/LGBM, matplotlib/seaborn, Streamlit, Heroku |
---
