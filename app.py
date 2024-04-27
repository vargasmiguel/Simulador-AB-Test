import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(layout="wide",
    page_title="Simulador A/B Test",
    page_icon="🆎"
)

ct=st.columns([3,5])
with ct[0]:
    st.image("abtest.png",width=300)
with ct[1]:
    st.html('''<h1><strong>Simulador de Pruebas A/B</strong></h1>
<p><strong>Curso:</strong> Gesti&oacute;n de Proyectos para la Anal&iacute;tica</p>
<p><strong>Profesor:</strong> Miguel Vargas</p>''')
st.divider()

st.html('''<h3 style="text-align: center;">Configuraci&oacute;n</h3>''')

n_trials=st.number_input("Cantidad de Ensayos",10,100,20)
col=st.columns(3)
with col[0]:
    c=st.slider("Rango de Clicks", 10000,30000, value=(15000, 20000), step=1)
    ti=st.slider("Rango de Tiempo en página (seg)", 5, 600, value=(10, 300))
with col[1]:
    con=st.slider("Rango de Conversiones", 1000, 10000, value=(1000, 4000), step=1)
    ret=st.slider("Rango Porcentaje de Retorno de usuarios", 0.0, 100.0, value=(10.0, 46.0), step=0.1)
with col[2]:
    v=st.slider("Rango de Visitas", 30000,90000, value=(40000, 60000), step=1)
    up=st.slider("Rango de Unidades por Transacción", 0,8, value=(1, 5), step=1)

def generar_datos(trial):
  # Generar datos para cada columna
  clicks = np.random.randint(c[0],c[1])
  conversions = np.random.randint(con[0],con[1])
  seg= np.random.randint(ti[0],ti[1])
  m=seg // 60
  s=seg % 60
  time_on_page = "00:{:02d}:{:02d}".format(m,s)
  returning_customers = str(np.random.randint(ret[0], ret[1]))+"%"
  visits = np.random.randint(v[0],v[1])
  units_per_transaction = np.random.randint(up[0],up[1])

  # Crear un diccionario con los datos
  datos = {
    "Ensayo": trial,
    "Clicks": clicks,
    "Conversiones": conversions,
    "Tiempo en página": time_on_page,
    "Retorno de usuarios": returning_customers,
    "Visitas": visits,
    "Unidades por Transacción": units_per_transaction
  }

  return datos




if st.button("Generar Datos", type="primary", use_container_width=True):
    # Generar datos para 20 trials
    datos_trials = []
    for i in range(2, 2*n_trials+2):
        if i % 2 == 1:
            trial = "B{}".format((i) // 2)
        else:
            trial = "A{}".format((i+1) // 2)
        datos_trials.append(generar_datos(trial))

    # Crear DataFrame de Pandas
    df_trials = pd.DataFrame(datos_trials)

    # Mostrar el DataFrame
    st.divider()
    st.html('''<h3 style="text-align: center;">Datos de Simulaci&oacute;n</h3>''')
    st.dataframe(df_trials, hide_index=True, use_container_width=True)

st.divider()
st.write("Construido sólo para fines educativos")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.html(hide_st_style)