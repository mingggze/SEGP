# Generated by Django 3.1.3 on 2021-04-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('trend_score', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_update', models.DateField(blank=True, null=True)),
            ],
        ),
    ]