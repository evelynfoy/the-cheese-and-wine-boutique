# Generated by Django 3.2 on 2022-07-28 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_cheese'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='products.product')),
                ('wine_type', models.CharField(max_length=20)),
                ('origin', models.CharField(blank=True, max_length=20, null=True)),
                ('grape', models.CharField(blank=True, max_length=20, null=True)),
                ('production_method', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
