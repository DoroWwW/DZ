class Auto:
    brand = "afdasde"

    def __int__(self, brand) -> None:
        self.brand = brand
      

    def move(self):
        print('move')

    def birthday(self, age):
        self.age = age
        age += 1
        print(f'{age}')

    def stop(self):
        print('stop')


auto = Auto("adsw")

auto.stop()
auto.move()
auto.birthday(0)