# coding: utf-8

""" Create on: 2022-02-08

# @author: Denner

"""

# Import libs #
import pandas as pd
import streamlit as st


df = pd.read_csv('covid-variants.csv')

pais = list(df['location'].unique())
variante = list(df['variant'].unique())

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')


pais = st.sidebar.selectbox('Selecione o país', ['Todos'] + pais)
variante = st.sidebar.selectbox('Selecione a variante', ['Todas'] + variante)


if(pais != 'Todos'):
    st.text('Mostrando resultado de' + pais)
    df = df[df['location'] == pais]

if(variante != 'Todas'):
    st.text('Mostrando resultado de' + variante)
    df = df[df['variant'] == variante]

dfShow = df.groupby(by = ['date']).sum()


#Figure
import plotly.express as px

fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title_text='Casos de Covid-19')
st.plotly_chart(fig, use_container_width=True)