import streamlit as st
import pandas as pd
st.success("¡Bienvenido al Dashboard Académico!")
st.info("Aqui puedes consultar las calificaciones de los estudiantes.")
st.subheader("Calificaciones de los estudiantes")


df = pd.read_csv("data/estudiantes.csv")

st.title("Mi Dashboard Académico")

# Crear tres columnas
col1, col2, col3, col4 = st.columns(4)

# Mostrar el total de estudiantes
col1.metric("Total de estudiantes", len(df))

# Mostrar el promedio
col2.metric(
    "Promedio de calificaciones",
    df["calificacion"].mean()
)

# Mostrar la calificacion mas alta
col3.metric("Calificación más alta", df["calificacion"].max())

# Mostrar la calificacion mas baja
col4.metric("Calificación más baja", df["calificacion"].min())

# Mostrar la tabla de estudiantes

# Titulo de la tabla
st.subheader("Calificaciones de los estudiantes")

# Mostrar nombres y calificaciones
st.dataframe(df[["nombre", "calificacion"]])

# Grafico de Calificaciones
st.subheader("Grafico de calificaciones")

st.bar_chart(
    df.set_index("nombre")["calificacion"]
)

# Estudiantes con calificaciones bajas
st.subheader("Estudiantes con calificaciones bajas")

st.dataframe(df[df["calificacion"] < 80])

# Contar estudiantes con calificaciones bajas
st.metric(
    "Estudiantes con calificaciones bajas",
    len(df[df["calificacion"] < 80])
)

# Porcentaje de estudiantes con notas bajas
porcentaje = (
    len(df[df["calificacion"] < 80]) / len(df)
) * 100

st.metric("Porcentaje de notas bajas", f"{porcentaje:.1f}%")

# Mensaje informativo
st.info(
    f"El {porcentaje:.1f}% de los estudiantes tiene una calificación inferior a 80."
)

# Filtro interactivo de calificaciones
st.subheader("Filtro interactivo")

nota_minima = st.slider(
    "Selecciona la calificación mínima",
    0,
    100,
    80
)

estudiantes_filtrados = df[df["calificacion"] >= nota_minima]

st.dataframe(estudiantes_filtrados)

# Contar estudiantes que cumplen el filtro
st.metric(
    "Estudiantes encontrados",
    len(estudiantes_filtrados)
)

# Contar estudiantes filtrados
cantidad = len(estudiantes_filtrados)

# Mostrar un mensaje según el resultado
if cantidad == 0:
    st.info("No se encontraron estudiantes con esa calificación.")
else:
    st.success(f"Se encontraron {cantidad} estudiantes que cumplen el filtro.")
    promedio_filtrado = estudiantes_filtrados["calificacion"].mean()
    st.metric("Promedio de estudiantes filtrados", round(promedio_filtrado, 1))
    # Consultar un estudiante
st.subheader("Consultar un estudiante")

estudiante = st.selectbox(
    "Selecciona un estudiante",
    df["nombre"]
)
nota_estudiante = df[df["nombre"] == estudiante]["calificacion"].iloc[0]
st.metric("Calificación del estudiante", nota_estudiante)
if nota_estudiante < 80:
    st.warning("Este estudiante necesita apoyo académico.")

elif nota_estudiante >= 90:
    st.success("¡Excelente rendimiento académico!")

else:
    st.info("Este estudiante tiene una calificación satisfactoria.")

    excelentes = len(df[df["calificacion"] >= 90])