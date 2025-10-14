import pandas as pd
import plotly.express as px
import streamlit as st


st.set_page_config(
    page_title="Visualización de Datos de Vehículos", layout="wide")
st.title(" Visualización Interactiva de Datos de Vehículos")


car_data = pd.read_csv('vehicles_us.csv')


st.sidebar.header("🔍 Filtros")

# Filtro por tipo de vehículo
types = car_data['type'].dropna().unique()
selected_type = st.sidebar.multiselect(
    "Selecciona el tipo de vehículo:", types, default=types)

# Filtro por combustible
fuels = car_data['fuel'].dropna().unique()
selected_fuel = st.sidebar.multiselect(
    "Selecciona el tipo de combustible:", fuels, default=fuels)

# Filtro por año
min_year, max_year = int(car_data['model_year'].min()), int(
    car_data['model_year'].max())
year_range = st.sidebar.slider(
    "Selecciona el rango de años del modelo:", min_year, max_year, (min_year, max_year))

# Aplicar filtros
filtered_data = car_data[
    (car_data['type'].isin(selected_type)) &
    (car_data['fuel'].isin(selected_fuel)) &
    (car_data['model_year'].between(year_range[0], year_range[1]))
]

st.markdown("###  Datos filtrados")
st.write(f"Total de vehículos mostrados: {len(filtered_data)}")
st.dataframe(filtered_data.head())

st.divider()


st.subheader(" Gráficos interactivos")

col1, col2 = st.columns(2)

# Histograma
with col1:
    if st.checkbox('Construir un histograma'):
        st.write('Distribución del kilometraje (odometer)')
        fig = px.histogram(filtered_data, x="odometer", nbins=50,
                           title="Distribución del kilometraje",
                           labels={'odometer': 'Kilometraje'})
        st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión
with col2:
    if st.checkbox('Construir un gráfico de dispersión'):
        st.write('Relación entre precio y kilometraje')
        fig2 = px.scatter(filtered_data, x="odometer", y="price", color="type",
                          title="Precio vs Kilometraje (según tipo de vehículo)",
                          labels={'odometer': 'Kilometraje', 'price': 'Precio (USD)'})
        st.plotly_chart(fig2, use_container_width=True)

st.divider()


st.subheader(" Gráficos adicionales")

col3, col4 = st.columns(2)

# Precio promedio por tipo de vehículo
with col3:
    if st.checkbox("Mostrar gráfico de precio promedio por tipo de vehículo"):
        avg_price = filtered_data.groupby('type')['price'].mean(
        ).reset_index().sort_values('price', ascending=False)
        fig3 = px.bar(avg_price, x='type', y='price', color='price',
                      title='Precio promedio por tipo de vehículo',
                      labels={'type': 'Tipo de vehículo', 'price': 'Precio promedio (USD)'})
        st.plotly_chart(fig3, use_container_width=True)


# Gráfico de pastel de tipos de vehículos
with col4:
    if st.checkbox("Mostrar gráfico de pastel de tipos de vehículos"):

        type_counts = filtered_data['type'].value_counts().reset_index()

        type_counts.columns = ['type', 'count']

        # Crear gráfico de pastel
        fig4 = px.pie(
            type_counts,
            names='type',
            values='count',
            title='Distribución porcentual de los tipos de vehículos',
            hole=0.3,
            color_discrete_sequence=px.colors.qualitative.Set3
        )

        # Mostrar gráfico en Streamlit
        st.plotly_chart(fig4, use_container_width=True)


st.markdown(" *Proyecto creado con Streamlit y Plotly. Puedes combinar los filtros para explorar patrones específicos en el mercado de vehículos usados.*")
