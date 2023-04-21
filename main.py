class Person:
    def __init__(self, in_, out_):
        self.in_ = in_
        self.out_ = out_


class Persons:
    def __init__(self, sp):
        self.sp = [Person(*v) for v in sp]

    def next_by_time(self, time):
        sp = list(filter(lambda x: x.in_ == time, self.sp))
        return sp


class Cell:
    def __init__(self, id, group):
        self.id = id
        self.is_full = 0
        self.person = None
        self.group = group

    def put(self, person):
        self.is_full = 1
        self.person = person

    def tick(self, time):
        if self.is_full:
            if time == self.person.out_:
                self.person = None
                self.is_full = 0
                if self.id < self.group.min_free or self.group.min_free == -1:
                    self.group.min_free = self.id


class Group:
    def __init__(self, n_cells):
        self.len = n_cells
        self.sp = [Cell(i, self) for i in range(n_cells)]
        self.min_free = 0
        self.counter = 0
        self.last_id = None

    def on_visit(self, person):
        if self.min_free != -1:
            self.counter += 1
            self.sp[self.min_free].put(person)
            self.last_id = self.min_free
            for v in self.sp[self.min_free:]:
                if not v.is_full:
                    self.min_free = v.id
                    break
            else:
                self.min_free = -1

    def tick(self, time):
        for cell in self.sp:
            cell.tick(time)


class Main:
    def __init__(self, n_cells, persons_sp):
        self.group = Group(n_cells)
        self.persons = Persons(persons_sp)
        self.time = 0

    def tick(self):
        next_persons = self.persons.next_by_time(self.time)
        for person in next_persons:
            self.group.on_visit(person)
        self.group.tick(self.time)

    def run(self, time_end=1440):
        while self.time <= time_end:
            self.tick()
            self.time += 1


def main():
    with open('26.txt') as f:
        n_cells, _ = int(next(f)), int(next(f))
        pers = list(map(lambda x: list(map(int, x.split())), f))
    pers.sort()

    process = Main(n_cells, pers)
    process.run()

    print(process.group.counter)
    print(process.group.last_id+1)
    

if __name__ == "__main__":
    main()
