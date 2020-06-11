# Generated by Django 3.0.7 on 2020-06-11 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_delete_booking'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.CharField(max_length=50)),
                ('nbPerson', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True)),
                ('message', models.TextField(null=True)),
                ('validate', models.TextField(default='false')),
            ],
            options={
                'verbose_name': 'Reservation',
                'ordering': ['validate', 'date'],
            },
        ),
    ]
