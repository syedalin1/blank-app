import streamlit as st
import pandas as pd

st.set_page_config(page_title="Amelle TikTok Analytics App", layout="wide")

st.title("Amelle TikTok Analytics App")
st.write("Upload your TikTok Excel file and I will analyse it.")

uploaded_file = st.file_uploader(
    "Upload your TikTok Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    st.success("Excel file uploaded successfully!")

    st.subheader("Your TikTok Data")
    st.dataframe(data, use_container_width=True)

    st.subheader("Quick Summary")
    st.write("Number of rows:", len(data))
    st.write("Number of columns:", len(data.columns))

    st.subheader("Columns in your file")
    st.write(list(data.columns))
    st.subheader("Top 10 TikTok Videos")

    view_columns = [col for col in data.columns if "view" in str(col).lower()]

    if view_columns:
        view_column = "playCount"

        top_10 = data.sort_values(
            by=view_column,
            ascending=False
        ).head(10)

        st.dataframe(top_10, use_container_width=True)
    else:
        st.warning("I could not automatically find the Views column.")
