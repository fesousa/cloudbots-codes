# cloudbots-codes

## Implantar função lambda com SAM

### Configurar variáveis de ambiente para conectar na AWS

Windows/PowerShell

```powershell
$Env:AWS_DEFAULT_REGION="regiao"
$Env:AWS_ACCESS_KEY_ID="aws_access_key_id"
$Env:AWS_SECRET_ACCESS_KEY="aws_secret_access_key"
$Env:AWS_SESSION_TOKEN="aws_session_token"
```

Linux

```bash
export AWS_DEFAULT_REGION=regiao
export AWS_ACCESS_KEY_ID=aws_access_key_id
export AWS_SECRET_ACCESS_KEY=aws_secret_access_key
export AWS_SESSION_TOKEN=aws_session_token
```

### Implantar com SAM

Construir código

```bash
sam build
```

Criar pacote

```bash
sam package --region us-east-1 --resolve-s3
```

Implantar

```bash
sam deploy --stack-name amazon-lex-bob-stack --region us-east-1 --capabilities CAPABILITY_IAM --resolve-s3 --parameter-overrides role=FuncaoIAMPermissao
```


## Exemplo de evento do Lex

```json
{
   "sessionId":"242841987931764",
   "inputTranscript":"IA",
   "interpretations":[
      {
         "intent":{
            "slots":{
               "NomeCurso":{
                  "shape":"Scalar",
                  "value":{
                     "resolvedValues":[
                        "IA",
                        "Big Data"
                     ],
                     "interpretedValue":"IA",
                     "originalValue":"IA"
                  }
               }
            },
            "confirmationState":"None",
            "name":"Informacoes",
            "state":"InProgress"
         },
         "nluConfidence":1.0
      },
      {
         "intent":{
            "slots":{
               
            },
            "confirmationState":"None",
            "name":"FallbackIntent",
            "state":"InProgress"
         }
      },
      {
         "intent":{
            "slots":{
               "NomeUsuario":"None"
            },
            "confirmationState":"None",
            "name":"ContatoInicial",
            "state":"InProgress"
         },
         "nluConfidence":0.17
      }
   ],
   "sessionState":{
      "sessionAttributes":{
         
      },
      "intent":{
         "slots":{
            "NomeCurso":{
               "shape":"Scalar",
               "value":{
                  "resolvedValues":[
                     "IA",
                     "Big Data"
                  ],
                  "interpretedValue":"IA",
                  "originalValue":"IA"
               }
            }
         },
         "confirmationState":"None",
         "name":"Informacoes",
         "state":"InProgress"
      },
      "originatingRequestId":"fe0c6dcf-ce24-471c-8802-81034f04e3d9"
   },
   "responseContentType":"text/plain; charset=utf-8",
   "invocationSource":"DialogCodeHook",
   "messageVersion":"1.0",
   "inputMode":"Text",
   "bot":{
      "aliasName":"TestBotAlias",
      "aliasId":"TSTALIASID",
      "name":"BobDev",
      "version":"DRAFT",
      "localeId":"pt_BR",
      "id":"LGCXKRCGLH"
   }
}
```