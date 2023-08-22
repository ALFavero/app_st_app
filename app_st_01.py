# -*- coding: utf-8 -*-
"""
python3 -m streamlit run App_ST_01.py

App estudo Python com Streamlit e Github - Video Curso - Mariane Neivas (EBAC)
Author: André L. Favero
"""
import pandas as pd
import streamlit as st
import plotly.express as pt

df = pd.read_csv('Objetos.csv', sep=';', usecols=('Objeto','Cor','Qtde'))

objetos = list(df.Objeto.unique())
cores = list(df.Cor.unique())
df['Qtde']=pd.to_numeric(df['Qtde'])

opcao = st.sidebar.multiselect('Escolha o que deseja:',['Tabela','Grafico'], ['Tabela','Grafico'])

def exibir(df = df, objetos = objetos, cores = cores, op = opcao):
    
    obj = st.sidebar.selectbox('Escolha o Objeto', ['Todos'] + objetos)
    cor = st.sidebar.selectbox('Escolha a Cor', ['Todas'] + cores)
  
    if (obj != 'Todos'):
        st.subheader('Exibindo Objeto:  ' + obj)
        df = df[df['Objeto']== obj]
    else:
        st.subheader('Todos os Objetos!')

    if (cor != 'Todas'):
        st.subheader('Exibindo Cor:  ' + cor)
        df = df[df['Cor'] == cor]
    else:
        st.subheader('Todas as Cores!')

#Tabela
    if(op == ['Tabela'] or op == ['Tabela','Grafico'] or op == ['Grafico', 'Tabela']):
        st.text('Tabela de Dados:')
        st.table(df)

#Grafico
    if(op == ['Grafico'] or op == ['Tabela','Grafico'] or op == ['Grafico', 'Tabela']):
        dfShow = df.groupby(by = ['Qtde']).sum()
        figura = pt.line(dfShow, x=dfShow.index, y=['Objeto', 'Cor'], labels={'Qtde':'Quantidade', 'value': 'Objetos e Cores'})
        figura.update_layout(title='Dados dos Objetos')
        st.plotly_chart(figura, use_container_width=True)

        
exibir()