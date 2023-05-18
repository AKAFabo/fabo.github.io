def Burbuja(lista):

    for i in range(1,len(lista)):
        for j in range(0,len(lista)-i):
            if(lista[j] > lista[j+1]):
                k = lista[j+1]
                lista[j+1] = lista[j]
                lista[j] = k
                print(lista)
        print(lista)


def Seleccion(lista):
    for  i in range(0,len(lista)-1):
        minimo=i
        for j in range(i+1,len(lista)):
            if lista[minimo] > lista[j]:
                minimo=j
            aux=lista[minimo]
            print(lista)
        lista[minimo]=lista[i]
        lista[i]=aux
        print(lista)
    print(lista)

def Insercion(lista):
    for i in range(1,len(lista)):
        v=lista[i]
        j=i-1
        while j >= 0 and lista[j] > v:
            lista[j+1] = lista[j]
            j=j-1 
            print(lista)
        lista[j+1]=v
        
    print(lista)

def Shell(lista):
    inc=int(len(lista)/2 )
    while  inc>0:
        for  i in range(inc,len(lista)):
            j=i
            temp=lista[i]
            while j>=inc and lista[j-inc]>temp:
                lista[j]=lista[j-inc]
                j=j-inc 
            lista[j]=temp
            print(lista)
        if (inc==2) :
            inc=1
        else :
            inc=int(inc/2.5)
        print(lista)
    print(lista)

def quicksort(lista):
    if len(lista) == 1 or len(lista) == 0:
        return lista
    else:
        pivot = lista[0]
        print(pivot)
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
            
        lista[0],lista[i] = lista[i],lista[0]
        primera = quicksort(lista[:i])
        segunda = quicksort(lista[i+1:])
        primera.append(lista[i])
        print(primera + segunda)   
        
    return (primera + segunda)

def Radix(lista):
    max_num = max(lista)
    exp = 1
    ordenada = []

    while max_num // exp > 0:
        L0 = []
        L1 = []
        L2 = []
        L3 = []
        L4 = []
        L5 = []
        L6 = []
        L7 = []
        L8 = []
        L9 = []

        for num in lista:
            if (num // exp) % 10 == 0:
                L0 = L0 + [num]
            elif (num // exp) % 10 == 1:
                L1 = L1 + [num]
            elif (num // exp) % 10 == 2:
                L2 = L2 + [num]
            elif (num // exp) % 10 == 3:
                L3 = L3 + [num]
            elif (num // exp) % 10 == 4:
                L4 = L4 + [num]
            elif (num // exp) % 10 == 5:
                L5 = L5 + [num]
            elif (num // exp) % 10 == 6:
                L6 = L6 + [num]
            elif (num // exp) % 10 == 7:
                L7 = L7 + [num]
            elif (num // exp) % 10 == 8:
                L8 = L8 + [num]
            else:
                L9 = L9 + [num]

        print("Lista L0: ", L0)
        print("Lista L1: ", L1)
        print("Lista L2: ", L2)
        print("Lista L3: ", L3)
        print("Lista L4: ", L4)
        print("Lista L5: ", L5)
        print("Lista L6: ", L6)
        print("Lista L7: ", L7)
        print("Lista L8: ", L8)
        print("Lista L9: ", L9)

        lista = L0 + L1 + L2 + L3 + L4 + L5 + L6 + L7 + L8 + L9
        exp *= 10
        ordenada[:] = []
        ordenada += lista
        print("Lista ordenada: ", ordenada)

    print (f"La lista ordenada es {ordenada}")

def Shake(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        # Mover los elementos más grandes al final
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                print(arr)
        if not swapped:
            break

        swapped = False
        end -= 1

        # Mover los elementos más pequeños al principio
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            print(arr)
        start += 1
        print(arr)
    print(arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividir la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Llamada recursiva para ordenar las dos mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combinar las dos mitades ordenadas
    sorted_arr = merge(left_half, right_half)
    print(f'{left_half} + {right_half} = {sorted_arr}')
    return sorted_arr

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    # Agregar los elementos restantes de la mitad izquierda
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Agregar los elementos restantes de la mitad derecha
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged

def busquedaBinaria(lista,item):
    lista.sort()
    primero=0
    ultimo=len(lista)-1
    encontrado=False
    while primero <=ultimo and not encontrado:
        puntoMedio=(primero+ultimo)//2
        print(f"El punto medio es {puntoMedio}")
        if lista[puntoMedio]==item:
            encontrado=True
        else:
            if item<lista[puntoMedio]:
                ultimo=puntoMedio-1
            else:
                primero=puntoMedio+1
    return encontrado

def busquedaSecuencial(lista,nume):
    
    posicion=0
    encontrado=False
    while posicion < len(lista) and not encontrado:
        if lista[posicion]== nume:
            encontrado = True
        else:
            posicion = posicion+1
    print (encontrado)

def menu():
    while True:
        print("1 = Ordenamiento burbuja")
        print("2 = Ordenamiento seleccion")
        print("3 = Ordenamiento insercion")
        print("4 = Ordenamiento shell")
        print("5 = Ordenamiento Quicksort")
        print("6 = Ordenamiento radix")
        print("7 = Ordenamiento shake")
        print("8 = Ordenamiento merge")
        print("9 = Busqueda binaria")
        print("10 = Busqueda secuencial")

        lista = input("Ingrese la lista a ordenar, separada por comas: ")
        lista = lista.replace(" ", "")  # Eliminar espacios en blanco
        lista = lista.replace("[", "").replace("]", "")
        lista = [x for x in lista.split(",") if x.isdigit()]  # Filtrar solo caracteres numéricos
        lista = list(map(int, lista))  # Convertir los elementos a enteros
        
        opcion = input("Ingrese el ordenamiento a correr: ")

        if opcion == '1':
            print(Burbuja(lista))

        if opcion == '2':
            print(Seleccion(lista))

        if opcion == '3':
            print(Insercion(lista))

        if opcion == '4':
            print(Shell(lista))
        
        if opcion == '5':
            print(quicksort(lista))
        
        if opcion == '6':
            print(Radix(lista))

        if opcion == '7':
            print(Shake(lista))

        if opcion == "8":
            print(merge_sort(lista))

        if opcion == "9":

            item = int(input("Ingrese el elemento a buscar: "))
            print(busquedaBinaria(lista,item))

        if opcion == "10":

            item = int(input("Ingrese el elemento a buscar: "))
            print(busquedaSecuencial(lista,item))


menu()
            


