def main():
    #escribe tu código abajo de esta línea
    AñoNacimiento=int(input('Dame el año de nacimiento: '))
    AñoActual=int(input('Dame el año actual: '))
    Lustros=(AñoActual-AñoNacimiento)/5
    print('Los lustros que has vivido son:',Lustros)



if __name__ == '__main__':
    main()
