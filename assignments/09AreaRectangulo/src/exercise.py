def area(b, h):
    a=b*h
    print("El área del rectángulo es:",a)
    
def main():
  #escribe tu código abajo de esta línea
    b=float(input("Dame la base: "))
    h=float(input("Dame la altura: "))
    area(b, h)
    
if __name__=='__main__':
    main()
