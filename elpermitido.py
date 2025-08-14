import streamlit as st
import urllib.parse
import pandas as pd
import pydeck as pdk
import random
import time

# --- Configuración de la Página ---
st.set_page_config(page_title="El Permitido", page_icon="🍦", layout="wide")

# --- Datos de la Aplicación (Productos, Precios, Sabores) ---

# Usar un diccionario anidado es más organizado
PRODUCTOS = {
    "Potes de Helado": {
        "Pote 1kg": 11000,
        "Pote 1/2kg": 7000,
        "Pote 1/4kg": 5000, # Precio corregido para consistencia
    },
    "Promos para compartir": {
        "Promo 1kg": 11500,
        "Promo 1kg + 1/4": 16500,
        "Promo 1kg + 1/2": 17500,
        "Promo 2kg": 22000,
    },
    "Conos y Vasitos": {
        "3 conos": 1000,
        "6 conos": 1800,
        "6 vasitos": 1000,
        "12 vasitos": 1800,
    },
    "Tortas Heladas": {
        "Chocotorta": 2800,
        "Torta Oreo": 3000,
        "Torta Mixta": 3500,
        "Tiramisú": 3300,
    }
}

SABORES_LISTA = [
    "Americana", "Dulce de Leche", "DDL Bombón", "Súper Dulce de Leche", "DDL con Nuez",
    "DDL Granizado", "Chocolate", "Choco Amargo", "Choco Shot", "Choco Suizo", "Choco Rocher",
    "Choco c/ Almendras", "Choco Raffaello", "Frambuesa", "Frutilla al Agua", "Limón",
    "Limón Tropical", "Durazno", "Vainilla", "Mantecol", "Mascarpone", "Crema Oreo",
    "Frutilla a la Crema", "Pistacho", "Banana Split", "Tramontana", "Granizado",
    "Menta Granizada"
]

# --- Estilo Visual (CSS) ---
st.markdown("""
    <style>
        .stApp {
            background-color: #1a1a1a; /* Un negro un poco más suave */
            color: #fff;
        }
        h1, h2, h3 {
            color: #f72585; /* Color principal para títulos */
        }
        .st-emotion-cache-16txtl3 { /* Contenedor de widgets */
             background-color: #2a2a2a;
             border-radius: 10px;
             padding: 15px !important;
        }
        .stButton>button {
            background-color: #7209b7;
            color: white;
            border-radius: 8px;
            border: none;
            padding: 10px 20px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #f72585;
        }
    </style>
""", unsafe_allow_html=True)


# --- Encabezado ---
col1, col2 = st.columns([1, 4])
with col1:
    # Usando la imagen local del logotipo
    st.image("logotipo.jpg", width=150)

with col2:
    st.title("🍨 Bienvenidos a El Permitido")
    st.write("Disfrutá nuestros helados artesanales, tortas heladas y promos para compartir.")

st.markdown("---")

# --- NUEVA SECCIÓN: Ruleta de Sabores ---
with st.container(border=True):
    st.header("🎡 ¡Ruleta de Sabores!")
    st.write("¿No te decidís? ¡Dejá que el azar elija tu próximo sabor favorito!")

    if st.button("¡Girar la Ruleta!"):
        with st.spinner("Girando... 🌀"):
            time.sleep(2) # Simula el giro
        sabor_ganador = random.choice(SABORES_LISTA)
        st.success(f"🎉 ¡Tu sabor para probar es: **{sabor_ganador}**! 🎉")
        st.balloons()

st.markdown("---")


# --- Selección de Productos ---
st.header("📦 Armá tu Pedido")

pedido_seleccionado = {}
total = 0

# Usamos columnas para una mejor distribución
col1, col2 = st.columns(2)

with col1:
    with st.container(border=True):
        st.subheader(list(PRODUCTOS.keys())[0]) # Potes de Helado
        for nombre, precio in PRODUCTOS["Potes de Helado"].items():
            if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
                pedido_seleccionado[nombre] = precio
    
    with st.container(border=True):
        st.subheader(list(PRODUCTOS.keys())[2]) # Conos y Vasitos
        for nombre, precio in PRODUCTOS["Conos y Vasitos"].items():
            if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
                pedido_seleccionado[nombre] = precio

with col2:
    with st.container(border=True):
        st.subheader(list(PRODUCTOS.keys())[1]) # Promos
        for nombre, precio in PRODUCTOS["Promos para compartir"].items():
            if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
                pedido_seleccionado[nombre] = precio

    with st.container(border=True):
        st.subheader(list(PRODUCTOS.keys())[3]) # Tortas Heladas
        for nombre, precio in PRODUCTOS["Tortas Heladas"].items():
            if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
                pedido_seleccionado[nombre] = precio


# --- Selección de Sabores (si aplica) ---
sabores_elegidos = {}
if "Pote 1kg" in pedido_seleccionado:
    with st.expander("🍦 Elegí los sabores para tu Pote de 1kg (hasta 4)", expanded=True):
        sabores_elegidos["1kg"] = st.multiselect("Sabores para 1kg", SABORES_LISTA, max_selections=4, key="sabores_1kg")
if "Pote 1/2kg" in pedido_seleccionado:
     with st.expander("🍦 Elegí los sabores para tu Pote de 1/2kg (hasta 3)", expanded=True):
        sabores_elegidos["1/2kg"] = st.multiselect("Sabores para 1/2kg", SABORES_LISTA, max_selections=3, key="sabores_1_2kg")
