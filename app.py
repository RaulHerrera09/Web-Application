import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

st.write(" Visualización de datos de vehículos ")

# Casilla para construir histograma
build_histogram = st.checkbox('Construir un histograma')

if build_histogram:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer",
                       title="Distribución del kilometraje (odometer)")
    st.plotly_chart(fig, use_container_width=True)

# Casilla para construir gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Creación de un gráfico de dispersión: precio vs kilometraje')
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title="Relación entre precio y kilometraje")
    st.plotly_chart(fig2, use_container_width=True)
