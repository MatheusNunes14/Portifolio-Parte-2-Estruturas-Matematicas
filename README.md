Matheus Augusto Nunes Santos - 2612130021

PORTFOLIO DE PROGRAMACAO MATEMATICA - PARTE 2

Python

ARQUIVOS
- atividade1_congruencia_tcr.py: verificacao de congruencia e Teorema Chines do Resto.
- atividade2_criptografia_rsa.py: parametros RSA, construcao de chaves, cifragem, decifragem, Euler e Fermat.
- Documento_Explicativo.docx: procedimentos, exemplos e testes com entradas validas e invalidas.

COMO EXECUTAR
1. Instale o Python 3.
2. Abra o terminal na pasta em que os arquivos foram salvos.
3. Para a primeira atividade, execute:
   python atividade1_congruencia_tcr.py
   No menu, digite 1 para executar somente a Parte A, 2 para executar somente a Parte B ou 3 para executar as duas.
4. Para a segunda atividade, execute:
   python atividade2_criptografia_rsa.py

EXEMPLOS PRINCIPAIS
Atividade 1 - Parte A:
 a = 23, b = 8, n = 5 -> congruentes.

Atividade 1 - Parte B (3 congruencias):
 x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7)
 Resultado: x = 23 + 105t.

Atividade 1 - Parte B (4 congruencias):
 x = 1 (mod 2), x = 2 (mod 3), x = 3 (mod 5), x = 4 (mod 7)
 Resultado: x = 53 + 210t.

Atividade 2:
 p = 5, q = 11, e = 3, M = 7
 n = 55, phi(n) = 40, d = 27, C = 13 e M' = 7.

TESTES DE CONDICOES INVALIDAS
- Congruencia falsa: a = 10, b = 3, n = 4.
- CRT com modulos nao coprimos: 6, 9 e 5 (o programa deve rejeitar).
- RSA: p = 4 nao e primo; p = q = 5 nao sao distintos; e = 2 nao e coprimo com phi(55) = 40.
- Mensagem M = 55 e invalida quando n = 55.
- Euler: M = 5 e n = 55 nao sao coprimos; o programa calcula por reducoes sucessivas.
- Fermat: com p = 5, a = 5 deve ser rejeitada; a = 2 deve resultar em 1 modulo 5.

