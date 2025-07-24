import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set wide layout
st.set_page_config(page_title="Data Analysis Assistant", layout="wide")

st.title("📊 Data Analysis Assistant")

# File uploader
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Preview data
    st.subheader("🔍 Data Preview")
    st.dataframe(df.head())

    # Summary stats
    st.subheader("📌 Summary Statistics")
    st.write(df.describe())

    # Visualization
    st.subheader("📈 Data Visualization")
    chart = st.selectbox("Choose Chart Type", ["Histogram", "Boxplot", "Scatterplot"])
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns.tolist()

    if chart == "Histogram":
        col = st.selectbox("Select column", numeric_cols)
        fig, ax = plt.subplots()
        df[col].hist(ax=ax, bins=20)
        st.pyplot(fig)

    elif chart == "Boxplot":
        col = st.selectbox("Select column", numeric_cols)
        fig, ax = plt.subplots()
        sns.boxplot(y=df[col], ax=ax)
        st.pyplot(fig)

    elif chart == "Scatterplot":
        x = st.selectbox("X-axis", numeric_cols)
        y = st.selectbox("Y-axis", numeric_cols)
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x=x, y=y, ax=ax)
        st.pyplot(fig)

    # Ask a question
    st.subheader("🤖 Ask a Question About the Data")
    question = st.text_input("Ask (e.g., 'average age', 'maximum score')")

    if st.button("Answer"):
        answered = False
        for col in numeric_cols:
            if col.lower() in question.lower():
                if "average" in question.lower():
                    st.success(f"Average {col}: {df[col].mean():.2f}")
                    answered = True
                elif "maximum" in question.lower():
                    st.success(f"Maximum {col}: {df[col].max()}")
                    answered = True
                elif "minimum" in question.lower():
                    st.success(f"Minimum {col}: {df[col].min()}")
                    answered = True
        if not answered:
            st.warning("I can only answer average, max, and min questions for numeric columns.")
else:
    st.info("Upload a CSV file to begin.")
