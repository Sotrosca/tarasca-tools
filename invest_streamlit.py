import streamlit as st
from utils import simular_inversion, calcular_precio_con_inflacion

color_activo = 'orange'
color_inversion = 'skyblue'

# Create a title and a sidebar
st.title('Investment simulator')
st.sidebar.title('Investment simulator')

# On sidebar add an int input with label 'Monto inicial'
monto_inicial = st.sidebar.number_input('Monto inicial', min_value=0, value=int(176e3))

# On sidebar add an input with label 'Precio del activo'
precio_activo = st.sidebar.number_input('Precio del activo', min_value=0, value=12038792)

# On sidebar add a slider with label 'Meses'
meses = st.sidebar.slider('Meses', min_value=1, max_value=96, value=50)

# On sidebar add a slider with label 'Tasa nominal anual' with limits 0.0 and 5.0
tna = st.sidebar.slider('Tasa nominal anual', min_value=0.0, max_value=5.0, value=0.54)

# On sidebar add a slider with label 'Inflacion mensual' with limits 0.0 and 0.1 and step 0.005
inflacion_mensual = st.sidebar.slider('Inflacion mensual', min_value=0.000, max_value=0.100, value=0.035, step=0.005, format='%0.3f')

# On sidebar add a checkbox with label 'Agregar monto inicial por mes'
agregar_monto_inicial_por_mes = st.sidebar.checkbox('Agregar monto inicial por mes', value=True)

# Simulate an investment
tenencia_por_mes, montos_agregados = simular_inversion(monto_inicial, meses, tna, agregar_monto_inicial_por_mes, inflacion_mensual)

# Calculate the price of the asset with inflation
precio_activo_con_inflacion = calcular_precio_con_inflacion(precio_activo, meses, inflacion_mensual)

# Plot the results
st.plotly_chart({
    'data': [
    {
        'x': list(range(0, meses + 1)),
        'y': precio_activo_con_inflacion,
        'name': 'Precio del activo con inflacion',
        'mode': 'lines',
        'line': {
            'color': color_activo,
            'width': 2
        }
    
    },
    {
        'x': list(range(0, meses + 1)),
        'y': tenencia_por_mes,
        'name': 'Tenencia por mes',
        'mode': 'lines',
        'line': {
            'color': color_inversion,
            'width': 2
        }
    }, 
],
    'layout': {
        'title': 'Simulación de inversión',
        'xaxis': {'title': 'Meses'},
        'yaxis': {'title': 'Monto'}
    },
})

# Plot montos agregados
st.plotly_chart({
    'data': [{
        'x': list(range(0, meses + 1)),
        'y': montos_agregados,
        'name': 'Montos agregados',
        'mode': 'lines',
        'line': {
            'color': color_inversion,
            'width': 2
        }
    }],
    'layout': {
        'title': 'Montos agregados',
        'xaxis': {'title': 'Meses'},
        'yaxis': {'title': 'Monto'}
    },
})

# Plot total montos agregados
st.plotly_chart({
    'data': [{
        'x': list(range(0, meses + 1)),
        'y': [sum(montos_agregados[:i]) for i in range(0, meses + 1)],
        'name': 'Total montos agregados',
        'mode': 'lines',
        'line': {
            'color': color_inversion,
            'width': 2
        },
    }],
    'layout': {
        'title': 'Total montos agregados',
        'xaxis': {'title': 'Meses'},
        'yaxis': {'title': 'Monto'}
    },
})

