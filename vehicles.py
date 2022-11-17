def gen_id(arr):
    ids = 0
    check = True
    while check:
        check_tmp = False
        for i in arr:
            if i.get_id(i) == ids:
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
        self.consumption = 0

    def set_power(self,in_power):
        self.power = in_power

    def get_type(self):
        return self.type


class Car(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.maxSpeed = 0
        self.type = 'BUS'
        self.id = 0

    def set_id(self,tmp):
        self.id = tmp

    def get_id(self):
        return self.id

    def set_maxSpeed(self,ms):
        self.maxSpeed = ms

    def print_info(self):
        print(f'{self.get_id(self)}: It is Car, Power = {self.power}, max Speed = {self.maxSpeed}')



class Bus(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.capacity = 0
        self.type = 'BUS'
        self.id = 0

    def set_id(self,tmp):
        self.id = tmp

    def get_id(self):
        return self.id

    def set_capacity(self,cap):
        self.capacity = cap

    def set_consumption(self,con):
        self.consumption = con

    def print_info(self):
        print(f'{self.get_id(self)}: It is BUS, Power = {self.power}, capacity = {self.capacity} consumption = {self.consumption}')


class Truck(Vehicle):
    def __init__(self):
        Vehicle.__init__(self)
        self.maxWeight = 0
        self.type = 'TRUCK'
        self.id = 0

    def set_id(self,tmp):
        self.id = tmp

    def get_id(self):
        return self.id

    def set_maxWeight(self,mw):
        self.maxWeight = mw

    def set_consumption(self, con):
        self.consumption = con

    def print_info(self):
        print(
            f'{self.get_id(self)}: It is BUS, Power = {self.power}, maxWeight = {self.maxWeight} consumption = {self.consumption}')

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
                veh = Bus
                text = f.readline()
                a = text.split(' ')
                power = int(a[0])
                tmp = int(a[1])
                con = int(a[2])
                veh.set_power(veh,in_power=power)
                veh.set_capacity(veh,cap=tmp)
                veh.set_id(veh,tmp= gen_id(objects))
                veh.set_consumption(veh,con=con)
                objects.append(veh)
            elif type == 2:
                veh = Truck
                text = f.readline()
                a = text.split(' ')
                power = int(a[0])
                tmp = int(a[1])
                con = int(a[2])
                veh.set_power(veh,in_power=power)
                veh.set_maxWeight(veh,mw=tmp)
                veh.set_id(veh, tmp=gen_id(objects))
                veh.set_consumption(veh, con=con)
                objects.append(veh)
            elif type == 3:
                veh = Car
                text = f.readline()
                a = text.split(' ')
                power = int(a[0])
                tmp = int(a[1])
                veh.set_power(veh,in_power=power)
                veh.set_maxSpeed(veh, ms=tmp)
                veh.set_id(veh, tmp=gen_id(objects))
                objects.append(veh)

def clear_container():
    objects.clear()