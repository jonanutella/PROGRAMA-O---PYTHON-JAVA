turmas = int(input("Digite a quantidade de turmas: "))  
total_alunos = int(input("Digite a quantidade total de alunos: "))  

media = total_alunos / turmas  

if media > 40:  
    print(f"A média de alunos por turma é {media:.2f}, mas há turmas com mais de 40 alunos!")  
else:  
    print(f"A média de alunos por turma é {media:.2f}.")  
