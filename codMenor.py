#!/usr/bin/env python3
"""
Calculadora básica con operaciones matemáticas
Ejemplo de código con menos de 100 líneas
"""

import math

class Calculadora:
    def _init_(self):
        self.historial = []
    
    def sumar(self, a, b):
        resultado = a + b
        self.historial.append(f"{a} + {b} = {resultado}")
        return resultado
    
    def restar(self, a, b):
        resultado = a - b
        self.historial.append(f"{a} - {b} = {resultado}")
        return resultado
    
    def multiplicar(self, a, b):
        resultado = a * b
        self.historial.append(f"{a} * {b} = {resultado}")
        return resultado
    
    def dividir(self, a, b):
        if b == 0:
            return "Error: División por cero"
        resultado = a / b
        self.historial.append(f"{a} / {b} = {resultado}")
        return resultado
    
    def potencia(self, a, b):
        resultado = a ** b
        self.historial.append(f"{a} ^ {b} = {resultado}")
        return resultado
    
    def raiz_cuadrada(self, a):
        if a < 0:
            return "Error: No se puede calcular raíz de número negativo"
        resultado = math.sqrt(a)
        self.historial.append(f"√{a} = {resultado}")
        return resultado
    
    def factorial(self, n):
        if n < 0:
            return "Error: El factorial no existe para números negativos"
        if n == 0 or n == 1:
            return 1
        resultado = math.factorial(n)
        self.historial.append(f"{n}! = {resultado}")
        return resultado
    
    def mostrar_historial(self):
        if not self.historial:
            print("No hay operaciones en el historial")
        else:
            print("Historial de operaciones:")
            for operacion in self.historial:
                print(f"  {operacion}")
    
    def limpiar_historial(self):
        self.historial.clear()
        print("Historial limpiado")

def menu():
    calc = Calculadora()
    
    while True:
        print("\n=== CALCULADORA BÁSICA ===")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Potencia")
        print("6. Raíz cuadrada")
        print("7. Factorial")
        print("8. Ver historial")
        print("9. Limpiar historial")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {calc.sumar(a, b)}")
        
        elif opcion == "2":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {calc.restar(a, b)}")
        
        elif opcion == "3":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {calc.multiplicar(a, b)}")
        
        elif opcion == "4":
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            print(f"Resultado: {calc.dividir(a, b)}")
        
        elif opcion == "5":
            a = float(input("Base: "))
            b = float(input("Exponente: "))
            print(f"Resultado: {calc.potencia(a, b)}")
        
        elif opcion == "6":
            a = float(input("Número: "))
            print(f"Resultado: {calc.raiz_cuadrada(a)}")
        
        elif opcion == "7":
            n = int(input("Número: "))
            print(f"Resultado: {calc.factorial(n)}")
        
        elif opcion == "8":
            calc.mostrar_historial()
        
        elif opcion == "9":
            calc.limpiar_historial()
        
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

if _name_ == "_main_":
    menu()