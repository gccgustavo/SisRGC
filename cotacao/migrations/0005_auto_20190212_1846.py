# Generated by Django 2.1.4 on 2019-02-12 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0004_cotacao_atualizado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cotacao',
            old_name='atualizado',
            new_name='exibir',
        ),
    ]
