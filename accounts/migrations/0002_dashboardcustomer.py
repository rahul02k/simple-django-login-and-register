# Generated by Django 2.2.20 on 2021-09-04 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DashboardCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(default=None, max_length=200)),
                ('account_id', models.CharField(default=None, max_length=200)),
                ('name', models.CharField(default=None, max_length=200)),
                ('type_of_account', models.CharField(default=None, max_length=200)),
                ('acc_balance', models.FloatField(default=None)),
                ('interest', models.FloatField(default=None)),
                ('money_paid', models.FloatField(default=None)),
                ('date_of_opening', models.DateTimeField(default=None)),
                ('date_of_maturity', models.DateTimeField(default=None)),
            ],
        ),
    ]
