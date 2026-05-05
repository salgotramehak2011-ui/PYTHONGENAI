# to use in streamlit

import streamlit as st
import requests
from PIL import Image
from io import BytesIO
url = "https://95be-34-91-17-127.ngrok-free.app/generate"
with st.form(key='my-form'):
    prompt= st.text_input("Enter Prompt ")

    if st.form_submit_button("Submit"):
        response = requests.post(url, data={"prompt_instructions": prompt})
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image)
            image.save("output.png")  # Save to file
        else:
            print("Error:", response.text)