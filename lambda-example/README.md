# Exemplo Lambda

Exemplo para utilizar parâmetro event de uma função lambda

Exemplos de eventos:

Retorno OK

```json
{
  "acao": "consulta_pedido",
  "numero_pedido": "123456"
}
```

Retorno OK

```json
{
  "acao": "consulta_pedido",
  "numero_pedido": "999999"
}
```

Retorno OK

```json
{
  "acao": "consulta_pedido",
  "numero_pedido": "123123"
}
```

Retorno Erro

```json
{
  "acao": "consulta_pedido",
  "numero_pedido": "111111"
}
```