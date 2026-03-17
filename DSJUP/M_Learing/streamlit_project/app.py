import streamlit as st
# st.title('My Streamlit App ')
# st.write('Welcome to my streamlit app!')

# # # text columns
# st.header('Header')
# st.subheader('Subheader')
# st.text('This is a text element')
# st.markdown('**This is a markdown element**')

# #Displaying the data
# import pandas as pd
# data = {
#     "Name" : ['Alice','Bob','Charlie'],
#     "Age": [12,13,14],
#     "City": ['New York','Los Angeles','Chircago']
# }
# df = pd.DataFrame(data)
# st.title("DataFrame Example")
# st.write('Here is a sample DataFrame')
# st.dataframe(df)

# Interactive widgets 

# st.title("Interactive widgets")
# name = st.text_input("Enter your name: ")
# age = st.number_input("Enter your age: ", min_value=0, max_value=120)

# if st.button("Submit"):
#     st.write(f"Hello,{name}You are{age} years old.")

# Sliders example
# st.title('Slider Example')
# value = st.slider("Selct a number:", 10,100,50)
# value2 = st.slider("Select a range:", min_value=0, max_value=100, value=(20,80))

# st.write(f"You selected: {value}")
# st.write(f"You select the range: {value2}")

# SideBar examples
st.title("Sidebar Example")
age = st.sidebar.number_input("Enter your age:", min_value=0, max_value=120)
st.sidebar.write(f"You selected: {age}")

mode = st.sidebar.selectbox("Select a mode:", ["Light","Dark"])
st.sidebar.write(f"You selected: {mode}")

feature = st.sidebar.multiselect("Select features:", ["features A","features B","features C"])
st.sidebar.write(f"You selected: {feature}")

# Chart Example
# st.title("Chart Example")
# import numpy as np
# import pandas as pd


# data= pd.DataFrame(
#     np.random.randn(100, 3),
#     columns=["A", "B", "C"]
# )

# st.line_chart(data)
# st.bar_chart(data)
# st.area_chart(data)


# st.title("Uploading the Data")

# file = st.file_uploader("Upload a CSV file", type=["csv"])

# if file is not None:
#     import pandas as pd

#     df = pd.read_csv(file)
#     st.write("DataFrame:")
    # st.dataframe(df)