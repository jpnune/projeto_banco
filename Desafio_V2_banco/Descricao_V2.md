# Em contrução

# Desafio V2 

Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes: Sacar, Depositar, Visualizar Extrato, Visualizar saldo. Além disso, para versão 2 do nosso sistena precisamos criar duas novas funções: Criar usuário(cliente do banco) e criar conta corrente (vincular comm usuário). 

## Separação das funções 
Devemos criar funções para todas as operaçoes do sistema. Para exercitar tudo o que aprendemos neste módulo, cada função vai ter uma regra na passagem de argumentos. O retorno e a forma como serão chamadas, podem ser definidas por você da forma que achar melhor. 

## Saque 
A função saqur deve receber argumentos apenas por nomes (keywords only). Sugestão se argumentos: saldo, valor, extrato, limite, num_saques, limites_saques. Sugestão de retorno: Saldo e extrato 

## Depósito
A função de depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: Saldo, valor, extrato. Sugestão de retorno: saldo e extrato.

## Extrato
A função de extrato deve receber os argumentos por argumentos e posição (positional only e keyword only). Argumentos posicionais: saldo, argumentos nomeados: extrato.

## Novas Funções 
Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais funções, exemplo: listar contas.

## Criar Usuário
O programa deve armazernar os usuários em uma lista um usuário é composto por: nome, data de nascimento, cpf e endereço. O endereço é uma string com formato: logradouro, numero - bairro - cidade/sigla estado. Deve ser armazenado somente os numeros do CPF. Não podemos armazenar 2 usuários com mesmo CPF.

## Criar conta corrente
O progrma deve armazenar contas em uma lista, uma conta é composta por: agência, numero da conta e usuário. O número da conta é sequecial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence somente a um usuário.