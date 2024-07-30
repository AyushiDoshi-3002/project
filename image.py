import streamlit as st
import google.generativeai as genai
from PIL import Image

# Set the API key directly in the code
api_key = "AIzaSyBE4HBk2Uw24urRk9QGMmXomlOlA8hs0Ws"
genai.configure(api_key=api_key)

# Function to load the Gemini model and get responses
def get_gemini_response(input_text, image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input_text != "":
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Initialize the Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me about the image")

# If ask button is clicked
if submit:
    response = get_gemini_response(input_text, image)
    st.subheader("The Response is")
    st.write(response)
