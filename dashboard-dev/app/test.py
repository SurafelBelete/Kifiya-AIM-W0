import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats



st.set_page_config(page_title="BlueLight Technologies",
                   page_icon=":new_moon:",
                 
                   )
st.title("Data Analysis Report: Environmental Measurement Analysis for MoonLight Energy Solutions")

@st.cache_data
def load_data(path:str):
    data = pd.read_csv(path)
    return data

with st.sidebar:
    upload_file = st.file_uploader("Choose a file", type=["csv", "xlsx",'pdf'])

    if upload_file is None:
        st.info("upload file through config",icon="ℹ️")
        st.stop()

df = load_data(upload_file)

# Sidebar
st.sidebar.title("Dashboard Options")
# Add interactive elements to sidebar (e.g., sliders, dropdowns)



st.write(df.sample(n=100))  # Display a random sample of 100 rows
 
# Or
st.line_chart(df[['GHI', 'DNI', 'DHI']])  # Display line chart of GHI, DNI, DHI

# Footer
st.text("Developed by Surafel Belete")


# Page Configuration
#st.set_page_config(page_title="Environmental Measurement Analysis", page_icon=":bar_chart:")

# Title and Author
#st.title("Data Analysis Report: Environmental Measurement Analysis for MoonLight Energy Solutions")
st.markdown("Author: Surafel Belete\nDate: 25/4/2024")

# Executive Summary
st.header("Executive Summary")
st.markdown("""
MoonLight Energy Solutions aims to enhance operational efficiency and sustainability through targeted solar investments. This report presents a comprehensive analysis of environmental measurement data to identify key trends and insights for strategic decision-making. Through exploratory data analysis (EDA) and statistical analysis, we uncover valuable insights that align with MoonLight Energy Solutions' long-term sustainability goals.
""")

# Introduction
st.header("Introduction")
st.markdown("""
The analysis focuses on understanding environmental measurement data provided by the engineering team. The objectives include identifying high-potential regions for solar installation and supporting data-driven decision-making for MoonLight Energy Solutions.
""")

# Data Overview
st.header("Data Overview")
st.markdown("""
The dataset contains environmental measurements such as solar radiation components (GHI, DNI, DHI), temperature measures (TModA, TModB, Tamb), wind speed, wind direction, and other variables. It comprises timestamps and numeric values for each measurement.
""")


# Exploratory Data Analysis (EDA)
st.header("Exploratory Data Analysis (EDA)")

# Summary Statistics
st.subheader("Summary Statistics")
st.write(df.describe())

# Data Quality Check
st.subheader("Data Quality Check")
# Show missing values
st.write("Missing Values:")
st.write(df.isnull().sum())


# Correlation Analysis
st.subheader("Correlation Analysis")
# Correlation Analysis
correlation_matrix = df[['GHI', 'DHI', 'DNI', 'TModA', 'TModB']].corr()
st.write(correlation_matrix)


# Display histograms
st.subheader("Histograms")

# Create histograms for GHI, DNI, DHI, WS, TModA, TModB, and Tamb
fig, axs = plt.subplots(3, 3, figsize=(12, 8))

# GHI histogram
axs[0, 0].hist(df['GHI'], bins=20, color='skyblue', edgecolor='black')
axs[0, 0].set_xlabel('GHI')
axs[0, 0].set_ylabel('Frequency')
axs[0, 0].set_title('GHI Histogram')

# DNI histogram
axs[0, 1].hist(df['DNI'], bins=20, color='lightgreen', edgecolor='black')
axs[0, 1].set_xlabel('DNI')
axs[0, 1].set_ylabel('Frequency')
axs[0, 1].set_title('DNI Histogram')

# DHI histogram
axs[0, 2].hist(df['DHI'], bins=20, color='salmon', edgecolor='black')
axs[0, 2].set_xlabel('DHI')
axs[0, 2].set_ylabel('Frequency')
axs[0, 2].set_title('DHI Histogram')

# WS histogram
axs[1, 0].hist(df['WS'], bins=20, color='orange', edgecolor='black')
axs[1, 0].set_xlabel('WS')
axs[1, 0].set_ylabel('Frequency')
axs[1, 0].set_title('WS Histogram')

# TModA histogram
axs[1, 1].hist(df['TModA'], bins=20, color='purple', edgecolor='black')
axs[1, 1].set_xlabel('TModA')
axs[1, 1].set_ylabel('Frequency')
axs[1, 1].set_title('TModA Histogram')

# TModB histogram
axs[1, 2].hist(df['TModB'], bins=20, color='brown', edgecolor='black')
axs[1, 2].set_xlabel('TModB')
axs[1, 2].set_ylabel('Frequency')
axs[1, 2].set_title('TModB Histogram')

# Tamb histogram
axs[2, 0].hist(df['Tamb'], bins=20, color='pink', edgecolor='black')
axs[2, 0].set_xlabel('Tamb')
axs[2, 0].set_ylabel('Frequency')
axs[2, 0].set_title('Tamb Histogram')

plt.tight_layout()

# Display the plots using st.pyplot()
st.pyplot(fig)

# Create histograms for GHI, DNI, DHI, WS, TModA, TModB, and Tamb
plt.figure(figsize=(12, 8))

# GHI histogram
plt.subplot(3, 3, 1)
plt.hist(df['GHI'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('GHI')
plt.ylabel('Frequency')
plt.title('GHI Histogram')

# DNI histogram
plt.subplot(3, 3, 2)
plt.hist(df['DNI'], bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('DNI')
plt.ylabel('Frequency')
plt.title('DNI Histogram')

# DHI histogram
plt.subplot(3, 3, 3)
plt.hist(df['DHI'], bins=20, color='salmon', edgecolor='black')
plt.xlabel('DHI')
plt.ylabel('Frequency')
plt.title('DHI Histogram')

# WS histogram
plt.subplot(3, 3, 4)
plt.hist(df['WS'], bins=20, color='orange', edgecolor='black')
plt.xlabel('WS')
plt.ylabel('Frequency')
plt.title('WS Histogram')

# TModA histogram
plt.subplot(3, 3, 5)
plt.hist(df['TModA'], bins=20, color='purple', edgecolor='black')
plt.xlabel('TModA')
plt.ylabel('Frequency')
plt.title('TModA Histogram')

# TModB histogram
plt.subplot(3, 3, 6)
plt.hist(df['TModB'], bins=20, color='brown', edgecolor='black')
plt.xlabel('TModB')
plt.ylabel('Frequency')
plt.title('TModB Histogram')

# Tamb histogram
plt.subplot(3, 3, 7)
plt.hist(df['Tamb'], bins=20, color='pink', edgecolor='black')
plt.xlabel('Tamb')
plt.ylabel('Frequency')
plt.title('Tamb Histogram')

plt.tight_layout()
#plt.show()


# Recommendations
st.header("Recommendations")
st.markdown("""
Based on the analysis, the following recommendations are proposed:
1. Identify High-Potential Regions: Utilize insights from EDA to identify regions with optimal solar conditions for installation.
2. Optimize Installation Locations: Use correlation analysis to inform the selection of installation sites with maximum solar radiation and favorable weather conditions.
3. Enhance Operational Efficiency: Implement strategies to mitigate the impact of outliers and anomalies, ensuring accurate data for decision-making.
""")

