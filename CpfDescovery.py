#Importando as bibliotecas:
import random
from time import sleep
import os, platform

#Função para limpar o terminal de acordo com o terminal:
def clear_os():
    
    #Se for Windows, ele limpa o terminal com "cls":
    if platform.system() == 'Windows': 
        os.system('cls')
    
    #Se for Linux ou Mac, limpa o terminal com "clear":
    else:
        os.system('clear')

#Criando uma função para verificar se os 2 digitos verificadores de um CPF usando sua matemática.
#Link para ver a matemática por trás do CPF (https://www.somatematica.com.br/faq/cpf.php):
def cpf_verificador(cpf: str):
    #Criando uma lista que "mapeia" todos os caracteres da string "cpf" e transforma em int:
    cpf_list = list(map(int, cpf))
    cpf_list.pop()
    cpf_list.pop()
    cpf_calc = 0
    count = 10
    for i in cpf_list:
        cpf_calc += i * count
        count -= 1
        
    fist_digit = cpf_calc % 11

    if fist_digit < 2:
        fist_digit = 0
        
    else:
        fist_digit = 11 - fist_digit
        
    cpf_list = list(map(int, cpf))
    cpf_list.pop()
    cpf_list.pop()
    cpf_list.append(fist_digit)
    
    cpf_calc = 0
    count = 11
    for i in cpf_list:
        cpf_calc += i * count
        count -= 1
        
    second_digit = cpf_calc % 11

    if second_digit < 2:
        second_digit = 0
        
    else:
        second_digit = 11 - second_digit
    
    #Retorna o primeiro e segundo digíto verificadores do CPF:
    return [fist_digit, second_digit]

clear_os()
print('Seja bem vindo ao CpfDiscovery!')
print('By: Arthur Speziali\n')
sleep(1)
print('Este programa valida CPF, minera CPFs válidos e descobre CPFs a partir de um incompleto.')
sleep(2)

#Menu princiapal:
clear_os()
print('Digite se quer validar, minerar ou completar um CPF. [V/M/C].\n')
while True:
    opção = input('> ').lower().strip()
    
    if opção != 'v' and opção != 'm' and opção != 'c':
        print('\nOpção inválida, tente novamente!\n')

    else:
        clear_os()
        break

if opção == 'v':
    print('Digite se quer validar manualmente ou abrir um arquivo. [M/F].\n')
    
    while True:    
        opção = input('> ').strip().lower()
        
        if opção != 'm' and opção != 'f':
            print('\nOpção inválida, tente novamente!\n')
            
        else:
            clear_os()
            break
    
    if opção == 'm':
        
        while True:
            print('Digite um CPF válido:\n')
            cpf = input('> ')
            
            #Formata o CPF para tirar seus símbolos ("-" e "."):
            cpf = cpf.replace(' ','')
            cpf = cpf.replace('-','')
            cpf = cpf.replace('.','')
            
            #Faz uma série de verificações para antes de verificar os últimos 2 dígitos, vê se o CPF está formatado:
            clear_os()
            if cpf.isnumeric():
                if len(cpf) == 11:
                    if cpf.count(cpf[0]) != len(cpf):
                        
                        #Chama a função "cpf_verificador" e verifica se os 2 últimos digitos do CPF corresponde aos digítos verificadores:
                        if int(cpf[-2]) == cpf_verificador(cpf)[0]:
                            if int(cpf[-1]) == cpf_verificador(cpf)[1]:
                                print('*- CPF Válido!\n')
                                enter = input('Pressione ENTER para continuar!')
                                clear_os()
                                
                            else:
                                print('>>> CPF Não existe (2).\n')
                                
                        else:
                            print('>>> CPF Não existe (1).\n')
                        

                    else:
                        print('>>> CPF inválido (Todos os digítos repetidos).\n')

                        
                else:
                    print('>>> CPF invalido (Não tem 11 números).\n')

            else:
                print('>>> CPF invalido (Contém letras).\n')


    elif opção == 'f':
        #Abre o arquivo para verificar se ele é válido
        print('Digite o caminho até o arquivo:\n')
        while True:
            pathe = input('> ').strip()
            
            #Verificando se o caminho esta correto, tentando abrir ele: 
            try:
                with open(pathe, encoding='utf-8') as v_path:         
                    break
                    
            except:
                print('\nCaminho mal-sucedido! Tente novamente!\n')
        
        #Detecta o So do usuário e seleciona a barra correta:           
        if platform.system == 'Windows':
            bar = '\\'
            
        else:
            bar = '/'
        
        #Formata o nome e extensão do arquivo:
        file = pathe.split(bar)[-1]
        name_file = '.'.join(file.split('.')[:-1])
        ext_file = '.' + file.split('.')[-1] 

        #Abre, lê e formata o arquivo:
        with open(pathe, 'r', encoding='utf-8') as file_txt:
            read_file = file_txt.read().split('\n')
            
            for l in read_file:
                if l == '' or l == ' ':
                    read_file.remove(l)
                
        #Verifica o CPF e coloca, se ele é valido, em uma lista onde depois é escrita no arquivo: 
        results = list()
        for i in read_file:
            verificador = cpf_verificador(i)
            
            if str(verificador[0]) == i[-2] and str(verificador[1]) == i[-1]:
                results.append(i)
                
        #Usa aquela formatação para dar nome personalizado ao arquivo:
        with open(name_file + '-validados' + ext_file, 'w') as cpf_txt:
            cpf_txt.write('')
            
        with open(name_file + '-validados' + ext_file, 'a') as cpf_txt:
            for i in results:
                cpf_txt.write(i + '\n')
                
        clear_os()
        print(f'Foram encontrados {len(results)} CPFs válidos! Localizados em "{name_file + "-validados" + ext_file}".')
            
        
