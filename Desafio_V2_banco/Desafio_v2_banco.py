# ------------------> INICIO CODIGO <------------------------

# Variáveis Globais
saldo = 0
quantidade_de_operacoes = 0
extrato = f'id{" "*15} tipo de transação {" "*26} Valor\n\n'
quantidide_saque_diario_realizado = 0

# Constantes
QUANTIDADE_SAQUE_DIARIO_MAXIMO = 3
VALOR_MAXIMO_POR_SAQUE = 500

# variaveis dos ususarios
lista_usuario = []
                

#variaveis das contas
lista_conta = []
contador_id_conta = 1




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
    print(f'{" "*15}[ 5 ] Criar um conta')
    print(f'{" "*15}[ 6 ] Visualizar lista de usuários e contas')
    print(f'{" "*15}[ 9 ] Sair')
    print()
    opcao = int(input(f'{"#"*51}{"\n"*3}Digite aqui --> '))
    return opcao

    
def sub_menu( operacao=None, menu_principal = False):
    if menu_principal == False:
        print('[ 0 ] Voltar ao menu principal\n[ 9 ] Sair\n ') 
    else:
        if operacao == "deposito" or operacao == 'saque':
            operacao = operacao
        else:
            print('Operação inválida! Digite "deposito" ou "saque"!')
            return None
        print(f'[ 0 ] Voltar ao menu principal\n[ 1 ] Fazer um novo {operacao}\n[ 9 ] Sair\n')
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
            sub_menu(operacao = operacao, menu_principal=True)

    
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

def visualizar_extrato(v_quantidade_de_operacoes = quantidade_de_operacoes):  
    if v_quantidade_de_operacoes == 0 :
        print('Não foram realizadas movimentações!\n')
    else:
        print(extrato)


def depositar(v_saldo=saldo, v_quantidade_de_operacoes=quantidade_de_operacoes, v_extrato=extrato):
    while True:
        try:
            deposito = input('digite o valor do depósito: ')
            if float(deposito) or '0':
                break
        except:
            limpar_tela()
            print(f'Valor {deposito} é um valor inválido!\nDigite um valor válido! Ex:3.14{'\n'*5}')
            
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

        print(f'Saldo: R${v_saldo :.2f}\n')
        saque = input('Digite o valor de saque desejado: ')
        limpar_tela()

        # Formata a casa decimal do número inserido no input "saque".
        saque = formatar_string(saque)

        saque_validado = validar_saque(saque, V_VALOR_MAXIMO_POR_SAQUE= VALOR_MAXIMO_POR_SAQUE, v_saldo = saldo)
        
        if saque_validado == True:
            confirmacao = confirmacao_saque(saque)
            limpar_tela() 
            if confirmacao == '1':
                v_saldo -= float(saque) # Retira o valor do saldo.
                v_quantidade_de_operacoes += 1 # Soma 1 ao contador "quantidade de operações" para ser usado no extrato.
                v_extrato += f'{v_quantidade_de_operacoes}{" "*(20 - len(str(v_quantidade_de_operacoes)))}  Saque {" "*(37-len(saque))} R${saque}\n' # Formata e adiciona item no extrato.
                v_quantidide_saque_diario_realizado +=1 # Soma em 1 na contagem de saques diários.
                print(f'Saque de R$ {saque} efetuado com sucesso!\n')
                print(f'Saldo atual é de R$ {v_saldo :.2f}\n\n')
                return v_saldo, v_quantidade_de_operacoes, v_extrato, v_quantidide_saque_diario_realizado
            elif confirmacao == '0':
                print('Saque CANCELADO!\n') 
        return v_saldo, v_quantidade_de_operacoes, v_extrato, v_quantidide_saque_diario_realizado

          

def confirmacao_saque(saque):
    print(f'O valor de R$ {saque} será descontado da conta, confirma?\n[ 0 ] NÃO\n[ 1 ] SIM\n')
    try:
        confirmacao = input('digite uma das opções acima: ')
        if confirmacao == "1" or confirmacao == "0":
            return confirmacao
        else:
            confirmacao_saque(saque)
    except:
        print('Opção inválida!\n')
        confirmacao_saque(saque)



def validar_saque(  valor,
                    V_VALOR_MAXIMO_POR_SAQUE= VALOR_MAXIMO_POR_SAQUE,
                    v_saldo = saldo,
                    quantidide_saque_diario_realizado = quantidide_saque_diario_realizado,
                    V_QUANTIDADE_SAQUE_DIARIO_MAXIMO = QUANTIDADE_SAQUE_DIARIO_MAXIMO ):


    if quantidide_saque_diario_realizado >= V_QUANTIDADE_SAQUE_DIARIO_MAXIMO:
        print('Limite de {V_QUANTIDADE_SAQUE_DIARIO_MAXIMO} saques diários atingido!\n')
        return None
    
    if v_saldo <= 0:
        print(f'Saldo insuficiente!\n')
        return None
    try:
        valor = float(valor)
    except:
        print('Valor inválido! Tipo de número não compatível. Ex: válido 3.14.\n')
        return None

    if valor > V_VALOR_MAXIMO_POR_SAQUE:
        print(f'Valor superior ao limite por saque permitido! Valor deve ser inferior a R$ {V_VALOR_MAXIMO_POR_SAQUE}.\n')
        return None

    if valor > v_saldo:
        print('Saldo insuficiente!\n')
        return None

    if valor <= 0:
        print('Valor de saque deve ser maior que R$ 0.00.\n')
        return None
    return True


    
def eh_duplicado(cpf, lista):
    return True if cpf in lista else False

