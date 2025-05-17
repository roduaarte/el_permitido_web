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

# Productos principales
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
# Productos principales
productos.update({
    "Promo 1kg": st.checkbox("Promo 1kg"),
    "Promo 1kg + 1/4": st.checkbox("Promo 1kg + 1/4"),
    "Promo 1kg + 1/2": st.checkbox("Promo 1kg + 1/2"),
    "Promo 2kg": st.checkbox("Promo 2kg"),
})

st.header("📦 Elegí tu TORTA HELADA") 
# Productos principales
productos.update({
    "Chocotorta": st.checkbox("Chocotorta"),
    "Torta Oreo":st.checkbox("Torta Oreo"),
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
        enviar = st.form_submit_button("Generar pedido")

    if enviar:
        mensaje = f"Hola! Soy {nombre}. Quiero pedir:\n" + "\n".join(f"- {p}" for p in pedido)
        for key, lista_sabores in sabores.items():
            if lista_sabores:
                mensaje += f"\n  Sabores para {key}: {', '.join(lista_sabores)}"
        mensaje += f"\nDirección: {direccion}\nHorario: {horario}"
        url = "https://wa.me/5492304307444?text=" + urllib.parse.quote(mensaje)
        st.markdown(f"[\ud83d\udcf2 Enviar pedido por WhatsApp]({url})", unsafe_allow_html=True)
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

st.subheader("🎈 Promociones")
st.image("sabores y precios.png", caption="Promos y sabores", use_container_width=True)

st.subheader("\ud83c\udf70 Tortas Heladas")
st.image("tortas heladas.jpg", caption="Nuestras tortas", use_container_width=True)

# Botones redes sociales
st.markdown("""
**Instagram:** [@heladeria.elpermitido](https://www.instagram.com/heladeria.elpermitido)
""")

# Opiniones
st.subheader("⭐ Valoraciones")
st.text_area("Dejanos tu opinión")

# Ubicación
st.subheader("📍 Dónde estamos")
st.map(data=None)  # Podés cargar coordenadas si querés una ubicación real

st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")