if "Pote 1/4kg" in pedido_seleccionado:
     with st.expander("🍦 Elegí los sabores para tu Pote de 1/4kg (hasta 2)", expanded=True):
        sabores_elegidos["1/4kg"] = st.multiselect("Sabores para 1/4kg", SABORES_LISTA, max_selections=2, key="sabores_1_4kg")


# --- Resumen y Formulario de Pedido ---
st.markdown("---")
if pedido_seleccionado:
    st.header("📝 Resumen y Envío")
    
    # Calcular el total
    total = sum(pedido_seleccionado.values())

    st.subheader("Tu selección:")
    for nombre, precio in pedido_seleccionado.items():
        st.write(f"- {nombre}: ${precio:,}")
        # Mostrar sabores elegidos para cada pote
        if nombre == "Pote 1kg" and sabores_elegidos.get("1kg"):
            st.caption(f"   Sabores: {', '.join(sabores_elegidos['1kg'])}")
        elif nombre == "Pote 1/2kg" and sabores_elegidos.get("1/2kg"):
            st.caption(f"   Sabores: {', '.join(sabores_elegidos['1/2kg'])}")
        elif nombre == "Pote 1/4kg" and sabores_elegidos.get("1/4kg"):
            st.caption(f"   Sabores: {', '.join(sabores_elegidos['1/4kg'])}")

    st.subheader(f"Total a pagar: ${total:,}")

    with st.form("Datos del cliente"):
        nombre_cliente = st.text_input("Nombre y apellido")
        direccion_cliente = st.text_input("Dirección de entrega")
        horario_cliente = st.text_input("Horario estimado de entrega (ej: 'Lo antes posible', 'Entre 21:00 y 21:30')")
        
        enviar_pedido = st.form_submit_button("Generar Pedido para WhatsApp")

        if enviar_pedido:
            if not nombre_cliente or not direccion_cliente:
                st.error("Por favor, completá tu nombre y dirección.")
            else:
                # Construir mensaje de WhatsApp
                mensaje_parts = [f"Hola! Soy {nombre_cliente}. Quiero hacer un pedido:"]
                for producto, precio in pedido_seleccionado.items():
                    mensaje_parts.append(f"- {producto}")
                    if producto == "Pote 1kg" and sabores_elegidos.get("1kg"):
                        mensaje_parts.append(f"  (Sabores: {', '.join(sabores_elegidos['1kg'])})")
                    elif producto == "Pote 1/2kg" and sabores_elegidos.get("1/2kg"):
                        mensaje_parts.append(f"  (Sabores: {', '.join(sabores_elegidos['1/2kg'])})")
                    elif producto == "Pote 1/4kg" and sabores_elegidos.get("1/4kg"):
                        mensaje_parts.append(f"  (Sabores: {', '.join(sabores_elegidos['1/4kg'])})")

                mensaje_parts.append(f"\nTotal: ${total:,}")
                mensaje_parts.append(f"Dirección: {direccion_cliente}")
                mensaje_parts.append(f"Horario: {horario_cliente}")
                
                mensaje_final = "\n".join(mensaje_parts)
                url_whatsapp = "https://wa.me/5492304307444?text=" + urllib.parse.quote(mensaje_final)
                
                st.success("¡Pedido generado! Hacé clic en el enlace para enviarlo.")
                st.markdown(f'## [📱 Enviar pedido por WhatsApp]({url_whatsapp})', unsafe_allow_html=True)
else:
    st.info("Seleccioná al menos un producto para comenzar tu pedido.")

# --- Secciones Adicionales (Imágenes, Mapa, etc.) ---
st.markdown("---")
st.header("📸 Nuestras Promos y Tortas")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("promociones.png", caption="Nuestras promociones")
with col2:
    # Usando la imagen local de sabores y precios
    st.image("sabores y precios.png", caption="Lista de precios")
with col3:
    # La imagen "tortas heladas.jpg" no estaba en tu lista de archivos.
    # Si la tienes con otro nombre, puedes cambiar "tortas heladas.jpg" por el nombre correcto.
    # st.image("tortas heladas.jpg", caption="Nuestras tortas")
    st.info("Imagen de tortas no encontrada.")


st.markdown("---")
st.header("📍 Dónde Encontrarnos")
col1, col2 = st.columns([2,1])
with col1:
    # Coordenadas de la heladería
    ubicacion_df = pd.DataFrame({'lat': [-34.4661085], 'lon': [-58.9037148]})
    st.pydeck_chart(pdk.Deck(
        # map_style='mapbox://styles/mapbox/light-v10', # Requiere token de Mapbox
        initial_view_state=pdk.ViewState(latitude=-34.4661085, longitude=-58.9037148, zoom=16, pitch=50),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=ubicacion_df,
                get_position='[lon, lat]',
                get_color='[247, 37, 133, 200]', # Color #f72585 con opacidad
                get_radius=50,
            ),
        ],
        tooltip={"text": "El Permitido Heladería"}
    ))
with col2:
    direccion = "San Luis 208, Pilar Centro, Provincia de Buenos Aires"
    enlace_google_maps = "https://www.google.com/maps/place/San+Luis+208,+Pilar+Centro,+Provincia+de+Buenos+Aires"
    st.markdown(f"#### Dirección:")
    st.markdown(f"### 📌 [{direccion}]({enlace_google_maps})")
    st.markdown("#### Redes Sociales:")
    st.markdown("[**Instagram:** @heladeria.elpermitido](https://www.instagram.com/heladeria.elpermitido)")


st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")

