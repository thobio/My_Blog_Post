# Generated by Django 4.2.2 on 2023-06-21 15:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5ff7e897-637e-426e-957d-c7024685f0a6'), editable=False, primary_key=True, serialize=False),
        ),
    ]