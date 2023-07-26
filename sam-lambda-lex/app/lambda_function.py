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
    print("EVENTO: ", event)

    # task: intent enviada    
    task = event.get('sessionState').get('intent').get('name')
    if task =='Informacoes':

        # nome do curso identificado do slot
        curso = event.get('sessionState').get('intent').get('slots')\
            .get('NomeCurso')
        if curso:
            curso = curso.get('value',{}).get('interpretedValue',{})

        #crawler para pegar informações
        nome_curso = curso_urls.get(curso)
        if nome_curso:
            r = requests.get(nome_curso).text
            info = BeautifulSoup(r, 'html.parser')(class_='content_destaque_sobre')[0].text
            retorno =  {
                "sessionState": {        
                    "dialogAction": {           
                        "type": "ElicitIntent"
                    }            
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": info,
                    }
                ]
            }
            print(retorno)
            return retorno

        # curso não encontrado
        else:
            retorno =  {
                "sessionState": {        
                    "dialogAction": {           
                        "type": "ElicitIntent"
                    }            
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Curso não encontrado",
                    }
                ]
            }
            print(retorno)
            return retorno
        
    retorno =  {
                "sessionState": {        
                    "dialogAction": {           
                        "type": "ElicitIntent"
                    }            
                },
                "messages": [
                    {
                        "contentType": "PlainText",
                        "content": "Curso não encontrado",
                    }
                ]
            }
    
    print(retorno)
    return retorno
