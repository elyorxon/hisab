# Generated by Django 4.1.5 on 2023-03-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_expenses_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kirim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('miqdori', models.PositiveIntegerField(max_length=15)),
                ('sanasi', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.RemoveField(
            model_name='salesreport',
            name='order',
        ),
        migrations.RemoveField(
            model_name='salesreport',
            name='order_item',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='order',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
        migrations.DeleteModel(
            name='SalesReport',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
