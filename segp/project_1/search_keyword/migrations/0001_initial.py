# Generated by Django 3.1.2 on 2021-01-13 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
<<<<<<< HEAD
=======
                ('score', models.DecimalField(max_digits=5, decimal_places=2)),
>>>>>>> d6522b2abbc23d6dc6b0fdc845480a317c9f8713
                ('last_update', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword_Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]