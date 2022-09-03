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
   "sessionId":"087395486615644",
   "inputTranscript":"ia",
   "interpretations":[
      {
         "intent":{
            "slots":{
               "NomeCurso":{
                  "shape":"Scalar",
                  "value":{
                     "originalValue":"ia",
                     "resolvedValues":[
                        "IA",
                        "Big Data"
                     ],
                     "interpretedValue":"IA"
                  }
               }
            },
            "confirmationState":"None",
            "name":"Informacoes",
            "state":"InProgress"
         }
      },
      {
         "intent":{
            "slots":{
               "Email":"None",
               "NomeCurso":{
                  "shape":"Scalar",
                  "value":{
                     "originalValue":"ia",
                     "resolvedValues":[
                        "IA",
                        "Big Data"
                     ],
                     "interpretedValue":"IA"
                  }
               },
               "NomeSemestre":"None"
            },
            "confirmationState":"None",
            "name":"Matricula",
            "state":"InProgress"
         },
         "nluConfidence":0.51
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
               "NomeUsuario":{
                  "shape":"Scalar",
                  "value":{
                     "originalValue":"ia",
                     "resolvedValues":[
                        
                     ],
                     "interpretedValue":"ia"
                  }
               }
            },
            "confirmationState":"None",
            "name":"ContatoInicial",
            "state":"InProgress"
         },
         "nluConfidence":0.41
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
                  "originalValue":"ia",
                  "resolvedValues":[
                     "IA",
                     "Big Data"
                  ],
                  "interpretedValue":"IA"
               }
            }
         },
         "confirmationState":"None",
         "name":"Informacoes",
         "state":"InProgress"
      },
      "originatingRequestId":"b752b2f2-f661-4ff9-a568-e81ae44c5d26"
   },
   "responseContentType":"text/plain; charset=utf-8",
   "invocationSource":"DialogCodeHook",
   "messageVersion":"1.0",
   "inputMode":"Text",
   "bot":{
      "aliasName":"TestBotAlias",
      "aliasId":"TSTALIASID",
      "name":"Bob",
      "version":"DRAFT",
      "localeId":"pt_BR",
      "id":"MXJ4CZ9LVO"
   }
}

```