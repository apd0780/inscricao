import streamlit as st
import pandas as pd
import validators
from datetime import date
from validate_email import validate_email

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
    html_temp = """
    		<div style="background-color:{};border-radius:10px;height: 148px;">
    		<h1 style="color:{};text-align:center;">'Amigos do Professor Ricardo Dantas' </h1>
    		</div>
    		<br/>
    		"""
    with st.container():
        st.image('./avatar.png', width=200)
        st.header('Amigos do Professor Ricardo Dantas')
        #st.markdown(html_temp.format('silver', '#10180b'), unsafe_allow_html=True)

    create_table()
    #st.title('Amigos do Professor Ricardo Dantas')

    nome = st.text_input('Nome Completo (obrigatório)', max_chars=50, placeholder='Nome Completo')

    col1, col2, col3 = st.columns(3)

    with col1:
        telefone = st.text_input('Celular (obrigatório)', max_chars=11, placeholder='61999999999')

    with col2:
        niver_dia = st.selectbox('Dia do Aniversário', [''] + list(range(1,32)))

    with col3:
        niver_mes = st.selectbox('Mês do Aniversário', ['', 'janeiro','fevereiro','março','abril','maio','junho', ''
                                                'julho','agosto','setembro','outubro','novembro','dezembro'])

    regiao = st.selectbox('Região em que vive (obrigatório)',
                          ['', 'Águas Claras ',
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
                           'NÃO MORO NO DF'])

    email = st.text_input('E-mail', max_chars=50, placeholder='exemplo@exemplo.com')
    facebook = st.text_input('Facebook', max_chars=50, placeholder='https://www.facebook.com/usuario')
    instagram = st.text_input('Instagram', max_chars=50, placeholder='https://www.instagram.com/usuario/')
    msg = st.text_area("Alguma menssagem?", height=50)

    if st.button("Enviar"):
        if not nome or len(nome) < 10:
            st.warning("Por favor, preencha seu nome completo.")
        elif not telefone or len(telefone) < 11 or not telefone.isdigit():
            st.warning("Por favor, preencha seu celular com o DDD apenas com números, exemplo: 61999999999")
        elif not regiao:
            st.warning("Por favor, preencha a região do DF em que vive, caso não resida no DF escolha a última opção: NÃO MORO NO DF ")
        elif email and not validate_email(email):
            st.warning("Por favor, preencha um email válido.")
        else:
            add_data(nome, telefone, niver_dia, niver_mes, regiao, email, facebook, instagram, msg)
            st.success("{}, recebemos sua inscrição! "
                       "Estaremos entrando em contato o mais breve possível, obrigado.".format(nome))

if __name__ == '__main__':
    main()