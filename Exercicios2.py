#Exercicio 1
#Solicitar numeros aos ususrios
numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))

#Verifica  e imprime o maior numero
if numero1 > numero2:
    print(f"O maior numero e {numero1}.")
if numero2 > numero1:
    print(f"O maior numero e {numero2}.")
if numero1 == numero2:
    print(f"Os dois numeros sao iguais.")

#Exercicio 2
#Solicitar turno que estuda
turno_estuda = input("Qual turno voce estuda? Digite M-matutino V-vespertino N Noturno. ")

#Verifica o turno
if turno_estuda == "M":
    print("Bom dia! ")
if turno_estuda == "V" :
    print("Boa tarde! ")
if turno_estuda == "N" :
    print("Boa noite! ")


#Exercicio 3

#Exercicio 4
#Solicitar nota do aluno
nota = float(input("Qual a sua nota? De 0 a 10. " ))

#Verifica aprovacao
if nota >= 7:
    print("Aprovado. ")
if nota < 7:
    print("Reprovados. ")

#Exercicio 5
