#Gerador de senhas:

chave = input("Digite a chave para geração da sua senha: ")

senha = ""

for letra in chave:
    if letra in "Aa": senha = senha + '10'
    elif letra in "Bb": senha = senha + '11'
    elif letra in "Cc": senha = senha + '12'
    elif letra in "Dd": senha = senha + '13'
    elif letra in "Ee": senha = senha + '14'
    elif letra in "Ff": senha = senha + '15'
    elif letra in "Ss": senha = senha + '$'
    elif letra in "Oo": senha = senha + '0'
    elif letra in "Hh": senha = senha + '#'
    elif letra in "Ii": senha = senha + '!'
    elif letra in "Tt": senha = senha + '7'
    elif letra in "Rr": senha = senha + '?'
    else: senha = senha + letra
print(senha)
