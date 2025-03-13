import random

def sortear_aluno():
    
    alunos = []
    print("Digite os nomes dos alunos (digite 'sair' para finalizar):")
    
    while True:
        nome = input("Nome do aluno: ").strip()
        if nome.lower() == "sair":  
            break
        alunos.append(nome)  
    
    if not alunos:  
        print("Nenhum aluno foi adicionado.")
        return
    
    aluno_sorteado = random.choice(alunos)  
    print(f"\nO aluno sorteado para limpar a lousa é: {aluno_sorteado}")


sortear_aluno()