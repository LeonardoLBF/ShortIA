import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "leonardlbf"
LOCATION = "us-central1"


def main():
  print("=== ShortIA: Iniciando no projeto leonardlbf ===")

  try:
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    model = GenerativeModel("gemini-1.5-flash")

    print("Conexão com o Vertex AI estabelecida com sucesso!")

    response = model.generate_content(
        "Escreva uma frase curta confirmando que o sistema ShortIA está"
        " operando perfeitamente."
    )

    print("\n--- Resposta da IA ---")
    print(response.text)
    print("----------------------")

  except Exception as e:
    print(f"Ocorreu um erro na execução: {e}")


if __name__ == "__main__":
  main()



