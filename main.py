import os

# Pega a chave secreta chamada SHORTIA que configuramos no GitHub
api_key = os.getenv("SHORTIA")

print("Olá! Meu projeto no GitHub começou a funcionar!")

if api_key:
  print("Tudo certo: a chave secreta foi lida com segurança!")
else:
  print("Atenção: a chave não foi encontrada.")

