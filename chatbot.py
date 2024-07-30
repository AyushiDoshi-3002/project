import streamlit as st
import google.generativeai as genai

# Set the API key directly
api_key = "AIzaSyBE4HBk2Uw24urRk9QGMmXomlOlA8hs0Ws"
genai.configure(api_key=api_key)

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])


# Function to get response from the Gemini model
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If ask button is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        print("_" * 80)

    st.write(chat.history)
