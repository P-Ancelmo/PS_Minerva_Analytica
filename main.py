from Q1 import media

from Switcher import Switcher
print("Olá, esse é o arquivo de respostas do Processo Seletivo da minerva Analytica.")
print("Deseja ver a resposta de qual questão ?")

questao = input("-> ")

switch = Switcher()

switch.questoes(questao)