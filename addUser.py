
import subprocess
import sys

# Função para adicionar um usuário
def adicionar_usuario(nome, senha, grupo):
    # Comando para adicionar o usuário
    comando_adduser = ["sudo", "adduser", nome]

    # Opções para o comando adduser
    if grupo:
        comando_adduser.append("--ingroup")
        comando_adduser.append(grupo)

    # Definir a senha do usuário
    comando_passwd = ["sudo", "passwd", nome]

    # Executa o comando para adicionar o usuário
    subprocess.run(comando_adduser)

    # Executa o comando para definir a senha
    subprocess.run(comando_passwd, input=senha + "\n")

# Obter nome, senha e grupo do usuário
nome = sys.argv[1]
senha = sys.argv[2]
grupo = sys.argv[3] if len(sys.argv) > 3 else None

# Adicionar o usuário
adicionar_usuario(nome, senha, grupo)

print(f"Usuário {nome} criado com sucesso!")
