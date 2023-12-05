# Final Viz Project
# Anna Carmody, Rafi Dahdal, and Jacob Stanley

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns

st.title("Global Salary Insights Dashboard")

# Load data
df = pd.read_csv("salaries.csv")
df["work_year"] = df["work_year"].astype("object")

st.header("Anna Carmody, Rafi Dahdal, Jacob Stanley")

# Plot 1: Line chart for Global Average Salary Over Time
df_grouped = df.groupby("work_year")["salary_in_usd"].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df_grouped["work_year"], df_grouped["salary_in_usd"], marker='o', linestyle='-')
ax1.set_title("Global Average Salary Over Time")
ax1.set_xlabel("Year")
ax1.set_ylabel("Average Salary in USD")
st.pyplot(fig1)

# Plot 2: Bar chart for Highest Paying Data Jobs Worldwide
color_map = {
    "Architect": "blue",
    "Data Sci": "green",
    "Engineer": "purple",
}

def assign_color(job_title):
    for keyword, color in color_map.items():
        if keyword.lower() in job_title.lower():
            return color
    return "gray"

df_grouped = df.groupby("job_title")["salary_in_usd"].mean().reset_index()
df_grouped_sorted = df_grouped.sort_values(by="salary_in_usd", ascending=False).head(20)

fig2, ax2 = plt.subplots(figsize=(12, 8))

colors = [assign_color(job) for job in df_grouped_sorted["job_title"]]
bars = ax2.barh(df_grouped_sorted["job_title"], df_grouped_sorted["salary_in_usd"], color=colors)
ax2.invert_yaxis()
ax2.set_title("Highest Paying Data Jobs Worldwide")
ax2.set_xlabel("Average Salary in USD")

legend_handles = [
    mpatches.Patch(color=color_map[group], label=group) for group in color_map
]
legend_handles.append(mpatches.Patch(color="gray", label="Other"))

plt.legend(handles=legend_handles)

st.pyplot(fig2)

# Plot 3: Bar chart for Global Average Salary by Company Size
df_grouped = df.groupby("company_size")["salary_in_usd"].mean().reset_index()

colors = sns.color_palette("mako", 3)

fig3, ax3 = plt.subplots(figsize=(10, 6))
bars = ax3.bar(df_grouped["company_size"], df_grouped["salary_in_usd"], color=colors)

ax3.set_title("Global Average Salary by Company Size")
ax3.set_xlabel("Size of Company")
ax3.set_ylabel("Average Salary in USD")
st.pyplot(fig3)
