import streamlit as st
import pandas as pd

# # NLP pkgs
# import spacy
# from spacy import displacy
# nlp = spacy.load('en')

# Database Functions
from db_fxns import *


# Reading Time
def readingTime(mytext):
    total_words = len([token for token in mytext.split(" ")])
    estimatedTime = total_words / 200.0
    return estimatedTime


def analyze_text(text):
    return nlp(text)


# Layout Templates
title_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<h6>Author:{}</h6>
	<br/>
	<br/>	
	<p style="text-align:justify">{}</p>
	</div>
	"""
article_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<h6>Author:{}</h6> 
	<h6>Post Date: {}</h6>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""
head_message_temp = """
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	<h6>Author:{}</h6> 		
	<h6>Post Date: {}</h6>		
	</div>
	"""
full_message_temp = """
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p style="text-align:justify;color:black;padding:10px">{}</p>
	</div>
	"""

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""


def main():
    """A Simple CRUD Blog App"""
    html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:{};text-align:center;">Simple Blog </h1>
		</div>
		"""
    #st.markdown(html_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    create_table()
    st.title('Registro de amigos do Professor Ricardo Dantas')

    nome = st.text_input('Nome Completo', max_chars=100, placeholder='Nome Completo')
    telefone = st.text_input('Celular', max_chars=8, placeholder='(dd)*****-****')
    nascimento = st.date_input('Data de Nascimento ')
    endereco = st.text_input('Endereço', max_chars=100, placeholder='Endereço')

    regiao = st.selectbox('Região em que mora no DF',
                          ['Águas Claras ',
                           'Arniqueira ',
                           'Brazlândia ',
                           'Candangolândia ',
                           'Ceilândia ',
                           'Cruzeiro ',
                           'Fercal ',
                           'Gama ',
                           'Guará ',
                           'Itapoã ',
                           'Jardim Botânico ',
                           'Lago Norte ',
                           'Lago Sul',
                           'Núcleo Bandeirante ',
                           'Paranoá ',
                           'Park Way ',
                           'Planaltina ',
                           'Plano Piloto ',
                           'Recanto das Emas ',
                           'Riacho Fundo ',
                           'Riacho Fundo II ',
                           'Samambaia ',
                           'Santa Maria ',
                           'São Sebastião ',
                           'SCIA/Estrutural ',
                           'SIA ',
                           'Sobradinho ',
                           'Sobradinho II ',
                           'Sol Nascente e Pôr do Sol ',
                           'Sudoeste/Octogonal ',
                           'Taguatinga ',
                           'Varjão ',
                           'Vicente Pires',
                           'Não moro no DF'])

    cep = st.text_input('CEP', max_chars=8, placeholder='CEP')
    email = st.text_input('E-mail', max_chars=100, placeholder='exemplo@exemplo.com')
    facebook = st.text_input('Facebook', max_chars=100, placeholder='https://www.facebook.com/usuario')
    instagram = st.text_input('Instagram', max_chars=100, placeholder='https://www.instagram.com/usuario/')
    sugestao = st.text_area("Sugestão", height=200)

    if st.button("Enviar"):
        add_data(nome,telefone,nascimento,endereco,regiao,cep,email,facebook,instagram,sugestao)
        st.success("Inscrição::' de {}' Enviada".format(nome))



if __name__ == '__main__':
    main()