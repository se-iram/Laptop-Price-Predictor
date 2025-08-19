# Analysis Phase Documentation

This document describes the **data cleaning, preprocessing, exploratory data analysis (EDA), and feature engineering** steps performed during the analysis phase of the **Laptop Price Predictor** project.  
The goal of this phase is to prepare high-quality features that can effectively predict laptop prices.

---

## 1. Data Cleaning & Preprocessing

- Dropped unnecessary column: **`Unnamed`**.  
- Removed string units (`"GB"`, `"kg"`) from **RAM** and **Weight** columns.  
- Converted these columns to **numeric** data types.  
- Cleaned inconsistent text data and standardized formats for further analysis.  

**The dataset is now consistent, numeric where necessary, and ready for analysis.**

---

## 2. Exploratory Data Analysis (EDA)

### 2.1 Univariate Analysis (Categorical)

#### Company
- Most laptops are from **Dell, Lenovo, and HP**.  
- Premium brands (**Razer, LG, Google, Microsoft, Samsung**) show significantly higher average prices.  
**Conclusion:** Brand is an important factor in laptop pricing.

#### TypeName
- **Workstations** are the most expensive, though less frequent.  
- **Notebooks** dominate the dataset and represent mid-range prices.  
- **Gaming laptops** and **Ultrabooks** are also costly compared to notebooks.  
**Conclusion:** Laptop type strongly influences cost.

---

### 2.2 Numerical Features

#### Screen Size (Inches)
- Larger screens tend to have higher prices.  
- Medium-sized laptops (~13–15 inches) show similar price ranges.  
**Conclusion:** Screen size affects price, but the correlation is not very strong.

#### Price Distribution
- Target variable (Price) was **skewed**.  
- Applied **log transformation** to stabilize distribution and improve model performance.

---

## 3. Feature Engineering

### 3.1 ScreenResolution
- Extracted hidden details:
  - **TouchScreen** (binary)
  - **IPS Panel** (binary)
  - **X_res** and **Y_res** (resolution dimensions)
- Constructed new feature:
  - **PPI (Pixels Per Inch)** = function of resolution and screen size  
**Conclusion:** PPI better represents screen quality, so we dropped `ScreenResolution`, `X_res`, `Y_res`, and `Inches`.

### 3.2 CPU
- Original `CPU` column had 118 unique strings.  
- Created meaningful features:
  - **CpuBrand** (Intel i3/i5/i7, Celeron, AMD, etc.)  
  - **CpuSpeed (GHz)**  
**Conclusion:** Both CPU brand and speed are significant price predictors.

### 3.3 RAM
- Clear **positive correlation** with price → more RAM = higher price.  

### 3.4 Memory (Storage)
- Raw `Memory` column was messy.  
- Extracted into **HDD, SSD, Hybrid, Flash** (GB only).  
- Observations:
  - **SSD** shows a strong positive correlation (0.67).  
  - **HDD** weak negative correlation (−0.09).  
  - **Hybrid** and **Flash** negligible effect.  
Used **SSD and HDD** for modeling, dropped Hybrid and Flash.

### 3.5 GPU
- Extracted **GpuBrand**.  
- GPU brand shows clear influence on price (premium GPUs → higher prices).  

### 3.6 Operating System (OpSys)
- Reduced categories into 3 groups:
  - **Windows**
  - **MacOS**
  - **Other OS** (Linux, Chrome, No OS, etc.)  

### 3.7 Weight
- Weak positive correlation: heavier laptops are slightly more expensive.

---

## 4. Key Insights

1. **Brand, TypeName, CPU, RAM, SSD, and PPI** are the most influential features for predicting price.  
2. Log transformation on price improves model stability.  
3. Effective **feature engineering** significantly improves the dataset quality by reducing noise and extracting hidden patterns.  

---

At the end of this phase, we obtained a **cleaned, feature-rich dataset** ready for modeling.
