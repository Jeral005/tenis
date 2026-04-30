class Gato():
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        
    def maullar (self,num_veces):
        return"maullar" * num_veces
        
    def largo(self):
        largo_cm=5+(self.edad*2)
        return largo_cm
        
     
gato1=Gato('Ellen',3)
print(f'tu gato se llama:{gato1.nombre}')
print(f'Tu gato tiene {gato1.edad}años')
print(f'Tu gato mide {gato1.largo()}cm')
print(f'Tu cato dice{gato1.maullar(2)}')

gato2=Gato('Pelusa',3)
print(f'tu gato se llama:{gato2.nombre}')
print(f'Tu gato tiene {gato2.edad}años')
print(f'Tu gato mide {gato2.largo()}cm')
print(f'Tu cato dice{gato2.maullar(2)}')