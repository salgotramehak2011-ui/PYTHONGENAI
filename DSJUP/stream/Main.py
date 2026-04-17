import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Main page', layout='centered')
st.header('Streamlit header')
st.subheader('This is the subheading')
st.write('Write paragraph here...')

## forms
st.text_input(label='Email')
st.number_input('Age')

# with st.form(key='forms'):
#     mail = st.text_input('Email', placeholder = 'Enter Email here...')
#     pwd = st.text_input('Password', placeholder ='Enter password', type='password')
#     btn = st.form_submit_button('Submit')
with st.form(key='forms'):
    col1,col2 = st.columns(2)
    with col1:
        name = st.text_input('First Name')
        mail = st.text_input('Email', placeholder='Enter Email here...')
        age = st.number_input('Age')
    with col2:
        lname= st.text_input('Last Name')
        pwd = st.text_input('Password',placeholder='Enter Password', type='password')
        gender = st.radio(label='Gender', options=['Male','Female'],index=0,horizontal=True)
    address = st.text_area('Address')
    terms = st.checkbox('Terms and Conditions')
    state = st.selectbox('State',options=['Punjab','HP','Haryana','UP'],index=3)
    hobbies = st.multiselect('Hobbies',options=['Reading','Watching Movie','Playing Cricket', 'Singing','Writing'])
    btn = st.form_submit_button('Submit')

if btn:
    st.write(mail, pwd)

# SideBar
with st.sidebar:
    st.header('header')
    # opt = st.selectbox('Menu',options=['Home','About','Info'])
    # opt = option_menu(menu_title='Menu',options=['Home','About','Info'])
    opt = option_menu(menu_title='Menu',options=['Home','About','Info'],orientation='horizontal',icons = ['house-fill', 'phone-fill', 'info-circle'])

if opt=='Home':
    st.header('Home page')
elif opt=='About':
    st.header('About page')
elif opt=='Info':
    st.header("Info page")
