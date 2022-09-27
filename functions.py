# Função básic para formatar os dados vindos do usuário
# from multiprocessing.sharedctypes import Value
import random


def formata_cnpj(cnpj):
    cnpj_formatado = cnpj.replace('.', '').replace(
        '-', '').replace('/', '')[: -2]

    return cnpj_formatado

# Fórmula para calcular validade do CNPJ (geral)


def formula(digito):
    return 11 - (digito % 11)


# Cálculo do CNPJ
# Código instável e tremendamente mal-feito. Necessário otimizar.


def calculo(cnpj):
    cnpj = formata_cnpj(cnpj)
    digito_1 = 0
    digito_2 = 0
    contador_1 = 5
    contador_2 = 6
    try:
        for x in range(0, 12):
            digito_1 += int(cnpj[int(x)]) * contador_1
            contador_1 -= 1
            if contador_1 < 2:
                contador_1 = 9
        primeiro_digito = formula(digito_1)

        for x in range(0, 12):
            digito_2 += int(cnpj[int(x)]) * contador_2
            contador_2 -= 1
            if contador_2 < 2:
                contador_2 = 9
        segundo_digito = primeiro_digito * 2 + digito_2
        segundo_digito = formula(segundo_digito)

        if primeiro_digito > 9:
            primeiro_digito = 0

        if segundo_digito > 9:
            segundo_digito = 0
        # Devolve os dados ao usuário após verificação.
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{primeiro_digito}{segundo_digito}'
    except ValueError:
        return 'erro inesperado.'


def check(cnpj, resultado):
    if cnpj == resultado:
        return 'validado >:)'
    else:
        return 'Inválido >:('


def gera_cnpj():
    primeiro_digito = random.randint(0, 9)
    segundo_digito = random.randint(0, 9)
    segundo_bloco = random.randint(100, 999)
    terceiro_bloco = random.randint(100, 999)
    quarto_bloco = '0001'
    digito_um = '0'
    digito_dois = '0'

    cnpj_raw = f'{primeiro_digito}{segundo_digito}.{segundo_bloco}.{terceiro_bloco}/{quarto_bloco}-{digito_um}{digito_dois}'
    cnpj_gerado = calculo(cnpj_raw)
    cnpj_gerado_final = calculo(cnpj_gerado)

    print(cnpj_gerado_final)
    return cnpj_gerado, cnpj_gerado_final
