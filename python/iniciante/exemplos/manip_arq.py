'''
###########################################################
##                                                       ##
##                IFNMG Campus Januária                  ##
##            Projeto Bate-papo Tecnológico              ##
##  Curso de capacitação em Python 3 - nível iniciante   ##
##          Exemplo de Manipulação de Arquivos           ##
##                                                       ##
###########################################################
'''

__project_name__ = 'Bate-papo tecnológico'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2016-06-27 19:45:55.278703'

from datetime import datetime # importa o módulo datetime (import...) presente no pacote datetime (from...)
import os
from pathlib import Path

# criando alguns métodos...

def listaDir(pDir='.'):
    '''
        -> Método listaDir(pDir)
        Objetivo listar o conteúdo do diretório informado como parâmetro.
        Caso não seja informado um diretório será listado o diretório onde o 
        script em execução está localizado.
    '''
    if os.path.exists(pDir): # verifica se o diretório existe
        p = Path(pDir) # instancia p como o diretório passado
        print(100 * '-')
        print('Diretório: ', os.path.abspath(pDir))
        for i in p.iterdir(): 
            print('\t->', i)
        print(100 * '-')
        
if __name__ == '__main__':
    listaDir()