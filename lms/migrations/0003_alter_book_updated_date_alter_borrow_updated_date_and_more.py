# Generated by Django 5.0.3 on 2024-03-10 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0002_alter_book_created_date_alter_book_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 10, 19, 32, 25, 574576)),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='updated_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 10, 19, 32, 25, 575634)),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='updated_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 10, 19, 32, 25, 574576)),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2024, 3, 10, 19, 32, 25, 573577)),
        ),
    ]
