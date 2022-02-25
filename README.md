# Demo simulación de transiciones

## Objetivo
En este repositorio se comparte el demo utilizado en la [presentación](https://www.youtube.com/watch?v=cSCZq9XgS_Y&t=1180s) realizada en el [Club de Gestión de Riesgos de la República Dominicana](https://gestionderiesgo.org/). El objetivo principal es mostrar de manera sencilla como se realizan las simulaciones de transición de calificación de riesgos en base a una matriz de probabilidad. 

## Organización del repositorio
Tiene dos documentos principales:
  - **demo_simulaciones.py**: Documento de python que contiene el demo. Utiliza el framework [streamlit](https://streamlit.io/) para convertir un script de python en un web app.
  - **excel_simulaciones**: Documento de excel que replica el demo.
  - **requirements.txt**: Los requerimientos de las librerías de python necesarias para poder ejecutar el demo de forma local.

## Streamlit en la nube:
Puede acceder a la aplicación en la nube a través de: [Demo Trancisiones App](https://share.streamlit.io/sbrd-estudios-pub/demo_transition_simulation/main/demo_simulaciones.py)

## Guía para ejecutar archivo de python local y realizar cambios

- Realizar fork al repositorio o descargar la carpeta para tenerla de forma local. 
- Tener Python (versión 3.9 en adelante) e instalar los requerimientos necesarios. Utilizando pip sería:
  - pip install -r requirements.
- Ejecutar el streamlit: 
  - streamlit run demo_simulaciones.py. 
  - Más información de [como ejecutar streamlit](https://docs.streamlit.io/knowledge-base/using-streamlit/how-do-i-run-my-streamlit-script).

## Guía archivo de Excel

El archivo contiene tres hojas:

- **matriz**: Contiene la matriz de probabilidades de transición. Las celdas de la matriz pueden ser editadas para generar diferentes escenarios (las filas siempre deben sumar 1 o dará error). De la fila 8 hacia abajo no debe editarse.
- **calificaciones**: Hoja donde se realizan las simulaciones. No debe editarse.
- **summary**: Hoja con los resultados. No debe editarse.

Los cálculos automáticos fueron deshabilitados para evitar que se ejecutara la simulación cada vez que se edite una entrada de la matriz. Tanto en la hoja **calificaciones** como en la hoja **summary** se incluyó un botón para ejecutar la simulación de manera manual.

El archivo puede descargarse haciendo [click aquí](https://github.com/estudiosdev/demo_transition_simulation/raw/main/excel_simulaciones.xlsm).


## Más información

La matriz de transición predeterminada utilizada en el ejercicio tiene la forma:

|    | A   | B   | C   | D1  | D2  | E   |
|----|-----|-----|-----|-----|-----|-----|
| A  | 0.5 | 0.5 | 0   | 0   | 0   | 0   |
| B  | 0.2 | 0.2 | 0.6 | 0   | 0   | 0   |
| C  | 0   | 0.2 | 0.2 | 0.6 | 0   | 0   |
| D1 | 0   | 0   | 0.2 | 0.2 | 0.6 | 0   |
| D2 | 0   | 0   | 0   | 0.2 | 0.2 | 0.6 |
| E0 | 0   | 0   | 0   | 0   | 0.1 | 0.9 |

Pero, podría modificarse el script. De manera específica de las líneas 20-25 para cambiar las probabilidades y observar como varía el análisis. De igual forma, podrían cambiarse otros parámetros o funciones en base a lo que desee analizar el usuario.

En el Excel las probabilidades pueden ajustarse en la hoja **matriz**.
