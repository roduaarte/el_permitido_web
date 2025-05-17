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

# Lista completa de sabores (ordenada alfabéticamente)
sabores_disponibles = sorted([
    "americana", "banana split", "choco amargo", "choco c/ almendras", "choco raffaello",
    "choco rocher", "choco shot", "choco suizo", "chocolate", "crema oreo", "ddl bombón",
    "ddl con nuez", "ddl granizado", "dulce de leche", "durazno", "frambuesa",
    "frutilla a la crema", "frutilla al agua", "granizado", "limón", "limón tropical",
    "mantecol", "mascarpone", "menta granizada", "pistacho", "súper dulce de leche",
    "tramontana", "vainilla"
])

sabores_elegidos = []

# Si se seleccionaron potes, mostrar selección de sabores
if any(productos[p] for p in ["Pote 1kg", "Pote 1/2kg", "Pote 1/4kg"]):
    st.subheader("🍦 Elegí tus sabores de helado")
    st.write("Podés elegir diferentes sabores por cada pote.")

    if productos["Pote 1kg"]:
        sabores_1kg = st.multiselect("Sabores para Pote 1kg (máx 4)", sabores_disponibles, key="sabores1kg")
        if len(sabores_1kg) > 4:
            st.error("Máximo 4 sabores para el Pote 1kg.")
        sabores_elegidos.append(("Pote 1kg", sabores_1kg[:4]))

    if productos["Pote 1/2kg"]:
        sabores_12kg = st.multiselect("Sabores para Pote 1/2kg (máx 3)", sabores_disponibles, key="sabores12kg")
        if len(sabores_12kg) > 3:
            st.error("Máximo 3 sabores para el Pote 1/2kg.")
        sabores_elegidos.append(("Pote 1/2kg", sabores_12kg[:3]))

    if productos["Pote 1/4kg"]:
        sabores_14kg = st.multiselect("Sabores para Pote 1/4kg (máx 2)", sabores_disponibles, key="sabores14kg")
        if len(sabores_14kg) > 2:
            st.error("Máximo 2 sabores para el Pote 1/4kg.")
        sabores_elegidos.append(("Pote 1/4kg", sabores_14kg[:2]))

if pedido:
    st.subheader("📝 Tu pedido:")
    for p in pedido:
        st.write(f"- {p}")
        # Mostrar sabores elegidos si corresponde
        for pote, sabores in sabores_elegidos:
            if p == pote and sabores:
                st.write("  Sabores:")
                for sabor in sabores:
                    st.write(f"   • {sabor}")

    # Armar mensaje para WhatsApp
    mensaje = "Hola! Quisiera hacer un pedido:\n"
    for p in pedido:
        mensaje += f"- {p}\n"
        for pote, sabores in sabores_elegidos:
            if p == pote and sabores:
                mensaje += "  Sabores:\n"
                for sabor in sabores:
                    mensaje += f"   • {sabor}\n"

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