elif opção == 'm':
    print('Digite quantos CPFs quer minerar:')
    while True:
        try:
            number = int(input())
            break
        
        except ValueError:
            print('\nNúmero inválido, tente novamente!\n')

    #Ele gera CPFs com números aleatórios e depoois passa pelo verificador:
    for n in range(number):
        while True:
            cpf = str()
            for i in range(11):
                cpf += str(random.randint(0, 9))

            if int(cpf[-2]) == cpf_verificador(cpf)[0] and int(cpf[-1]) == cpf_verificador(cpf)[1]:
                print(cpf, '\n')
                with open('cpf-miner.txt', 'a') as cpf_data:
                    cpf_data.write('\n' + cpf)
                    break
                
    print(f'Todos os {number} CPFs foram encontrados e escritos em "cpf-miner.txt"')
            

elif opção != 'c':
    print('Descubra qual é o CPF completo a partir de um incompleto. Digite "?" para os dígitos que não sabe.\n')
    while True:
        cpf = input('> ')
        
        cpf = cpf.replace(' ','')
        cpf = cpf.replace('-','')
        cpf = cpf.replace('.','')
        
        if '?' in cpf and cpf.replace('?', '').isnumeric() and len(cpf) == 11 and cpf.count(cpf[0]) != len(cpf):
            break

        else:
            print('\nCpf inválido, tente novamente!\n')

    clear_os()
    print('Gerando possibilidades...')

    #Cria um número com um dígito a mais do que os dígitos faltantes:
    number = 1
    for i in range(cpf.count('?')):
        number *= 10

    #Cria um limite, que é o dobro do "number", para que passe em todas as casas numerais:
    cpf_list = list()
    limit = number * 2
    #Para só o looping quando ele passar em todas as cassas, gerando todas as possibilidades de CPFs:
    while limit > number:
        
        cpf_copy = cpf
        count = 1
        while '?' in cpf_copy:
            #Retira o número faltante para prosseguir para o próximo, e no fim, acabar com este número:
            cpf_copy = cpf_copy.replace('?', str(number)[count], 1)
            count += 1
            
        cpf_list.append(cpf_copy)
        number += 1
        
    clear_os()
    print('Calculando as possibilidades...')

    results = list()
    for i in cpf_list:
        
        verificador = cpf_verificador(i)
        if str(verificador[0]) == i[-2] and str(verificador[1]) == i[-1]:
            results.append(i)

    
    #Se o resultado der mais de 10 CPFs válidos, redireciona a saída para um .txt:
    clear_os()    
    if len(results) < 1:
        print('Nenhum CPF foi encontrado.')
        
    elif len(results) <= 10:
        print(f'Foram encontrados esses CPFs:')
        
        for e, i in enumerate(results):
            print(f'{e}- {i}')
            
    elif len(results) > 10:
        with open('cpf.txt', 'w') as cpf_txt:
            cpf_txt.write('')
            
        with open('cpf.txt', 'a') as cpf_txt:
            for i in results:
                cpf_txt.write(i + '\n')
                
        
        print(f'Foram encontrados {len(results)} CPFs! Localizados em "cpf.txt".')
        