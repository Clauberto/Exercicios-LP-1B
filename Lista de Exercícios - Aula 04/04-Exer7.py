#Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
temp = float(input("Digite a temperatura em Fahrenheit:"))
print("O valor da temperatura {:.1f} em Fahrenheit, será a {:.1f} em Celsius.".format(temp,((temp-32)/1.8)))