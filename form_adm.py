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
nome_temp = """
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
	<h6>Inscricao Date: {}</h6>
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
	<h6>Inscricao Date: {}</h6>		
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
		<h1 style="color:{};text-align:center;">Inscrições do Professor Ricardo Dantas </h1>
		</div>
		"""
    st.markdown(html_temp.format('royalblue', 'white'), unsafe_allow_html=True)

    menu = [ "Pesquisar", "Gerenciar Inscrições"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Pesquisar":
        st.subheader("Pesquisar Inscricões")
        search_term = st.text_input("Digite o termo")
        search_choice = st.radio("Campo", ("nome", "telefone"))
        if st.button('Pesquisar'):
            if search_choice == "nome":
                inscricao_resultado = pegar_inscricao_pelo_nome(search_term)
            elif search_choice == "telefone":
                inscricao_resultado = pegar_inscricao_pelo_telefone(search_term)

            df = pd.DataFrame([[i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]] for i in inscricao_resultado], columns=('id', 'nome', 'telefone', 'niver_dia', 'niver_mes', 'regiao', 'email', 'facebook', 'instagram', 'mensagem'))

            st.table(df)


    elif choice == "Gerenciar Inscrições":
        st.subheader("Gerenciar Inscrições")
        result = ver_todas_incricoes()
        #clean_db = pd.DataFrame(result, columns=["Nome"])
        #st.dataframe(clean_db)
        unique_list = [str(i[0]) + ' - ' + i[1] + ' - ' + i[2] + ' - ' + i[5] for i in ver_todas_incricoes()]
        nome = st.selectbox("Selecione o nome", unique_list)
        if st.button("Delete"):
            apagar_dados(id_inscricao)
            st.warning("Deleted: '{}'".format(nome))


if __name__ == '__main__':
    main()