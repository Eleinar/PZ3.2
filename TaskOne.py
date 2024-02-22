class Human:
    def __init__(self, head, body, arms, legs):
        self.__head = head
        self.__body = body
        self.__arms = arms
        self.__legs = legs
    
    def getHead(self):
        return self.__head
    
    def getBody(self):
        return self.__body
    
    def getArms(self):
        return self.__arms
    
    def getLegs(self):
        return self.__legs
    
    def setHead(self, head):
        self.__head = head
    
    def setBody(self, body):
       self.__body = body
    
    def setArms(self, arms):
       self.__arms = arms
    
    def setLegs(self, legs):
       self.__legs = legs

    def showStats(self):
        print(f'Голова: {self.__head}\nТуловище: {self.__body}\nРуки: {self.__arms}\nНоги: {self.__legs}')


human1 = Human('Голова', 'Туловище', 'Руки', 'Ноги')
human2 = Human('Головы нет', 'Туловище', 'Руки 3 штука', 'НогиГоги')

human1.showStats()
    
    