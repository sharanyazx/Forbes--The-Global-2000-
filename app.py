
# Run:  streamlit run dashboard.py

import re
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import io

st.set_page_config(page_title="Forbes 2000 – 2025 Dashboard",
                   layout="wide", initial_sidebar_state="collapsed")


# Helper: load & clean once
# Add this to the top of your load_data function

def clean_number(x):
    if pd.isna(x):
        return np.nan
    x = str(x)
    # Remove commas and multiple dots
    x = x.replace(",", "")
    x = re.sub(r"\.+", ".", x)
    try:
        return float(x)
    except ValueError:
        return np.nan

@st.cache_data
def load_data():
    df = pd.read_csv("D:\Sharanya\Forbes_Dashboard\data\Forbes_2000_Companies_2025.csv", sep=";")
    num_cols = ['Sales ($B)', 'Profit ($B)', 'Assets ($B)', 'Market Value ($B)']
    for c in num_cols:
        df[c] = df[c].apply(clean_number)
    df = df[(df[num_cols] >= 0).all(axis=1)].dropna(subset=num_cols)
    return df

df = load_data()


# KPIs
total_sales   = df['Sales ($B)'].sum()
total_profit  = df['Profit ($B)'].sum()
total_assets  = df['Assets ($B)'].sum()
total_mktcap  = df['Market Value ($B)'].sum()


# Clustering
features = ['Sales ($B)', 'Profit ($B)', 'Assets ($B)', 'Market Value ($B)']
Xscl = StandardScaler().fit_transform(np.log1p(df[features]))
kmeans = KMeans(n_clusters=4, random_state=42)
df['Cluster'] = kmeans.fit_predict(Xscl)

cluster_names = {
    0: "Mid-Cap Industrials",
    1: "Profitable Specialists",
    2: "Mega-Caps",
    3: "Asset-Heavy Utilities"
}
df['Cluster_Name'] = df['Cluster'].map(cluster_names)

# ------------------------------------------------------------------
# Streamlit UI
st.title(" Forbes 2000 – 2025 Dashboard")
st.markdown("This dashboard provides insights into the Forbes 2000 companies from 2020 to 2025, including financial metrics, clustering analysis, and industry trends.")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", f"${total_sales/1e3:.1f} T")
col2.metric("Total Profit", f"${total_profit/1e3:.1f} T")
col3.metric("Total Assets", f"${total_assets/1e3:.1f} T")
col4.metric("Market Cap", f"${total_mktcap/1e3:.1f} T")

st.divider()

# ------------------------------------------------------------------
# Top-10 Market Cap
st.header("Top 10 Companies by Market Capitalisation")
top10 = df.sort_values('Market Value ($B)', ascending=False).head(10)
fig, ax = plt.subplots(figsize=(5, 2.7))
sns.barplot(y='Company', x='Market Value ($B)', data=top10, palette='viridis', ax=ax)
ax.set_title("Top 10 Companies by Market Cap")
ax.set_ylabel("")
st.pyplot(fig)

# ------------------------------------------------------------------
# Industry profit margins
st.header("Top 10 Industries by Median Profit Margin")
df['Profit Margin'] = df['Profit ($B)'] / df['Sales ($B)']
sector_pm = (df.groupby('Industry')['Profit Margin']
               .median()
               .sort_values(ascending=False)
               .head(10))
fig2, ax2 = plt.subplots(figsize=(5, 3))
sns.barplot(y=sector_pm.index, x=sector_pm.values, palette='mako', ax=ax2)
ax2.set_title("Top 10 Industries – Median Profit Margin")
ax2.set_ylabel("")
st.pyplot(fig2)

# ------------------------------------------------------------------
# Cluster scatter
st.header("Cluster Analysis")
tsne = TSNE(n_components=2, random_state=42)
coords = tsne.fit_transform(Xscl)
df['t-SNE-1'] = coords[:, 0]
df['t-SNE-2'] = coords[:, 1]

fig3, ax3 = plt.subplots(figsize=(5, 4))
sns.scatterplot(data=df, x='t-SNE-1', y='t-SNE-2',
                hue='Cluster_Name', palette='tab10', s=30, ax=ax3)
ax3.set_title("t-SNE Projection of Clusters")
ax3.legend(title='')
st.pyplot(fig3)

# ------------------------------------------------------------------
st.divider()
st.caption("Created by Sharanya, 2025. Data source: Forbes 2000 dataset.")