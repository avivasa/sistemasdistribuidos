## Livro Sistemas Distribuídos
## Prof. Alessandro Vivas Andrade
## Exemplo de um Servidor Web

# Importação da Biblioteca Flask
from flask import Flask           

# Criar uma instância do Flask
servidor = Flask(__name__)          

# definir as rotas
# método principal será executado quando entrarmos no servidor
# quando entrar no link http://host:porta:/ o método principal()
@servidor.route("/")        

def principal():             
    return "<center> <H1> Servidor Web </H1> </center>"         

# define a ação para execução do script
if __name__ == "__main__":        
    servidor.run()                     
