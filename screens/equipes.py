import psycopg2
import sqlalchemy
import panel as pn

# Inicializa a extensão do Panel para o Jupyter
pn.extension()

# Cria um componente simples de interface
texto = pn.widgets.StaticText(name='Status', value='Conectado ao ambiente!')
botao = pn.widgets.Button(name='Clique Aqui', button_type='primary')

# Renderiza na tela do Notebook
pn.Column(texto, botao)
