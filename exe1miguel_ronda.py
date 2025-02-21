#- Faça um programa que leia os números digitados pelo usuario, 
# a cada número digitado ele deve ser somado ao anterior digitado e a cada soma exibida na tela, 
# quando a soma for superior a 50 deve exibir a mensagem “ O total é... [total] ” e parar o programa.
print("miguel do amaral paes ronda")
total = 0
while total <= 50:
    num = int(input("didgte um numero: "))
    total += num
    if total > 50 :
        print("o total e {}".format(total))
        break