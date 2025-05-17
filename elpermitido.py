import streamlit as st
import urllib.parse

st.set_page_config(page_title="El Permitido", page_icon="🍦", layout="centered")

st.image("logotipo.jpg", width=200)

st.title("🍨 Bienvenidos a El Permitido")
st.write("Disfrutá nuestros helados artesanales, tortas heladas y promos para compartir.")

st.subheader("📦 Elegí tus productos")

# Productos
productos = {
    "Pote 1kg": st.checkbox("Pote 1kg (hasta 4 sabores)"),
    "Pote 1/2kg": st.checkbox("Pote 1/2kg (hasta 3 sabores)"),
    "Pote 1/4kg": st.checkbox("Pote 1/4kg (hasta 2 sabores)"),
    "Promo 1kg": st.checkbox("Promo 1kg"),
    "Promo 1kg + 1/4": st.checkbox("Promo 1kg + 1/4"),
    "Promo 1kg + 1/2": st.checkbox("Promo 1kg + 1/2"),
    "Promo 2kg": st.checkbox("Promo 2kg"),
    "Chocotorta": st.checkbox("Chocotorta"),
    "Torta Mixta": st.checkbox("Torta Mixta"),
    "Tiramisu": st.checkbox("Tiramisu"),
}

sabores_disponibles = [
    "americana", "dulce de leche", "ddl bombón", "súper dulce de leche", "ddl con nuez",
    "ddl granizado", "chocolate", "choco amargo", "choco shot", "choco suizo",
    "choco rocher", "choco c/ almendras", "choco raffaello", "frambuesa", "frutilla al agua",
    "limón", "limón tropical", "durazno", "vainilla", "mantecol", "mascarpone",
    "crema oreo", "frutilla a la crema", "pistacho", "banana split", "tramontana",
    "granizado", "menta granizada"
]

sabores_elegidos = []

if productos["Pote 1kg"]:
    seleccion = st.multiselect("🍦 Elegí hasta 4 sabores para tu Pote 1kg:", sabores_disponibles, key="kg")
    if len(seleccion) > 4:
        st.warning("Podés elegir hasta 4 sabores para el pote de 1kg.")
    sabores_elegidos.extend(seleccion[:4])

if productos["Pote 1/2kg"]:
    seleccion = st.multiselect("🍦 Elegí hasta 3 sabores para tu Pote 1/2kg:", sabores_disponibles, key="medio")
    if len(seleccion) > 3:
        st.warning("Podés elegir hasta 3 sabores para el pote de 1/2kg.")
    sabores_elegidos.extend(seleccion[:3])

if productos["Pote 1/4kg"]:
    seleccion = st.multiselect("🍦 Elegí hasta 2 sabores para tu Pote 1/4kg:", sabores_disponibles, key="cuarto")
    if len(seleccion) > 2:
        st.warning("Podés elegir hasta 2 sabores para el pote de 1/4kg.")
    sabores_elegidos.extend(seleccion[:2])

pedido = [nombre for nombre, seleccionado in productos.items() if seleccionado]

if pedido:
    st.subheader("📝 Tu pedido:")
    for p in pedido:
        st.write(f"- {p}")
    if sabores_elegidos:
        st.write("🍧 *Sabores elegidos:*")
        for sabor in sabores_elegidos:
            st.write(f"  - {sabor}")

    mensaje = "Hola! Quisiera hacer un pedido:\n" + "\n".join(f"- {p}" for p in pedido)
    if sabores_elegidos:
        mensaje += "\n\n*Sabores elegidos:*\n" + "\n".join(f"- {s}" for s in sabores_elegidos)

    url = "https://wa.me/5492304307444?text=" + urllib.parse.quote(mensaje)
    st.markdown(f"[📲 Enviar pedido por WhatsApp]({url})", unsafe_allow_html=True)
else:
    st.info("Seleccioná al menos un producto para hacer tu pedido.")

# Enlace a la imagen de sabores y precios
st.subheader("🍦 Sabores y Precios")
st.image("sabores y precios.png", use_container_width=True)

# Enlace a la imagen de tortas heladas
st.subheader("🍰 Tortas Heladas")
st.image("tortas heladas.jpg", use_container_width=True)

# Promociones
st.subheader("🎉 Promociones")
st.image("promociones.png", caption="Promos de la semana", use_container_width=True)

# Contacto
st.subheader("📞 Contacto")
st.markdown("""
**Instagram:** [@heladeria.elpermitido](https://www.instagram.com/heladeria.elpermitido)  
**Teléfono:** 2304307444  
**Correo:** heladeria.elpermitido@gmail.com
""")

st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")