def validar_cpf(cpf):
    cpf = str(cpf)
    return True if len(cpf) ==11 and str.isdigit(cpf) else False 
        

def validar_estado(estado):
    sigla_estado = ['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MS','MT',
                'MG','PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC',
                'SP','SE','TO']
    estado = str.upper(estado)
    return True if estado in sigla_estado else False

def valida_data_nascimento(data_nascimento):
    try:
        dia = int(data_nascimento[:2]) 
        mes = int(data_nascimento[3:5])
        ano = int(data_nascimento[6:11])
    except:
        return False
    
    if data_nascimento[2] != '/' or data_nascimento[5] != '/' :
        return False

    if ano < 1900 or ano > 2024:
        return False
    
    if dia < 1:
        return False

    match mes:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            if dia > 31:
                return False
        case 2 :
            if dia >28:
                return False
        case 4 | 6 | 9 | 11:
            if dia > 30:
                return False
        case _:
            return False
    return True
        


  

def criar_usuario(cpf, nome):

    data_nascimento = input('Digite sua data_nascimento. Formato dd/mm/aaaa: ')
    limpar_tela()
    if valida_data_nascimento(data_nascimento) == False:
        print('Data de nascimento inválida!\n\nDigite uma data válida no formato dd/mm/aaaa!\n')
        return False
    
    logradouro = input('Digite o nome do logradouro. EX: Rua, Av, Alameda... : ')
    limpar_tela()

    numero = input('Digite o número da residência. Somente número: ')
    limpar_tela()
    if str.isdigit(numero) == False:
        print('Número da residência inválido!\n\nDigite um número somente com dígitos numéricos\n')
        return False

    bairro = input('Digite o nome do bairro: ')
    limpar_tela()

    cidade = input('Digite o nome da cidade: ')
    limpar_tela()

    sigla_estado = input('Digite a sigla do estado. Ex: SP, RJ, MG... : ')
    limpar_tela()
    if validar_estado(sigla_estado) == False:
        print('Sigla de Estado inválido\n')
    
    endereço = f'{logradouro}, {numero} - {bairro} - {cidade}/{str.upper(sigla_estado)}'
    
    print('Usuário criado com sucesso!\n')
    return [cpf, nome, data_nascimento, endereço]


def criar_contas(cpf, usuario):
    # agência, numero da conta e usuário
    global contador_id_conta 

    agencia = '0001'
    id_conta = str(contador_id_conta)
    usuario = usuario
    contador_id_conta += 1 

    return [agencia, id_conta, usuario, cpf]



        
  


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
            voltar_menu = sub_menu('deposito', menu_principal=True)
            if voltar_menu != "1":
                break
    # ----> Fim bloco Depósito <----
    
    # ----> Inicio bloco Saque <----     
    # Refere-se a opção 3 do Menu
    elif opcao == 3:         

        # Cria um looping do submenu de saque.   
        while True: 
            saldo, quantidade_de_operacoes, extrato, quantidide_saque_diario_realizado = sacar(
                v_saldo=saldo,
                v_quantidade_de_operacoes=quantidade_de_operacoes,
                v_extrato=extrato,
                v_quantidide_saque_diario_realizado=quantidide_saque_diario_realizado,
                V_VALOR_MAXIMO_POR_SAQUE= VALOR_MAXIMO_POR_SAQUE)
            
            # validaçao para fazer novo saque ou sair
            if quantidide_saque_diario_realizado >= QUANTIDADE_SAQUE_DIARIO_MAXIMO:
                print('Limite de saques diários atingido!\n')
                voltar_menu = sub_menu() 
            else:
                voltar_menu = sub_menu(operacao ='saque',menu_principal = True)
            if voltar_menu != "1":
                break
    # ----> Fim bloco Saque <----

    # ----> Inicio bloco Extrato <----            
    # Refere-se a opção 4 do Menu.
    elif opcao == 4:
        visualizar_extrato(v_quantidade_de_operacoes = quantidade_de_operacoes)
        voltar_menu = sub_menu()

    # ----> Fim bloco Extrato <----

    # ----> Inicio bloco Extrato <---- 
    elif opcao == 5:
        while True:
            cpf = input("digite o numero do seu cpf! ")
            limpar_tela()
            if validar_cpf(cpf) ==False:
                print('CPF inválido!\n Digite um cpf somente com números e com 11 digitos')
            else:
                break
        
        nome_temp = ''
        for x in lista_conta:
            if x[3] == cpf:
                nome_temp = x[2]
                break
              
        if nome_temp !='':
            lista_conta.append(criar_contas(cpf, nome_temp))  
        else:
            nome = input('Digite o nome do titular da conta: ')
            limpar_tela()
            lista_conta.append(criar_contas(cpf, nome))
            lista_usuario.append(criar_usuario(cpf, nome))
            
        voltar_menu = sub_menu()
        
    
    # ----> Início bloco visualizar contas e usuario <----
    elif opcao == 6:
        print('lista de contas por usuario.\n')

        for x in lista_usuario:
            print(f' CPF {x[0]}: cadastro = {x}')
            print('Contas:')
            for y in lista_conta:
                if y[3] == x[0]:
                    print(y)
            print()

        print()    
        voltar_menu = sub_menu()
    # ----> Fim bloco Extrato <----
    
    #[['11111111111', 222222222222
    # ----> Início bloco Sair <----
    # # Refere-se a opção 9 do Menu, finaliza o looping do menu e encerra o código. 
    if opcao == 9 or voltar_menu == '9':
        print(f'Obrigado pela preferência e volte sempre!{"\n"*5}')
        break
    # ----> Fim bloco Sair <----

# ------------------> FIM CÓDIGO <-------------------------------

