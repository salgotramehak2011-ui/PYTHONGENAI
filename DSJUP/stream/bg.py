# import streamlit as st
# import base64

# st.set_page_config(page_title='BG Img')

# with open('img.jpg','rb') as file:
#     image = file.read()
# img = base64.b64encode(image).decode()


# css = f"""
#     <style>
#     [data-testid ="" ] 
#     """ 

import streamlit as st
import base64

st.set_page_config(page_title='BG Img')

# Read and encode image
with open('img.jpg', 'rb') as file:
    image = file.read()
img = base64.b64encode(image).decode()

# Apply as background using CSS
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("Background Image Applied")
st.write("Now your app has a background image 🎉")
