import streamlit as st
import urllib.parse

# Configuración de la página
st.set_page_config(page_title="El Permitido", page_icon="🍦", layout="centered")

# Colores personalizados
st.markdown(
    \"\"\"
    <style>
        body {
            background-color: #000000;
            color: #FFFFFF;
        }
        .title {
            color: #FF00FF;
        }
        .section {
            color: #00FFFF;
        }
        .highlight {
            color: #39FF14;
        }
    </style>
    \"\"\",
    unsafe_allow_html=True
)

# Logo
st.image("logotipo.jpg", width=200)

# Título y bienvenida
st.markdown("<h1 class='title'>🍨 Bienvenidos a El Permitido</h1>", unsafe_allow_html=True)
st.write("Disfrutá nuestros helados artesanales, tortas heladas y promos para compartir.")

# Productos: Potes
st.markdown("<h2 class='section'>📦 Elegí tus productos</h2>", unsafe_allow_html=True)

sabores = [
    "americana", "dulce de leche", "ddl bombón", "súper dulce de leche", "ddl con nuez",
    "ddl granizado", "chocolate", "choco amargo", "choco shot", "choco suizo", "choco rocher",
    "choco c/ almendras", "choco raffaello", "frambuesa", "frutilla al agua", "limón", "limón tropical",
    "durazno", "vainilla", "mantecol", "mascarpone", "crema oreo", "frutilla a la crema", "pistacho",
    "banana split", "tramontana", "granizado", "menta granizada"
]

productos = {
    "Pote 1kg": {"check": st.checkbox("Pote 1kg ($7000)"), "max_sabores": 4, "precio": 7000},
    "Pote 1/2kg": {"check": st.checkbox("Pote 1/2kg ($4000)"), "max_sabores": 3, "precio": 4000},
    "Pote 1/4kg": {"check": st.checkbox("Pote 1/4kg ($2500)"), "max_sabores": 2, "precio": 2500},
}

sabores_elegidos = {}

for nombre, data in productos.items():
    if data["check"]:
        sabores_selec = st.multiselect(f"Elegí hasta {data['max_sabores']} sabores para {nombre}", sabores, key=nombre)
        if len(sabores_selec) > data["max_sabores"]:
            st.warning(f"⚠️ Elegiste más de {data['max_sabores']} sabores para {nombre}. Por favor, corregí.")
        sabores_elegidos[nombre] = sabores_selec

# Tortas heladas
st.markdown("<h2 class='section'>🍰 Tortas Heladas</h2>", unsafe_allow_html=True)
tortas = {
    "Chocotorta ($20000)": 20000,
    "Torta Mixta ($20000)": 20000,
    "Tiramisu ($20000)": 20000
}
tortas_elegidas = [t for t in tortas if st.checkbox(t)]

st.image("tortas heladas.jpg", use_container_width=True)

# Promos
st.markdown("<h2 class='section'>🎉 Promociones</h2>", unsafe_allow_html=True)
promos = {
    "Promo 1kg ($11500)": 11500,
    "Promo 1kg + 1/4 ($16500)": 16500,
    "Promo 1kg + 1/2 ($17500)": 17500,
    "Promo 2kg ($22000)": 22000
}
promos_elegidas = [p for p in promos if st.checkbox(p)]

st.image("sabores y precios.png", use_container_width=True)

# Vasitos y conos
st.markdown("<h2 class='section'>🍧 Vasitos y Conos</h2>", unsafe_allow_html=True)
vasos_y_conos = {
    "3 conos ($1000)": 1000,
    "6 conos ($1800)": 1800,
    "6 vasitos ($1000)": 1000,
    "12 vasitos ($1800)": 1800
}
vasos_conos_elegidos = [v for v in vasos_y_conos if st.checkbox(v)]

# Formulario adicional
st.markdown("<h2 class='section'>📝 Información adicional</h2>", unsafe_allow_html=True)
nombre = st.text_input("Tu nombre")
direccion = st.text_input("Dirección de entrega")
horario = st.text_input("Horario deseado")

# Calculadora de precios
total = 0
for key, value in productos.items():
    if value["check"]:
        total += value["precio"]
for t in tortas_elegidas:
    total += tortas[t]
for p in promos_elegidas:
    total += promos[p]
for v in vasos_conos_elegidos:
    total += vasos_y_conos[v]

# Pedido resumen
if st.button("📋 Ver pedido"):
    st.markdown("<h2 class='highlight'>🧾 Tu pedido:</h2>", unsafe_allow_html=True)

    for key, value in sabores_elegidos.items():
        if value:
            st.write(f"- {key}: {', '.join(value)}")
    for t in tortas_elegidas:
        st.write(f"- {t}")
    for p in promos_elegidas:
        st.write(f"- {p}")
    for v in vasos_conos_elegidos:
        st.write(f"- {v}")
    
    if nombre or direccion or horario:
        st.markdown("**🧍 Datos personales:**")
        st.write(f"Nombre: {nombre}")
        st.write(f"Dirección: {direccion}")
        st.write(f"Horario: {horario}")

    st.success(f"💵 Total: ${total}")

    # Mensaje para WhatsApp
    mensaje = "Hola! Quiero hacer un pedido:\\n"
    for key, value in sabores_elegidos.items():
        if value:
            mensaje += f"- {key}: {', '.join(value)}\\n"
    for t in tortas_elegidas:
        mensaje += f"- {t}\\n"
    for p in promos_elegidas:
        mensaje += f"- {p}\\n"
    for v in vasos_conos_elegidos:
        mensaje += f"- {v}\\n"
    if nombre:
        mensaje += f"Nombre: {nombre}\\n"
    if direccion:
        mensaje += f"Dirección: {direccion}\\n"
    if horario:
        mensaje += f"Horario: {horario}\\n"
    mensaje += f"Total: ${total}"
    
    url = "https://wa.me/5492304307444?text=" + urllib.parse.quote(mensaje)
    st.markdown(f"[📲 Enviar pedido por WhatsApp]({url})", unsafe_allow_html=True)

# Redes sociales
st.markdown("<h2 class='section'>📱 Seguinos</h2>", unsafe_allow_html=True)
st.markdown("[Instagram](https://www.instagram.com/heladeria.elpermitido/)")

# Pie de página
st.markdown("---")
st.markdown("© 2025 El Permitido - Todos los derechos reservados.")
'''

codigo_actualizado

