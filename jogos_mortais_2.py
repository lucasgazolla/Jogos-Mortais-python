import os
import asyncio
import edge_tts
import time
import random
import sys
import random
from playsound import playsound

def falar(texto):
    VOZ = "pt-BR-AntonioNeural" 
    ARQUIVO = "voz_mestre.mp3"
    
    async def gerar():
        communicate = edge_tts.Communicate(texto, VOZ)
        await communicate.save(ARQUIVO)

    try:
        asyncio.run(gerar())
        playsound(ARQUIVO)
        if os.path.exists(ARQUIVO):
            os.remove(ARQUIVO)
    except Exception:
        pass 

os.system("cls")
os.system('color 0a')

#nome = input("Digite seu nome: ")
os.system("cls")

#frase_inicial = f"Bem vindo {nome}. Você passou a vida desperdiçando seu tempo, mas hoje, cada segundo vale a sua sobrevivência. Você tem o que é preciso para sair vivo?"

#print(frase_inicial)
#falar(frase_inicial) 

os.system("cls")
os.system('color 04')

print(''' 
░██████╗░█████╗░██████╗░████████╗███████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░██║░░██║██████╔╝░░░██║░░░█████╗░░███████║██║░░██║██║░░██║██████╔╝
░╚═══██╗██║░░██║██╔══██╗░░░██║░░░██╔══╝░░██╔══██║██║░░██║██║░░██║██╔══██╗
██████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║
╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝    
      ''')

time.sleep(2)
os.system("cls")

numero1 = random.randint(1,3)

print(f"GABARITO: {numero1}") 

frase_p1 = "Um número entre 1 e 3 separa sua vida da sua morte. Qual é a sua escolha? "

print(frase_p1, end="", flush=True)
falar(frase_p1)
resposta1 = int(input())

if resposta1 == numero1:
    os.system("cls")
    os.system("color 0a")
    v1 = "A sorte o favoreceu... desta vez, mas não se iluda."
    print(v1)
    falar(v1)
    time.sleep(2)
    os.system("cls")
    os.system("color 07")
else:
    os.system("cls")
    os.system("color 0c")
    e1 = f"Sério? Você realmente achou que o número era esse? HAHAHA o número era o {numero1}"
    print(e1)
    falar(e1)
    time.sleep(3)
    os.system("cls")
    print('''      
░██████╗░░█████╗░███╗░░░███╗███████╗  ░█████╗░██╗░░░██╗███████╗██████╗░
██╔════╝░██╔══██╗████╗░████║██╔════╝  ██╔══██╗██║░░░██║██╔════╝██╔══██╗
██║░░██╗░███████║██╔████╔██║█████╗░░  ██║░░██║╚██╗░██╔╝█████╗░░██████╔╝
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░  ██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗  ╚█████╔╝░░╚██╔╝░░███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝  ░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝
    ''')
    time.sleep(2)
    os.system("cls")
    os.system("color 07")
    sys.exit()

numero2 = random.randint(1,10)
numero3 = random.randint(1,10)
resposta2 = numero2 ** numero3

print(f"GABARITO: {resposta2}") 
 
frase_p2 = f"O sistema gerou 2 números aleatórios. Prepare sua mente para o cálculo: quanto é {numero2} elevado a {numero3}? "

print(frase_p2, end="", flush=True)
falar(frase_p2)
escolha2 = int(input())

os.system("cls")

if escolha2 == resposta2:
    os.system("color 0a")
    v2 = "Sobreviveu novamente... por enquanto."
    print(v2)
    falar(v2)
    time.sleep(2)
    os.system("cls")
    os.system("color 07")
