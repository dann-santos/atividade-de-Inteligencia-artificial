# Definição do ambiente

ambiente = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
]

# Definição do agente

class Agente:

    def __init__(self, energia, bolsa):
        self.energia = energia
        self.bolsa = bolsa

    def mover(self, direcao):
        # Move o agente na direção especificada

        if direcao == "N":
            self.posicao[0] -= 1
        elif direcao == "S":
            self.posicao[0] += 1
        elif direcao == "E":
            self.posicao[1] += 1
        elif direcao == "W":
            self.posicao[1] -= 1

        self.energia -= 1

    def aspirar(self):
        # Aspira a sujeira no quadrado atual

        if ambiente[self.posicao[0]][self.posicao[1]] == 1:
            ambiente[self.posicao[0]][self.posicao[1]] = 0
            self.bolsa.adicionar_sujeira()

        self.energia -= 1

    def voltar_para_casa(self):
        # Move o agente de volta para a posição inicial

        direcoes = ["N", "S", "E", "W"]
        direcao_atual = direcoes[self.posicao[0] - self.posicao_inicial[0]]

        while self.posicao != self.posicao_inicial:
            self.mover(direcao_atual)
            direcao_atual = direcoes[(direcao_atual + 1) % 4]

    def decidir_acao(self):
        # Decide qual ação tomar

        if self.bolsa.cheia:
            return "Voltar para casa"

        if ambiente[self.posicao[0]][self.posicao[1]] == 1:
            return "Aspirar"

        return "Mover"

    def encontrar_rota(self):

        fronteira = []

        fronteira.append((self.posicao, []))
        
        while fronteira:

            estado_atual, caminho = fronteira.pop(0)


            if estado_atual == self.posicao_inicial:
                return caminho

            for vizinho in self.obter_vizinhos(estado_atual):
                fronteira.append((vizinho, caminho + [vizinho]))

        return None

# Instanciação do agente

class Bolsa:

    def __init__(self, limite):
        self.limite = limite
        self.sujeira = 0 
    def adicionar_sujeira(self):
        self.sujeira += 1
    def cheia(self):
        return self.sujeira == self.limite 


agente = Agente(100, Bolsa(10))

# Início do algoritmo

agente.posicao = [0, 0]
agente.posicao_inicial = agente.posicao

while True:
    # Decide qual ação tomar
    direcao = agente.decidir_acao()

    # Realiza a ação
    if direcao == "Mover":
        agente.mover(direcao)
    elif direcao == "Aspirar":
        agente.aspirar()
    elif direcao == "Voltar para casa":
        agente.voltar_para_casa()
        break

# Verifica se o objetivo foi alcançado

if ambiente.count(0) == 16:
    print("Objetivo alcançado!")
else:
    print("Objetivo não alcançado!")
