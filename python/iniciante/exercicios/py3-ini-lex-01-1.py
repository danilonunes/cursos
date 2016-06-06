'''
###########################################################
##                                                       ##
##                IFNMG Campus Januária                  ##
##            Projeto Bate-papo Tecnológico              ##
##  Curso de capacitação em Python 3 - nível iniciante   ##
##          Lista de exercícios py3-ini-lex-01           ##
##                     Exercício 01                      ##
##                                                       ##
###########################################################

Enunciado (http://wiki.python.org.br/EstruturaDeDecisao):

    As Organizações Tabajara resolveram dar um aumento de salário aos seus 
    colaboradores e lhe contrataram para desenvolver o programa que calculará os 
    reajustes. 
    
    Faça um programa que recebe o salário de um colaborador e calcule o reajuste
    segundo o seguinte critério, baseado no salário atual:
    
        -> salários até R$ 280,00 (incluindo): aumento de 20%
        -> salários entre R$ 280,00 e R$ 700,00: aumento de 15%
        -> salários entre R$ 700,00 e R$ 1500,00: aumento de 10%
        -> salários de R$ 1500,00 em diante: aumento de 5% 
        
    Após o aumento ser realizado, informe na tela:
        -> o salário antes do reajuste;
        -> o percentual de aumento aplicado;
        -> o valor do aumento;
        -> o novo salário, após o aumento. 

'''

__project_name__ = 'Bate-papo tecnológico'
__author__ = 'Prof. Danilo Nunes <danilo.nunes@ifnmg.edu.br>'
__updated__ = '2016-06-06T18:00:00.000000'


salario_atual = float(input('Informe o salário: '))
salario_ok = False

if (salario_atual >= 0) and (salario_atual <= 280.0):
    
    salario_ok = True
    reajuste = 0.2
    vr_aumento = salario_atual * reajuste
    salario_novo = salario_atual + vr_aumento
    
elif salario_atual > 280.00 and salario_atual <= 700.00:
    
    salario_ok = True
    reajuste = 0.15
    vr_aumento = salario_atual * reajuste
    salario_novo = salario_atual + vr_aumento
    
elif salario_atual > 700.00 and salario_atual <= 1500.00:
    
    salario_ok = True
    reajuste = 0.10
    vr_aumento = salario_atual * reajuste
    salario_novo = salario_atual + vr_aumento
    
elif salario_atual > 1500.00:
    
    salario_ok = True
    reajuste = 0.05
    vr_aumento = salario_atual * reajuste
    salario_novo = salario_atual + vr_aumento

if salario_ok:
    
    print('-' * 60)
    print('Salário base: R$', salario_atual)
    print('Percentual de aumento: ', reajuste * 100, '%')
    print('Valor do aumento: R$', vr_aumento)
    print('Salário reajustado: R$', salario_novo)
    print('-' * 60)
    
else:
    print('!' * 60)
    print('O salário \'', salario_atual, '\' informado é inválido.')
    print('!' * 60)