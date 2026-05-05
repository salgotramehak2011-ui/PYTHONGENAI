import streamlit as st 
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px 
import base64
st.set_page_config(page_title='Zomato Page', page_icon='🏠')

df=pd.read_csv('zomato_dataset.csv')
# st.write(df.shape)
# df.dropna(axis=0, inplace=True)
# st.write(df.shape)
df.drop_duplicates(inplace=True)
# st.write(df.shape)
# st.write(df)

res_index= df.loc[:,'Restaurant_Name',].value_counts().index
# st.write(res_index)

with st.sidebar:
    selected_res= st.selectbox(label='Select Restaurant', options=res_index)
    
df_selected= df[df.loc[:,'Restaurant_Name']==selected_res]
print(df_selected.columns)
df_selected=df_selected.sort_values(by='Votes',ascending=False)
st.write(df_selected)


ch=px.bar(df_selected[:20], x='Item_Name', y='Votes', color='City')
st.plotly_chart(ch)

ch2=px.pie(df_selected[:20], names='Item_Name', values='Votes', color='City')
st.plotly_chart(ch2)

    