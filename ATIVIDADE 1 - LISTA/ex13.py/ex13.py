salario = float(input("Digite o salário inicial: "))  
aumento = float(input("Digite o percentual de aumento no primeiro ano: "))  
anos = int(input("Digite a quantidade de anos: "))  

for i in range(anos):  
    salario += salario * (aumento / 100)  
    aumento *= 2  

print(f"O salário após {anos} anos será: R$ {salario:.2f}")  
