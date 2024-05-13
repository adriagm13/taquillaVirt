from django.core.management.base import BaseCommand
from core.models import *  

class Command(BaseCommand):
    help = 'Elimina todos los datos de la base de datos'

    def handle(self, *args, **options):
        # Elimina todos los objetos de cada modelo
        modelos = [Cliente, Usuario, Grada, Localidad, LocalidadesOfertadas, Evento, Espectaculo, Reserva, Recinto] 
        for modelo in modelos:
            modelo.objects.all().delete()

        # Imprime un mensaje de confirmación
        self.stdout.write(self.style.SUCCESS('¡Todos los datos de la base de datos han sido eliminados con éxito!'))
