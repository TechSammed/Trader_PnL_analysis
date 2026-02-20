import streamlit as st
import pandas as pd
import pickle

# ================= LOAD MODEL & DATA =================

@st.cache_resource
def load_model():
    return pickle.load(open("model.pkl", "rb"))

@st.cache_data
def load_data():
    df = pd.read_csv("datasets/analysis_df.csv")
    pred = pd.read_csv("datasets/daily_predictions.csv")
    return df, pred

model = load_model()
df, pred = load_data()

# ================= SIDEBAR NAVIGATION =================

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Prediction Tool", "Dashboard"])

# ================= PAGE 1: PREDICTION =================

if page == "Prediction Tool":

    st.title("Trader Profitability Predictor")

    st.write("Estimate the likelihood of a profitable trading day based on behavior and market sentiment.")

    trade_size = st.number_input("Average Trade Size (USD)", value=3000)
    trades = st.number_input("Number of Trades", value=10)

    sentiment = st.selectbox(
        "Market Sentiment",
        ["Fear", "Greed"]
    )

    sentiment_map = {"Fear": 0, "Greed": 1}
    sentiment_val = sentiment_map[sentiment]

    if st.button("Predict"):

        prediction = model.predict([[trade_size, trades, sentiment_val]])
        probability = model.predict_proba([[trade_size, trades, sentiment_val]])[0][1]

        if prediction[0] == 1:
            st.success(f"Predicted: Profitable Day ✅")
            st.info(f"Confidence: {probability*100:.1f}%")
        else:
            st.error(f"Predicted: Loss Day ⚠️")
            st.info(f"Confidence: {(1-probability)*100:.1f}%")

# ================= PAGE 2: DASHBOARD =================

elif page == "Dashboard":

    st.title("Trading Behavior Dashboard")
    st.caption("Interactive insights into trader performance under Fear vs Greed market sentiment.")

    # -------- Performance Metrics --------
    st.subheader("Overall Performance")

    col1, col2 = st.columns(2)

    col1.metric("Average Trade PnL", round(df['Closed PnL'].mean(), 2))
    col2.metric("Win Rate", f"{round((df['Closed PnL'] > 0).mean() * 100, 2)}%")

    # -------- Charts --------
    st.subheader("Average Trade Size by Sentiment")
    size_chart = df.groupby('classification')['Size USD'].mean()
    st.bar_chart(size_chart)

    st.subheader("Trading Activity by Sentiment")
    activity_chart = df.groupby('classification').size()
    st.bar_chart(activity_chart)

    st.subheader("Long vs Short Distribution")
    long_short = df.groupby('Side').size().sort_values(ascending=False)
    st.bar_chart(long_short)

    # -------- Table --------
    st.subheader("Performance Summary Table")

    perf_table = df.groupby('classification').agg(
        avg_pnl=('Closed PnL', 'mean'),
        win_rate=('Closed PnL', lambda x: (x > 0).mean() * 100),
        avg_size=('Size USD', 'mean'),
        trades=('Side', 'count')
    )

    st.dataframe(
        perf_table.style.format({
            "avg_pnl": "{:.2f}",
            "win_rate": "{:.2f}",
            "avg_size": "{:.2f}"
        })
    )

    # -------- Prediction Insights --------
    st.subheader("Predicted Profitability Insights")

    profit_rate = pred['prediction'].mean() * 100
    st.metric("Predicted Profitable Days", f"{profit_rate:.2f}%")

    st.subheader("Prediction Distribution")
    st.bar_chart(pred['prediction'].value_counts())