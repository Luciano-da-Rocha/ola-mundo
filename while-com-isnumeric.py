# -*- coding: utf-8 -*-
"""
Created on Thu May 21 19:57:07 2020

@author: Luciano da rocha!
""" #EXERCICIO 104 do Curso em video Python


        
def numerovalido(n):    
    #n=input('Digite um numero inteiro: ').strip()
    if n.isnumeric():
        n= int(n)
    while type(n)!=int:
        n=input('Digite um numero inteiro, sem espaços, digitos ou caracteres: ')
        if n.isnumeric():
            n= int(n)
            break
        else:
            continue
    return print(f'Você digitou o numero: {n}')    

n=input('Digite um numero: ')
numerovalido(n)