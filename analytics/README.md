# Analytics — Titanic Survival & Fare Prediction

## Overview

The Analytics module performs exploratory data analysis and predictive modeling on the Titanic dataset.

The module contains:

- Exploratory Data Analysis (EDA)
- Data preprocessing
- Titanic survival classification
- Class imbalance analysis
- Random Forest hyperparameter tuning
- Fare regression
- Model comparison
- Model persistence using Joblib

---

## Dataset

The Titanic dataset is used for this module.

Two dataset files are maintained:

- `titanic.csv` — raw dataset saved as an offline fallback
- `cleaned_titanic.csv` — cleaned dataset used for modeling

The cleaned dataset contains **889 rows and 14 columns**.

The target variable for classification is:

```text
survived
```

The target variable for regression is:

```text
fare
```

---

# Exploratory Data Analysis

EDA is performed in:

```text
01_EDA.ipynb
```

The EDA includes:

- Dataset shape and information
- Descriptive statistics
- Missing-value analysis
- Missing-value percentage calculation
- Missing-value handling based on defined thresholds
- Age distribution analysis
- Fare distribution analysis
- IQR-based outlier detection
- Fare mean, median, and mode
- Fare skewness analysis
- Survival analysis by sex
- Survival analysis by passenger class
- Survival analysis by sex and passenger class
- Correlation analysis
- Correlation heatmap
- Multivariate analysis
- Z-score standardization sanity check

---

## Dataset Cleaning

The original Titanic dataset contained missing values in:

- `age`
- `embarked`
- `deck`
- `embark_town`

The following decisions were made based on the percentage of missing values:

| Column | Missing Percentage | Treatment |
|---|---:|---|
| `age` | 19.87% | Median imputation |
| `embarked` | 0.22% | Drop affected rows |
| `deck` | 77.22% | Drop column |
| `embark_town` | 0.22% | Drop affected rows |

After cleaning:

- Rows: **889**
- Columns: **14**
- Missing values: **0**

The raw Titanic dataset is preserved as:

```text
titanic.csv
```

The cleaned dataset is saved as:

```text
cleaned_titanic.csv
```

---

# Univariate Analysis

Age and Fare distributions were analyzed using histograms and boxplots.

## Age

Using the IQR method:

- Q1 = **22.00**
- Q3 = **35.00**
- IQR = **13.00**
- Lower Bound = **2.50**
- Upper Bound = **54.50**
- Potential Outliers = **65**

## Fare

Using the IQR method:

- Q1 = **7.8958**
- Q3 = **31.00**
- IQR = **23.1042**
- Lower Bound = **-26.7605**
- Upper Bound = **65.6563**
- Potential Outliers = **114**

Fare statistics:

- Mean = **32.0967**
- Median = **14.4542**
- Mode = **8.05**

Since:

```text
Mean > Median > Mode
```

the Fare distribution is positively/right-skewed.

---

# Bivariate Analysis

## Survival by Sex

- Female survival rate: **74.04%**
- Male survival rate: **18.89%**

Female passengers had a substantially higher survival rate than male passengers.

## Survival by Passenger Class

- First Class: **62.62%**
- Second Class: **47.28%**
- Third Class: **24.24%**

Higher passenger class was associated with a higher survival rate.

## Survival by Sex and Passenger Class

| Sex | Class | Survival Rate |
|---|---:|---:|
| Female | 1 | 96.74% |
| Female | 2 | 92.11% |
| Female | 3 | 50.00% |
| Male | 1 | 36.89% |
| Male | 2 | 15.74% |
| Male | 3 | 13.54% |

The combination of sex and passenger class shows a strong difference in survival. Female first-class passengers had the highest survival rate, while male third-class passengers had the lowest.

---

# Correlation Analysis

The correlation matrix was calculated using exactly the following six numerical features:

```text
survived
pclass
age
sibsp
parch
fare
```

The two strongest feature relationships based on absolute correlation were:

- `pclass` ↔ `fare`: **-0.5482**
- `pclass` ↔ `age`: **-0.3365**

The negative correlation between passenger class and fare indicates that the numerical encoding of passenger class is inversely related to fare. The relationship between passenger class and age is weaker but also negative.

---

# Multivariate Analysis

Four multivariate visualizations were used to investigate survival patterns:

1. Sex + Passenger Class + Survival
2. Age + Survival + Sex
3. Fare + Passenger Class + Survival
4. Age Group + Sex + Survival

These visualizations provide a combined view of factors associated with Titanic passenger survival.

---

# Standardization Sanity Check

Z-score standardization was performed on `age` and `fare` as an EDA sanity check.

Before standardization:

| Feature | Mean | Standard Deviation |
|---|---:|---:|
| `age` | 29.3152 | 12.9849 |
| `fare` | 32.0967 | 49.6975 |

After standardization:

```text
Mean ≈ 0
Standard Deviation ≈ 1
```

The standardized values were used only for the EDA sanity check and are not used directly as the machine-learning preprocessing pipeline.

---

# Machine Learning

Machine learning is implemented in:

```text
02_modeling.ipynb
```

The modeling workflow includes:

- Stratified train/test split
- Numerical preprocessing
- Categorical preprocessing
- Logistic Regression
- Decision Tree
- Random Forest
- Class imbalance analysis
- SMOTE
- Random Forest GridSearchCV
- Fare regression
- Model evaluation
- Model persistence

