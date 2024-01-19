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
#Solicita os lados do triangulo
lado1 = float(input("Digite o primeiro lado do triangulo. "))
lado2 = float(input("Digite o segundo lado do triangulo. "))
lado3 = float(input("Digite o terceiro lado do triangulo. "))

#Verifica os lados do triangulo
if lado1 == lado2 == lado3:
    print("O triangulo e equilatero. ")
if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triangulo e isosceles. ")
else :
    print("O triangulo e escaleno. ")

#Exercicio 6


#Exercicio 7
#Solicita a idade do usuario
idade = float(input("Digite sua idade. "))

#Verificacao
if idade <= 12 :
    print("Voce e uma crianca. ")
if idade == 13 < 18:
    print("Voce e um adolescente. ")
if idade == 18 < 65: 
    print("Voce e um adulto. ")
if idade >= 66 :
    print("Voce e um idoso. ")

#Exercicio 8
#Solicitar 3 numeros
numero10 = float(input("Digite o primeiro numero: "))
numero11 = float(input("Digite o segundo numero: "))
numero12 = float(input("Digite o terceiro numero: "))

#Solucao 
if numero10 > numero11 and numero10 > numero12 : 
    maior_numero = numero10
if numero11 > numero10 and numero11 > numero12 :
    maior_numero = numero11
else:
    maior_numero = numero12

#Resultado
print(f"O maior numero entre {numero10}, {numero11} e {numero12} e : {maior_numero}. ")    

#Exercicio 9