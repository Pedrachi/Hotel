# -*- coding: utf-8 -*-
"""
Created on Mon May 15 22:10:24 2023

@author: diego
"""

import colorama
from colorama import Fore
from colorama import Style

class Restaurante:
    
    def menu(self, **kwargs):
        for key, value in kwargs.items():
            print(f'{key} ${value}') 

class Mesa(Restaurante):

    def reservar_mesa(self, cantidad_personas, hora_reserva):
        if self.verificar_disponibilidad(cantidad_personas, hora_reserva):
            print(f"¡Mesa reservada para {cantidad_personas} personas a las {hora_reserva}!")
        else:
            print("Lo sentimos, no hay mesas disponibles en ese horario.")

    def verificar_disponibilidad(self, cantidad_personas, hora_reserva):
        # Lógica para verificar la disponibilidad de mesas
        # Puedes personalizar esta lógica según tus necesidades
        if cantidad_personas <= 4 and hora_reserva >= 18 and hora_reserva <= 21:
            return True
        elif cantidad_personas > 4 and hora_reserva >= 19 and hora_reserva <= 21:
            return True
        else:
            return False

class ReservaRestaurante(Restaurante):
    def __init__(self):
        self.mesas_disponibles = {'mesa1': 4, 'mesa2': 6, 'mesa3': 2}
        self.mesas_reservadas = {'mesa1': 0, 'mesa2': 0, 'mesa3': 0}

    def reservar_mesa(self, mesa, cantidad_personas, hora_reserva):
        if self.mesas_disponibles[mesa] >= cantidad_personas and self.verificar_disponibilidad(cantidad_personas, hora_reserva):
            self.mesas_reservadas[mesa] += cantidad_personas
            self.mesas_disponibles[mesa] -= cantidad_personas
            print(f"¡Mesa {mesa} reservada para {cantidad_personas} personas a las {hora_reserva}!")
        else:
            print(f"No se pudo reservar la mesa {mesa}. Por favor, elige otro horario o cantidad de personas.")

    def verificar_disponibilidad(self, cantidad_personas, hora_reserva):
        # Lógica para verificar la disponibilidad de mesas
        # Puedes personalizar esta lógica según tus necesidades
        if cantidad_personas <= 4 and hora_reserva >= 18 and hora_reserva <= 21:
            return True
        elif cantidad_personas > 4 and hora_reserva >= 19 and hora_reserva <= 21:
            return True
        else:
            return False

    def reporte(self):
        print('Resumen de reservaciones:')
        for mesa, cantidad in self.mesas_reservadas.items():
            print(f'Mesa {mesa}: {cantidad} persona(s) reservada(s)')

class MenuRestaurante(Restaurante):
    def __init__(self):
        self.menu_comidas = {'Hamburguesa': 8.99, 'Pizza': 10.99, 'Ensalada': 6.99}

    def mostrar_menu(self):
        print('Menú del restaurante:')
        for comida, precio in self.menu_comidas.items():
            print(f'{comida}: ${precio}')

    def realizar_pedido(self, comida, cantidad):
        if comida in self.menu_comidas:
            precio_total = self.menu_comidas[comida] * cantidad
            print(f'¡Pedido realizado! Total a pagar: ${precio_total:.2f}')
        else:
            print('Lo sentimos, esa comida no está disponible en el menú.')

print(Fore.BLUE + Style.BRIGHT + "Bienvenido al sistema de reservaciones y venta de comida en nuestro restaurante")
print("Por favor, ingresa para acceder al sistema" + Fore.RESET)

usuarios = {'pedrachi': '123', 'eco': '123456', 'yari': '123456789'}

usuario = input("Ingrese el Usuario: ")
contrasena = input("Ingrese la Contraseña: ")

if (usuario in usuarios and usuarios[usuario] == contrasena):
    print("\nInicio de sesión exitoso.")
    
    miReserva = ReservaRestaurante()
    miMenu = MenuRestaurante()
    
    while True:
        print('------------------------------------------')
        print('¡Reserva una mesa o realiza un pedido en nuestro restaurante!')
        print('1. Reservar una mesa\n2. Ver menú\n3. Realizar pedido\n4. Salir')
        print('------------------------------------------')
        print('-Ingresa solo números para hacer tu selección-')
        opcion = int(input('Selecciona tu opción: '))
    
        if opcion == 1:
            mesa = input('Ingresa el número de mesa: ')
            cantidad_personas = int(input('Ingresa la cantidad de personas: '))
            hora_reserva = int(input('Ingresa la hora de la reserva (formato 24 horas): '))
    
            miReserva.reservar_mesa(mesa, cantidad_personas, hora_reserva)
        elif opcion == 2:
            miMenu.mostrar_menu()
        elif opcion == 3:
            comida = input('Ingresa el nombre de la comida: ')
            cantidad = int(input('Ingresa la cantidad deseada: '))
    
            miMenu.realizar_pedido(comida, cantidad)
        elif opcion == 4:
            miReserva.reporte()
            print('Gracias por usar el sistema de reservas y venta de comida.')
            break
        else:
            print('Opción inválida. Intente nuevamente.')
            
else:
    print(Fore.RED + "\nNombre de usuario o contraseña incorrectos.")
    import winsound
    frequency = 1000
    duration = 999
    winsound.Beep(frequency, duration)