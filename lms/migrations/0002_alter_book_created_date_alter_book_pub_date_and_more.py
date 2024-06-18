# Generated by Django 5.0.3 on 2024-03-10 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='updated_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='updated_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='librarian',
            name='updated_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='created_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='updated_date',
            field=models.DateTimeField(),
        ),
    ]
