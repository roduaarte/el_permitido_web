import streamlit as st
import urllib.parse

st.set_page_config(page_title="El Permitido", page_icon="🍦", layout="centered")

# Estilo visual personalizado
st.markdown("""
    <style>
        body {
            background-color: black;
            color: #fff;
        }
        .stApp {
            background-color: black;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #f72585;
        }
        .st-bb {
            color: #7209b7;
        }
        .st-ef {
            background-color: #3a0ca3;
        }
    </style>
""", unsafe_allow_html=True)

st.image("logotipo.jpg", width=200)

st.title("🍨 Bienvenidos a El Permitido")
st.write("Disfrutá nuestros helados artesanales, tortas heladas y promos para compartir.")

st.header("📦 Elegí tus Sabores")

productos = {
    "Pote 1kg": st.checkbox("Pote 1kg"),
    "Pote 1/2kg": st.checkbox("Pote 1/2kg"),
    "Pote 1/4kg": st.checkbox("Pote 1/4kg"),
    "3 conos": st.checkbox("3 conos - $1000"),
    "6 conos": st.checkbox("6 conos - $1800"),
    "6 vasitos": st.checkbox("6 vasitos - $1000"),
    "12 vasitos": st.checkbox("12 vasitos - $1800"),
}

st.header("📦 Elegí tu Promo")
productos.update({
    "Promo 1kg": st.checkbox("Promo 1kg"),
    "Promo 1kg + 1/4": st.checkbox("Promo 1kg + 1/4"),
    "Promo 1kg + 1/2": st.checkbox("Promo 1kg + 1/2"),
    "Promo 2kg": st.checkbox("Promo 2kg"),
})

st.header("🍰 Elegí tu TORTA HELADA")
productos.update({
    "Chocotorta": st.checkbox("Chocotorta"),
    "Torta Oreo": st.checkbox("Torta Oreo"),
    "Torta Mixta": st.checkbox("Torta Mixta"),
    "Tiramisu": st.checkbox("Tiramisu"),
})

sabores_lista = [
    "americana", "dulce de leche", "ddl bombón", "súper dulce de leche", "ddl con nuez",
    "ddl granizado", "chocolate", "choco amargo", "choco shot", "choco suizo", "choco rocher",
    "choco c/ almendras", "choco raffaello", "frambuesa", "frutilla al agua", "limón",
    "limón tropical", "durazno", "vainilla", "mantecol", "mascarpone", "crema oreo",
    "frutilla a la crema", "pistacho", "banana split", "tramontana", "granizado",
    "menta granizada"
]

sabores = {}
if productos["Pote 1kg"]:
    sabores["1kg"] = st.multiselect("Seleccioná hasta 4 sabores para el Pote 1kg", sabores_lista, max_selections=4)
if productos["Pote 1/2kg"]:
    sabores["1/2kg"] = st.multiselect("Seleccioná hasta 3 sabores para el Pote 1/2kg", sabores_lista, max_
