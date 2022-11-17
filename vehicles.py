def gen_id(arr):
    ids = 0
    check = True
    while check:
        check_tmp = False
        for i in arr:
            if i.get_id() == ids:
                check_tmp = True
        if check_tmp:
            ids = ids + 1
        else:
            check = False
    return ids


objects = []

class Vehicle:
    def __init__(self):
        self.power = 0

    def set_power(self,in_power):
        self.power = in_power

    # def get_type(self):
    #     return self.type


def sort_objects():
    N = len(objects)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if objects[j].get_type() > objects[j+1].get_type():
                objects[j], objects[j+1] = objects[j+1], objects[j]




class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.capacity = 0
        self.id = 0
        self.type = 'BUS'

    def get_type(self):
        return self.type

    def set_id(self,tmp):
        self.type = 'BUS'
        self.id = tmp

    def get_id(self):
        return self.id

    def set_capacity(self,cap):
        self.capacity = cap

    def print_info(self):
        print(f'{self.get_id()}: It is BUS, Power = {self.power}, capacity = {self.capacity}')


class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.maxWeight = 0
        self.id = 0
        self.type = 'TRUCK'

    def get_type(self):
        return self.type

    def set_id(self,tmp):
        self.id = tmp

    def get_id(self):
        self.type = 'TRUCK'
        return self.id

    def set_maxWeight(self,mw):
        self.maxWeight = mw

    def print_info(self):
        print(f'{self.get_id()}: It is TRUCK, Power = {self.power}, maxWeight = {self.maxWeight}')

def file_in():
    f = open('in.txt')
    check = True
    while check:
        text = f.readline()
        if text == '':
            check = False
        else:
            text = text.split('\n')
            type = int(text[0])
            if type == 1:  # это BUS
                veh = Bus()
                text = f.readline()
                a = text.split(' ')
                power = int(a[0])
                tmp = int(a[1])
                veh.set_power(in_power=power)
                veh.set_capacity(cap=tmp)
                veh.set_id(tmp= gen_id(objects))
                objects.append(veh)
            elif type == 2:
                veh = Truck()
                text = f.readline()
                a = text.split(' ')
                power = int(a[0])
                tmp = int(a[1])
                veh.set_power(in_power=power)
                veh.set_maxWeight(mw=tmp)
                veh.set_id(tmp=gen_id(objects))
                objects.append(veh)

def clear_container():
    objects.clear()