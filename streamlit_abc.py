import streamlit as st
import pandas as pd

# Title of the Streamlit App
st.title("Movie Recommendation System")

# About section
if st.button("ABOUT"):
    st.text("A movie recommendation system suggests movies to users based on their preferences and behaviors.\n "
            "These systems enhance user experience by providing personalized movie recommendations\n, "
            "helping users discover films they are likely to enjoy.")

# Load association rules
try:
    dfr1 = pd.read_csv(r'C:\Users\DELL\Downloads\New folder\rules1_inoice (1).csv', index_col=0)
except FileNotFoundError:
    st.error("The CSV file 'rules1_invoice.csv' was not found. Please check the file path.")
    st.stop()

# Display the DataFrame
st.write("Association Rules DataFrame:")
st.write(dfr1.head())

# Display antecedents value counts
st.write("Antecedents Value Counts:")
st.write(dfr1['antecedents'].value_counts())

# Load merged data
try:
    dfDF = pd.read_csv(r'C:\Users\DELL\Downloads\New folder\rules1_inoice (1).csv')  # Adjust the path as needed
except FileNotFoundError:
    st.error("The CSV file 'merged_data.csv' was not found. Please check the file path.")
    st.stop()

# User input for movie name
movie_name = st.text_input("Enter the name of a movie you have watched:")

if st.button("Get Recommendations"):
    # Provide recommendations based on user input
    if movie_name:
        recommendations = dfr1[dfr1['antecedents'].apply(lambda x: movie_name in x)]['consequents']
        if not recommendations.empty:
            st.write(f"Recommendations based on {movie_name}:")
            for rec in recommendations.head(4):  # Limit to 4 recommendations
                st.write(rec)
        else:
            st.write("Movie not found in the antecedents. Please select a movie from the available list.")
    else:
        st.write("Please enter a movie name to get recommendations.")

# Button to show the most recommended movie based on support
if st.button("Show Most Recommended Movie"):
    b = dfr1['support'].max()
    c = dfr1[dfr1['support'] == b]
    st.write("The most recommended movie based on support:")
    st.write(c)
