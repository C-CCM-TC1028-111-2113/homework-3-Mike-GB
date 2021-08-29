def bisiesto(a):
    if a % 4 == 0 :
        if a % 100 == 0 :
            if a % 400 == 0 :
                print("True")
            else :
                print("False")     
        else :
            print("True")
    else :
        print("False")
        
def main():
  #escribe tu código abajo de esta línea
    a=int(input(""))
    bisiesto(a)
    
if __name__=='__main__':
    main()
