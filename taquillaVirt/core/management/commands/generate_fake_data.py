import random
from typing import Collection
from django.core.management.base import BaseCommand
from faker import Faker
from core.models import * 

class Command(BaseCommand):
    help = 'Genera datos ficticios y los inserta en la base de datos'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, help='Número total de registros a generar')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        # Generamos Clientes
        for _ in range(total):
            # Genera datos ficticios
            nombre = fake.name()
            apellido = fake.last_name()
            direccion = fake.address()
            ciudad = fake.city()
            codigo_postal = fake.zipcode()
            telefono = fake.phone_number()
            email = fake.email()
            datos_tarjeta = fake.credit_card_number()

            # Crea un nuevo objeto del modelo y lo guarda en la base de datos
            objeto = Cliente(nombre=nombre, apellido=apellido, direccion=direccion, ciudad=ciudad, codigo_postal=codigo_postal, telefono=telefono, email=email, datos_tarjeta=datos_tarjeta)
            objeto.save()

        # Generamos Usuarios
        tipos_usuario = ['J', 'A', 'I', 'P', 'B']
        for usuario in tipos_usuario:
            tipo_usuario = usuario
            objeto = Usuario(tipo_usuario=tipo_usuario)
            objeto.save()
        
        # Generamos Localidades
        for _ in range(total*2):
            numeracion = _
            numero_aleatorio = random.randint(0, 99)

            if numero_aleatorio < 10:
                estado = 'D'                    
                print("se ha deteriorado")
            else:
                estado = 'L'
            objeto = Localidad(numeracion=numeracion, estado=estado)
            objeto.save()

        # Generamos Gradas
        tipos_grada = ['Norte', 'Sur', 'Este', 'Oeste', 'General', 'VIP', 'Tribuna', 'Palco', 'Anillo', 'Fondo', 'Lateral', 'Central']
        for grada in tipos_grada:
            nombre_grada = grada
            aforo = fake.random_int(min=100, max=1000)
            objeto = Grada(nombre_grada=nombre_grada, aforo=aforo)
            objeto.save()

        # Generamos Espectaculos
        espectaculos_inventados = ['Concierto', 'Teatro', 'Cine', 'Deportes', 'Festival', 'Circo', 'Conferencia', 'Exposición', 'Feria', 'Fiesta']
        for espectaculo in espectaculos_inventados:
            nombre_espectaculo = espectaculo
            descripcion = fake.sentence()
            productor = fake.name()
            objeto = Espectaculo(nombre_espectaculo=nombre_espectaculo, descripcion=descripcion, productor=productor)
            objeto.save()

        # Generamos Recintos
        recintos_disponibles = ['Estadio', 'Teatro', 'Cine', 'Pabellón', 'Auditorio', 'Sala', 'Plaza', 'Centro', 'Palacio', 'Recinto', 'Parque', 'Campo']
        for recintos in recintos_disponibles:
            nombre_recinto = recintos
            direccion_recinto = fake.address()
            objeto = Recinto(nombre_recinto=nombre_recinto, direccion=direccion_recinto)
            objeto.save()

        # Generamos Eventos
        for _ in range(int(total/2)):
            espectaculo = fake.random_element(Espectaculo.objects.all())
            recinto = fake.random_element(Recinto.objects.all())
            nombre_evento =  espectaculo.nombre_espectaculo + f' en {recinto.nombre_recinto}'
            fecha_evento = fake.date_this_year(before_today=False, after_today=True)
            descripcion = fake.sentence()
            participantes = fake.name()
            objeto = Evento(nombre_evento=nombre_evento, fecha_evento=fecha_evento, descripcion=descripcion, participantes=participantes, recinto=recinto, espectaculo=espectaculo)
            objeto.save()

        # # Generamos Reservas
        # for _ in range(total):
        #     cliente = fake.random_element(Cliente.objects.all())
        #     fecha_reserva = fake.date_this_year(before_today=True, after_today=False)
        #     metodo_pago = fake.random_element(elements=('Tarjeta', 'Paypal', 'Transferencia', 'Efectivo'))
        #     objeto = Reserva(cliente=cliente, fecha_reserva=fecha_reserva, metodo_pago=metodo_pago)
        #     objeto.save()

        # Generamos LocalidadesOfertadas, asignando a cada localidad una grada y los distintos tipos de usuario
        localidades_seleccionadas = []
        tipos_usuario_existentes = Usuario.objects.all()
        gradas_existentes = Grada.objects.all()
        # TODO: Check aforo
        for grada in gradas_existentes:
            recinto = fake.random_element(Recinto.objects.all())
            localidades_disponibles = list(Localidad.objects.exclude(numeracion__in=[localidad.numeracion for localidad in localidades_seleccionadas]))

            if len(localidades_disponibles) > 0:
                for localidad in localidades_disponibles[:5]:
                    localidades_seleccionadas.append(localidad)
                    if localidad.estado != 'D':
                        for usuario in tipos_usuario_existentes:
                            localidad_to_offer = localidad
                            usuario = usuario
                            # Reserva no asignada
                            reserva = None
                            objeto = LocalidadesOfertadas(grada=grada, localidad=localidad_to_offer, usuario=usuario, recinto=recinto, reserva=reserva)
                            objeto.save()
                    
            else:
                break

            






        self.stdout.write(self.style.SUCCESS(f'Se han generado y guardado {total} clientes, y x2 localidades, en la base de datos'))

    def obtener_muestra_aleatoria(self, elementos, porcentaje):
        elementos = list(elementos)
        num_elementos_muestra = int(len(elementos) * (porcentaje / 100))

        # Seleccionar una muestra aleatoria de elementos
        muestra_aleatoria = random.sample(elementos, num_elementos_muestra)

        return muestra_aleatoria