from datetime import datetime
from django.core.management.base import BaseCommand
from core.models import * 

class Command(BaseCommand):
    help = 'Hace una reserva de localidades en un evento'

    def add_arguments(self, parser):
        parser.add_argument('id_cliente', type=int, help='ID del cliente que realiza la reserva')
        parser.add_argument('nombre_evento', type=str, help='Nombre del evento al que se desea asistir')
        parser.add_argument('fecha_evento', type=str, help='Fecha del evento al que se desea asistir')     

    def handle(self, *args, **kwargs):
        id_cliente = kwargs['id_cliente']
        nombre_evento = kwargs['nombre_evento']
        fecha_evento = kwargs['fecha_evento']

        # Buscamos el cliente
        cliente = Cliente.objects.get(id_cliente=id_cliente)

        # Buscamos el evento
        evento = Evento.objects.get(nombre_evento=nombre_evento, fecha_evento=fecha_evento)

        # Buscamos las localidades ofertadas cuya localidad esté libre
        localidades = LocalidadesOfertadas.objects.filter(localidad__estado='L', recinto=evento.recinto)

        # Preguntamos qué localidades quiere reservar enseñando las disponibles por numeración
        print('Localidades disponibles:')
        for localidad_ofertada in localidades:
            print(localidad_ofertada.localidad.numeracion + " Usuario: " + localidad_ofertada.usuario.tipo_usuario)

        localidades_reservar = input('Introduce las localidades que deseas reservar separado por comas: ')
        localidades_reservar = localidades_reservar.split(',')
        localidades_reservar = [localidad.strip() for localidad in localidades_reservar]

        entrada_tipo_usuario = input('Ingrese los tipos de usuario (Jubilado, Adulto, Infantil, Parado, Bebé), separados por comas: ')
        tipos_usuario = entrada_tipo_usuario.split(',')
        tipos_usuario = [usuario.strip() for usuario in tipos_usuario]


        localidades_encontradas = LocalidadesOfertadas.objects.filter(localidad__numeracion__in=localidades_reservar, usuario__tipo_usuario__in=tipos_usuario)
        print(len(localidades_encontradas))
        # Preguntamos si va a pagar ahora o después
        pago = input('¿Desea pagar ahora (S/N)? ')
        if pago.capitalize() == 'S':
            metodo_pago = input('Introduce el método de pago (Tarjeta, Transferencia, PayPal, Efectivo): ')
            pago_efectuado = True
        else:
            metodo_pago = 'Ninguno'
            pago_efectuado = False
        fecha_actual = datetime.now()
        reserva = Reserva(cliente=cliente, fecha_reserva=fecha_actual, metodo_pago=metodo_pago, pago_efectuado=pago_efectuado)
        reserva.save()

        if pago_efectuado:
            print('Pago realizado con éxito')
            estado_localidades = 'R'
        else:
            print('Pago pendiente')
            estado_localidades = 'P'

        # Reservamos las localidades
        for localidad in localidades_encontradas:
            localidad.localidad.estado = estado_localidades
            localidad.localidad.save()
            localidad.reserva = reserva
            localidad.save()

        self.stdout.write(self.style.SUCCESS('Reserva realizada con éxito'))