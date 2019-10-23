def normal(i):
    return i

def cuadrado(x):
    return x*x

def sumaTodos(limitTo, f):
    resultado=0
    for i in range(limitTo+1):
        resultado += f(i)
    
    return resultado

#Si queremos evitar que se ejecuten los print al importar la funcion sumaTodos, se indica que solo lo hago
#cuando ejecuto el programa Funciones1nivel desde la consola, que es main y no cuando sea invocado
if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))
