## Web-Application 

Esta aplicación web está diseñada para analizar datos de anuncios de venta de vehículos de forma interactiva. Utiliza Streamlit como marco principal para crear una interfaz amigable y dinámica, y Plotly Express para generar gráficos visuales e intuitivos.

En la aplicación, el usuario puede cargar el conjunto de datos vehicles_us.csv y explorar la información desde su navegador sin necesidad de escribir código. Se añadieron casillas de verificación que permiten construir distintos tipos de gráficos:

Histograma: muestra la distribución del kilometraje (odometer), ayudando a visualizar qué rangos son los más comunes entre los vehículos.

Gráfico de dispersión: representa la relación entre el precio (price) y el kilometraje, lo que permite observar tendencias o patrones, como la disminución del precio a medida que aumenta el kilometraje.

Gráfico de barras: presenta el precio promedio por tipo de vehículo, lo que facilita comparar cuáles categorías (sedán, SUV, camioneta, etc.) tienden a tener un costo más alto.

Gráfico de pastel (donut): muestra la distribución porcentual de los tipos de vehículos, permitiendo entender qué categorías son más frecuentes dentro del mercado.

Además, se incorporaron filtros interactivos que permiten seleccionar el tipo de vehículo, el tipo de combustible y el rango de años del modelo. Estos filtros hacen que los gráficos se actualicen automáticamente según las opciones elegidas, ofreciendo una experiencia de análisis personalizada y flexible.


