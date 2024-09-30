import streamlit as st
import pandas as pd


# Load data into DataFrame
df = pd.read_excel("team.xlsx", index_col=0)

# Title of the app
st.title("Football Teams Dataset Chat")

# Sidebar for user input
st.sidebar.header("Filter Options")

# Filtering by country
selected_country = st.sidebar.selectbox("Select a country", options=["All"] + df['country'].unique().tolist())
# Filtering by trophies
trophy_range = st.sidebar.slider("Select trophy range", 0, 15, (0, 5))

# Main area
st.write("### Dataset Overview")
st.dataframe(df)

st.write("### Filtered Results")
# Filter by selected country
filtered_df = df
if selected_country != "All":
    filtered_df = filtered_df[filtered_df['country'] == selected_country]

# Filter by trophy range
filtered_df = filtered_df[(filtered_df['trophies'] >= trophy_range[0]) & (filtered_df['trophies'] <= trophy_range[1])]

# Display the filtered results
st.dataframe(filtered_df)

# Chat-like interaction
user_input = st.text_input("Ask a question about the dataset (e.g., 'Which teams have more than 3 trophies?')")

# Simple keyword matching for queries
if user_input:
    user_input = user_input.lower()
    if "more than 3 trophies" in user_input:
        response = df[df['trophies'] > 3]
        st.write("### Teams with more than 3 trophies:")
        st.dataframe(response)
    elif "teams in england" in user_input:
        response = df[df['country'] == "England"]
        st.write("### Teams in England:")
        st.dataframe(response)
    elif "teams with 2 trophies" in user_input:
        response = df[df['trophies'] == 2]
        st.write("### Teams with exactly 2 trophies:")
        st.dataframe(response)
    else:
        st.write("### Sorry, I don't understand that question.")
