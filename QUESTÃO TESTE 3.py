user=input("Digite o login: ")
senha= int(input("Digite a senha: "))
if user== "admin":
    print("O usuário está correto.")
    if senha== 1234:
        print("A senha está correta.")
        print("Login realizado com sucesso!")
else: 
    if user!= "admin":
        print("O usuário está incorreto.")
    if senha!= 1234:
        print("A senha está incorreta.")
    print("Usuário ou senha incorretos.")