import json

# simulação dos dados de pedidos
pedidos = {
    '123456': {
        'pedido':{
            'data_pedido':'2022-03-04',
            'status':'entregue',
            'data_entrega':'2022-03-07',
            'recebedor': 'João Sousa'
        }
    },
    '999999': {
        'pedido': {
            'data_pedido':'2022-06-23',
            'status':'em rota de entrega',
            'data_entrega': None,
            'recebedor': None
        }
    },
    '123123': {
        'pedido': {
            'data_pedido':'2022-07-13',
            'status':'faturado',
            'data_entrega': None,
            'recebedor': None
        }
    }
}

def lambda_handler(event, context):
    acao = event.get('acao')
    numero_pedido = event.get('numero_pedido')
    pedido = pedidos.get(numero_pedido, {'erro':'Pedido não encontrado'})
    
    return {
        'statusCode': 200,
        'body': json.dumps(pedido)
    }
