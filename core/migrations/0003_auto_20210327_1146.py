# Generated by Django 2.2 on 2021-03-27 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_propertymaster_netprar'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvgMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountId', models.BigIntegerField()),
                ('acres', models.FloatField()),
                ('address', models.CharField(max_length=255)),
                ('Url', models.URLField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('county', models.CharField(max_length=255)),
                ('lwPropertyId', models.BigIntegerField()),
                ('price', models.FloatField()),
                ('state', models.CharField(max_length=255)),
                ('Rate', models.FloatField()),
                ('NetPrAr', models.FloatField(default=0.0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='propertymaster',
            name='NetPrAr',
            field=models.FloatField(default=0.0),
        ),
    ]