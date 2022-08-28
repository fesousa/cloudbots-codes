# cloudbots-codes

## Implantar função lambda com SAM

Configurar variáveis de ambiente para conectar na AWS

Windows/PowerShell

```ps
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