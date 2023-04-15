class week:
    def __init__(self) -> None:
        self.days ={
            1: 'Lunes',
            2: 'Martes',
            3: 'Miercoles'
        }

    def week_gen(self):
        for x in self.days:
            yield self.days[x]


if __name__ == '__main__':
    wk = week()
    iter1 = wk.week_gen()
    iter2 = iter(wk.week_gen())  #hacer 

    print(next(iter1))
    print(list(iter1))
    print(next(iter2))


