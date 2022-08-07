import json

# módulos para crawler das informações
import requests
from bs4 import BeautifulSoup

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

def lambda_handler(event, context):
    task = event['task']
    if task =='info':

        # nome do curso enviado
        curso = event['curso']

        #crawler para pegar informações
        nome_curso = curso_urls.get(curso)
        if nome_curso:
            r = requests.get(nome_curso).text
            info = BeautifulSoup(r, 'html.parser')(class_='background-base-site')[0].text

            retorno =  {
                'statusCode': 200,
                'body': json.dumps({'info': info})
            }
            print(retorno)
            return retorno

        # curso não encontrado
        else:
            retorno =  {
                'statusCode': 404,
                'body': json.dumps({'info': 'Não encontramos informações sobre este curso'})
            }
            print(retorno)
            return retorno
        
    retorno =  {
        'statusCode': 404,
        'body': json.dumps({'erro': 'Tarefa não encontrado'})
    }
    
    print(retorno)
