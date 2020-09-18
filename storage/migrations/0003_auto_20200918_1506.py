# Generated by Django 2.2 on 2020-09-18 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20200916_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incominginventoryset',
            name='name',
        ),
        migrations.RemoveField(
            model_name='outcominginventoryset',
            name='name',
        ),
        migrations.AddField(
            model_name='incominginventoryset',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='storage.Product'),
        ),
        migrations.AddField(
            model_name='incominginventoryset',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='outcominginventoryset',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='storage.Product'),
        ),
        migrations.AlterField(
            model_name='outcominginventoryset',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]