# Implemente um termostato orientado a objetos.
# Minimo: 16ºC
# Incremento: 0.5ºC
# Maximo: 30ºC
#   name:       Termostato
#   atributos:  __temperatura (-)
#   atributos:  @temperatura  (+)
#   atributos:  @ftemperatura (+)

from Termostato import Termostato

def main():

    t = Termostato()

    try:
        t.temperatura = 22.5
    except Exception as e:
        print(f"Houve um problema: {e}")

    print(f"A temperatura atual é de {t.ftemperatura}")

if __name__ == "__main__":
    main()