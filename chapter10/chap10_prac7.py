class Marvel(object):
    def __init__(self,name,characteristic):
        self.name=name
        self.characteristic=characteristic
    def __str__(self):
        return 'my name is {0} and  my weapon{1}'.format(self.name, self.characteristic)
class Villain(Marvel):
    pass
first_villain=Villain("Thanos",'infinity gauntlet')
print(first_villain)