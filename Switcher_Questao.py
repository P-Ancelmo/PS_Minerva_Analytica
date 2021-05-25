from Q1 import media
from Q2 import cavalo
from Q3 import caixa

#classe criada para exercer a mesma função do switch case e facilitar a chamada das fuções na main
class Switcher_Questao(object):
    def questoes(self,questao):
        quest = 'quest_' + questao
        case = getattr(self,quest,lambda: -1)
        return case()
    def quest_1(self):
        print("\nQuestão 1:")
        return media()

    def quest_2(self):
        print("\nQuestão 2:")
        return cavalo()

    def quest_3(self):
        print("\nQuestão 3:")
        return cavalo()
