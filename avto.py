from uuid import uuid4
class Avto:
    __num_avto=0
    def __init__(self,make,model,color,price,km=0):
        self.make=make
        self.model=model
        self.color=color
        self.price=price
        self.__km=km
        self.__id=uuid4()
        Avto.__num_avto+=1
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    def get_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def add_km(self,km):
        if km>=0:
            self.__km+=km
        else:
            return "Mashina km kamaytirib bo\'lmaydi"
    def get_info(self):
        info=f"city:{self.make} car:{self.model} color:{self.color} "
        info+=f"km:{self.__km}"
        return info