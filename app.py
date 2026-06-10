import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.set_page_config(page_title="Encuesta de Seguridad Informática")

# 🔐 contraseña del profesor
PASSWORD = "4321"

st.title("🔒 Encuesta de Seguridad Informática")

st.info("""
¿Alguna vez te has preguntado qué tan fácil puede ser que alguien robe tu información personal?

Una contraseña débil, un enlace falso o compartir datos en sitios no confiables puede poner en riesgo tu identidad, tus cuentas y tu privacidad.

Responde esta encuesta y descubre qué tan seguras son tus prácticas digitales.
""")

st.write("""
Hola, mi nombre es Citlally Monserrat Rodríguez Peña de la carrera de Ciberseguridad.

Esta encuesta tiene como objetivo concientizar sobre la importancia de la seguridad informática.
""")

# 🔐 acceso profesor (SOLO SIDEBAR)
with st.sidebar:
    modo_admin = st.text_input("🔐 Acceso profesor", type="password")


# 📋 PREGUNTAS (FUERA DEL SIDEBAR)
preguntas = [
    "¿Usa contraseñas seguras y diferentes en cada cuenta o correo electrónico?",
    "¿Tiene activada la verificación en dos pasos (2FA)?",
    "¿Revisa los permisos de las aplicaciones antes de instalarlas?",
    "¿Configura adecuadamente la privacidad en sus redes sociales?",
    "¿Realiza respaldos periódicos de información importante?",
    "¿Actualiza sus contraseñas regularmente?",
    "¿Evita conectarse a redes WiFi públicas para operaciones bancarias?",
    "¿Mantiene actualizado su sistema operativo y aplicaciones?",
    "¿Comparte información personal sensible en sitios no confiables?",
    "¿Usa antivirus o herramientas de seguridad en sus dispositivos?"
]

respuestas = []

for i, pregunta in enumerate(preguntas):
    respuesta = st.selectbox(
        f"{i+1}. {pregunta}",
        ["Elige tu respuesta", "Sí", "No"],
        key=f"p{i}"
    )
    respuestas.append(respuesta)

# =========================
# 👨‍🎓 ALUMNO
# =========================
if st.button("Ver resultado"):

    if "Elige tu respuesta" in respuestas:
        st.warning("⚠️ Por favor responde todas las preguntas.")

    else:

        total = 0

        for i, respuesta in enumerate(respuestas):

            if i == 8:
                if respuesta == "No":
                    total += 1
            else:
                if respuesta == "Sí":
                    total += 1

        if total >= 9:
            mensaje = "Excelente"
            st.success("🟢 Excelente. Mantienes buenas prácticas de seguridad digital.")

        elif total >= 7:
            mensaje = "Regular"
            st.warning("🟡 Regular. Se recomienda reforzar algunas prácticas.")

        else:
            mensaje = "Malo"
            st.error("🔴 Debes mejorar tus hábitos de seguridad digital.")

        st.success("🙏 Gracias por responder esta encuesta de seguridad informática.")

        # 💾 guardar resultados
        datos = {
            "Fecha": [datetime.now()],
            "Resultado": [mensaje]
        }

        df = pd.DataFrame(datos)

        if os.path.exists("respuestas.csv"):
            df.to_csv("respuestas.csv", mode="a", header=False, index=False)
        else:
            df.to_csv("respuestas.csv", index=False)

# =========================
# 👨‍🏫 PROFESOR
# =========================
if modo_admin == PASSWORD:

    st.success("🔓 Modo profesor activado")

    if os.path.exists("respuestas.csv"):
        df_admin = pd.read_csv("respuestas.csv")

        st.subheader("📊 Datos de alumnos")
        st.dataframe(df_admin)

        st.subheader("📥 Descargar datos")

        with open("respuestas.csv", "rb") as file:
            st.download_button(
                "Descargar CSV",
                data=file,
                file_name="respuestas.csv",
                mime="text/csv"
            )
