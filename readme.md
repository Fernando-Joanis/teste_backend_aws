# Backend AWS

## Como rodar o projeto:

Após clonar o projeto, instalar o requirements.txt

Criar um layer na função lambda e inserir os pacotes necessários.

Configurar a IAM e a VPC para acessar o S3 da AWS e o banco que hoje está alocado na RDS também da AWS.

###Passar as variaveis de ambiente na função lambda:

HOST_DB

NAME_DB

PORT_DB

PSW_DB

USER_DB

## URL e Parametros para chamar a função:

### URL = https:"Link da função lambda"/?bucket_name=NOME_DO_BUCKET&object_key=NOME_DO_ARQUIVO.csv

##Query Params

bucket_name

object_key

