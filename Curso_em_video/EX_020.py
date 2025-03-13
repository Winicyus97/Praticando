import random

def sortear_ordem_apresentacao():
    
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
    
    random.shuffle(alunos) 
    print("\nOrdem de apresentação dos alunos:")
    for i, aluno in enumerate(alunos, start=1):
        print(f"{i}º: {aluno}")


sortear_ordem_apresentacao()
