
import streamlit as st
import json
import pandas as pd

st.set_page_config(page_title="IA Jurídica", layout="wide")

# Cargar Código Penal
with open("codigo_penal_completo.json", "r", encoding="utf-8") as f:
    codigo_penal = json.load(f)

# Cargar Juicios Reales
with open("juicios_reales_demo.json", "r", encoding="utf-8") as f:
    juicios = json.load(f)

# --- Sidebar ---
st.sidebar.title("Menú")
seccion = st.sidebar.radio("Selecciona una sección:", [
    "Consulta Código Penal",
    "Modo Estudio",
    "Subir Archivos",
    "Investigación de Juicios"
])

# --- Consulta Código Penal ---
if seccion == "Consulta Código Penal":
    st.title("Consulta del Código Penal")
    articulo = st.text_input("Buscar artículo (ej: 138):")
    if articulo:
        resultados = [a for a in codigo_penal if articulo in a["articulo"]]
        for r in resultados:
            st.subheader(f"{r['articulo']} – {r['capitulo']}")
            st.write(r["texto"])

# --- Modo Estudio ---
elif seccion == "Modo Estudio":
    st.title("Modo Estudio Jurídico")
    pregunta = st.text_input("Haz tu pregunta jurídica:")
    if pregunta:
        st.write("Respuesta generada por la IA (demo):")
        st.success("Esta es una respuesta simulada basada en tus apuntes y la base legal.")

# --- Subida de Archivos ---
elif seccion == "Subir Archivos":
    st.title("Sube tus Apuntes o Modelos de Examen")
    archivo = st.file_uploader("Sube un archivo PDF, DOCX o TXT", type=["pdf", "docx", "txt"])
    if archivo:
        st.success(f"Archivo '{archivo.name}' subido correctamente.")
        st.write("En la versión final, la IA responderá usando este contenido como referencia.")

# --- Investigación de Juicios ---
elif seccion == "Investigación de Juicios":
    st.title("Investigación de Juicios Reales")
    tipo = st.selectbox("Filtrar por tipo de caso:", ["Todos"] + sorted(set(j["tipo"] for j in juicios)))
    for j in juicios:
        if tipo == "Todos" or j["tipo"] == tipo:
            st.subheader(f"{j['tipo']} – {j['resultado']}")
            st.write(f"Tribunal: {j['tribunal']} ({j['año']})")
            st.write(f"Resumen: {j['resumen']}")
            st.caption(f"Abogado: {j['abogado']}")
