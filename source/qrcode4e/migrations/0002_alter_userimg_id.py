# Generated by Django 3.2.4 on 2021-09-21 08:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qrcode4e', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimg',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
