# ATIVIDADE 2 - CRIPTOGRAFIA RSA
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


def eh_primo(numero, mostrar=False):
    """Verifica se um numero e primo testando divisores."""
    if numero <= 1:
        if mostrar:
            print(f"{numero} nao e primo, pois precisa ser maior que 1.")
        return False

    divisor = 2
    while divisor * divisor <= numero:
        resto = numero % divisor
        if mostrar:
            print(f"Teste: {numero} mod {divisor} = {resto}")
        if resto == 0:
            if mostrar:
                print(f"{numero} e divisivel por {divisor}; portanto, nao e primo.")
            return False
        divisor += 1

    if mostrar:
        print(f"Nenhum divisor foi encontrado. {numero} e primo.")
    return True


def inverso_modular(numero, modulo):
    """Encontra d tal que numero * d == 1 (modulo modulo)."""
    print(f"\nProcurando o inverso de {numero} modulo {modulo}:")
    for candidato in range(1, modulo):
        resto = (numero * candidato) % modulo
        print(f"Teste: ({numero} * {candidato}) mod {modulo} = {resto}")
        if resto == 1:
            print(f"Inverso encontrado: {candidato}")
            return candidato
    return None


def potencia_modular(base, expoente, modulo, titulo):
    """Calcula base**expoente mod modulo por multiplicacoes e reducoes sucessivas."""
    print(f"\n{titulo}")
    print(f"Calculando {base}^{expoente} mod {modulo} por reducoes sucessivas:")

    resultado = 1
    base_atual = base % modulo
    expoente_atual = expoente
    etapa = 1

    while expoente_atual > 0:
        print(
            f"Etapa {etapa}: expoente = {expoente_atual}, "
            f"base = {base_atual}, resultado acumulado = {resultado}"
        )

        if expoente_atual % 2 == 1:
            resultado_anterior = resultado
            resultado = (resultado_anterior * base_atual) % modulo
            print(
                f"Expoente impar: resultado = ({resultado_anterior} * "
                f"{base_atual}) mod {modulo} = {resultado}"
            )

        base_anterior = base_atual
        base_atual = (base_anterior * base_anterior) % modulo
        expoente_atual = expoente_atual // 2
        print(f"Nova base = ({base_anterior} * {base_anterior}) mod {modulo} = {base_atual}")
        print(f"Novo expoente = {expoente_atual}")
        etapa += 1

    resultado = resultado % modulo
    print(f"Resultado final: {base}^{expoente} mod {modulo} = {resultado}")
    return resultado


def parte_a():
    print("\n========== PARTE A - PRIMALIDADE E PARAMETROS RSA ==========")

    while True:
        p = ler_inteiro("Digite o numero primo p: ")
        q = ler_inteiro("Digite o numero primo q: ")

        if p <= 1 or q <= 1:
            print("p e q precisam ser inteiros maiores que 1. Tente novamente.\n")
            continue
        if p == q:
            print("p e q precisam ser distintos. Tente novamente.\n")
            continue

        primo_p = eh_primo(p, mostrar=True)
        primo_q = eh_primo(q, mostrar=True)
        if not primo_p or not primo_q:
            print("Os dois valores precisam ser primos. Informe novos valores.\n")
            continue

        n = p * q
        phi = (p - 1) * (q - 1)
        if phi <= 2:
            print("Esses valores nao permitem escolher e com 1 < e < phi(n). Informe outros primos.\n")
            continue
        break

    print("\nCalculos dos parametros:")
    print(f"n = p * q = {p} * {q} = {n}")
    print(f"phi(n) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi}")

    while True:
        e = ler_inteiro(f"Escolha o expoente publico e (1 < e < {phi}): ")
        if not (1 < e < phi):
            print("O expoente precisa estar entre 1 e phi(n).")
            continue

        resultado_mdc = mdc(e, phi, mostrar=True)
        if resultado_mdc == 1:
            break
        print("O MDC precisa ser 1. Escolha outro expoente.\n")

    print("\nParametros escolhidos:")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n}")
    print(f"phi(n) = {phi}")
    print(f"e = {e}")

    return p, q, n, phi, e


