# Generated by Django 4.0.5 on 2023-01-27 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRQEuLRn-ihcl1SPkCVInXgmGPSWQheqGIzjA&usqp=CAU', max_length=1000),
        ),
    ]
