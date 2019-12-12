# Generated by Django 2.2.6 on 2019-11-17 18:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('calificacion', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Flor',
            fields=[
                ('name', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('precio', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(null=True, upload_to='')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
