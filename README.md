# 🚗 Vehicle Market Insights Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75)
![Status](https://img.shields.io/badge/Status-Live-success)

> **🚀 LIVE DEMO:** [Click aquí para probar la aplicación en tiempo real](https://vehicle-market-insights-dashboard.streamlit.app/)

---

## 📌 Contexto & El Problema (The Challenge)
El mercado de vehículos usados suele ser opaco. Los compradores se enfrentan a precios inconsistentes y falta de información centralizada, lo que dificulta saber si un vehículo tiene un "precio justo" o si está sobrevalorado.

El objetivo de este proyecto fue **procesar un dataset masivo (+47,000 registros)** con datos "sucios" y no estructurados, para crear una herramienta que democratice la valoración de mercado, permitiendo identificar tendencias de depreciación y anomalías de precios en segundos.

## 🛠 Solución Técnica (Technical Implementation)
Diseñé una arquitectura de datos completa utilizando Python, enfocada en el rendimiento y la interactividad:

### 1. Ingeniería de Datos (ETL con Pandas)
* **Limpieza:** Se eliminaron valores nulos y duplicados que sesgaban el análisis.
* **Normalización:** Estandarización de nombres de modelos y fabricantes.
* **Tratamiento de Outliers:** Identificación de precios irreales (ej. coches a $0 o $1,000,000 irrelevantes) para asegurar estadísticas fiables.

### 2. Visualización Interactiva (Plotly Express)
En lugar de gráficos estáticos, implementé gráficos dinámicos que permiten al usuario explorar los datos:
* **Histogramas de Distribución:** Para visualizar la frecuencia de precios y kilometraje por marca.
* **Scatter Plots (Dispersión):** Análisis de correlación *Precio vs. Kilometraje* con diferenciación por colores según la condición del vehículo.

### 3. Despliegue & Optimización (Streamlit)
* Uso de `st.cache_data` para cargar los 47k registros en memoria una sola vez, permitiendo filtrados instantáneos sin recargar la página.
* Interfaz web responsive desplegada en **Streamlit Cloud**.

## 📊 Resultados e Impacto
* **Eficiencia:** Reducción del tiempo de investigación de mercado de horas a segundos.
* **Transparencia:** Visualización clara de la curva de depreciación de vehículos.
* **Accesibilidad:** Herramienta 100% web, accesible desde cualquier dispositivo sin instalación.

---

## 💻 Instalación y Uso Local

Si deseas correr este proyecto en tu propia máquina:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/RaulHerrera09/Web-Application.git](https://github.com/RaulHerrera09/Web-Application.git)
   cd Web-Application

2. **Crear un entorno virtual (Opcional pero recomendado):**

Bash

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
3. **Instalar dependencias:**

Bash

pip install -r requirements.txt
4. **Ejecutar la aplicación:**

Bash

streamlit run app.py

## 📂 Estructura del Proyecto

├── .streamlit/          # Configuración de tema (opcional)
├── notebooks/           # Jupyter Notebooks con el análisis exploratorio (EDA)
├── vehicles_us.csv      # Dataset original
├── app.py               # Lógica principal de la aplicación Streamlit
├── requirements.txt     # Librerías necesarias
└── README.md            # Documentación del proyecto





