# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 22:00:37 2022

@author: gusan
"""
import datetime
import easygui
import os

folder = easygui.diropenbox()
data = datetime.datetime.now()
data_texto = (str(data.strftime("%y.%m.%d_%H.%M.%S")))

arquivos = os.listdir(folder)

entrada = easygui.enterbox(msg="Qual a palavra solicitada",title='Buscador')

textos = []

lista_ok = []
lista_nok = []


for file in arquivos:
    if ".txt" in file:
        name = os.path.join(folder,file)
        with open (name, 'r', encoding='utf-8') as leitor:
            texto = leitor.read()
            textos.append(texto)
    
        # for item in textos:
        #     prep_check = item.split(' ')
        prep_check = texto.split(' ')
            
        for palavra in prep_check:
            # print (palavra)
            if entrada in palavra:
                print (f'Ok - Localizado : {palavra} | Buscador: {entrada}')
                lista_ok.append(f'{file}\n')
                break
        else:
            lista_nok.append(f'{file}\n')
    else:
        pass

achados = len(lista_ok)
nachados = len(lista_nok)

        
with open (f"output - {data_texto}.txt", "a") as writer:
    lista_ok = "".join(lista_ok)
    lista_nok = "".join(lista_nok)
    writer.write(f"({data_texto})\nNo diretorio: {folder}\n")
    writer.write(f"========================\n")
    writer.write(f'\n=D - {achados} arquivos TEM a palvara solicitada:\n{lista_ok}')
    writer.write(f'\n===================================\n')
    writer.write(f'\n=( - {nachados} arquivos NAO tem a palvara solicitada:\n{lista_nok}\n')
    
easygui.msgbox(f"Foram encontrados {achados} arquivos com a palavra solicitada")