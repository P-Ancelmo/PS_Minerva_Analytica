from Q1 import  media
class Switcher(object):
    def questoes(self,questao):
        quest = 'quest_' + str(questao)
        case = getattr(self,quest,'opção inválida')
        return case()
    def quest_1(self):
        return media()
