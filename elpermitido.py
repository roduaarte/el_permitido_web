import streamlit as st
import urllib.parse
import pandas as pd
import pydeck as pdk

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
    "Pote 1kg": st.checkbox("Pote 1kg - $11000"),
    "Pote 1/2kg": st.checkbox("Pote 1/2kg - $7000"),
    "Pote 1/4kg": st.checkbox("Pote 1/4kg - $5500"),
    "3 conos": st.checkbox("3 conos - $1000"),
    "6 conos": st.checkbox("6 conos - $1800"),
    "6 vasitos": st.checkbox("6 vasitos - $1000"),
    "12 vasitos": st.checkbox("12 vasitos - $1800"),
}

st.header("📦 Elegí tu Promo")
productos.update({
    "Promo 1kg": st.checkbox("Promo 1kg - $11500"),
    "Promo 1kg + 1/4": st.checkbox("Promo 1kg + 1/4 - $16500"),
    "Promo 1kg + 1/2": st.checkbox("Promo 1kg + 1/2 - $17500"),
    "Promo 2kg": st.checkbox("Promo 2kg - $22000"),
})

st.header("🍰 Elegí tu TORTA HELADA")
productos.update({
    "Chocotorta": st.checkbox("Chocotorta - $2800"),
    "Torta Oreo": st.checkbox("Torta Oreo - $3000"),
    "Torta Mixta": st.checkbox("Torta Mixta - $3500"),
    "Tiramisu": st.checkbox("Tiramisu - $3300"),
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
    sabores["1/2kg"] = st.multiselect("Seleccioná hasta 3 sabores para el Pote 1/2kg", sabores_lista, max_selections=3)
if productos["Pote 1/4kg"]:
    sabores["1/4kg"] = st.multiselect("Seleccioná hasta 2 sabores para el Pote 1/4kg", sabores_lista, max_selections=2)

pedido = [nombre for nombre, seleccionado in productos.items() if seleccionado]

if pedido:
    st.subheader("📝 Tu pedido:")
    for p in pedido:
        st.write(f"- {p}")
        if p in sabores:
            for s in sabores[p.split()[1]]:
                st.write(f"   - sabor: {s}")

    # Formulario personalizado
    with st.form("Datos del cliente"):
        nombre = st.text_input("Nombre y apellido")
        direccion = st.text_input("Dirección")
        horario = st.text_input("Horario estimado de entrega")
        enviar = st.form_submit_button("Generar pedido")

    if enviar:
        mensaje = f"Hola! Soy {nombre}. Quiero pedir:\n" + "\n".join(f"- {p}" for p in pedido)
        for key, lista_sabores in sabores.items():
            if lista_sabores:
                mensaje += f"\n  Sabores para {key}: {', '.join(lista_sabores)}"
        mensaje += f"\nDirección: {direccion}\nHorario: {horario}"
        url = "https://wa.me/5492304307444?text=" + urllib.parse.quote(mensaje)
        st.markdown(f"[📱 Enviar pedido por WhatsApp]({url})", unsafe_allow_html=True)
else:
    st.info("Seleccioná al menos un producto para hacer tu pedido.")

# Calculadora de precios
precios = {
    "Pote 1kg": 11000,
    "Pote 1/2kg": 7000,
    "Pote 1/4kg": 5500,
    "Promo 1kg": 11500,
    "Promo 1kg + 1/4": 16500,
    "Promo 1kg + 1/2": 17500,
    "Promo 2kg": 22000,
    "3 conos": 1000,
    "6 conos": 1800,
    "6 vasitos": 1000,
    "12 vasitos": 1800,
}

total = sum(precios[p] for p in pedido if p in precios)
if total:
    st.success(f"Total estimado: ${total}")

st.subheader("🎉 Promociones")
st.image("promociones.png", caption="Nuestras promociones", use_container_width=True)

st.subheader("🎈 Sabores y precios")
st.image("Precio actualizado.png", caption="Precio actualizado", use_container_width=True)

st.subheader("🍰 Tortas Heladas")
st.image("tortas heladas.jpg", caption="Nuestras tortas", use_container_width=True)

# Botones redes sociales
st.markdown("""
**Instagram:** [@heladeria.elpermitido](https://www.instagram.com/heladeria.elpermitido)
""")

# Opiniones
st.subheader("⭐ Valoraciones")
st.text_area("Dejanos tu opinión")

st.subheader("📍 Ubicación")

# Coordenadas de la heladería
ubicacion = pd.DataFrame({
    'lat': [-34.4661085],
    'lon': [-58.9037148]
})

# Mapa con marcador
st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/streets-v11',  # Si no tenés token de Mapbox, usá map_style=None
    initial_view_state=pdk.ViewState(
        latitude=-34.4661085,
        longitude=-58.9037148,
        zoom=17,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=ubicacion,
            get_position='[lon, lat]',
            get_color='[255, 0, 0, 160]',
            get_radius=50,
        ),
    ],
))

# Dirección y link a Google Maps
direccion = "San Luis 208, Pilar Centro, Provincia de Buenos Aires"
enlace_google_maps = "https://www.google.com/maps/place/San+Luis+208,+Pilar+Centro,+Provincia+de+Buenos+Aires"

st.markdown(f"📌 [**{direccion}**]({enlace_google_maps})")

st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")
