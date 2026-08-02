import os
import google.generativeai as genai

# 1. Recupera a chave secreta guardada no GitHub Actions
api_key = os.getenv("SHORTIA")

if not api_key:
  print("Atenção: A chave de API não foi encontrada nas variáveis de ambiente.")
else:
  print("Chave de API carregada com segurança!")

  # 2. Configura a Inteligência Artificial com a sua chave
  genai.configure(api_key=api_key)

  # 3. Escolhe o modelo de IA que vai responder (Gemini)
  model = genai.GenerativeModel("gemini-1.5-flash")

  # 4. Envia uma mensagem de teste para a IA
  print("Conectando com a IA...")
  response = model.generate_content(
      "Escreva uma frase curta e motivacional sobre começar a programar."
  )

  print("\n--- Resposta da Inteligência Artificial ---")
  print(response.text)
  print("------------------------------------------")


