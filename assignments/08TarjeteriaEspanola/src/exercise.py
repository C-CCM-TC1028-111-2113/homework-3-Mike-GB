def tarjetas(pliego, plumon) :
    
    tarjplie= pliego*12
    tarjplum= plumon*35
    
    if tarjplie < tarjplum :
        print("El número máximo de tarjetas que se pueden hacer es:",tarjplie)
    elif tarjplie > tarjplum :
        print("El número máximo de tarjetas que se pueden hacer es:",tarjplum)
    elif tarjplie == tarjplum:
        print("El número máximo de tarjetas que se pueden hacer es:",tarjplum)    

def main():
    #escribe tu código abajo de esta línea
    pliego=int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumon=int(input("Dame la cantidad de plumones: "))
    tarjetas(pliego, plumon)

if __name__=='__main__':
    main()
