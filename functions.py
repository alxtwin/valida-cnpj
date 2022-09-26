#Função básic para formatar os dados vindos do usuário
from multiprocessing.sharedctypes import Value


def formata_cnpj(cnpj):
    cnpj_formatado = cnpj.replace('.', '').replace(
        '-', '').replace('/', '')[: -2]

    return cnpj_formatado

#Fórmula para calcular validade do CNPJ (geral)
def formula(digito):
    return 11 - (digito % 11)

#Cálculo do CNPJ
#Código instável e tremendamente mal-feito. Necessário otimizar.
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
        if segundo_digito > 9:
            segundo_digito = 0

        #Devolve os dados ao usuário após verificação.
        return f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{primeiro_digito}{segundo_digito}'
    except ValueError:
        return 'erro inesperado.'


def check(cnpj, resultado):
    if cnpj == resultado:
        return ':)'
    else:
        return ':('