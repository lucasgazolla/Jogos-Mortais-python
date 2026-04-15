import os
import time
import random
import sys
os.system("cls")
os.system('color 0a')

nome = input ("Digite seu nome: ")

os.system("cls")

print(f"""Bem vindo {nome}. Você passou a vida desperdiçando seu tempo, mas hoje, 
cada segundo vale a sua sobrevivência. Você tem o que é preciso para sair vivo?""")

time.sleep(3)
os.system('color 04')
os.system("cls")

print(''' 
░██████╗░█████╗░██████╗░████████╗███████╗██╗░█████╗░  ███╗░░░███╗░█████╗░██████╗░████████╗░█████╗░██╗░░░░░
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║██╔══██╗  ████╗░████║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██║░░░░░
╚█████╗░██║░░██║██████╔╝░░░██║░░░█████╗░░██║██║░░██║  ██╔████╔██║██║░░██║██████╔╝░░░██║░░░███████║██║░░░░░
░╚═══██╗██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██║██║░░██║  ██║╚██╔╝██║██║░░██║██╔══██╗░░░██║░░░██╔══██║██║░░░░░
██████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗██║╚█████╔╝  ██║░╚═╝░██║╚█████╔╝██║░░██║░░░██║░░░██║░░██║███████╗
╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░╚════╝░  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  
      ''')

numero1 = random.randint(1,3)

# print(numero1) #ative somente se quiser o gabarito para conferir

resposta1 = int(input ("Um número entre 1 e 3 separa sua vida da sua morte. Qual é a sua escolha? "))

if resposta1 == numero1:
    os.system("cls")
    os.system("color 0a")
    print("A sorte o favoreceu... desta vez, mas não se iluda.")
    time.sleep(2)
    os.system("cls")
    os.system("color 07")
else:
    os.system("cls")
    os.system("color 0c")
    print(f"Sério? Você realmente achou que o número era esse? HAHAHA o número era o {numero1}")
    time.sleep(3)
    os.system("cls")
    print('''   
██╗░░░██╗░█████╗░░█████╗░███████╗  ███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██╗░░░██╗
██║░░░██║██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░  ██╔████╔██║██║░░██║██████╔╝██████╔╝█████╗░░██║░░░██║
░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░  ██║╚██╔╝██║██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░░██║
░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗  ██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║███████╗╚██████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░
    ''')
    time.sleep(2)
    os.system("cls")
    os.system("color 07")
    sys.exit()

numero2 = random.randint(1,10)
numero3 = random.randint(1,10)
resposta2 = numero2 ** numero3

# print(resposta2) #ative somente se quiser o gabarito para conferir
 
os.system("color 07")

escolha2 = int(input (f"O sistema gerou 2 números aleatórios. Prepare sua mente para o cálculo: quanto é {numero2} elevado a {numero3}? "))

os.system("cls")

if escolha2 == resposta2:
    os.system("color 0a")
    print("Sobreviveu novamente... por enquanto.")
    time.sleep(3)
    os.system("cls")
    os.system("color 07")
else:
    os.system("color 0c")
    print(f"Parece que alguém faltou às aulas de matemática e agora vai pagar o preço em bits. O resultado era {resposta2}")
    os.system("cls")
    print('''
██╗░░░██╗░█████╗░░█████╗░███████╗  ███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██╗░░░██╗
██║░░░██║██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░  ██╔████╔██║██║░░██║██████╔╝██████╔╝█████╗░░██║░░░██║
░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░  ██║╚██╔╝██║██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░░██║
░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗  ██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║███████╗╚██████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░
        ''')
    time.sleep(5)
    os.system("cls")
    os.system("color 07")
    sys.exit()

os.system("color 07")

print ('''
 █████╗  ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗ ███████╗
██╔══██╗██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗██╔════╝
███████║██║  ███╗██║   ██║███████║██████╔╝██║  ██║█████╗  
██╔══██║██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║██╔══╝  
██║  ██║╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗
╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝            
''')

time.sleep(5)
os.system("cls")
os.system("color 07")
resultado3 = (resposta1 + resposta2) ** resposta1 - resposta2

# print(resultado3) #ative somente se quiser o gabarito para conferir

