# Generated by Django 3.0.3 on 2020-06-18 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0004_post_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ip',
            field=models.GenericIPAddressField(editable=False, null=True),
        ),
    ]
