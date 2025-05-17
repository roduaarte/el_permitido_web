import streamlit as st
import urllib.parse

st.set_page_config(page_title="El Permitido", page_icon="🍦", layout="centered")

st.image("logotipo.jpg", width=200)

st.title("🍨 Bienvenidos a El Permitido")
st.write("Disfrutá nuestros helados artesanales, tortas heladas y promos para compartir.")

st.subheader("📦 Elegí tus productos")

productos = {
    "Pote 1kg": st.checkbox("Pote 1kg"),
    "Pote 1/2kg": st.checkbox("Pote 1/2kg"),
    "Pote 1/4kg": st.checkbox("Pote 1/4kg"),
    "Torta Oreo": st.checkbox("Torta Oreo"),
    "Chocotorta": st.checkbox("Chocotorta"),
    "Torta Mixta": st.checkbox("Torta Mixta"),
    "Tiramisu": st.checkbox("Tiramisu"),
}

pedido = [nombre for nombre, seleccionado in productos.items() if seleccionado]

if pedido:
    st.subheader("📝 Tu pedido:")
    for p in pedido:
        st.write(f"- {p}")

    mensaje = "Hola! Quisiera hacer un pedido:\n" + "\n".join(f"- {p}" for p in pedido)
    url = "https://wa.me/5492304307444?text=" + urllib.parse.quote(mensaje)

    st.markdown(f"[📲 Enviar pedido por WhatsApp]({url})", unsafe_allow_html=True)
else:
    st.info("Seleccioná al menos un producto para hacer tu pedido.")

st.subheader("🎉 Promociones")
st.image("promociones.png", caption="Promos de la semana", use_column_width=True)

st.subheader("📞 Contacto")
st.markdown("""
**Instagram:** [@heladeria.elpermitido](https://www.instagram.com/heladeria.elpermitido)  
**Teléfono:** 2304307444  
**Correo:** heladeria.elpermitido@gmail.com
""")

st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")
