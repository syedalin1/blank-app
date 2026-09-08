import streamlit as st
import pandas as pd

st.title("Amelle TikTok Analytics App")
st.write("Upload your TikTok Excel file and I will analyse it.")

uploaded_file = st.file_uploader(
    "Upload your TikTok Excel file",
    type=["xlsx"]
)

if uploaded_file is not None:
    data = pd.read_excel(uploaded_file)

    selected_columns = [
        "createTimeISO",
        "playCount",
        "diggCount",
        "commentCount",
        "shareCount",
        "collectCount",
        "text",
        "textLanguage",
        "videoMeta/duration",
        "webVideoUrl"
    ]

    data = data[selected_columns].copy()

    st.success("Excel file uploaded successfully!")

    st.subheader("Your TikTok Data")
    st.dataframe(data, use_container_width=True)

    st.subheader("Quick Summary")
    st.write("Number of rows:", data.shape[0])
    st.write("Number of columns:", data.shape[1])

    st.subheader("Columns in Your File")
    st.write(list(data.columns))

    st.subheader("Top 10 TikTok Videos")

    if "playCount" in data.columns:
        top_10 = data.sort_values(
            by="playCount",
            ascending=False
        ).head(10)

        st.dataframe(top_10, use_container_width=True)
    else:
        st.warning("The playCount column was not found in the Excel file.")

    st.subheader("Data Quality Check")

    st.write("Number of rows:", data.shape[0])
    st.write("Number of columns:", data.shape[1])
    st.write("Duplicate rows:", data.duplicated().sum())

    quality_report = pd.DataFrame({
        "Column": data.columns,
        "Missing values": data.isnull().sum().values,
        "Data type": data.dtypes.astype(str).values
    })

    st.dataframe(quality_report, use_container_width=True)

    st.subheader("Raw Data Preview")
    st.dataframe(data.head(10), use_container_width=True)
    top_10 = data.sort_values(
    by="playCount",
    ascending=False
).head(10).copy()

    comments_chart = top_10[["text", "commentCount"]].copy()

    comments_chart["Video"] = (
    comments_chart["text"]
    .fillna("No title")
    .str.slice(0, 35)
)

            comments_chart["Video"] = (
            comments_chart["text"]
            .fillna("No title")
            .str.slice(0, 35)
        )

        st.subheader("Comments on Top 10 TikTok Videos")

        st.bar_chart(
            comments_chart,
            x="Video",
            y="commentCount",
            horizontal=True,
            sort="-commentCount"
        )
