#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salário do funcionário:"))
print("O salário do funcionário após aumento será de R${:.2f}".format(salario*1.15))