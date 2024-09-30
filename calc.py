while True: 
    print("Calculadora")
    numero1 = float(input("Digite o número 1: "))
    operacao = str(input("Digite a operação desejada ([+]Para somar, [-]Para subtrair, [*]Para multiplicar, [/]Para dividir: "))
    numero2 = float(input("Digite o número 2: "))
    if operacao == "+":
        resp = numero1 + numero2
        print(resp)
    elif operacao == "-":
        resp = numero1 - numero2
        print(resp)
    elif operacao == "*":
        resp = numero1 * numero2
        print(resp)
    elif operacao == "/":
        resp = numero1 / numero2
        print(resp)
print("________"*10)
