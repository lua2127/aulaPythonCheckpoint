emails = ["email1@gmail.com", "email2@gmail.com","email3@gmail.com","email4@gmail.com","email5@gmail.com","email6@gmail.com","email7@gmail.com","email8@gmail.com","email9@gmail.com","email10@gmail.com","email11@gmail.com","email12@gmail.com","email13@gmail.com","email14@gmail.com","email15@gmail.com","email16@gmail.com","email17@gmail.com","email18@gmail.com","email19@gmail.com","email20@gmail.com","email21@gmail.com","email22@gmail.com","email23@gmail.com","email24@gmail.com","email25@gmail.com","email26@gmail.com","email27@gmail.com","email28@gmail.com","email29@gmail.com","email30@gmail.com"]
vazamento = input("Qual o email que quer verificar?: ")

while vazamento in emails:
        print("Vish... o email foi vazado.")
        vazamento = input("Qual o email que quer verificar?: ")
       
        print("O email não foi vazado.")
#para procurar um email, digite como o exemplo "email1@gmail.com", os emails cadastrados só mudam o número antes do "@"