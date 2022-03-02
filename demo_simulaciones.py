# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 09:50:31 2022

@author: gbournigal
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px


calificaciones = ["A", "B", "C", "D1", "D2", "E"]


## Aquí se definen las probabilidades de transición para cada calificación.
## Pueden modificar esta para probar con diferentes escenarios.

select_matriz = st.sidebar.selectbox('Seleccionar Matriz', [1, 2])

if select_matriz == 1:

    A = [0.5, 0.5, 0, 0, 0, 0]
    B = [0.2, 0.2, 0.6, 0, 0, 0]
    C = [0, 0.2, 0.2, 0.6, 0, 0]
    D1 = [0, 0, 0.2, 0.2, 0.6, 0]
    D2 = [0, 0, 0, 0.2, 0.2, 0.6]
    E = [0, 0, 0, 0, 0.1, 0.9]

else:
    
    A = [0.7, 0.3, 0, 0, 0, 0]
    B = [0.25, 0.5, 0.25, 0, 0, 0]
    C = [0, 0.25, 0.5, 0.25, 0, 0]
    D1 = [0, 0, 0.25, 0.5, 0.25, 0]
    D2 = [0, 0, 0, 0.25, 0.5, 0.25]
    E = [0, 0, 0, 0, 0.1, 0.9]
    

cals_dict = dict({"A": A, "B": B, "C": C, "D1": D1, "D2": D2, "E": E})


def main():
    tab = st.sidebar.radio("Visualización", options=["Simple", "Múltiples Individuos"])

    df = pd.DataFrame(
        [A, B, C, D1, D2, E], columns=calificaciones, index=calificaciones
    )

    if tab == "Simple":
        st.header("Demo de simulación simple")
        st.subheader("Calificaciones Dummy")
        st.dataframe(df.style.format("{:.2%}"))

        with st.expander("Generador de Números Aleatorios"):
            with st.form("my_form"):
                st.write("Calificación Inicial")
                cal = st.selectbox("Calificación", options=calificaciones)

                submitted = st.form_submit_button("Ejecutar simulación")
            if submitted:
                random_num = np.random.uniform()
                st.markdown(
                    f"La calificación actual es: {cal}. El número aleatorio generado es: {random_num}"
                )
        with st.expander("Simulación de transición"):
            with st.form("my_form2"):
                st.write("Calificación Inicial, selección automática")
                cal2 = st.selectbox("Calificación", options=calificaciones)

                submitted2 = st.form_submit_button("Ejecutar simulación")
            if submitted2:
                random_cal = np.random.choice(calificaciones, 1, p=cals_dict[cal2])[0]
                st.markdown(
                    f"La calificación actual es: {cal2}. Se transicionó a la: {random_cal}"
                )
    else:
        st.header("Demo de simulación múltiples individuos")
        st.subheader("Calificaciones Dummy")
        st.dataframe(df.style.format("{:.2%}"))

        with st.form("form_mult"):
            st.write("Cantidad de individuos")
            st.write(
                "Se ejecuta la simulación por 12 meses para la cantidad de individuos seleccionada."
            )
            ind_cant = st.number_input("Cantidad de Individuos", min_value=1, value=1, max_value=50000)
            st.write("Por razones de rendimiento se limitó el número máximo a 50,000. Puede ajustarlo ejecutándolo de manera local.")

            # Every form must have a submit button.
            submitted2 = st.form_submit_button("Ejecutar simulación")
        if submitted2:
            individuos = simulation_individuos("A", ind_cant, 12)
            hist_df, indicador = final_counter(individuos, ind_cant)

            fig = px.histogram(
                hist_df,
                x=hist_df.index,
                y="cantidad",
                color_discrete_sequence=["indianred"],
            )
            fig.update_traces(hovertemplate="Calificación: %{x} <br>Cantidad: %{y}")
            fig.update_layout(
                template="simple_white",
                width=600,
                height=600,
                yaxis_title="Cantidad",
                xaxis_title="Calificación",
            )

            st.markdown("La calificación final de los deudores fue:")
            st.plotly_chart(fig, use_container_width=True)

            cant_E = int(hist_df.loc["E"])
            st.markdown(
                f"""La cantidad de deudores que alcanzaron E fueron: {cant_E:,}. 
                El indicador de la investigación sería: {indicador:.2%}."""
            )


def simulation_individuos(cal_inicial, individuos_cant, meses):
    """La calificación inicial de donde empieza la simulacón.
    La cantidad de indiviuos.
    La cantidad de meses que se simularán para cada uno.
    Esta función podría ser modificada para incluir diferentes proporciones
    para cada calificación. Ahora mismo sería 100% para cal_inicial."""

    individuos = []

    for i in range(individuos_cant):
        serie = []
        random_cal = cal_inicial
        serie.append(cal_inicial)
        for i in range(meses - 1):
            random_cal = str(
                np.random.choice(calificaciones, 1, p=cals_dict[random_cal])[0]
            )
            serie.append(random_cal)
        individuos.append(serie[meses - 1])
    return individuos


def final_counter(cadena_cals, individuos_cant):
    """Recibe la cadena de calificaciones finales de una simulación.
    Lo convierte en dataframe con el conteo de cada calificación final
    y en el estimador del paper, % que terminan en E.
    """
    hist_df = dict()
    for i in calificaciones:
        hist_df[i] = int(cadena_cals.count(i))
    cant_E = hist_df["E"]
    indicador = cant_E / individuos_cant
    hist_df = pd.DataFrame.from_dict(hist_df, orient="index", columns=["cantidad"])
    return hist_df, indicador


if __name__ == "__main__":
    main()
