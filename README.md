# 🏦 ATM Fraud Transaction Detection

## 🔎 Problem Statement

**PredCatch Analytics** serves leading Australian banks whose profitability and reputation are being severely affected by **fraudulent ATM transactions**. The company has tasked its data science team with developing a **real-time fraud detection model** that can proactively identify and decline suspicious transactions before they are processed.

Your role as a **PredCatch Data Scientist** is to:
- Build a robust predictive model to classify transactions as fraudulent or clean.
- Handle extreme class imbalance.
- Leverage additional proprietary and network-based variables to improve fraud detection accuracy.

## 🎯 Project Objective

> Build an end-to-end machine learning pipeline to detect fraudulent ATM transactions using historical transaction metadata and advanced modeling techniques, ensuring **high recall**, **low false positives**, and **real-time readiness**.

## 🗂️ Folder Structure

```bash
fraud-transaction-detector/
├── data/
│   ├── processed/
│   │   ├── xtrain.csv
│   │   ├── xtest.csv
│   │   └── ytrain.csv
│   └── raw/
├── images/
│   └── *.png (visuals and box plots)
├── models/
│   └── final_model.pkl
├── notebooks/
│   └── data-exploration.ipynb
├── scripts/
│   ├── preprocessing.py
│   ├── modeling.py
│   └── utils.py
├── venv/
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## 📊 Dataset Overview

The project uses **six main datasets** (renamed for clarity):
- `geo.csv`
- `instance.csv`
- `lambdawts.csv`
- `qset.csv`
- `train.csv`
- `test.csv`

These contain customer and transaction-level features including:
- Geographic location
- Proprietary fraud indices
- Vulnerability scores
- System network turnaround times

The **target** column in the train set:
- `1` = Fraudulent  
- `0` = Legitimate

## 🧪 Data Exploration & Cleaning

✔️ Loaded and reviewed all files  
✔️ Inspected key fields like `id` and `group` for uniqueness and merging  
✔️ Combined `train` and `test` datasets for uniform processing  
✔️ Aggregated `geo`, `instance`, and `qset` data using `.groupby('id').mean()`  
✔️ Handled shape mismatches by imputing missing values using **median imputation**  
✔️ Successfully merged all data into one final dataset  
✔️ Separated clean `train` and `test` sets and saved them in `/data/processed/`

## 🧹 Feature Engineering

- Dropped irrelevant fields: `id`, `group`, and `target` (after separation)
- Verified absence of null values
- Detected outliers using **boxplots** (but didn’t treat them due to minimal impact)
- Visuals saved to `/images/`

## ⚖️ Class Imbalance

- The dataset had:
  - ✅ 227,451 normal transactions
  - ❌ 394 fraudulent transactions
- Severe imbalance addressed during modeling via careful metric selection and model tuning

## ⚙️ Data Standardization

- Standardization significantly improved model performance
- All final model training done using **standardized features**

## 🤖 Models Implemented

| Model                  | Status         | Notes                                      |
|------------------------|----------------|--------------------------------------------|
| Logistic Regression    | ✅ Completed   | Performed well after standardization       |
| Decision Tree          | ✅ Completed   | Moderate performance                       |
| Random Forest          | ✅ Completed   | Solid baseline                             |
| XGBoost                | ✅ Completed   | Top performer                              |
| Support Vector Machine | ✅ Completed   | Improved with scaling                      |
| Voting Classifier      | ✅ Completed   | Ensemble of best models                    |
| Stacking Classifier    | ✅ Completed   | Final model used for deployment            |
| Isolation Forest       | ✅ Completed   | Unsupervised anomaly detection baseline    |

## 📈 Key Learnings

- Data **standardization** was crucial for performance
- Class imbalance required careful evaluation (focus on **recall**, **precision**, **AUC**)
- No outlier treatment was required due to limited effect
- Proper preprocessing pipelines and modular coding improved project clarity and maintainability

## 📂 Output Files

- Final cleaned datasets in `/data/processed/`
- Visuals saved to `/images/`
- Trained model saved as `final_model.pkl` in `/models/`

## 🚀 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the pipeline
python main.py
```

## 🛠️ Future Improvements

- Integrate streaming fraud detection using Kafka or Spark
- Add SHAP/LIME for interpretability
- Use time-series modeling for evolving fraud patterns
- Implement cost-sensitive learning or focal loss

## 👨‍💻 Author

**Bikram Singh**  
Data Scientist | AI & Finance Enthusiast |  
📧 Email: 1k99bikramsingh@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/1k99bikramsingh/