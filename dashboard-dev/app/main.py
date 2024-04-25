import streamlit as st
import pandas as pd

# Load dataset
@st.cache
def load_data():
    data = pd.read_csv(r"..\src\benin-malanville.csv")


    return data

data = load_data()

# Sidebar
st.sidebar.title("Dashboard Options")
# Add interactive elements to sidebar (e.g., sliders, dropdowns)

# Main content
st.title("Streamlit Dashboard")

# Add visualizations and other content based on user selections
# For example:
st.write(data)  # Display the entire dataset
# Or
st.line_chart(data[['GHI', 'DNI', 'DHI']])  # Display line chart of GHI, DNI, DHI

# Footer
st.text("Developed by Your Name")

