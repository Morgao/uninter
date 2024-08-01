class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

class TabelaHash:
    def __init__(self):
        self.tabela = [self.criarNodoNone() for _ in range(10)]  

    def criarNodoNone(self):
        return Nodo("None", "None")

    def hash(self, sigla):
        if sigla == "DF":
            return 7
        e1 = ord(sigla[0])
        e2 = ord(sigla[1])
        return (e1 + e2) % 10

    def inserir(self, sigla, nomeEstado):
        indice = self.hash(sigla)
        novo_nodo = Nodo(sigla, nomeEstado)
        atual = self.tabela[indice]
        if atual.sigla == "None": 
            self.tabela[indice] = novo_nodo
            novo_nodo.proximo = self.criarNodoNone()
        else:
            while atual.proximo and atual.proximo.sigla != "None":
                atual = atual.proximo
            novo_nodo.proximo = atual.proximo
            atual.proximo = novo_nodo

    def imprimirTabela(self):
        for i in range(len(self.tabela)):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            while atual is not None:
                print(f"{atual.sigla} ", end="")
                atual = atual.proximo
            print()

def menu():
    tabela_hash = TabelaHash()
    estados = {
        "AC": "Acre", "AL": "Alagoas", "AP": "Amapá", "AM": "Amazonas", "BA": "Bahia",
        "CE": "Ceará", "DF": "Distrito Federal", "ES": "Espírito Santo", "GO": "Goiás",
        "MA": "Maranhão", "MT": "Mato Grosso", "MS": "Mato Grosso do Sul", "MG": "Minas Gerais",
        "PA": "Pará", "PB": "Paraíba", "PR": "Paraná", "PE": "Pernambuco", "PI": "Piauí",
        "RJ": "Rio de Janeiro", "RN": "Rio Grande do Norte", "RS": "Rio Grande do Sul",
        "RO": "Rondônia", "RR": "Roraima", "SC": "Santa Catarina", "SP": "São Paulo",
        "SE": "Sergipe", "TO": "Tocantins", "MN": "Matheus Nakade"  
    }

    while True:

        print("###################################")
        print("##             Menu              ##")
        print("##1 - Mostrar tabela hash        ##")
        print("##2 - Inserir estado             ##")
        print("##3 - Sair                       ##")
        print("###################################")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            tabela_hash.imprimirTabela()
        elif opcao == 2:
            sigla = input("Digite a sigla do estado (2 letras): ").upper()
            if sigla in estados:
                nomeEstado = estados[sigla]
                tabela_hash.inserir(sigla, nomeEstado)
                print(f"Estado {nomeEstado} ({sigla}) inserido na tabela hash.")
            else:
                print("Sigla inválida. Tente novamente.")
        elif opcao == 3:
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
