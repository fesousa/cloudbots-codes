
def lambda_handler(event, context):
    print("EVENTO: ", event)
               
    retorno =  {
        'statusCode': 200,
        'body': event.get('queryStringParameters').get('mensagem') if event.get('queryStringParameters') else event.get('body').get('mensagem') 
    }
    
    return retorno
