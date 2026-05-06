print("=== CHOCÓ PARK ===")

tipo = input("Tipo de vehículo (moto/carro/camioneta): ").lower()
horas = float(input("Horas estacionado: "))
placa = input("Placa del vehículo: ").upper()
estudiante = input("¿Tiene tarjeta de estudiante? (s/n): ").lower()

# Tarifas
if tipo == "moto":
    primera = 2500
    adicional = 1800
elif tipo == "carro":
    primera = 5000
    adicional = 3500
elif tipo == "camioneta":
    primera = 7500
    adicional = 5000
else:
    print(" Tipo inválido")
    exit()

# Cálculo base
if horas <= 1:
    total = primera
else:
    total = primera + (horas - 1) * adicional

# Tope máximo diario
if total > 25000:
    total = 25000

descuentos = 0

# Descuento residente
if placa.startswith("CHO"):
    descuentos += 0.20

# Descuento estudiante
if estudiante == "s":
    descuentos += 0.15

# Descuento nocturno
hora_ingreso = int(input("Hora de ingreso (0-23): "))
if hora_ingreso >= 20 or hora_ingreso < 6:
    descuentos += 0.50

# Aplicar descuento
total_final = total * (1 - descuentos)

print("\n RESUMEN")
print(f"Tiempo: {horas} horas")
print(f"Subtotal: ${total}")
print(f"Descuentos aplicados: {descuentos*100}%")
print(f" Total a pagar: ${round(total_final)}")

# Vehículo abandonado
if horas > 12:
    print(" ALERTA: Vehículo abandonado")