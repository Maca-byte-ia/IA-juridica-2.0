
import streamlit as st
import datetime

st.set_page_config(page_title="IA Legal – MVP", layout="wide")

def interpretar_articulo(articulo):
    if "138" in articulo:
        return "Artículo 138 del Código Penal: Trata sobre el homicidio. Pena de prisión de 10 a 15 años. Jurisprudencia reciente refuerza la interpretación dolosa."
    elif "154" in articulo:
        return "Artículo 154 del Código Civil: Regula la patria potestad. Padres deben velar por los hijos, alimentarlos, educarlos, etc. Muy aplicado en casos de custodia."
    else:
        return "Artículo no encontrado en esta versión demo. Puedes agregar más artículos en el futuro."

def simular_juicio(caso, nivel):
    if nivel == "Rápido":
        fallo = "Fallo simulado: El tribunal desestima la demanda por falta de pruebas directas."
    else:
        fallo = ("Fallo simulado (detalle):\n"
                 "- Argumento del demandante: {}\n"
                 "- Contraparte: La defensa presentó jurisprudencia contradictoria.\n"
                 "- Juez (IA): En base al art. 138 y sentencias recientes, se estima parcialmente.\n"
                 "- Recomendación: Reforzar pruebas documentales y testigos.").format(caso[:200])
    return fallo

st.title("IA Legal – Simulador y Asistente Jurídico")
st.markdown("Consulta artículos legales, simula juicios y genera informes.")

st.sidebar.header("Opciones")
modo = st.sidebar.selectbox("¿Qué deseas hacer?", ["Consultar Artículo", "Simular Juicio"])
nivel = st.sidebar.radio("Complejidad del juicio (si aplica)", ["Rápido", "Detallado"])

if modo == "Consultar Artículo":
    articulo = st.text_input("Introduce el número del artículo legal:")
    if st.button("Interpretar"):
        resultado = interpretar_articulo(articulo)
        st.markdown("**Interpretación Legal:**")
        st.write(resultado)

elif modo == "Simular Juicio":
    st.subheader("Simulación de juicio")
    caso = st.text_area("Describe tu caso jurídico (hechos, argumentos, pruebas):")
    if st.button("Simular"):
        resultado = simular_juicio(caso, nivel)
        st.markdown("**Resultado de la Simulación:**")
        st.text(resultado)

        st.markdown("---")
        st.subheader("Informe generado")
        fecha = datetime.date.today()
        informe = f"---\nIA Legal – Informe de Simulación ({fecha})\n\nCaso:\n{caso}\n\nResultado:\n{resultado}\n"
        st.download_button("Descargar Informe (.txt)", informe, file_name="informe_legal.txt")
