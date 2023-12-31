# Generated by Django 4.2.4 on 2023-08-23 15:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('postal_code', models.CharField(default='', max_length=20)),
                ('compound_name', models.CharField(max_length=255)),
                ('compound_image', models.ImageField(upload_to='compound_images/')),
                ('compound_location', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('facilities', models.TextField(default='')),
                ('security_level', models.CharField(default='', max_length=50)),
                ('contact_email', models.EmailField(default='', max_length=254)),
                ('contact_phone', models.CharField(default='', max_length=20)),
                ('website', models.URLField(blank=True, null=True)),
                ('social_media_links', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PassRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arrival_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('approval_date', models.DateTimeField(blank=True, null=True)),
                ('is_approved', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('cancellation_reason', models.TextField(blank=True, null=True)),
                ('is_expired', models.BooleanField(default=False)),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.compound')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('postal_code', models.CharField(default='', max_length=20)),
                ('property_name', models.CharField(max_length=255)),
                ('property_image', models.ImageField(upload_to='property_images/')),
                ('property_type', models.CharField(max_length=50)),
                ('bedrooms', models.PositiveIntegerField()),
                ('bathrooms', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_available', models.BooleanField(default=True)),
                ('amenities', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='')),
                ('city', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('postal_code', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('mobile_number', models.CharField(max_length=15)),
                ('language_preference', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('social_media_links', models.URLField(blank=True, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PropertyOwnerVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_document', models.FileField(upload_to='verification_documents/')),
                ('verification_status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.property')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pass_share_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_status', models.CharField(choices=[('pending', 'Pending'), ('success', 'Success'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=100)),
                ('payment_method', models.CharField(max_length=50)),
                ('receipt_url', models.URLField(blank=True, null=True)),
                ('is_refunded', models.BooleanField(default=False)),
                ('refund_date', models.DateTimeField(blank=True, null=True)),
                ('passrequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.passrequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='PassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passtype_name', models.CharField(max_length=255)),
                ('passtype_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('geo_restricted', models.BooleanField(default=False)),
                ('valid_from', models.DateTimeField()),
                ('valid_to', models.DateTimeField()),
                ('duration', models.PositiveIntegerField()),
                ('max_users', models.PositiveIntegerField()),
                ('special_conditions', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('compound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.compound')),
            ],
        ),
        migrations.AddField(
            model_name='passrequest',
            name='passtypes_selected',
            field=models.ManyToManyField(to='pass_share_app.passtype'),
        ),
        migrations.AddField(
            model_name='passrequest',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.user'),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('notification_type', models.CharField(max_length=50)),
                ('is_read', models.BooleanField(default=False)),
                ('action_link', models.URLField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pass_share_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='NationalIDVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_result', models.BooleanField()),
                ('verification_date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='national_id_verifications', to='pass_share_app.user')),
                ('verifier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='verified_national_ids', to='pass_share_app.user')),
            ],
        ),
    ]
