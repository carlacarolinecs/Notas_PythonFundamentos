print("*********************************** Python Calculator ******************************************")

print("\n")
print("Selecione o número da operação desejada: ")
print("\n")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

print("\n")

oper= int(input("Digite sua opção (1/2/3/4): "))
num1= int(input("Digite o primeiro número: "))
num2= int(input("Digite o segundo número: "))

print("\n")

if oper == 1:
    Soma = num1 + num2
    print("%s + %r =" %(num1,num2),Soma)
elif oper == 2:
    Subt = num1 - num2
    print("%s - %r =" %(num1,num2),Subt)
elif oper ==3:
    Mult = num1 * num2
    print("%s * %r =" %(num1,num2),Mult)
elif oper ==4:
    Div = num1 / num2
    print("%s / %r =" %(num1,num2),Div)
else:
    print("Opção inválida!")
