# Importar clases Car y Engine del módulo models
from models import Car, Engine

fiat_multiple = Car("Fiat", "Múltipla", "light grey", 1.2, 55, 900)

print(fiat_multiple.manufacturer + " " + fiat_multiple.model)

engine_gti = Engine("GTI", 2.3, 240)

print(engine_gti.version, engine_gti.cc, engine_gti.cv)
