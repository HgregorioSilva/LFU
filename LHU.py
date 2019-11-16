Entrada = []
Contador_paginacao = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while True:
    valor_entrada = int(input("Digite a páginação: "))
    if valor_entrada in Entrada:
        Contador_paginacao[valor_entrada - 1] = Contador_paginacao[valor_entrada - 1] + 1
        print(Entrada)
        print(Contador_paginacao)
    else:
        if (len(Entrada) < 5):
            Entrada.append(valor_entrada)
            Contador_paginacao[valor_entrada - 1] = Contador_paginacao[valor_entrada - 1] + 1
            print(Entrada)
            print(Contador_paginacao)
        else:
            i = 0
            while i < len(Entrada):
                print(i)
                if (Contador_paginacao[(Entrada[i - 1]) - 1]) == 1:
                    Contador_paginacao[Entrada[i - 1] - 1] = 0
                    Contador_paginacao[valor_entrada - 1] = Contador_paginacao[valor_entrada - 1] + 1
                    Entrada[i - 1] = valor_entrada
                i = i + 1
                break
