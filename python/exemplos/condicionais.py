'''
###########################################################
##                                                       ##
##                IFNMG Campus Januária                  ##
##            Projeto Bate-papo Tecnológico              ##
##  Curso de capacitação em Python 3 - nível iniciante   ##
##          Exemplo de estruturas condicionais           ##
##                                                       ##
###########################################################
'''

__project_name__ = 'Bate-papo tecnológico'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2016-05-30T20:00:00.071699'


# importando módulos

import os

# definindo métodos
def limpaTela():
    
    if os.name == 'nt': # verifica se é Windows
        os.system('cls')
        
    elif os.name == 'posix': # verifica se é Posix (Linux, Mac, BSD, etc)
        os.system('clear')
        
    else:
        print('[ERRO: OS \'', os.name, '\' não identificado]')
    
# FIM --- definindo métodos

while True:
    
    # menu inicial
    print('\nEscolha uma das opções:\n\t1 -> Faixa etária')
    print('\t2 -> Maior número')
    print('\t0 -> Sair')
    
    opcao = int(input('Sua escolha: '))
    
    if opcao == 0:
        print('Fui!')
        break # Pára o programa
    
    elif opcao == 1:
        # criança 0-11 | Adolescente 12-18 | Adulto 19-59 | Idoso 60+
        limpaTela()
        
        idade = int(input('Informa uma idade: '))
        
        if (idade >= 0) and (idade < 12):
            print('Uma pessoa nessa idade é criança.')
            
        elif (idade >= 12) and (idade < 19):
            print('Uma pessoa nessa idade é adolescente.')

        elif (idade >= 19) and (idade < 59):
            print('Uma pessoa nessa idade é adulto.')

        elif (idade >= 60):
            print('Uma pessoa nessa idade é idoso.')

        continue
    
    elif opcao == 2:
        
        limpaTela()
        qtde_num = int(input('Quantos números você deseja informar: '))
        
        lista = list()
        
        for i in range(qtde_num):
            lista.append(int(input('Informe um número inteiro: ')))
            
            if len(lista) == 1: # se a lista tiver apenas um item esse será o maior
                maior = lista[0]
                
            elif maior < lista[len(lista) - 1]: # verifica se foi adicionado a lista (último item) um número maior
                maior = lista[len(lista) - 1]
                
        print('Os números foram:\n', lista, ',\nsendo o número \"', maior, '\" o maior informado.')
        
        continue
    
    else:
        input('\n\t#### ALERTA ####\n\tOpção inválida!\n\t[pressione ENTER]')
        limpaTela()
            
        
