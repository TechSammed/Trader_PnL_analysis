# Trader Performance vs Market Sentiment Analysis

## 📌 Overview
This project analyzes how market sentiment (Fear vs Gre ed) influences trader behavior and performance. The objective is to identify behavioral patterns and profitability trends that can support smarter trading decisions and risk management.

---

## 📊 Datasets

### Bitcoin Fear & Gre ed Index
Daily sentiment classification used to capture market psychology.

### Hyperliquid Trader Data
Trade-level data including:
- execution price
- trade size
- trade direction (long/short)
- closed PnL
- timestamps

---

## 🧹 Data Preparation

The dataset was cleaned and prepared using the following steps:

- Removed irrelevant columns
- Converted timestamps to daily format
- Merged trader activity with daily sentiment
- Filtered sentiment to **Fear** and **Gre ed** for focused analysis
- Created derived metrics such as daily PnL, trade counts, and win indicators

---

## 📈 Performance Analysis

Key metrics evaluated:

- Average PnL
- Median PnL
- Win Rate

**Insights**
- Gre ed conditions show slightly improved performance.
- Median PnL of zero indicates most trades yield minimal profit.
- Overall profitability is driven by a small number of large winning trades.

---

## ⚙️ Trading Behavior Analysis

Behavioral metrics examined:

- Average trade size (proxy for risk exposure)
- Trading frequency
- Long vs short positioning

**Insights**
- Fear periods trigger significantly higher trading activity and larger position sizes, indicating reactive risk-taking.
- Gre ed conditions show calmer trading behavior and smaller position sizes.

---

## 👥 Trader Segmentation

### Consistent vs Inconsistent Traders
Profitability remained similar across both groups, indicating that overall returns depend more on large winning trades than frequent wins.

---

## 📊 Visual Insights

Visualizations included:

- PnL distribution comparison
- Trade size by sentiment
- Trading activity comparison
- Long vs short distribution

These charts support behavioral and performance insights.

---

## 🤖 Predictive Modeling

A Logistic Regression model was developed to predict daily trader profitability using:

- average trade size
- number of trades
- market sentiment (Fear vs Gre ed)

**Model Accuracy:** ~64%

This indicates that trader behavior and sentiment provide meaningful predictive signals for profitability.

---

## 🖥️ Interactive Dashboard

An interactive Streamlit dashboard was built to explore insights and predictions.

### Prediction Tool
- Input trade size, trade count, and sentiment
- Predict likelihood of a profitable day with confidence score

### Dashboard Insights
- Performance metrics
- Risk & activity charts
- Sentiment comparisons
- Prediction distribution

---

## 💡 Strategy Recommendations

- Reduce position sizes and avoid overtrading during Fear markets to manage volatility risk.
- Focus on selective, high-quality trades during Gre ed conditions.
- Allow profitable trades to run while maintaining disciplined risk management.

---

## ⚠️ Limitations

- Trade size was used as a proxy for leverage due to unavailable leverage data.
- Daily sentiment classification may not capture intraday market changes.
- Market outcomes are influenced by external factors beyond sentiment and behavior.

---

## 🚀 How to Run

### Install dependencies
```bash
pip install -r requirements.txt
```

Run the Dashboard
```
streamlit run app.py
```

### 🛠 Tech Stack

- Python

- Pandas & NumPy

- Scikit-learn

- Matplotlib & Seaborn

- Streamlit

### 🌟 Project Highlights

- Sentiment-driven trading analysis
- Behavioral risk insights
- Profitability prediction model
- Interactive decision-support dashboard
