# Generated by Django 3.0.8 on 2020-09-04 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Res1', '0004_auto_20200904_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indian',
            name='image',
            field=models.FileField(null=True, upload_to='media/'),
        ),
    ]