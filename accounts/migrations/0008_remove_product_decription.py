# Generated by Django 3.0.7 on 2021-03-13 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='decription',
        ),
    ]
