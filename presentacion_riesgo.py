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

matriz = st.sidebar.radio("Matriz de ejemplo:", options=["1", "2"])

if matriz == "1":
    A = [0.5, 0.5, 0, 0, 0, 0]
    B = [0.2, 0.2, 0.6, 0, 0, 0]
    C = [0, 0.2, 0.2, 0.6, 0, 0]
    D1 = [0, 0, 0.2, 0.2, 0.6, 0]
    D2 = [0, 0, 0, 0.2, 0.2, 0.6]
    E = [0, 0, 0, 0, 0.1, 0.9]
else:
    A = [0.8, 0.2, 0, 0, 0, 0]
    B = [0.2, 0.5, 0.3, 0, 0, 0]
    C = [0, 0.2, 0.5, 0.3, 0, 0]
    D1 = [0, 0, 0.2, 0.5, 0.3, 0]
    D2 = [0, 0, 0, 0.2, 0.5, 0.3]
    E = [0, 0, 0, 0, 0.1, 0.9]
cals_dict = dict({"A": A, "B": B, "C": C, "D1": D1, "D2": D2, "E": E})

tab = st.sidebar.radio(
    "Visualización", options=["Simple", "Múltiples Períodos", "Múltiples Individuos"]
)

df = pd.DataFrame([A, B, C, D1, D2, E], columns=calificaciones, index=calificaciones)

if tab == "Simple":
    st.header("Demo de simulación simple")
    st.subheader("Calificaciones Dummy")
    st.dataframe(df.style.format("{:.2%}"))

    with st.expander("Generador de Números Aleatorios"):
        with st.form("my_form"):
            st.write("Calificación Inicial")
            cal = st.selectbox("Calificación", options=calificaciones)

            # Every form must have a submit button.
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

            # Every form must have a submit button.
            submitted2 = st.form_submit_button("Ejecutar simulación")
        if submitted2:
            random_cal = np.random.choice(calificaciones, 1, p=cals_dict[cal2])[0]
            st.markdown(
                f"La calificación actual es: {cal2}. Se transicionó a la: {random_cal}"
            )
elif tab == "Múltiples Períodos":
    st.header("Demo de simulación múltiples períodos")
    st.subheader("Calificaciones Dummy")
    st.dataframe(df.style.format("{:.2%}"))

    with st.form("form_mult"):
        st.write("Períodos de la simulación")
        simulaciones = st.number_input("Períodos", min_value=1, value=1)

        # Every form must have a submit button.
        submitted2 = st.form_submit_button("Ejecutar simulación")
    if submitted2:
        serie = []
        random_cal = "A"
        serie.append("A")
        for i in range(simulaciones - 1):
            random_cal = str(
                np.random.choice(calificaciones, 1, p=cals_dict[random_cal])[0]
            )
            serie.append(random_cal)
        st.markdown(serie)
else:
    st.header("Demo de simulación múltiples individuos")
    st.subheader("Calificaciones Dummy")
    st.dataframe(df.style.format("{:.2%}"))

    with st.form("form_mult"):
        st.write("Cantidad de individuos")
        ind_cant = st.number_input("Cantidad de Individuos", min_value=1, value=1)

        # Every form must have a submit button.
        submitted2 = st.form_submit_button("Ejecutar simulación")
    if submitted2:
        individuos = []

        for i in range(ind_cant):
            serie = []
            random_cal = "A"
            serie.append("A")
            for i in range(11):
                random_cal = str(
                    np.random.choice(calificaciones, 1, p=cals_dict[random_cal])[0]
                )
                serie.append(random_cal)
            individuos.append(serie[11])
        hist_df = dict()
        for i in calificaciones:
            hist_df[i] = int(individuos.count(i))
        cant_E = hist_df["E"]
        indicador = cant_E / ind_cant
        hist_df = pd.DataFrame.from_dict(hist_df, orient="index", columns=["cantidad"])
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

        st.markdown(
            f"La cantidad de deudores que alcanzaron E fueron: {cant_E:,}. El indicador de la investigación sería: {indicador:.2%}"
        )
