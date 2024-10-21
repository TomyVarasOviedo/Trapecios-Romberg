import math
import Trapecios as tp

def romberg(f, a, b, e=1e-3):
    """
    a:Numero inferior del intervalo
    b:Numero superior del intervalo
    f:funcion ha integrar
    e:tolerancia de error del metodo
    """
    R = [tp.trapecio_simple(a,b,f)]  # Primera aproximación trapezoidal
    n = 1
    error = float('inf')

    while error > e:
        h = (b - a) / 2 ** n
        trapecio_suma = 0

        # Suma los valores de la función en los puntos intermedios
        for k in range(1, 2 ** n, 2):
            trapecio_suma += f(a + k * h)
        
        # Nueva estimación usando la regla trapecio
        i = 0.5 * R[-1] + h * trapecio_suma
        error = abs(i - R[-1])
        R.append(i)
        n += 1

    return R[-1]

a = 0 
b = math.pi 
resultado = round(romberg(lambda x:math.sin(x), a, b),6)
print(f"Resultado de la integral: {resultado}")