# Generated by Django 2.1.4 on 2019-02-12 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cotacao', '0002_cotacao_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='ListaPP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkpp', models.TextField()),
            ],
        ),
    ]
