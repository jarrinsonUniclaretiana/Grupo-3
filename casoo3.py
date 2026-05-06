def es_venta_grande(valor_venta):

    if valor_venta > 20000:
        return True
    else:
        return False


def solicitar_venta():
 
    while True:
        try:
            entrada_usuario = input("Ingrese el valor de la venta (-1 para finalizar): ")
            valor = float(entrada_usuario)

            if valor < -1:
                print("Error: El valor no puede ser negativo, excepto -1 para terminar.")
            else:
                return valor

        except ValueError:
            print("Error: Debe ingresar un numero valido.")


def analizar_ventas():


    total_ventas = 0.0
    contador_ventas_grandes = 0
    contador_total_ventas = 0

    while True:
        venta = solicitar_venta()

        if venta == -1:
            break

        total_ventas = total_ventas + venta

        contador_total_ventas = contador_total_ventas + 1

        if es_venta_grande(venta):
            contador_ventas_grandes = contador_ventas_grandes + 1

    print("\n===== RESULTADOS DEL ANÃLISIS =====")
    print("Total de ventas registradas:", contador_total_ventas)
    print("Monto total acumulado: ${:,.0f}".format(total_ventas))
    print("Cantidad de ventas grandes (> $20.000):", contador_ventas_grandes)

if __name__ == "__main__":
    analizar_ventas()