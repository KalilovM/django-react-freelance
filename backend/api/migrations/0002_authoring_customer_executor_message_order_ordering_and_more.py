# Generated by Django 4.0.5 on 2022-06-20 09:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Authoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Executor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_date', models.DateTimeField(auto_now_add=True)),
                ('is_edited', models.BooleanField(default=False)),
                ('description', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('service_type', models.CharField(choices=[('1', 'Фронт-енд'), ('2', 'Бэк-енд'), ('3', 'Дизайн'), ('4', 'Разработка'), ('5', 'Тестирование'), ('6', 'Разное')], default='1', max_length=1)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Ordering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.executor')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.order')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=1)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('service_type', models.CharField(choices=[('1', 'Фронт-енд'), ('2', 'Бэк-енд'), ('3', 'Дизайн'), ('4', 'Разработка'), ('5', 'Тестирование'), ('6', 'Разное')], default='1', max_length=1)),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.executor')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('order', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.order')),
                ('service', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.service')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('severity', models.CharField(choices=[('1', 'Низкий'), ('2', 'Средний'), ('3', 'Высокий')], default='1', max_length=1)),
                ('description', models.TextField()),
                ('ticket_date', models.DateTimeField(auto_now_add=True)),
                ('is_resolved', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer')),
                ('executor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.executor')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='ordering',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service'),
        ),
        migrations.AddField(
            model_name='authoring',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customer'),
        ),
        migrations.AddField(
            model_name='authoring',
            name='executor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.executor'),
        ),
        migrations.AddField(
            model_name='authoring',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.review'),
        ),
    ]
