from external import Musician,Dancer

class Club:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'Klub {self.name}'

    def organize_event(self):
        return "koncert muzyki z oprawą taneczną..."


class Adapter:
    def __init__(self,obj,adapted_methods):
        self.obj=obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Club("Jazz Cafe"),Musician("Roy Robson"),Dancer("Mary Smith")]
    for obj in objects:
        if hasattr(obj, 'play') or hasattr(obj, 'dance'):
            if hasattr(obj,'play'):
                adapted_methods = dict(organize_event = obj.play)
            elif hasattr(obj,'dance'):
                adapted_methods = dict(organize_event = obj.dance)
            obj = Adapter(obj,adapted_methods)
        print(f'{obj} {obj.organize_event()}')


if __name__ == '__main__':
    main()