else:
    os.system("color 0c")
    e2 = f"Parece que alguém faltou às aulas de matemática e agora vai pagar o preço em bits. O resultado era {resposta2}"
    print(e2)
    falar(e2)
    os.system("cls")
    print('''
██████╗░███████╗██████╗░██████╗░███████╗██╗░░░██╗
██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║░░░██║
██████╔╝█████╗░░██████╔╝██║░░██║█████╗░░██║░░░██║
██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██╔══╝░░██║░░░██║
██║░░░░░███████╗██║░░██║██████╔╝███████╗╚██████╔╝
╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝░╚═════╝░
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
resultado3 = (resposta1 + resposta2) ** resposta1 - resposta2
print(f"GABARITO: {resultado3}") 

frase_p3 = "Se prestou atenção até agora, Boa sorte: (resposta1 + resposta2) ** resposta1 - resposta2. Qual o resultado ? "
print(frase_p3, end="", flush=True)
falar(frase_p3)
resposta3 = int(input())

os.system("cls")

if resposta3 == resultado3:
    v3 = "Parabéns, você ainda está vivo."
    print(v3)
    falar(v3)
    time.sleep(3)
else:
    os.system("color 0c")
    e3 = "Não foi dessa vez"
    print(e3)
    falar(e3)
    time.sleep(3)
    sys.exit()

os.system("cls")
os.system("color 07")

print("Preste muita atenção...")
falar("Preste muita atenção")
time.sleep(2)
os.system("cls")

memoria1 = random.randint(1,10)
memoria2 = random.randint(1,10)
memoria3 = random.randint(1,10)
memoria4 = random.randint(1,10)
memoria5 = random.randint(1,10)

print(f"{memoria1} {memoria2} {memoria3} {memoria4} {memoria5}")
time.sleep(3)
os.system("cls")

frase_p4 = "Digite os 5 números que apareceram na tela, separados por espaço: "
print(frase_p4, end="", flush=True)
falar("Quais números se apresentaram na tela?")

try:
    entrada = input().strip().split()
    r1, r2, r3, r4, r5 = [int(x) for x in entrada]
except:
    print("Entrada inválida!")
    quit()

os.system("cls")

if r1 == memoria1 and r2 == memoria2 and r3 == memoria3 and r4 == memoria4 and r5 == memoria5:
    v4 = "Meus parabéns, está indo mais longe do que o esperado"
    print(v4)
    falar(v4)
else:
    e4 = "Sabia que não teria competência para ir até o final HAHAHA"
    print(e4)
    falar(e4)
    time.sleep(2)
    quit()

os.system("color 07")

os.system("cls")
msg_f = "Você chegou na fase final, agora vamos resolver um mistério...preste muita atenção."
print(msg_f)
falar(msg_f)
time.sleep(3)
os.system("cls")

print("Dica:Lembre-se, 1 byte = 8 bits, 1024 bytes = 1 KB, 1024 KB = 1 MB")
frase_p5 = '''Um programador encontra um nano computador que trabalha apenas com bits. O
computador tem exatamente 41.943.040 bits de memória. 
Quantos Megabytes isso representa ?  '''

print(f"GABARITO: 5") 
print(frase_p5, end="", flush=True)
falar(frase_p5)
resposta5 =  int(input())

os.system("cls")

resultado5 = 5

if resposta5 == resultado5:
    os.system("color 0a")
    v5 = "Você sobreviveu, está livre para ir..."
    print(v5)
    falar(v5)
    time.sleep(2)
    os.system("color 0c")
    v5_2 = "Para seu descanso eterno, ninguém sai vivo do meu jogo HAHAHA"
    print(v5_2)
    falar(v5_2)
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
    sys.exit()
else:
    os.system("color 0c")
    e5 = "Você nunca teve a menor chance HAHAHAH"
    print(e5)
    falar(e5)
    os.system("cls")
    print('''
          
       ██╗   ██╗ ██████╗  ██████╗███████╗                  
██║   ██║██╔═══██╗██╔════╝██╔════╝                  
██║   ██║██║   ██║██║     █████╗                    
╚██╗ ██╔╝██║   ██║██║     ██╔══╝                    
 ╚████╔╝ ╚██████╔╝╚██████╗███████╗                  
  ╚═══╝   ╚═════╝   ╚═════╝╚══════╝                  
                                                      
███╗   ███╗ ██████╗ ██████╗ ██████╗ ███████╗██╗   ██╗
████╗ ████║██╔═══██╗██╔══██╗██╔══██╗██╔════╝██║   ██║
██╔████╔██║██║   ██║██████╔╝██████╔╝█████╗  ██║   ██║
██║╚██╔╝██║██║   ██║██╔══██╗██╔══██╗██╔══╝  ██║   ██║
██║ ╚═╝ ██║╚██████╔╝██║   ██║██║   ██║███████╗╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚═╝   ╚═╝╚═╝   ╚═╝╚══════╝ ╚═════╝    
          
''')
    time.sleep(3)
    sys.exit()