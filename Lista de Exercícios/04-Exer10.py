# Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere: US$ 1.00 = R$ 5.41
money = float(input("Quantos R$ você possui?")) 
print("Você poderá comprar ${:.2f}".format(money/5.41))
