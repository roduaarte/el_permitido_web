import streamlit as st
import urllib.parse
import pandas as pd
import pydeck as pdk
import random
import time
from datetime import datetime
import pytz # Necesario para manejar la zona horaria correctamente

# --- Configuración de la Página ---
st.set_page_config(page_title="El Permitido", page_icon="🍦", layout="wide")

# --- Datos de la Aplicación ---
PRODUCTOS = {
    "Potes de Helado": {
        "Pote 1kg": 11000,
        "Pote 1/2kg": 7000,
        "Pote 1/4kg": 5000,
    },
    "Promos para Compartir": {
        "1Kg + 6 vasitos": 11500,
        "1kg + 1/4 + 6 vasitos": 16500,
        "1kg + 1/2 + 6 vasitos": 18500,
        "2kg + 12 vasitos": 22000,
    },
    "Extras (Conos y Vasitos)": {
        "3 Cucuruchos": 1000,
        "6 Cucuruchos": 1800,
        "6 Vasitos": 1000,
        "12 Vasitos": 1800,
    }
}

# --- ACTUALIZADO: Diccionario de tortas con sus imágenes individuales ---
TORTAS = {
    "Torta Mixta": {"precio": 20000, "img": "Mixta.png"},
    "Chocotorta": {"precio": 20000, "img": "Chocotorta.png"},
    "Torta Oreo": {"precio": 20000, "img": "Oreo.png"},
    "Tiramisú": {"precio": 20000, "img": "Tiramisú.png"},
}

SABORES_LISTA = [
    "Americana", "Dulce de Leche", "DDL Bombón", "Súper Dulce de Leche", "DDL con Nuez",
    "DDL Granizado", "Chocolate", "Choco Amargo", "Choco Shot", "Choco Suizo", "Choco Rocher",
    "Choco c/ Almendras", "Choco Raffaello", "Frambuesa", "Frutilla al Agua", "Limón",
    "Limón Tropical", "Durazno", "Vainilla", "Mantecol", "Mascarpone", "Crema Oreo",
    "Frutilla a la Crema", "Pistacho", "Banana Split", "Tramontana", "Granizado",
    "Menta Granizada"
]