resposta3 = int(input("Se prestou atenção até agora, Boa sorte: (resposta1 + resposta2) ** resposta1 - resposta2. Qual o resultado ? "))

os.system("cls")

if resposta3 == resultado3:
    print("Parabéns, você ainda está vivo.")
    os.system("color 0a")
    time.sleep(3)
else:
    os.system("color 0c")
    print("Não foi dessa vez!")
    time.sleep(3)
    os.system("cls")
    os.system("color 07")
    sys.exit()

os.system("cls")
os.system("color 07")

print("Preste muita atenção...")
time.sleep(3)
os.system("cls")
print("Responda utilizando espaços somente entre os números...um passo em falso poderá causar o seu fim!!!")
time.sleep(5)
os.system("cls")

memoria1 = random.randint(1,10)
memoria2 = random.randint(1,10)
memoria3 = random.randint(1,10)
memoria4 = random.randint(1,10)
memoria5 = random.randint(1,10)

print(f"{memoria1} {memoria2} {memoria3} {memoria4} {memoria5}")
time.sleep(2)
os.system("cls")

resposta4= input("Quais números se apresentaram na tela? ")

os.system("cls")

resultado4Ok=f"{memoria1} {memoria2} {memoria3} {memoria4} {memoria5}"

if resposta4 == resultado4Ok:
    print("Meus parabéns, está indo mais longe do que o esperado")
    os.system("color 0a")
else:
    print("Sabia que não teria competência para ir até o final HAHAHA")
    os.system('color 04')
    time.sleep(2)
    os.system("cls")
    quit()

os.system("cls")
print("Você chegou na fase final, agora vamos resolver um mistério...preste muita atenção.")
os.system("color 0a")
time.sleep(3)
os.system("cls")

os.system("color 07")

resposta5= int(input('''Um programador encontra um nano computador que trabalha apenas com bits. O
computador tem exatamente 41.943.040 bits de memória. 
Dica:Lembre-se, 1 byte = 8 bits, 1024 bytes = 1 KB, 1024 KB = 1 MB
Quantos Megabytes isso representa ?  '''))

os.system("cls")

resultado5=5

if resposta5==resultado5:
    os.system("color 0a")
    print("Você sobreviveu, está livre para ir...")
    time.sleep(2)
    os.system("cls")
    os.system("color 0c")
    print("Para seu descanso eterno, ninguém sai vivo do meu jogo HAHAHA")
    time.sleep(2)
    os.system("cls")
    print('''
                                                                                     
       ░░░     ░░░       
       ░░░░   ░░░░       
        ░░░░  ░░░░       
      ▓███▓▓▒▓▓▓███▓     
  ▓▓ ▓▓▒▒▒▓█▓██▓▒▒▒█▒ ▓░ 
 ▒▓▓██░░▒░░▒▓▓▒░▓░░▓█▓█▓ 
 ▓█▓█▓░▓▓░░░█▓░░▓▒░▓███▓░
▒▓█▒█▓░░▓░░▒█▓░░▓░░▓█▒█▓▒
▒██░▒█▒▒▓░░▓██▒░▓▒▒█▓░▓█▒
░▓▓░░▒█▓▓▓▓████▓▓▓█▓░░▓▓░
   ░░░░▒▓███▓▓███▒░░░░   
    ░░░░░░░░▒░░░░░░░░░   
      ░░░░░░░░░░░░░░     
       ▒█▓▒▒▒░░▒▓▓       
      ░▓██████████▓      
    ░▒████▓▓▓▓▓▓███▓▒░       
             ''')
    time.sleep(3)
    sys.exit
else:
    os.system("color 0c")
    print("Você nunca teve a menor chance HAHAHAH")
    os.system("cls")
    print('''          
██╗░░░██╗░█████╗░░█████╗░███████╗  ███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██╗░░░██╗
██║░░░██║██╔══██╗██╔══██╗██╔════╝  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║
╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░  ██╔████╔██║██║░░██║██████╔╝██████╔╝█████╗░░██║░░░██║
░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░  ██║╚██╔╝██║██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░░██║
░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗  ██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║███████╗╚██████╔╝
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░
''')
    