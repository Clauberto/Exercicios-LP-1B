#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
temp = float(input("Digite a temperatura em Celsius:"))
print("O valor da temperatura {:.1f} em Celsius, será {:.1f} em Fahrenheit.".format(temp,(temp*1.8+32)))