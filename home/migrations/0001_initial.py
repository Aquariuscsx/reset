# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-14 07:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('photo_id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'banner',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='CategorySub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('cid', models.ForeignKey(blank=True, db_column='cid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category')),
            ],
            options={
                'db_table': 'category_sub',
            },
        ),
        migrations.CreateModel(
            name='CategorySub1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('cid', models.ForeignKey(blank=True, db_column='cid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category')),
            ],
            options={
                'db_table': 'category_sub1',
            },
        ),
        migrations.CreateModel(
            name='CategorySub2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('cs1id', models.ForeignKey(blank=True, db_column='cs1id', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.CategorySub1')),
            ],
            options={
                'db_table': 'category_sub2',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(blank=True, db_column='orderCode', max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('post', models.CharField(blank=True, max_length=255, null=True)),
                ('receiver', models.CharField(blank=True, max_length=255, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('user_message', models.CharField(blank=True, db_column='userMessage', max_length=255, null=True)),
                ('create_date', models.DateTimeField(blank=True, db_column='createDate', null=True)),
                ('pay_date', models.DateTimeField(blank=True, db_column='payDate', null=True)),
                ('delivery_date', models.DateTimeField(blank=True, db_column='deliveryDate', null=True)),
                ('confirm_date', models.DateTimeField(blank=True, db_column='confirmDate', null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid', models.IntegerField(blank=True, null=True)),
                ('number', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'orderitem',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('subtitle', models.CharField(blank=True, db_column='subTitle', max_length=255, null=True)),
                ('orignal_price', models.FloatField(blank=True, db_column='orignalPrice', null=True)),
                ('promote_price', models.FloatField(blank=True, db_column='promotePrice', null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, db_column='createDate', null=True)),
                ('cid', models.ForeignKey(blank=True, db_column='cid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('pid', models.ForeignKey(blank=True, db_column='pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Product')),
            ],
            options={
                'db_table': 'product_image',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('cid', models.ForeignKey(blank=True, db_column='cid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Category')),
            ],
            options={
                'db_table': 'property',
            },
        ),
        migrations.CreateModel(
            name='PropertyValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.IntegerField(blank=True, null=True)),
                ('value', models.CharField(blank=True, max_length=255, null=True)),
                ('ptid', models.ForeignKey(blank=True, db_column='ptid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Property')),
            ],
            options={
                'db_table': 'property_value',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=4000, null=True)),
                ('create_date', models.DateTimeField(blank=True, db_column='createDate', null=True)),
                ('pid', models.ForeignKey(blank=True, db_column='pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Product')),
            ],
            options={
                'db_table': 'review',
            },
        ),
        migrations.CreateModel(
            name='ShopCar',
            fields=[
                ('shop_car_id', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('update_date', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('pid', models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.Product')),
            ],
            options={
                'db_table': 't_shop_car',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('icon', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.AddField(
            model_name='shopcar',
            name='uid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='home.User'),
        ),
        migrations.AddField(
            model_name='review',
            name='uid',
            field=models.ForeignKey(blank=True, db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.User'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='pid',
            field=models.ForeignKey(blank=True, db_column='pid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.Product'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='uid',
            field=models.ForeignKey(blank=True, db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.User'),
        ),
        migrations.AddField(
            model_name='order',
            name='uid',
            field=models.ForeignKey(blank=True, db_column='uid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='home.User'),
        ),
    ]