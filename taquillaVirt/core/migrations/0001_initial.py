# Generated by Django 5.0.6 on 2024-05-09 16:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=100)),
                ('codigo_postal', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('datos_tarjeta', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Espectaculo',
            fields=[
                ('nombre_espectaculo', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
                ('productor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Grada',
            fields=[
                ('nombre_grada', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('aforo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('numeracion', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('D', 'Disponible'), ('R', 'Reservada'), ('V', 'Vendida')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Recinto',
            fields=[
                ('nombre_recinto', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('tipo_usuario', models.CharField(choices=[('J', 'Jubilado'), ('A', 'Adulto'), ('I', 'Infantil'), ('P', 'Parado'), ('B', 'Bebé')], max_length=1, primary_key=True, serialize=False)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id_reserva', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_reserva', models.DateField(auto_now_add=True)),
                ('metodo_pago', models.CharField(choices=[('Tarjeta', 'Tarjeta de crédito/débito'), ('Transferencia', 'Transferencia bancaria'), ('Paypal', 'PayPal'), ('Efectivo', 'Pago en efectivo')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='LocalidadesOfertadas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeracion', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('grada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.grada')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.localidad')),
                ('reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.reserva')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=100)),
                ('fecha_evento', models.DateField()),
                ('descripcion', models.TextField()),
                ('participantes', models.TextField()),
                ('espectaculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.espectaculo')),
                ('recinto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.recinto')),
            ],
            options={
                'unique_together': {('nombre_evento', 'fecha_evento')},
            },
        ),
        migrations.AddConstraint(
            model_name='localidadesofertadas',
            constraint=models.UniqueConstraint(fields=('grada', 'localidad', 'usuario'), name='unique_grada_localidad_usuario'),
        ),
    ]
