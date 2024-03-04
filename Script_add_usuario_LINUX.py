
import os 
import sys
import subprocess 
import getpass 
import platform 
import crypt

usuario = input ("Nome de usuario: ")
diretorio = input("Diretorio: ")
grupo = input("Grupo: ")
senha = (crypt.crypt(getpass.getpass("Senha: "), crypt.mksalt(crypt.METHOD_SHA512)))  


# adicionar grupo
def novogrupo():
    try:
        subprocess.run(['groupadd', grupo ])

    except: 
         print(f"Erro ao criar grupo.")                      
         sys.exit(1)

# criar diretorio
def novodir():
    try:
        # rodar o comando mkdir do Linux 
        subprocess.run(['mkdir', "-p", diretorio ])

    except: 
         print(f"Erro ao criar diretorio.")                      
         sys.exit(1) 

# adicionar o usuario
def novaconta(): 

    try: 
         # rodar o comando useradd do Linux
         subprocess.run(['useradd', '-c', comentario, '-d', diretorio, '-g', grupo, '-M', '-s', '/sbin/nologin', '-p', senha, usuario ])

    except: 
         print(f"Erro ao criar usuario.")                      
         sys.exit(1)

novogrupo()
novodir()
novaconta()
