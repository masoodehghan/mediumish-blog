# Generated by Django 4.0.2 on 2022-02-16 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='c2.jpg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]
