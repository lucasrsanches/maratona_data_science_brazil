'''Faça um formulario que pergunte o nome, cpf, endereço, idade, altura e telefone
e imprima isso organizadamente'''

print('Informe seus dados a seguir:')

nome = input('Nome: ')
idade = input('Idade: ')
altura = input('Altura: ')
cpf = input('Cpf: ')
adress = input('Endereço: ')
tel = input('Telefone: ')

print('Sr/Sra.', nome, 'tem', idade, 'anos e', altura, 'de altura\nCpf:',
      cpf, '\nReside em:', adress, '\nTelefone para contato:', tel)
