import sys
import Levenshtein

def carregar_perguntas(caminho):
    perguntas_respostas = []
    with open(caminho, 'r', encoding='utf-8') as f:
        for linha in f:
            linha = linha.strip()
            if not linha or '|' not in linha:
                print(f"Linha inválida ignorada: {linha}")
                continue
            pergunta, resposta = linha.split('|', 1)
            perguntas_respostas.append((pergunta, resposta))
    return perguntas_respostas

def encontrar_pergunta_similar(perguntas_respostas, pergunta, limiar):
    for p, r in perguntas_respostas:
        if Levenshtein.distance(p.lower(), pergunta.lower()) <= limiar:
            return r
    return "Desculpe, não sei a resposta para isso."

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python chat_bot.py <limiar_distancia>")
        sys.exit(1)

    limiar_distancia = int(sys.argv[1])
    perguntas_respostas = carregar_perguntas("perguntas.txt")

    while True:
        pergunta = input("Faça uma pergunta: ").lower()
        if pergunta == "sair":
            break
        resposta = encontrar_pergunta_similar(perguntas_respostas, pergunta, limiar_distancia)
        print(resposta)
