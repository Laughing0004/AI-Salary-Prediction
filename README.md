# AI Job Salary Prediction

## Project Overview

The AI Job Salary Prediction project aims to predict the salary of AI-related job positions based on job details, company information, and candidate-related attributes. This machine learning solution helps organizations make informed salary decisions and assists job seekers in understanding salary trends within the AI industry.

---

## Problem Statement

Companies often face challenges in determining competitive salary packages for job roles. Salary decisions depend on multiple factors such as experience level, company size, job location, required skills, and benefits offered.

The objective of this project is to build a Machine Learning model capable of predicting the salary offered for a job position using historical job data.

---

## Business Impact

* Helps companies offer competitive salaries
* Supports recruiters in identifying suitable candidates
* Improves hiring decisions through data-driven insights
* Assists job seekers in understanding salary expectations
* Provides valuable salary trend analysis for the AI job market

---

## Dataset Information

### Dataset Size

* Total Records: 15,000
* Input Features: 18
* Target Variable: 1

### Target Variable

* salary_usd

### Features Used

* job_title
* experience_level
* employment_type
* company_location
* company_size
* company_name
* employee_residence
* education_required
* years_experience
* required_skills
* job_description_length
* industry
* remote_ratio
* posting_date
* application_deadline
* benefits_score
* salary_currency
* job_id

---

# Project Workflow

## Sprint 1: Data Understanding & Preprocessing

### Tasks Completed

* Data Collection and Loading
* Initial Data Inspection
* Data Cleaning
* Missing Value Handling
* Duplicate Removal
* Data Type Corrections
* Exploratory Data Analysis (EDA)
* Outlier Detection and Treatment
* Feature Encoding
* Feature Scaling
* Train-Test Split

### Techniques Used

* Pandas
* NumPy
* Matplotlib
* Correlation Analysis
* Boxplots
* IQR Method
* One-Hot Encoding
* StandardScaler

---

## Sprint 2: Model Building & Evaluation

### Models Trained

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor

### Evaluation Metrics

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### Additional Analysis

* Overfitting and Underfitting Check
* Model Comparison
* Best Model Selection

---

## Sprint 3: Optimization & Final Model

### Tasks Completed

* Feature Engineering
* Feature Selection
* Feature Importance Analysis
* Hyperparameter Tuning
* Final Model Training
* Final Evaluation
* Model Serialization

### Optimization Techniques

* Random Forest Feature Importance
* GridSearchCV
* Hyperparameter Tuning
* Model Optimization

### Model Saving

The final trained model was saved using Joblib for future deployment.

---

## Sprint 4: Deployment & MLOps

### Deployment Components

* Machine Learning Pipeline
* Streamlit Application
* Prediction Interface
* Model Loading and Prediction

### MLOps Practices

* Version Control using GitHub
* Experiment Tracking
* Logging and Monitoring
* Project Documentation

---

# Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit

### Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

# Project Structure

```text
AI_Job_Salary_Prediction/

├── data/
│   └── ai_job_dataset.csv
│
├── notebooks/
│   └── AI_Job_Salary_Prediction.ipynb
│
├── models/
│   └── salary_prediction_pipeline.pkl
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── app/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

---

# Model Development Process

### Data Preprocessing

* Missing value treatment
* Duplicate removal
* Data type conversion
* Feature encoding
* Feature scaling

### Model Training

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor

### Model Evaluation

Models were evaluated using:

* MAE
* RMSE
* R² Score

The best-performing model was selected based on overall performance and generalization capability.

---

# Key Insights

* Experience level significantly influences salary.
* Benefits offered by companies impact salary packages.
* Remote work availability affects salary trends.
* Company characteristics contribute to salary prediction accuracy.
* Machine Learning models can effectively estimate AI job salaries.

---

# Future Improvements

* Advanced Feature Engineering
* More Robust Hyperparameter Tuning
* Cloud Deployment
* Real-Time Prediction API
* Automated Model Monitoring
* Continuous Model Retraining

---

# Installation

Clone the repository:

```bash
git clone https://github.com/your-username/AI-Job-Salary-Prediction.git
```

Move into the project directory:

```bash
cd AI-Job-Salary-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run the Project

### Jupyter Notebook

```bash
jupyter notebook
```

### Streamlit Application

```bash
python -m streamlit run app.py
```

---

# Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow for salary prediction, including data preprocessing, exploratory data analysis, model development, optimization, evaluation, deployment, and MLOps practices. The solution provides valuable insights into AI job salary trends and supports data-driven decision-making for both recruiters and job seekers.
