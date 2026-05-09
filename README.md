# 🛡️ Financial Fraud Detection & Trend Analysis

## 📌 Project Overview
This project focuses on analyzing large-scale financial transaction data to identify potential fraudulent activity. Using Python and Pandas, I implemented statistical methods to establish behavioral baselines for users and detect suspicious anomalies.

## 🚀 Key Features
* **Data Preprocessing:** Cleaned and categorized transaction types (CASH_OUT, TRANSFER, DEBIT, etc.) from a dataset of 1M+ rows.
* **Simple Moving Average (SMA):** Implemented a 20-period rolling window to smooth transaction volatility and identify long-term spending trends.
* **Anomaly Detection:** Developed logic to flag transactions that significantly deviate from the calculated moving average.
* **Automated Summaries:** Generated insights on average transaction amounts per category.

## 🛠️ Technical Stack
* **Language:** Python
* **Library:** Pandas (Data Manipulation), NumPy (Mathematical logic)
* **Tools:** VS Code, Git/GitHub

## 📊 Sample Analysis
One of the core metrics used is the **Simple Moving Average (SMA)**. 
Unlike raw data, which can be noisy due to random spikes, the SMA helps in visualizing the "true" direction of an account's activity.

## 📂 How to Run
1. Clone the repository.
2. Install dependencies: `pip install pandas numpy`
3. Run the script: `python pandas_project.py`

Dataset: Due to file size limits, the 'Synthetic Financial Datasets' CSV is not included. You can download the dataset from Kaggle or use your own financial transaction log.
