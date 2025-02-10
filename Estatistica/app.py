import streamlit as st
import pandas as pd
import openpyxl
import matplotlib.pyplot as plt

st.title('Marketing Analytics')
st.text('Esse dashboard resume os dados das campanhas de marketinkg para melhores tomadas de decisões')

uploaded_file = st.file_uploader('coloque o seu file aqui')

if uploaded_file:
    # df = pd.read_csv(uploaded_file)
    df = pd.read_excel(uploaded_file)
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())

    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Reach'], y=df['Likes'])
    ax.set_xlabel('Alcance')
    ax.set_ylabel('Like')

    st.pyplot(fig)

 