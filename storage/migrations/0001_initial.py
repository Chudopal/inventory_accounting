# Generated by Django 2.2 on 2020-09-15 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoldingAccounting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incoming', models.IntegerField(default=0)),
                ('outcoming', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='IncomingInvoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=60)),
                ('position', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='OutcomingInvoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=60)),
                ('position', models.CharField(max_length=30)),
                ('storage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Storage')),
            ],
        ),
        migrations.CreateModel(
            name='OutcomingInventorySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('quantity', models.IntegerField()),
                ('incoming_invoices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.IncomingInvoices')),
            ],
        ),
        migrations.AddField(
            model_name='incominginvoices',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Storage'),
        ),
        migrations.CreateModel(
            name='IncomingInventorySet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incoming_invoices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.IncomingInvoices')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.FoldingAccounting')),
            ],
        ),
        migrations.AddField(
            model_name='foldingaccounting',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Product'),
        ),
        migrations.AddField(
            model_name='foldingaccounting',
            name='storage',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Storage'),
        ),
    ]