---

# Stratified Train/Test Split

The cleaned dataset was divided into **80% training data and 20% testing data** using a stratified split with `survived` as the target variable.

The original dataset contains approximately:

- **61.75% non-survivors**
- **38.25% survivors**

After splitting:

| Dataset | Not Survived | Survived |
|---|---:|---:|
| Original | 61.75% | 38.25% |
| Training | 61.74% | 38.26% |
| Testing | 61.80% | 38.20% |

The class proportions remain very similar across the original, training, and testing datasets, showing that stratification successfully preserved the class distribution.

---

# Preprocessing

The preprocessing pipeline uses separate transformations for numerical and categorical features.

## Numerical Features

```text
pclass
age
sibsp
parch
fare
```

Processing:

```text
Median Imputation
        ↓
StandardScaler
```

## Categorical Features

```text
sex
embarked
```

Processing:

```text
Most-Frequent Imputation
        ↓
One-Hot Encoding
```

The preprocessing is fitted using the training data and then applied to the test data.

---

# Classification Models

Three classification models were trained using the same train/test split:

1. Logistic Regression
2. Decision Tree
3. Random Forest

The following metrics were used:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

Confusion matrices were generated for the classification models.

A Decision Tree visualization was generated using `plot_tree`.

---

## Classification Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8090 | 0.7833 | 0.6912 | 0.7344 | 0.8610 |
| Decision Tree | 0.7697 | 0.6901 | 0.7206 | 0.7050 | 0.7541 |
| Random Forest | 0.8202 | 0.7812 | 0.7353 | 0.7576 | 0.8179 |

---

# Class Imbalance Analysis

The classification problem was evaluated under three approaches:

1. Baseline Logistic Regression
2. Logistic Regression with `class_weight="balanced"`
3. Logistic Regression with SMOTE

| Strategy | Precision | Recall | F1 Score |
|---|---:|---:|---:|
| Baseline | 0.7833 | 0.6912 | 0.7344 |
| Class Weight Balanced | 0.7183 | 0.7500 | 0.7338 |
| SMOTE | 0.7353 | 0.7353 | 0.7353 |

SMOTE was applied only to the training data.

Both balancing approaches increased recall compared with the baseline, while SMOTE produced the highest F1-score among the three approaches.

---

# Random Forest Hyperparameter Tuning

GridSearchCV with **5-fold cross-validation** was used to tune:

- `n_estimators`
- `max_depth`
- `max_features`

## Best Parameters

```text
n_estimators = 300
max_depth = None
max_features = sqrt
```

Best cross-validation F1-score:

```text
0.7456
```

Out-of-Bag score:

```text
0.8073
```

---

# Fare Regression

A multivariate Linear Regression model was used to predict:

```text
fare
```

using:

```text
pclass
sex
age
sibsp
parch
embarked
```

The regression model was evaluated using:

- MAE
- RMSE
- R²
- Adjusted R²

---

## Regression Results

| Metric | Value |
|---|---:|
| MAE | 21.1386 |
| RMSE | 41.7465 |
| R² | 0.3468 |
| Adjusted R² | 0.3118 |

A residual plot was generated to evaluate the regression errors.

The residual plot shows evidence of **heteroscedasticity**, because the spread of residuals is not constant across the predicted fare values.

At lower predicted fares, residuals are relatively close to zero, while at higher predicted fares, the residuals show a wider spread and several larger deviations.

Therefore, the Linear Regression model exhibits heteroscedasticity.

---

# Final Model Comparison

## Classification

The classification models produced the following results:

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.8090 | 0.7833 | 0.6912 | 0.7344 | 0.8610 |
| Decision Tree | 0.7697 | 0.6901 | 0.7206 | 0.7050 | 0.7541 |
| Random Forest | 0.8202 | 0.7812 | 0.7353 | 0.7576 | 0.8179 |

Random Forest achieved the highest accuracy of **0.8202** and F1-score of **0.7576** among the three classifiers.

Logistic Regression achieved the highest ROC-AUC of **0.8610**.

Decision Tree achieved an accuracy of **0.7697**, F1-score of **0.7050**, and ROC-AUC of **0.7541**.

## Regression

The Linear Regression model achieved:

- MAE: **21.1386**
- RMSE: **41.7465**
- R²: **0.3468**
- Adjusted R²: **0.3118**

Classification and regression metrics are evaluated separately because they measure different types of predictive tasks.

---

# Model Persistence

The final Random Forest pipeline was saved using Joblib.

The complete pipeline contains:

```text
Preprocessing
     ↓
Random Forest Classifier
```

The fitted pipeline was saved using:

```python
joblib.dump(best_pipeline, "best_titanic_pipeline.joblib")
```

The saved pipeline was reloaded using:

```python
loaded_pipeline = joblib.load("best_titanic_pipeline.joblib")
```

The reloaded pipeline was successfully tested using raw input data.

This demonstrates that preprocessing and prediction can be performed directly through the saved pipeline without manually transforming the input data.

Saved model:

```text
best_titanic_pipeline.joblib
```

---

# Files

```text
analytics/
├── 01_eda.ipynb
├── 02_modeling.ipynb
├── titanic.csv
├── cleaned_titanic.csv
├── best_titanic_pipeline.joblib
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Imbalanced-learn
- Joblib

---

# Analytics Status

**Completed**