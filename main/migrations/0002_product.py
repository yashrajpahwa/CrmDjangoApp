# Generated by Django 3.1.1 on 2020-09-06 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.DecimalField(decimal_places=0, max_digits=2, max_length=255, null=True)),
                ('category', models.CharField(max_length=255, null=True)),
                ('description', models.CharField(max_length=255, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]