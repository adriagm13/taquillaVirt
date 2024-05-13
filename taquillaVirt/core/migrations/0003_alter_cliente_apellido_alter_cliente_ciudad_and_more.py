# Generated by Django 5.0.6 on 2024-05-11 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_localidadesofertadas_numeracion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='ciudad',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='datos_tarjeta',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='espectaculo',
            name='nombre_espectaculo',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='espectaculo',
            name='productor',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='evento',
            name='nombre_evento',
            field=models.CharField(max_length=516),
        ),
        migrations.AlterField(
            model_name='grada',
            name='nombre_grada',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='localidad',
            name='numeracion',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='recinto',
            name='direccion',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='recinto',
            name='nombre_recinto',
            field=models.CharField(max_length=255, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='metodo_pago',
            field=models.CharField(choices=[('Tarjeta', 'Tarjeta de crédito/débito'), ('Transferencia', 'Transferencia bancaria'), ('Paypal', 'PayPal'), ('Efectivo', 'Pago en efectivo'), ('Ninguno', 'Sin especificar')], max_length=30),
        ),
    ]