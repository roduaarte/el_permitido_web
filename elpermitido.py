import streamlit as st
import os
from PIL import Image
import urllib.parse

# Configuración inicial
st.set_page_config(page_title="Pedidos Online - Helados", layout="centered")

# Estilos
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .title {
            color: #4a4a4a;
            text-align: center;
        }
        .footer {
            font-size: 12px;
            text-align: center;
            color: #888;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# Logo
if os.path.exists("logotipo.jpg"):
    st.image("logotipo.jpg", width=200)
else:
    st.warning("⚠️ Falta la imagen 'logotipo.jpg'")

st.title("📦 Hacé tu pedido de helado")

# Productos
st.header("🍨 Elegí tus productos")

helados = {
    "¼ kg": 1300,
    "½ kg": 2200,
    "1 kg": 3900,
}

conos = {
    "Cono simple": 600,
    "Cono doble": 1000,
}

promos = {
    "Promo 2 potes de 1 kg": 7200,
    "Promo 1 pote de 1 kg + 1 de ½ kg": 5900,
}

vasitos = {
    "Vasito chico": 500,
    "Vasito mediano": 700,
    "Vasito grande": 1000,
}

tortas = {
    "Torta helada chica": 4000,
    "Torta helada grande": 7000,
}

sabores = {
    "¼": ["Dulce de leche", "Chocolate", "Frutilla", "Granizado", "Vainilla"],
    "½": ["Dulce de leche", "Chocolate", "Frutilla", "Granizado", "Vainilla", "Tramontana", "Cookies"],
    "1": ["Dulce de leche", "Chocolate", "Frutilla", "Granizado", "Vainilla", "Tramontana", "Cookies", "Marroc", "Frutos rojos"],
}

pedido = []
total = 0

# Selección de helados
st.subheader("Helados:")
for nombre, precio in helados.items():
    if st.checkbox(f"{nombre} - ${precio}"):
        pedido.append(nombre)
        cant_sabores = 1 if "¼" in nombre else (2 if "½" in nombre else 3)
        seleccionados = st.multiselect(f"Elegí {cant_sabores} sabor(es) para {nombre}", sabores[nombre.split()[0].replace("kg", "")], max_selections=cant_sabores)
        pedido.extend(seleccionados)
        total += precio

# Conos
st.subheader("Conos:")
for nombre, precio in conos.items():
    if st.checkbox(f"{nombre} - ${precio}"):
        pedido.append(nombre)
        total += precio

# Promos
st.subheader("Promociones:")
for nombre, precio in promos.items():
    if st.checkbox(f"{nombre} - ${precio}"):
        pedido.append(nombre)
        total += precio

# Vasitos
st.subheader("Vasitos:")
for nombre, precio in vasitos.items():
    if st.checkbox(f"{nombre} - ${precio}"):
        pedido.append(nombre)
        total += precio

# Tortas
st.subheader("Tortas heladas:")
for nombre, precio in tortas.items():
    if st.checkbox(f"{nombre} - ${precio}"):
        pedido.append(nombre)
        total += precio

# Mostrar imágenes de productos
st.subheader("📸 Imágenes de productos:")
if os.path.exists("sabores y precios.png"):
    st.image("sabores y precios.png", caption="Sabores y precios")
else:
    st.warning("⚠️ Falta la imagen 'sabores y precios.png'")

if os.path.exists("tortas heladas.jpg"):
    st.image("tortas heladas.jpg", caption="Tortas heladas")
else:
    st.warning("⚠️ Falta la imagen 'tortas heladas.jpg'")

# Mostrar pedido
if pedido:
    st.subheader("🧾 Pedido actual:")
    st.write(pedido)
    st.success(f"💰 Total estimado: ${total}")

# Datos del cliente
st.header("📝 Completá tus datos")
nombre = st.text_input("Tu nombre")
direccion = st.text_input("Dirección")
horario = st.text_input("Horario deseado de entrega")

# WhatsApp
if st.button("📲 Enviar pedido por WhatsApp"):
    if nombre and direccion and horario and pedido:
        mensaje = f"Hola,
