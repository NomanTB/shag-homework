import random

class Student():
    '''создаем класс студета'''
    def __init__(self, name,live_student):
        '''создаем функцию в которой создаем и назначаем начальные значения "деньги,ум,духовная сила,и статус жизни"'''
        self.name = name
        self.moni = 10
        self.um = 6
        self.moral_power = 12
        self.live_student = live_student
    def chill(self):
        ''' создаем функцию отдыха и что во время ние будет происходить '''
        self.moni -= 5
        self.moral_power += 10
        self.um -= 3
    def job(self):
        '''создаем функцию для зароботка денег'''
        self.moni += 10
        self.moral_power -= 3
        self.um += 1
    def scoli(self):
        '''создаем функцию учебы'''
        self.um += 6
        self.moral_power -= 3

    def ower(self):
        if self.moni < 0:
            self.live_student = False
            print("Банкрот")
        elif self.um < 0:
            if self.um < 0:
                b = random.randint(1,3)
                self.live_student = False
                if b == 1:
                    print("От вашей тупости вас сбила машина")
                elif b == 2:
                    print('Вы завалили все экзамены вас перестали обеспечивать родители и вы умерлиот голод')
                else:
                    print('Из-за того что вы не знали кого оскарбили вас забили ногами до смерти зауневерситетом ')
        elif self.moral_power < 0:
            self.live_student = False
            print("Дипресия")



    def one(self):
        i = 0
        while i == 0:
            a = random.randint(1, 3)
            if a == 1:
                self.chill()
            elif a == 2:
                self.job()
            elif a == 3:
                self.scoli()

    def avre_day(self):
        print(f'деньги {self.moni}')
        print(f'ум {self.um}')
        print(f'духовное равновесие {self.moral_power}')

    def live(self, day):

        day = f'day {day} of {self.name} life'
        print('=' * 10, day, self.name, '=' * 10)

        c = random.randint(1,3)

        if c == 1:
            self.job()
        elif c == 2:
            self.scoli()
        elif c == 3:
            self.chill()
        self.ower()
        self.avre_day()

Roma = Student(name = "Roma" , live_student = True)

for day in range(365):

    if Roma.live:
        Roma.live(day)


# print(dead.live_student)
#
# print(self.mozg,'/n',self.moni,'/n',self.moral_power)
# St = Student(0,0,0)
# print(St.mozg)