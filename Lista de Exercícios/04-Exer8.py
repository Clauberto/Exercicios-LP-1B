# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele.
algumacoisa = input('Digite alguma coisa:')
print("É um valor numérico? ",algumacoisa.isnumeric()) #verifica se é numérico
print("É uma letra?", algumacoisa.isalpha()) #verifica se é letra
print("Tem espaçamento? ",algumacoisa.isspace()) #se é só espaço
print("Alpha é numérico? ",algumacoisa.isalnum()) # se é alpha numerico por exemplo 3a
print("Possui letras maiúsculas? ",algumacoisa.isupper()) # se esta em letras maiusculas
print("Possui letras minúsculas? ",algumacoisa.islower()) # se esta em letras minuscula
print("A palavra é capitalizada? ",algumacoisa.istitle()) # palavra capitalizada por exemplo, Python 