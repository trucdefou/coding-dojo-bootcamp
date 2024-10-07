def basico():
    print("Ejercicio 1: Básico")
    for i in range(101):
        print(i)

def multiples_de_2():
    print("\nEjercicio 2: Múltiples de 2")
    for i in range(2, 501, 2):
        print(i)

def contando_vanilla_ice():
    print("\nEjercicio 3: Contando Vanilla Ice")
    for i in range(1, 101):
        if i % 10 == 0:
            print("baby")
        elif i % 5 == 0:
            print("ice ice")
        else:
            print(i)

def numero_gigante():
    print("\nEjercicio 4: Wow. Número gigante a la vista")
    suma = sum(i for i in range(0, 500001, 2))
    print("La suma total de los números pares del 0 al 500,000 es:", suma)

def regresame_al_3():
    print("\nEjercicio 5: Regrésame al 3")
    for i in range(2024, 0, -3):
        print(i)

def contador_dinamico(numInicial, numFinal, multiplo):
    print("\nEjercicio 6: Contador dinámico")
    for i in range(numInicial, numFinal + 1):
        if i % multiplo == 0:
            print(i)

if __name__ == "__main__":
    basico()
    multiples_de_2()
    contando_vanilla_ice()
    numero_gigante()
    regresame_al_3()
    contador_dinamico(3, 10, 2)