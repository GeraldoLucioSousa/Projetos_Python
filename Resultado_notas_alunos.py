#  Resultado de notas de  alunos


nome=str(input('Digite o nome do aluno: '))
prova_mensal=float(input(' Digite a nota mensal do aluno:  ')) 
prova_bimestral=float(input('Digite a nota bimestral do aluno:  '))
nota_caderno=float(input('Digite a nota de caderno : '))
nota_trabalho=float(input('Digite a nota do trabalho: '))
media=float


media=(prova_mensal+prova_bimestral+nota_caderno+nota_trabalho/4)

print(media)


if media <=5:
    print('Aluno reprovado')

   
elif media <=6.9:
    print('Aluno em recuperação ')
    
elif  media >=7:
    print(' Aluno aprovado')


 
    
    

                    

