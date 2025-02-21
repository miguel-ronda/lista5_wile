#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.
print("miguel do amaral paes ronda")
num1 = float(input("digite um numero: "))
num2 = float(input("digite um segundo numero: "))
soma = num1 + num2 
print("a soma destes numeros e de:",soma)
resp = str(input("voce deseja adcionar mais algum numero (s/n)"))
while resp == "s":
    num = float(input("difite outro numero:"))
    soma += num
    resp = input("voce deseja adcionar mais algum numero (s/n)")
print("a soma destes numeros e de:",soma)