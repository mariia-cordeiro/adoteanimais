import streamlit as st

st.markdown("### HTML")
html_code = """
  <h1 style='color: #4169E1;'>AdotaPet!</h1>
"""
st.markdown(html_code, unsafe_allow_html=True)

st.markdown("""---""")
st.subheader ("Cachorros resgatados das ruas e de maus tratos")
st.write(
    "Pequenas ações transformam destinos. Adote! Mude a vida de um animal."
)
st.markdown("""---""")
st.markdown(""""
            Encontre seu Pet
            Preencha nosso formulário
            Seja convocado para avaliação
            Busque seu Pet
""")

st.write("Faça um upload do seu pet ou verifique os animais disponíveis para adoção:")
st.write("Para realizar o upload, clique aqui:]
imagem = st.file_uploader("Escolha uma imagem do seu pet", type=["jpg", "png", "jpeg"])

colunas = st.columns(5)
with colunas[0]:
    st.image("img/IMG_8642.jpg")
with colunas[1]:
    st.image("img/IMG_8643.jpg")
with colunas[2]:
    st.image("img/IMG_8644.jpg")
with colunas[3]:
    st.image("img/IMG_8645.jpg")
with colunas[4]:
    st.image("img/IMG_8646.jpg")