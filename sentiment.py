import streamlit as st  
from textblob import TextBlob  
from streamlit_extras.let_it_rain import rain  

# Title of the web app
st.title("A Simple Sentiment Analysis WebApp.")

# Text area for user input
t = st.text_area("Please Enter your text")

# Button to analyze the sentiment
if st.button("Analyze the Sentiment"):
    if t:  # Check if text is provided
        blob = TextBlob(t)  
        result = blob.sentiment  
        polarity = result.polarity  
        subjectivity = result.subjectivity  
        
        # Display the results
        st.write(result)
        
        if polarity < 0:  
            st.warning(f"The given text has negative sentiments associated with it: {polarity}")  
            rain(
                emoji="😭",  
                font_size=20,  
                falling_speed=3,  
                animation_length="infinite"  
            )  
        else:  
            st.success(f"The given text has positive sentiments associated with it: {polarity}")  
            rain(
                emoji="😊",  
                font_size=20,  
                falling_speed=3,  
                animation_length="infinite"  
            )  
    else:
        st.warning("Please enter some text to analyze.")
