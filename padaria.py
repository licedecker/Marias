pao_frances=0
pao_farofa=0
pao_liso=0
pao_integral=0
pao_forma=0
valor_frances=0
valor_farofa=0
valor_liso=0
valor_integral=0
valor_forma=0
valor_total=0
print("***Padaria das Marias***")
print("1-Pão Frances")
print("2-Pão Farofa")
print("3-Pão liso")
print("4-Pão Integral")
print("5-Pão Forma")
print("6-Sair")
opcao=int(input("Escolha a sua opcão: "))
while opcao!=6:
    if opcao==1:
        print("Você escolheu o pão frances")
        pao_frances=int(input("Digite a quantidade de pão frances: "))
        valor_frances=pao_frances*1.04
        print(f"O valor total de pães doces franceses é igual a ${valor_frances}")
        opcao=int(input("Escolha outra opção: "))
    if opcao==2:
        print("Você escolheu o pão doce com farofa")
        pao_farofa=int(input("Digite a quantidade de pão doce com farofa: "))
        valor_farofa=pao_farofa*1.11
        print(f"O valor total de pães doces com farofa é igual a ${valor_farofa}")
        opcao=int(input("Escolha outra opção: "))
    if opcao==3:
        print("Você escolheu o pão doce liso")
        pao_liso=int(input("Digite a quantidade de pão doce liso: "))
        valor_liso=pao_liso*1.08
        print(f"O valor total de pães doces lisos é igual a ${valor_liso}")
        opcao=int(input("Escolha outra opção: "))
    if opcao==4:
        print("Você escolheu o pão integral")
        pao_integral=int(input("Digite a quantidade de pão integral: "))
        valor_integral=pao_integral*1.04
        print(f"O valor total de pães integrais é igual a ${valor_integral}")
        opcao=int(input("Escolha outra opção: "))
    if opcao==5:
        print("Você escolheu o pão forma")
        pao_forma=int(input("Digite a quantidade de pão forma: "))
        valor_forma=pao_forma*1.95
        print(f"O valor total de pães de forma é igual a ${valor_forma}")
        opcao=int(input("Escolha outra opção: "))
    if opcao==6:
        print("Saindo")
if valor_frances>0:
    print (f"Pão Frances-- Quantidade {pao_frances}-- Valor ${valor_frances}")
if valor_farofa>0:
    print (f"Pão Doce com Farofa-- Quantidade {pao_farofa}-- Valor ${valor_farofa}")
if valor_liso>0:
    print (f"Pão Doce Liso-- Quantidade {pao_liso}-- Valor ${valor_liso}")
if valor_integral>0:
    print (f"Pão Integral-- Quantidade {pao_integral}-- Valor ${valor_integral}")
if valor_forma>0:
    print (f"Pão Forma-- Quantidade {pao_forma}-- Valor ${valor_forma}")
valor_total=valor_integral+valor_farofa+valor_forma+valor_frances+valor_liso
print(f"O valor total da compra é:  ${valor_total}")