# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    def __init__(self, field, x_coord, y_coord, is_fly, crawl, speed=1):
        self.field = field
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.is_fly = is_fly
        self.crawl = crawl
        self.speed = speed

    def move(self, direction):
        self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y_coord + self.speed, x=self.x_coord, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y_coord - self.speed, x=self.x_coord, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y_coord, x=self.x_coord - self.speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y_coord, x=self.x_coord + self.speed, unit=self)

    def _get_speed(self):
        if self.is_fly:
            self.speed *= 1.2
        elif self.crawl:
            self.speed *= 0.5
        else:
            raise ValueError('Эк тебя раскорячило')
