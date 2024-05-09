from django.db import models

class Espectaculo(models.Model):
    nombre_espectaculo = models.CharField(max_length=100, primary_key=True)
    descripcion = models.TextField()
    productor = models.CharField(max_length=100)

class Recinto(models.Model):
    nombre_recinto = models.CharField(max_length=100, primary_key=True)
    direccion = models.CharField(max_length=200)
    evento = models.ForeignKey('Evento', on_delete=models.CASCADE)

    
class Evento(models.Model):
    nombre_evento = models.CharField(max_length=100)
    fecha_evento = models.DateField()
    descripcion = models.TextField()
    participantes = models.TextField()
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE)
    espectaculo = models.ForeignKey(Espectaculo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nombre_evento', 'fecha_evento')


class Grada(models.Model):
    nombre_grada = models.CharField(max_length=100, primary_key=True)
    aforo = models.IntegerField()

class Localidad(models.Model):
    numeracion = models.CharField(max_length=100, primary_key=True)

    ESTADO_CHOICES = [
        ('D', 'Disponible'),
        ('R', 'Reservada'),
        ('V', 'Vendida'),
    ]
    estado = models.CharField(max_length=1, choices=ESTADO_CHOICES)

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('J', 'Jubilado'),
        ('A', 'Adulto'),
        ('I', 'Infantil'),
        ('P', 'Parado'),
        ('B', 'Bebé'),
    ]
    tipo_usuario = models.CharField(max_length=1, choices=TIPO_USUARIO_CHOICES, primary_key=True)
    descripcion = models.TextField()

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    datos_tarjeta = models.CharField(max_length=100)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Añadimos la clave foránea a Cliente
    fecha_reserva = models.DateField(auto_now_add=True)
    METODO_PAGO_CHOICES = [
        ('Tarjeta', 'Tarjeta de crédito/débito'),
        ('Transferencia', 'Transferencia bancaria'),
        ('Paypal', 'PayPal'),
        ('Efectivo', 'Pago en efectivo'),
        # Añade más opciones según sea necesario
    ]
    metodo_pago = models.CharField(max_length=20, choices=METODO_PAGO_CHOICES)

class LocalidadesOfertadas(models.Model):
    grada = models.ForeignKey(Grada, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numeracion = models.IntegerField()
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE) 
    
    class Meta:
        primary_key = models.ForeignKeyConstraint(['grada', 'localidad', 'usuario'], name='pk_localidades_ofertadas')
    
    def save(self, *args, **kwargs):
        self.precio = self.calcular_precio()
        super().save(*args, **kwargs)

    def calcular_precio(self):
        # Implementa aquí la lógica para calcular el precio según la grada, localidad y tipo de usuario
        # Puedes acceder a los atributos del objeto como self.grada, self.localidad, self.tipo_usuario, etc.
        # Devuelve el precio calculado
        # Este es solo un ejemplo de cómo podría ser el cálculo del precio
        # Aquí deberás adaptarlo según tus necesidades específicas
        # Por ejemplo, podrías tener una tabla de precios en la base de datos o una lógica más compleja
        return 10.0  # Precio base de ejemplo

