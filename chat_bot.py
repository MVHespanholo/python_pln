import Levenshtein

def carregar_perguntas(caminho):
    perguntas_respostas = []
    with open(caminho, 'r', encoding='utf-8') as f:  # Adicione encoding='utf-8'
        for linha in f:
            pergunta, resposta = linha.strip().split('|')
            perguntas_respostas.append((pergunta, resposta))
    return perguntas_respostas


def encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia=5):
  menor_distancia = float("inf")
  melhor_resposta = ""
  for p, r in perguntas_respostas.items():
    distancia = Levenshtein.distance(pergunta, p)
    if distancia < menor_distancia:
      menor_distancia = distancia
      melhor_resposta = r
  if menor_distancia <= limiar_distancia:
      return melhor_resposta
  else:
      return "Pergunta não encontrada."

if __name__ == "__main__":
  perguntas_respostas = carregar_perguntas("perguntas.txt")
    limiar_distancia = 10
    pergunta = "Quem é Você?"
    if pergunta == "sair":
      break
    resposta = encontrar_resposta(pergunta, perguntas_respostas, limiar_distancia)
    print("Resposta:", resposta)
