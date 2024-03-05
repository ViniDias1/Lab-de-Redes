

import sys
import os
import crypt

def adicionarUsuario(nome):
    #try:
        os.system("useradd "+nome)
        os.system("passwd "+nome)
    #except:
        #print("Erro")
        #sys.exit(1)
nome = sys.argv[1]
#senha = sys.argv[2]

adicionarUsuario(nome)
print "Usuario criado com sucesso!" 
