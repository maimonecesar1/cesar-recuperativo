def clasificar(vector):
    vector_primo = []
    vector_par = []
    vector_impar = []
    for i in range(len(vector)):
        vector_primo.append(0)
        vector_par.append(0)
        vector_impar.append(0)        

    for i in range(len(vector)):
        primo = False
        impar_mayor = False
        par_menor =  False

        if vector[i] < 2:
            primo = False
        elif vector[i] == 2:
            primo = True
        elif vector[i] > 2 and vector[i] % 2 == 0:
            primo = False
        else:
            for j in range(3, vector[i]):
                if vector[i] % j == 0:
                    primo = False
                else:
                    primo = True

        if(primo): 
            vector_primo[i] = vector[i]

        if(primo == False):
            if(vector[i]%2 == 0):
                vector_par[i] = vector[i]
            else:
                vector_impar[i] = vector[i]

    return [vector_primo, vector_par, vector_impar, vector]

def ordenar(vectores):
    nuevo_vector = []
    vector_primo = vectores[0]
    vector_par = vectores[1]
    vector_impar = vectores[2]
    vector = vectores[3]

    vector_par.sort(reverse = True)
    vector_impar.sort(reverse = True)

    # for i in range(len(vector_par)):
    #     if(vector_par[i] != 0):

    print(vector_primo)
    print(vector_par)
    print(vector_impar)


ordenar(clasificar([4,1,7,6]))



        