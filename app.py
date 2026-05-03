import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Personal Dashboard", layout="wide")

# Title and description
st.title("Personal Decision Intelligence Dashboard")
st.caption("Analyzing how daily habits impact productivity")
st.markdown("### Built by MSc Computer Science student focusing on Data Science and AI")

st.write("This dashboard analyzes how your habits affect productivity.")

# Load data
df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df["date"])

# Show data
st.subheader("Your Data")
st.dataframe(df)

# Metrics
col1, col2, col3 = st.columns(3)

col1.metric("Avg Sleep", round(df["sleep_hours"].mean(), 2))
col2.metric("Avg Study", round(df["study_hours"].mean(), 2))
col3.metric("Avg Productivity", round(df["productivity"].mean(), 2))

# Productivity over time
st.subheader("Productivity Over Time")

fig, ax = plt.subplots()
ax.plot(df["date"], df["productivity"], marker="o")
ax.set_xlabel("Date")
ax.set_ylabel("Productivity")
plt.xticks(rotation=45)

st.pyplot(fig)

# Sleep vs Productivity
st.subheader("Sleep vs Productivity")

fig2, ax2 = plt.subplots()
ax2.scatter(df["sleep_hours"], df["productivity"])
ax2.set_xlabel("Sleep Hours")
ax2.set_ylabel("Productivity")

st.pyplot(fig2)

# Insights
st.subheader("Insights")

high_sleep = df[df["sleep_hours"] >= 7]["productivity"].mean()
low_sleep = df[df["sleep_hours"] < 7]["productivity"].mean()

st.write(f"Avg productivity (>=7h sleep): {round(high_sleep, 2)}")
st.write(f"Avg productivity (<7h sleep): {round(low_sleep, 2)}")

if high_sleep > low_sleep:
    st.success("Insight: Higher productivity is associated with sleeping 7 hours or more.")
else:
    st.warning("Insight: No clear relationship between sleep and productivity based on current data.")

# Conclusion
st.subheader("Conclusion")
st.write("This project demonstrates how personal data can be analyzed to generate meaningful insights and support better decision-making.")