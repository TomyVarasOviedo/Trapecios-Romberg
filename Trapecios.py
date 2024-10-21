import math

def trapecio_simple(a:float, b:float, f) ->float:
    """
    Metodo para calcular la integral definida de una funcion atraves del metodo de trapecio simple
    a: numero inferior del intervalo
    b: numero superior del intervalo
    f: funcion ha calcular
    """
    h = (b - a)/2
    return h*(f(a) + f(b))

def trapecio_complejo(a:float, b:float, f, n:int)->float:
    """
    a:Numero inferior del intervalo
    b:Numero superior del intervalo
    f:Funcion ha integrar
    n:Numero de fracciones del intervalo
    """
    h=(b-a)/n
    j:float=a
    suma=f(j)
    for i in range(0,n-1):
        j = j + h
        suma = suma + 2*f(j)
    suma = suma + f(b)
    
    return h*(suma/2)
def main():
    print(f"El area de la funcion por trapecio simple es: {trapecio_simple(1.0,2.0,lambda x: math.exp(x))}")
    print(f"El area de la funcion por trapecio complejo es: {trapecio_complejo(1.0,2.0, lambda x: math.exp(x),4)}")

if __name__ == '__main__':
    main()