class Televisao:

    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            if self.canal < 11:
                self.canal += 1
            else:
                self.canal = 1

    def diminui_canal(self):
        if self.ligada:
            if self.canal > 1:
                self.canal -= 1
            else:
                self.canal = 11

tv = Televisao()

print('Tv está ligada: {}'.format(tv.ligada))
tv.power()
print('Tv está ligada: {}'.format(tv.ligada))
tv.power()
print('Tv está ligada: {}'.format(tv.ligada))

tv.power()
for i in range(1, 11):
    print(tv.canal)
    tv.diminui_canal()
tv.power()
print('Tv está ligada: {}'.format(tv.ligada))

res = 0 % 2
print(res)

remunera = 30 * 10 * 3
print(remunera)