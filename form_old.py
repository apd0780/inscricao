import streamlit as st
import pandas as pd
from helperSqlite import *


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
# Every form must have a submit button.'
submit = st.button("Enviar")


if nome and telefone and submit:

    insertSQL = f"""
    INSERT INTO inscritos (nome,telefone)
        VALUES ('{nome}','{telefone}');
    """
    crud(insertSQL, "DB/inscricoes.db")







