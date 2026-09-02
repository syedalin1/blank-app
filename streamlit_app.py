import streamlit as st
import pandas as pd

st.title("TikTok Analytics App")

st.write("Upload your TikTok data and I will analyse it.")

uploaded_file = st.file_uploader("Upload your TikTok CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader("Your TikTok Data")
    st.dataframe(data)