def parte_b(e, n, phi):
    print("\n========== PARTE B - CONSTRUCAO DAS CHAVES ==========")
    d = inverso_modular(e, phi)

    if d is None:
        print("Nao foi possivel encontrar o inverso multiplicativo.")
        return None

    verificacao = (e * d) % phi
    print("\nVerificacao do inverso:")
    print(f"e * d = {e} * {d} = {e * d}")
    print(f"({e} * {d}) mod {phi} = {verificacao}")

    if verificacao == 1:
        print("A verificacao esta correta: e * d == 1 (mod phi(n)).")
    else:
        print("A verificacao falhou.")

    print(f"Chave publica: (e, n) = ({e}, {n})")
    print(f"Chave privada: (d, n) = ({d}, {n})")
    return d


def parte_c(n, e, d):
    print("\n========== PARTE C - CIFRAGEM E DECIFRAGEM ==========")

    M = ler_inteiro(f"Digite o numero M (0 <= M < {n}): ")
    while M < 0 or M >= n:
        print("M precisa estar entre 0 e n - 1.")
        M = ler_inteiro(f"Digite novamente M (0 <= M < {n}): ")

    C = potencia_modular(M, e, n, "CIFRAGEM")
    M_linha = potencia_modular(C, d, n, "DECIFRAGEM")

    print("\nResultado da cifragem e decifragem:")
    print(f"Numero original: M = {M}")
    print(f"Numero cifrado: C = {C}")
    print(f"Numero decifrado: M' = {M_linha}")

    if M_linha == M:
        print("Conclusao: M' = M. A decifragem recuperou o numero original.")
    else:
        print("Conclusao: M' diferente de M. Verifique os parametros informados.")

    return M


def parte_d(p, n, phi, M):
    print("\n========== PARTE D - TEOREMAS DE EULER E FERMAT ==========")

    # Teorema de Euler: exige MDC(M, n) = 1.
    print("\n1) Verificacao do Teorema de Euler:")
    resultado_mdc = mdc(M, n, mostrar=True)

    if resultado_mdc == 1:
        print(f"Como MDC({M}, {n}) = 1, o Teorema de Euler pode ser aplicado.")
        resultado_euler = potencia_modular(
            M, phi, n, "Aplicacao do Teorema de Euler"
        )
        print(f"Verificacao: {M}^{phi} mod {n} = {resultado_euler} (esperado: 1).")
    else:
        print(f"Como MDC({M}, {n}) = {resultado_mdc}, o Teorema de Euler nao pode ser aplicado a base {M} e modulo {n}.")
        print("Nesse caso, calculamos a potencia diretamente por reducoes sucessivas:")
        resultado_direto = potencia_modular(
            M, phi, n, "Reducao sucessiva sem usar Euler"
        )
        print(f"Resultado calculado: {M}^{phi} mod {n} = {resultado_direto}.")

    # Pequeno Teorema de Fermat: p precisa ser primo e p nao pode dividir a.
    print("\n2) Verificacao do Pequeno Teorema de Fermat:")
    a = ler_inteiro(f"Digite uma base a que nao seja divisivel por {p}: ")
    while a % p == 0:
        print(f"A base nao pode ser multipla de {p}. Tente novamente.")
        a = ler_inteiro(f"Digite outra base a: ")

    print(f"O modulo {p} e primo e {a} mod {p} = {a % p}, diferente de zero.")
    resultado_fermat = potencia_modular(
        a, p - 1, p, "Aplicacao do Pequeno Teorema de Fermat"
    )
    print(f"Verificacao: {a}^{p - 1} mod {p} = {resultado_fermat} (esperado: 1).")

    print("\nCondicoes:")
    print("- Euler: o MDC entre a base e o modulo deve ser 1.")
    print("- Fermat: o modulo deve ser primo e a base nao pode ser divisivel por ele.")
    print("- Quando essas condicoes nao forem atendidas, a potencia modular por reducoes sucessivas continua valida.")


def main():
    print("ATIVIDADE 2 - CRIPTOGRAFIA RSA")
    p, q, n, phi, e = parte_a()
    d = parte_b(e, n, phi)

    if d is None:
        print("Fim do programa: nao foi possivel construir as chaves.")
        return

    M = parte_c(n, e, d)
    parte_d(p, n, phi, M)
    print("\nFim da Atividade 2.")


if __name__ == "__main__":
    main()
