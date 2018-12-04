# Generated by Django 2.0.6 on 2018-12-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FuG202_api', '0003_restaurant_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='tags',
            field=models.ManyToManyField(related_name='restaurants', to='FuG202_api.Tag'),
        ),
    ]
