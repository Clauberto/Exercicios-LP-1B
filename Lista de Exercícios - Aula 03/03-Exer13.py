# Faça um programa que leia a largura e a altura de uma parede em metros, e calcule a sua área e
# a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
largura = float(input("Qual a largura?"))
altura = float(input("Qual a altura?"))
print("A área em metros será de {}m² \nE a quantidade de tinta necessária será de {}l/m²".format((largura*altura),((largura*altura/2))))
