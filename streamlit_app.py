import streamlit as st
import pandas as pd

st.title("Amelle Analytics App")

st.write("Upload your TikTok Excel file and I will analyse it.")

uploaded_file = st.file_uploader(
    "Upload your TikTok Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    st.subheader("Your TikTok Data")
    st.dataframe(data)