# --- Estilo Visual (CSS con Degradado) ---
st.markdown("""
    <style>
        .stApp {
            background-image: linear-gradient(to right top, #fdd5e2, #e6d9f1, #d5def9, #cde2fb, #d0e5f9);
            color: #7209b7; /* Color principal del texto cambiado a morado oscuro para legibilidad */
        }
        h1, h2, h3 {
            color: #f72585; /* Títulos en fucsia como pediste */
        }
        .st-emotion-cache-16txtl3, .st-emotion-cache-1jicfl2, .st-emotion-cache-1r4qj8v {
             background-color: rgba(255, 255, 255, 0.7);
             border-radius: 15px;
             padding: 20px !important;
             backdrop-filter: blur(10px);
             border: 1px solid rgba(255, 255, 255, 0.2);
        }
        .stButton>button {
            background-color: #f72585;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 12px 24px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #7209b7;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)


# --- Encabezado ---
col1, col2 = st.columns([1, 5])
with col1:
    st.image("logotipo.jpg", width=120)
with col2:
    st.title("Bienvenidos a El Permitido")
    st.write("Helados artesanales, tortas y las mejores promos para vos.")

st.markdown("---")

# --- Lógica y Visualización de la "Promo del Día" ---
def mostrar_promo_del_dia():
    try:
        tz = pytz.timezone('America/Argentina/Buenos_Aires')
        now = datetime.now(tz)
        weekday = now.weekday()  # Lunes=0, Domingo=6
        current_time = now.time()

        happy_hour_start = datetime.strptime("17:00", "%H:%M").time()
        happy_hour_end = datetime.strptime("20:30", "%H:%M").time()

        promo_title = "🔥 PROMO DEL DÍA 🔥"
        promo_message = ""
        promo_emoji = "🎉"

        if weekday in [2, 3]: # Miércoles y Jueves
            dia_semana = "Miércoles" if weekday == 2 else "Jueves"
            if happy_hour_start <= current_time <= happy_hour_end:
                promo_title = f"¡HAPPY HOUR DE {dia_semana.upper()}!"
                promo_message = "¡Estás a tiempo! Tenés un **15% de DESCUENTO** en el total de tu compra. ¡No te lo pierdas!"
                promo_emoji = "🥳"
            else:
                promo_message = f"Hoy es {dia_semana}, y de 17:00 a 20:30hs tenés **15% OFF**. ¡Falta poco!"
                promo_emoji = "⏳"
        elif weekday == 4: # Viernes
            promo_message = "¡Llegó el Viernes de 3x2! Pedí 2 potes de 1/4 y **el tercero va DE REGALO**."
            promo_emoji = "🍦"
        elif weekday == 5: # Sábado
            promo_message = "¡Sábado a puro sabor! Llevate **1/2 Kg + 3 cucuruchos por solo $7.000**."
            promo_emoji = "🙌"
        elif weekday == 6: # Domingo
            promo_message = "¡Domingo en familia! Disfrutá nuestra súper promo de **2 Kilos + 9 cucuruchos**."
            promo_emoji = "👨‍👩‍👧‍👦"
        else: # Lunes y Martes
            promo_title = "👀 ¡Mirá la promo que se viene!"
            promo_message = "Agendalo: este Miércoles y Jueves vuelve el Happy Hour con **15% OFF** (de 17:00 a 20:30hs)."
            promo_emoji = "🗓️"

        with st.container(border=True):
            st.header(f"{promo_emoji} {promo_title}")
            st.subheader(promo_message)

    except Exception as e:
        st.error(f"No se pudo cargar la promo del día: {e}")

mostrar_promo_del_dia()
st.markdown("---")

# --- Ruleta de Sabores ---
with st.container(border=True):
    st.header("🎡 ¡Ruleta de Sabores!")
    st.write("¿Indeciso/a? ¡Dejá que el azar elija por vos y sorprendete!")
    if st.button("¡Girar la Ruleta!"):
        with st.spinner("Eligiendo un sabor increíble... 🌀"):
            time.sleep(1.5)
        sabor_ganador = random.choice(SABORES_LISTA)
        st.success(f"🎉 ¡Salió **{sabor_ganador}**! ¿Te animás a probarlo? 🎉")
        st.balloons()

st.markdown("---")

# --- Selección de Productos ---
st.header("📦 Armá tu Pedido")
pedido_seleccionado = {}

# --- Sección de Tortas Interactivas ---
with st.container(border=True):
    st.subheader("Nuestras Tortas Heladas - ($20.000 c/u)")
    st.write("Marcá la casilla para agregar la torta que querés a tu pedido.")
    
    torta_cols = st.columns(len(TORTAS))
    for i, (nombre, data) in enumerate(TORTAS.items()):
        with torta_cols[i]:
            st.image(data['img'], use_container_width=True, caption=nombre)
            if st.checkbox(f"Agregar {nombre}", key=f"torta_{nombre}"):
                pedido_seleccionado[nombre] = data["precio"]

# --- Potes, Promos y Extras ---
col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):
        st.subheader("Potes de Helado")
        for nombre, precio in PRODUCTOS["Potes de Helado"].items():
            if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
                pedido_seleccionado[nombre] = precio
    
with col2:
    with st.container(border=True):
        st.subheader("Promos para Compartir")
        for nombre, precio in PRODUCTOS["Promos para Compartir"].items():
            if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
                pedido_seleccionado[nombre] = precio

with st.container(border=True):
    st.subheader("Extras")
    for nombre, precio in PRODUCTOS["Extras (Conos y Vasitos)"].items():
        if st.checkbox(f"{nombre} - ${precio:,}", key=nombre):
            pedido_seleccionado[nombre] = precio

# --- Selección de Sabores (si aplica) ---
sabores_elegidos = {}
if "Pote 1kg" in pedido_seleccionado:
    with st.expander("🍦 Elegí hasta 4 sabores para tu Pote de 1kg", expanded=True):
        sabores_elegidos["1kg"] = st.multiselect("Sabores para 1kg", SABORES_LISTA, max_selections=4, key="sabores_1kg")
if "Pote 1/2kg" in pedido_seleccionado:
     with st.expander("🍦 Elegí hasta 3 sabores para tu Pote de 1/2kg", expanded=True):
        sabores_elegidos["1/2kg"] = st.multiselect("Sabores para 1/2kg", SABORES_LISTA, max_selections=3, key="sabores_1_2kg")
if "Pote 1/4kg" in pedido_seleccionado:
     with st.expander("🍦 Elegí hasta 2 sabores para tu Pote de 1/4kg", expanded=True):
        sabores_elegidos["1/4kg"] = st.multiselect("Sabores para 1/4kg", SABORES_LISTA, max_selections=2, key="sabores_1_4kg")

# --- Resumen y Formulario de Pedido ---
if pedido_seleccionado:
    st.markdown("---")
    st.header("📝 Resumen y Envío")
    
    total = sum(pedido_seleccionado.values())

    st.subheader("Tu selección:")
    for nombre, precio in pedido_seleccionado.items():
        st.write(f"- {nombre}: ${precio:,}")
        if nombre == "Pote 1kg" and sabores_elegidos.get("1kg"):
            st.caption(f"   Sabores: {', '.join(sabores_elegidos['1kg'])}")
        elif nombre == "Pote 1/2kg" and sabores_elegidos.get("1/2kg"):
            st.caption(f"   Sabores: {', '.join(sabores_elegidos['1/2kg'])}")
        elif nombre == "Pote 1/4kg" and sabores_elegidos.get("1/4kg"):
            st.caption(f"   Sabores: {', '.join(sabores_elegidos['1/4kg'])}")

    st.subheader(f"Total a pagar: ${total:,}")
    st.info("Recordá que el envío es GRATIS dentro de los 4km a la redonda.")

    with st.form("Datos del cliente"):
        nombre_cliente = st.text_input("Nombre y apellido")
        direccion_cliente = st.text_input("Dirección (Calle y altura)")
        entre_calles = st.text_input("Entre calles (para ubicarte mejor)")
        metodo_pago = st.selectbox("Método de pago", ["Efectivo", "Transferencia"])
        
        enviar_pedido = st.form_submit_button("Confirmar y Enviar Pedido por WhatsApp")

        if enviar_pedido:
            if not nombre_cliente or not direccion_cliente:
                st.error("Por favor, completá tu nombre y dirección.")
            else:
                mensaje_parts = [f"Hola! Soy {nombre_cliente}. Quiero hacer un pedido:"]
                for producto in pedido_seleccionado:
                    mensaje_parts.append(f"- {producto}")
                    if producto == "Pote 1kg" and sabores_elegidos.get("1kg"):
                        mensaje_parts.append(f"  (Sabores: {', '.join(sabores_elegidos['1kg'])})")
                    elif producto == "Pote 1/2kg" and sabores_elegidos.get("1/2kg"):
                        mensaje_parts.append(f"  (Sabores: {', '.join(sabores_elegidos['1/2kg'])})")
                    elif producto == "Pote 1/4kg" and sabores_elegidos.get("1/4kg"):
                        mensaje_parts.append(f"  (Sabores: {', '.join(sabores_elegidos['1/4kg'])})")
                
                mensaje_parts.append(f"\nTotal: ${total:,}")
                mensaje_parts.append(f"Dirección: {direccion_cliente} (entre {entre_calles})")
                mensaje_parts.append(f"Método de pago: {metodo_pago}")
                
                url_whatsapp = "https://wa.me/5492304307444?text=" + urllib.parse.quote("\n".join(mensaje_parts))
                
                st.success("¡Pedido generado! Hacé clic en el enlace para enviarlo por WhatsApp.")
                st.markdown(f'<h2><a href="{url_whatsapp}" target="_blank" style="text-decoration: none; color: #7209b7;">📱 Enviar Pedido Ahora</a></h2>', unsafe_allow_html=True)

# --- Secciones Adicionales ---
st.markdown("---")
st.header("📍 Dónde Encontrarnos y Contacto")

col1, col2 = st.columns([2,1])
with col1:
    ubicacion_df = pd.DataFrame({'lat': [-34.4661085], 'lon': [-58.9037148]})
    st.pydeck_chart(pdk.Deck(
        initial_view_state=pdk.ViewState(latitude=-34.4661085, longitude=-58.9037148, zoom=16, pitch=50),
        layers=[pdk.Layer('ScatterplotLayer', data=ubicacion_df, get_position='[lon, lat]', get_color='[247, 37, 133, 200]', get_radius=50)],
        tooltip={"text": "El Permitido Heladería - Pilar Centro"}
    ))
with col2:
    st.markdown("#### Estamos en:")
    st.markdown("### 📌 Pilar Centro")
    st.markdown("##### (Calle La Pampa)")
    st.markdown("---")
    st.markdown("#### Contactanos:")
    # --- ACTUALIZADO: Se agrega el teléfono de contacto ---
    st.markdown("##### 📱 [**WhatsApp: 230-4307444**](https://wa.me/5492304307444)")
    st.markdown("##### 📸 [**Instagram:** @heladeria.elpermitido](https://www.instagram.com/heladeria.elpermitido)")

st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")
