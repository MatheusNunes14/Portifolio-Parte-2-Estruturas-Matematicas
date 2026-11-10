# ATIVIDADE 1 - CONGRUENCIA MODULAR E TEOREMA CHINES DO RESTO
# Estruturas Matematicas para Computacao - Python


def ler_inteiro(mensagem):
    """Le um numero inteiro e repete a pergunta se a entrada for invalida."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um numero inteiro valido.")


def mdc(a, b, mostrar=False):
    """Calcula o MDC pelo algoritmo de Euclides."""
    a = abs(a)
    b = abs(b)

    if mostrar:
        print(f"\nCalculando MDC({a}, {b}) pelo algoritmo de Euclides:")

    while b != 0:
        resto = a % b
        if mostrar:
            quociente = a // b
            print(f"{a} = {b} * {quociente} + {resto}")
        a, b = b, resto

    if mostrar:
        print(f"MDC = {a}")
    return a


def inverso_modular(numero, modulo):
    """Procura um inverso y tal que numero * y tenha resto 1 no modulo."""
    if modulo == 1:
        print("Modulo 1: podemos usar o representante 0, pois todos os inteiros sao congruentes modulo 1.")
        return 0

    print(f"\nProcurando o inverso de {numero} modulo {modulo}:")
    for candidato in range(1, modulo):
        resto = (numero * candidato) % modulo
        print(f"Teste: ({numero} * {candidato}) mod {modulo} = {resto}")
        if resto == 1:
            print(f"Inverso encontrado: {candidato}")
            return candidato

    return None


def parte_a():
    print("\n========== PARTE A - VERIFICACAO DE CONGRUENCIA ==========")

    a = ler_inteiro("Digite o valor de a: ")
    b = ler_inteiro("Digite o valor de b: ")

    n = ler_inteiro("Digite o modulo n (maior que zero): ")
    while n <= 0:
        print("O modulo precisa ser positivo.")
        n = ler_inteiro("Digite novamente n: ")

    diferenca = a - b
    resto = diferenca % n

    print("\nCalculos:")
    print(f"a - b = {a} - ({b}) = {diferenca}")
    print(f"Resto de {diferenca} dividido por {n} = {resto}")

    if resto == 0:
        print(f"Conclusao: {a} e {b} sao congruentes modulo {n}.")
        print(f"Portanto, {a} == {b} (mod {n}).")
    else:
        print(f"Conclusao: {a} e {b} NAO sao congruentes modulo {n}.")


def parte_b():
    print("\n========== PARTE B - TEOREMA CHINES DO RESTO ==========")

    quantidade = ler_inteiro("Quantas congruencias deseja resolver (3 ou 4)? ")
    while quantidade not in (3, 4):
        print("Escolha somente 3 ou 4 congruencias.")
        quantidade = ler_inteiro("Quantidade: ")

    restos = []
    modulos = []

    for i in range(quantidade):
        print(f"\nCongruencia {i + 1}: x == a{i + 1} (mod n{i + 1})")
        ai = ler_inteiro(f"Digite o resto a{i + 1}: ")
        ni = ler_inteiro(f"Digite o modulo n{i + 1} (positivo): ")
        while ni <= 0:
            print("O modulo precisa ser positivo.")
            ni = ler_inteiro(f"Digite novamente n{i + 1}: ")
        restos.append(ai)
        modulos.append(ni)

    print("\nVerificando se os modulos sao dois a dois coprimos:")
    for i in range(quantidade):
        for j in range(i + 1, quantidade):
            resultado_mdc = mdc(modulos[i], modulos[j], mostrar=True)
            if resultado_mdc != 1:
                print("\nO sistema esta fora das condicoes desta atividade.")
                print(f"Os modulos {modulos[i]} e {modulos[j]} nao sao coprimos.")
                return

    # Produto de todos os modulos.
    N = 1
    for modulo in modulos:
        N *= modulo

    print("\nProduto dos modulos:")
    print("N = " + " * ".join(str(valor) for valor in modulos) + f" = {N}")

    soma = 0
    print("\nCalculando cada parcela da solucao:")

    for i in range(quantidade):
        ai = restos[i]
        ni = modulos[i]
        Ni = N // ni

        print(f"\nEquacao {i + 1}: x == {ai} (mod {ni})")
        print(f"N{i + 1} = N / n{i + 1} = {N} / {ni} = {Ni}")

        yi = inverso_modular(Ni, ni)
        if yi is None:
            print("Nao foi possivel encontrar o inverso. Confira os modulos informados.")
            return

        parcela = ai * Ni * yi
        soma += parcela
        print(f"Parcela = a{i + 1} * N{i + 1} * y{i + 1}")
        print(f"Parcela = {ai} * {Ni} * {yi} = {parcela}")

    x0 = soma % N

    print("\nSomando as parcelas:")
    print(f"Soma = {soma}")
    print(f"x0 = {soma} mod {N} = {x0}")

    print("\nVerificacao da solucao:")
    tudo_certo = True
    for i in range(quantidade):
        resto_verificacao = x0 % modulos[i]
        confere = resto_verificacao == (restos[i] % modulos[i])
        print(
            f"{x0} mod {modulos[i]} = {resto_verificacao}; "
            f"resto esperado = {restos[i] % modulos[i]} -> "
            f"{'OK' if confere else 'ERRO'}"
        )
        if not confere:
            tudo_certo = False

    if tudo_certo:
        print("\nSolucao encontrada!")
        print(f"Solucao geral: x = {x0} + t * {N}, com t pertencente aos inteiros.")
    else:
        print("\nA verificacao falhou. Confira os dados e os calculos.")


def main():
    print("ATIVIDADE 1 - CONGRUENCIA MODULAR E TEOREMA CHINES DO RESTO")
    print("\nEscolha o que deseja executar:")
    print("1 - Parte A: verificacao de congruencia modular")
    print("2 - Parte B: Teorema Chines do Resto")
    print("3 - Executar as duas partes")

    opcao = ler_inteiro("Digite 1, 2 ou 3: ")

    if opcao == 1:
        parte_a()
    elif opcao == 2:
        parte_b()
    elif opcao == 3:
        parte_a()
        parte_b()
    else:
        print("Opcao invalida. Execute o programa novamente e escolha 1, 2 ou 3.")

    print("\nFim da Atividade 1.")


if __name__ == "__main__":
    main()
