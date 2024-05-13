from django.db import models


class Espectaculo(models.Model):
    nombre_espectaculo = models.CharField(max_length=255, primary_key=True)
    descripcion = models.TextField()
    productor = models.CharField(max_length=255)

class Recinto(models.Model):
    nombre_recinto = models.CharField(max_length=255, primary_key=True)
    direccion = models.CharField(max_length=255)

    
class Evento(models.Model):
    nombre_evento = models.CharField(max_length=516)
    fecha_evento = models.DateField()
    descripcion = models.TextField()
    participantes = models.TextField()
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE)
    espectaculo = models.ForeignKey(Espectaculo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nombre_evento', 'fecha_evento')


class Grada(models.Model):
    nombre_grada = models.CharField(max_length=255, primary_key=True)
    aforo = models.IntegerField()

class Localidad(models.Model):
    numeracion = models.CharField(max_length=255, primary_key=True)

    ESTADO_CHOICES = [
        ('L', 'Libre'),
        ('R', 'Reservada'),
        ('P', 'Pre-reservada'),
        ('D', 'Deteriorada'),
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

    def create_descripcion(self):
        if self.tipo_usuario == 'J':
            return 'Jubilado'
        elif self.tipo_usuario == 'A':
            return 'Adulto'
        elif self.tipo_usuario == 'I':
            return 'Infantil'
        elif self.tipo_usuario == 'P':
            return 'Parado'
        elif self.tipo_usuario == 'B':
            return 'Bebé'
        else:
            return 'Usuario no identificado'
        
    def save(self, *args, **kwargs):
        self.descripcion = self.create_descripcion()
        super().save(*args, **kwargs)

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField()
    email = models.EmailField()
    datos_tarjeta = models.CharField(max_length=255)

class Reserva(models.Model):
    id_reserva = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Añadimos la clave foránea a Cliente
    fecha_reserva = models.DateField(auto_now_add=True)
    METODO_PAGO_CHOICES = [
        ('Tarjeta', 'Tarjeta de crédito/débito'),
        ('Transferencia', 'Transferencia bancaria'),
        ('Paypal', 'PayPal'),
        ('Efectivo', 'Pago en efectivo'),
        ('Ninguno', 'Sin especificar')
    ]
    metodo_pago = models.CharField(max_length=30, choices=METODO_PAGO_CHOICES)
    pago_efectuado = models.BooleanField(default=False)

class LocalidadesOfertadas(models.Model):
    grada = models.ForeignKey(Grada, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE, default=None)
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, default=None, null=True) 
    
    class Meta:
            constraints = [
                models.UniqueConstraint(fields=['grada', 'localidad', 'usuario'], name='unique_grada_localidad_usuario')
            ]

    def save(self, *args, **kwargs):
        self.precio = self.calcular_precio()
        super().save(*args, **kwargs)

    def calcular_precio(self):

        if self.usuario.tipo_usuario == 'J':
            return 5.0
        elif self.usuario.tipo_usuario == 'A':
            return 15.0
        elif self.usuario.tipo_usuario == 'I':
            return 10.0
        elif self.usuario.tipo_usuario == 'P':
            return 7.5
        elif self.usuario.tipo_usuario == 'B':
            return 2.5
        else:
            return 10.0  # Precio base de ejemplo
        
    def __str__(self) -> str:
        return self.localidad.numeracion

