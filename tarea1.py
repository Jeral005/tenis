import math as mt

class GMS():
    def __init__(self, tipo_gms, tipo_coord):
        self.tipo_gms = tipo_gms
        self.tipo_coord = tipo_coord
    
    def MGLo(self):
        grado_en_m_lo = 111321
        conver_s_lo = grado_en_m_lo / 60 / 60
        return conver_s_lo
        
    def MGLa(self):
        grado_en_m_la = 111111
        conver_s_la = grado_en_m_la / 60 / 60
        return conver_s_la


segundo = GMS('segundo', 'latitud')

print(f'Un {segundo.tipo_gms} en {segundo.tipo_coord} equivale a: {segundo.MGLa()} m')
