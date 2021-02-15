# Generated by Django 3.1.2 on 2021-01-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('trend_score', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_update', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
