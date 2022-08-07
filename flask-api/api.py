# módulos necessários do flask
from flask import Flask, request, jsonify

# módulos para crawler das informações
import requests
from bs4 import BeautifulSoup

# criar app Flask
app = Flask(__name__, static_url_path='')

# mapeamento das URLs dos cursos para crawler
curso_urls = {
    'IA':'https://www.impacta.edu.br/mba/artificial-intelligence',
    'Big Data':'https://www.impacta.edu.br/mba/business-intelligence-e-analytics',
    'DE': 'https://www.impacta.edu.br/mba/data-engineering',
    'Marketing': 'https://www.impacta.edu.br/mba/executivo-em-marketing-digital',
    'Full Stack': 'https://www.impacta.edu.br/mba/full-stack-developer',
    'UX': 'https://www.impacta.edu.br/mba/ux-design-digital-experience',
    'Cloud': 'https://www.impacta.edu.br/mba/cloud-computing-devops'
}


# endpoint do webhook - POST
@app.route('/chatbot',  methods=['POST'])
def watsonwebhook():
  # retornar dados enviados no formato JSON
  req = request.get_json()

  # tipo da task enviada: info ou email
  task = req['task']
  if task =='info':

    # nome do curso enviado
    curso = req['curso']

    #crawler para pegar informações
    nome_curso = curso_urls.get(curso)
    if nome_curso:
        r = requests.get(nome_curso).text
        info = BeautifulSoup(r, 'html.parser')(class_='background-base-site')[0].text

        #retornar informações no campo info, no formato JSON
        return jsonify({'info':info})
    # curso não encontrado
    else:
        return jsonify({'info':'Não encontramos informações sobre este curso'})
        
# executar app flask
if __name__ == '__main__':
  app.run()
