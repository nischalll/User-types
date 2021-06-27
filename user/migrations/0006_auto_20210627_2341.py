# Generated by Django 2.1.5 on 2021-06-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210627_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile',
            field=models.ImageField(default='path/to/my/default/image.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_patient',
            field=models.BooleanField(default='True'),
        ),
    ]
