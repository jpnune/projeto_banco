# ------------------> INICIO CODIGO <------------------------

# Variáveis Globais
saldo = 0
quantidade_de_operacoes = 0
extrato = f'id{" "*15} tipo de transação {" "*26} Valor\n\n'
quantidide_saque_diario_realizado = 0

# Constantes
QUANTIDADE_SAQUE_DIARIO_MAXIMO = 3
VALOR_MAXIMO_POR_SAQUE = 500



#funções
def menu(sacar = False):
     # Menu sem opção de saque.
    limpar_tela()
    print(f'{"#"*15}  MEMENU DE OPÇOES  {"#"*15}\n')
    print(f'{" "*10}Escolha uma opcão do menu abaixo\n')
    print(f'{" "*15}[ 1 ] Consultar saldo')
    print(f'{" "*15}[ 2 ] Depositar')
    if sacar == True:
        print(f'{" "*15}[ 3 ] Sacar')
    print(f'{" "*15}[ 4 ] Extrato')
    print(f'{" "*15}[ 9 ] Sair')
    print()
    opcao = int(input(f'{"#"*51}{"\n"*3}Digite aqui --> '))
    return opcao

    
def sub_menu(menu_principal = False):
    if menu_principal == False:
        print('[ 0 ] Voltar ao menu principal\n[ 9 ] Sair\n ') 
    else:
        print('[ 0 ] Voltar ao menu principal\n[ 1 ] Fazer um novo depósito\n[ 9 ] Sair\n')
    voltar_menu = input('digite uma das opções acima: ') 
    limpar_tela() 

    # Sai da função caso seja digitado 0 ou 9.
    if voltar_menu == '0' or voltar_menu == '9':
        return voltar_menu  
    if menu_principal == False:
        print('Opção invalida!\nDigite: 0 para voltar ao menu principal ou 9 para encerrar o atendimento!\n')
        sub_menu()
    else:      
        if voltar_menu == '1':
            return voltar_menu
        else:
            print('Opção incorreta, digite 0, 1 ou 9 conforme as opções apresentada!\n')
            sub_menu(menu_principal=True)

    
def limpar_tela():
    print(f'{"\n"*20}') #limpar a tela 


# Formata a casa decimal do número inserido no input "deposito".
def formatar_string(texto):
    try:
        texto = float(texto)    
    except:
        return "Valor digitado não é um número válido. Tente um numero com casas decimais. Ex: 3.14"

    texto = str(texto)
    if (len(texto) - (str.find(texto,'.')+1) < 2) or (str.find(texto,'.') == -1): 
        texto = f'{float(texto)}0'
    else:
        texto = texto[:str.find(texto,'.')+3] 
    return texto

def visualizar_saldo(v_salda=saldo):
    print(f'Saldo disponivel: R${v_salda:.2f}\n')



def depositar(v_saldo=saldo, v_quantidade_de_operacoes=quantidade_de_operacoes, v_extrato=extrato):
    deposito = input('digite o valor do depósito: ')
    limpar_tela()
    
    deposito = formatar_string(deposito)
    
    # Verifica se o depósito é um valor positivo (maior que 0).
    if float(deposito) > 0:
        v_saldo += float(deposito) # Adiciona o valor do deposito no saldo.
        v_quantidade_de_operacoes += 1 # Soma 1 ao contador "quantidade de operações" para ser usado no extrato.
        v_extrato += f'{v_quantidade_de_operacoes}{" "*(20 - len(str(v_quantidade_de_operacoes)))}  Depósito {" "*(34-len(deposito))} R${deposito}\n' # Formata e adiciona item no extrato.
        print(f'Depósito efetuado com sucesso! {"\n"*5}')
    else:
        print('O depósito tem que ser um valor maior que R$ 0.00\n')

    return v_saldo, v_quantidade_de_operacoes, v_extrato
           

def sacar(v_saldo=saldo,
          v_quantidade_de_operacoes=quantidade_de_operacoes,
          v_extrato=extrato,
          v_quantidide_saque_diario_realizado=quantidide_saque_diario_realizado,
          V_VALOR_MAXIMO_POR_SAQUE= VALOR_MAXIMO_POR_SAQUE):
    
    while True:

            # Verifica o saldo para saber se é possível fazer saque.
            if v_saldo == 0:
                print(f'Saldo insuficiente!\n')
                break
            else:
                print(f'Saldo: R${v_saldo :.2f}\n')
                saque = input('Digite o valor de saque desejado: ')

                # Formata a casa decimal do número inserido no input "saque".
                formatar_string(saque)

                flt_saque = float(saque)
                limpar_tela() 

                # Verifica se o numero digitado é positivo.
                if flt_saque <= 0:
                    print('Valor de saque deve ser maior que R$ 0.00\n')
                else:

                    #  Verifica se o valor é menor que a restrição de valor máximo por dia.
                    if flt_saque <= V_VALOR_MAXIMO_POR_SAQUE:

                        # Verifica se valor do saldo é maior que valor do saque.
                        if flt_saque <= v_saldo:

                            # Confirmação e execução do valor do saque.
                            while True:
                                print(f'O valor de R$ {saque} será descontado da conta, confirma?\n[ 0 ] NÃO\n[ 1 ] SIM\n')
                                confirmacao = input('digite uma das opções acima: ')
                                limpar_tela() 
                                if confirmacao == '1':
                                    v_saldo -= flt_saque # Retira o valor do saldo.
                                    v_quantidade_de_operacoes += 1 # Soma 1 ao contador "quantidade de operações" para ser usado no extrato.
                                    v_extrato += f'{v_quantidade_de_operacoes}{" "*(20 - len(str(v_quantidade_de_operacoes)))}  Saque {" "*(37-len(saque))} R${saque}\n' # Formata e adiciona item no extrato.
                                    v_quantidide_saque_diario_realizado +=1 # Soma em 1 na contagem de saques diários.
                                    print(f'Saque de R$ {saque} efetuado com sucesso!\n')
                                    print(f'Saldo atual é de R${v_saldo}\n\n')
                                    break
                                elif confirmacao == '0':
                                    print('Saque CANCELADO!\n')
                                    break
                                else:
                                    print('Opção incorreta, digite 0 para cancelar o saque ou 1 para confirmar o saque.\n')
                        else:
                            print('Saldo insuficiente!\n')
                    else:
                        print(f'Valor superior ao limite por saque permitido!\n') 
            #return voltar_menu, v_saldo, v_quantidade_de_operacoes, v_extrato
            

