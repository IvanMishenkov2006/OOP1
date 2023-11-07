class Vector:
    def __init__(self,*args):
        self.values=[]
        for n in args:
            if isinstance(n,int):
                self.values.append(n)

    def __str__(self):
        if self.values:
            return f'вектор{tuple(sorted(self.values))}'
        else:
            return f'ПУСРОЙ ВЕКТОР'
v1=Vector(1,2,3)
print(v1)#печатает "вектор(1,2,3)"
v2=Vector()
print(v2)#печатает "ПУСРОЙ ВЕКТОР"