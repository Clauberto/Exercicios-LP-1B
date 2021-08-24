#Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
temp = float(input("Digite a temperatura em Celsius:"))
print("O valor da temperatura {:.1f} em Celsius, será a {:.1f} em Kelvin.".format(temp,temp+273))