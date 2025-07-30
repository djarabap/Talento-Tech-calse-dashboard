import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='centered', 
                    page_title='Talento Tech',
                    page_icon = ':smile:')

t1, t2 = st.columns([0.7, 0.3])
t1.image('jara.jfif',width=3200)
#t1.image('davi.jpg',width=3200)
t2.title('Mi Primer Tablero')
t2.markdown('**tel:** 131313 **| email:** david.jaraba@udea.edu.co')

#Secciones
steps = st.tabs(['Pestaña','Pestaña 2', 'Pestaña $\sqrt{9}$'])

with steps[0]:
    st.markdown('Geo-Localizacón de Proyectos')
    st.write('Hola Mundo')
    st.image('pinzon.png',width=200)
    data={'Nombre': ['Adan', 'Eva', 'Cain', 'Abel'], 'fecha de nacimiento': [0,0,3,4]}
    df=pd.DataFrame(data)
    st.table(df)
    st.dataframe(df)

with steps[0]:
    camp_df = pd.read_csv('Campanhas.csv', encoding='latin-1',sep=';')
    camp = st.selectbox('Escoge un ID de campana',camp_df['ID_Campana'], help='Muestra las campanas existentes')
    met_df = pd.read_csv('Metricas.csv', encoding='latin-1', sep=';')
    m1, m2, m3 = st.columns([1,1,1])

    id1 = met_df[(met_df['ID_Campana']== camp)]
    id2 = met_df[met_df['ID_Campana']== camp]
    m1.write('Métricas filtradas')
    m1.metric(label='Métrica 1', value=sum(id1['Conversiones']), 
              delta=str(sum(id1['Rebotes']))+'Total de Rebotes',
              delta_color='inverse')
    m2.metric(label= 'Metrica 2', value=np.mean(id1['Clics']),
              delta=str(np.mean(id1['Impresiones']))+ 'promedios',
              delta_color='inverse')
#with steps[1]:
    #id st.button('podemos usar botones', type='primary')