def visualizar_extrato(v_quantidade_de_operacoes = quantidade_de_operacoes):
    while True:  
        if v_quantidade_de_operacoes == 0 :
            print('Não foram realizadas movimentações!\n')
        else:
            print(extrato)
        print('[ 0 ] Voltar ao menu principal\n[ 9 ] Sair\n ')
        voltar_menu = input('Digite uma das opções acima: ')
        limpar_tela()    
        if voltar_menu == '0' or voltar_menu == '9':
            return voltar_menu, v_quantidade_de_operacoes 

def criar_usuário():
    pass

def criar_contos():
    pass



        
  


# -----------> Main Code < ---------------------------

#looping do menu.
while True:
    # ----> Início bloco Menu <----
    
    # Verifica se é possivel fazer saque no dia, muda o layout do menu com ou sem opção de saque.
    opcao = menu() if (saldo ==0 or quantidide_saque_diario_realizado == QUANTIDADE_SAQUE_DIARIO_MAXIMO) else  menu(sacar=True)
    print(f'{"\n"*1000}') # Limpar a tela.
    # ----> FIM bloco Menu <----
        
    # ----> Início bloco Saldo <----
    # Refere-se a opção 1 do Menu.
    if opcao == 1: 
        visualizar_saldo(saldo)
        voltar_menu = sub_menu()
    # ----Fim bloco Saldo <----

    # ----> Início bloco Depósito <----        
    # Refere-se a opção 2 do Menu.
    elif opcao == 2: 
        while True:
            saldo, quantidade_de_operacoes, extrato = depositar(saldo, quantidade_de_operacoes, extrato)
            voltar_menu = sub_menu(menu_principal=True)
            if voltar_menu != "1":
                break

        
    # ----> Fim bloco Depósito <----
    
    # ----> Inicio bloco Saque <----     
    # Refere-se a opção 3 do Menu
    elif opcao == 3: 
        voltar_menu, saldo, quantidade_de_operacoes, extrato, quantidide_saque_diario_realizado = sacar(v_saldo=saldo, v_quantidade_de_operacoes=quantidade_de_operacoes,
          v_extrato=extrato,
          v_quantidide_saque_diario_realizado=quantidide_saque_diario_realizado,
          V_VALOR_MAXIMO_POR_SAQUE= VALOR_MAXIMO_POR_SAQUE,
          V_QUANTIDADE_SAQUE_DIARIO_MAXIMO=QUANTIDADE_SAQUE_DIARIO_MAXIMO)
        

        # Cria um looping do submenu de saque.   
        while True: 
            v_saldo, v_quantidade_de_operacoes, v_extrato, v_quantidide_saque_diario_realizado = sacar(
                v_saldo=saldo,
                v_quantidade_de_operacoes=quantidade_de_operacoes,
                v_extrato=extrato,
                v_quantidide_saque_diario_realizado=quantidide_saque_diario_realizado,
                V_VALOR_MAXIMO_POR_SAQUE= VALOR_MAXIMO_POR_SAQUE,
                V_QUANTIDADE_SAQUE_DIARIO_MAXIMO=QUANTIDADE_SAQUE_DIARIO_MAXIMO)
            

            if quantidide_saque_diario_realizado >= QUANTIDADE_SAQUE_DIARIO_MAXIMO:
                print('Limite de saques diários atingido!\n')
                voltar_menu = sub_menu(menu_principal = False) 
                #
            else:
                voltar_menu = sub_menu(menu_principal = True)
            if voltar_menu != "1":
                break
    # ----> Fim bloco Saque <----

    # ----> Inicio bloco Extrato <----            
    # Refere-se a opção 4 do Menu.
    elif opcao == 4:
        voltar_menu, quantidade_de_operacoes = visualizar_extrato(v_quantidade_de_operacoes = quantidade_de_operacoes)
        
    # ----> Fim bloco Extrato <----
    
    # ----> Início bloco Sair <----
    # # Refere-se a opção 9 do Menu, finaliza o looping do menu e encerra o código. 
    if opcao == 9 or voltar_menu == '9':
        print(f'Obrigado pela preferência e volte sempre!{"\n"*5}')
        break
    # ----> Fim bloco Sair <----

# ------------------> FIM CÓDIGO <-------------------------------