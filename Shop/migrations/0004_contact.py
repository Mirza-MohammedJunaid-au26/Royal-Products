# Generated by Django 3.2.8 on 2021-11-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0003_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('city', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('zip', models.IntegerField(default=0)),
                ('enquiry', models.CharField(default='', max_length=300)),
            ],
        ),
    ]