num = int(input("Digite um número inteiro maior que 1: "))  

if num > 1:  
    primo = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))  
    print("É primo" if primo else "Não é primo")  
else:  
    print("Número inválido. Digite um inteiro maior que 1.")  
