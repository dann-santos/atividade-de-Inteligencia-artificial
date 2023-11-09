class AgenteAspirador:
    def _init_(self):
        self.localizacao = 'A'
        self.energia = 100
        self.bolsa_sujeira = 0

    def decidir_acao(self, ambiente):
        if self.bolsa_sujeira == 10 or self.energia == 0:
            return 'VoltarParaCasa'
        elif ambiente.tem_sujeira(self.localizacao):
            return 'Aspirar'
        else:
            return 'Mover'

    def mover(self, ambiente):
        if self.localizacao in ambiente.localizacoes:
        
            indice_atual = ambiente.localizacoes.index(self.localizacao)
            if indice_atual < len(ambiente.localizacoes) - 1:
                self.localizacao = ambiente.localizacoes[indice_atual + 1]
                self.energia -= 1
            else:
                self.localizacao = ambiente.localizacoes[0]  
                self.energia -= 1
        else:
            print("Erro: Localização atual não encontrada na lista de localizações.")


    def voltar_para_casa(self):
        self.energia -= 1
        self.localizacao = 'A'
        self.bolsa_sujeira = 0

    def aspirar(self, ambiente):
        self.energia -= 1
        ambiente.remover_sujeira(self.localizacao)
        self.bolsa_sujeira += 2

class Ambiente:
    def _init_(self):
        self.localizacoes = [
            'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H',
            'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P'
        ]
        self.sujeira = {'A', 'F','I','K', 'L','M'}

    def tem_sujeira(self, localizacao):
        return localizacao in self.sujeira

    def remover_sujeira(self, localizacao):
        if localizacao in self.sujeira:
            self.sujeira.remove(localizacao)

if __name__ == "_main_":
    agente = AgenteAspirador()
    ambiente = Ambiente()

    while agente.energia > 0:
        acao = agente.decidir_acao(ambiente)

        if acao == 'VoltarParaCasa':
            agente.voltar_para_casa()
        elif acao == 'Aspirar':
            agente.aspirar(ambiente)
        elif acao == 'Mover':
            agente.mover(ambiente)

        print(f"Localização: {agente.localizacao}, Energia: {agente.energia}, Bolsa de Sujeira: {agente.bolsa_sujeira}")