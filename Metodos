

def verificar_sequencia(seq):
    for i in range(len(seq)):
        if seq[i] not in ["A","T","C","G"]:
            return False
        return True

class Pessoa:
    def __init__(self):
        self.contatos = []

    def novo_cliente(self, dicionario, dados):
        nome = input("Insira o nome do Cliente:")
        contato = input("Insira o contacto do Cliente:")
        self.contatos.append(contato)
        dados['contatos'] = self.contatos
        while True:
            outro_contato = input("Insira outro contacto (ou digite 0 para sair):")
            if outro_contato == '0':
                break
            else:
                dados['contatos'].append(outro_contato)
        dicionario[nome] = dados

        return dicionario

    def novo_contato_cliente(self, dicionario):
        nome = input("Insira o nome do Cliente:")

        if nome in dicionario.keys():
            print("O",nome,"tem os seguintes contatos:",dicionario[nome]['contatos'])
            novo_contato = input("Insira o novo contato de " + nome + ":")
            dicionario[nome]['contatos'].append(novo_contato)
        else:
            print("Erro- Cliente não existe. Crie primeiro uma entrada...")
        return dicionario

    def associar_DNA(self, dicionario):
        nome = input("Insira o nome do Cliente:")

        if nome in dicionario.keys():
            while True:
                sequencia = input("Insira a sequencia de DNA de " + nome + ":").upper()
                if verificar_sequencia(sequencia):
                    dicionario[nome]['DNA'] = sequencia
                    break
                else:
                    print("Erro- A sequência de DNA não é valida...")
        else:
            print("Erro- Cliente não existe. Crie primeiro uma entrada...")
        return dicionario

    def apagar_contato(self, dicionario):
        nome = input("Insira o nome do Cliente:")
        print("Contatos de",nome,"são", dicionario[nome]['contatos'])
        contato = input("Insira o contato que deseja excluir:")
        if contato in dicionario[nome]['contatos']:
            dicionario[nome]['contatos'].remove(contato)
        else:
            print("Erro- O contacto",contato,"não está associado ao Cliente", nome)
        return dicionario

    def agenda(self, dicionario):
        nome = input("Insira o nome do Cliente:")
        print("Cliente: ", nome)
        if len(dicionario[nome]['contatos']) != 0:
            for i in range(len(dicionario[nome]['contatos'])):
                print("\tcontato " + str(i+1) + " :  " + dicionario[nome]['contatos'][i])
            if dicionario[nome]['DNA'] is None:
                print('ola')
            # if len(dicionario[nome]['DNA']) != 0:
            #    print("\tDNA:   ", dicionario[nome]['DNA'])
        else:
            print("\tDNA:   ", dicionario[nome]['DNA'])

