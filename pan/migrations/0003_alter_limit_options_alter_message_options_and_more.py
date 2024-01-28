# Generated by Django 4.1.3 on 2023-06-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import pan.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pan', '0002_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='limit',
            options={'verbose_name': 'условия', 'verbose_name_plural': 'условия'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'сообщение', 'verbose_name_plural': 'сообщение'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'verbose_name': 'уведомление', 'verbose_name_plural': 'уведомление'},
        ),
        migrations.AlterModelOptions(
            name='userlog',
            options={'verbose_name': 'Журнал посещений пользователя', 'verbose_name_plural': 'Журнал посещений пользователя'},
        ),
        migrations.AlterField(
            model_name='fileshare',
            name='secret_key',
            field=models.CharField(db_index=True, max_length=10, verbose_name='Поделиться ключом'),
        ),
        migrations.AlterField(
            model_name='fileshare',
            name='user_file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.genericfile', verbose_name='документ'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='suffix',
            field=models.CharField(blank=True, max_length=10, unique=True, verbose_name='Суффикс'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='type_name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='filetype',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='genericfile',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='files', to=settings.AUTH_USER_MODEL, verbose_name='создатель'),
        ),
        migrations.AlterField(
            model_name='genericfile',
            name='del_flag',
            field=models.CharField(choices=[('0', 'Не собранный'), ('1', 'Переработанный')], default='0', max_length=1, verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='genericfile',
            name='file_cate',
            field=models.CharField(choices=[('0', 'документ'), ('1', 'папка')], max_length=1, verbose_name='Классификация файлов'),
        ),
        migrations.AlterField(
            model_name='genericfile',
            name='file_size',
            field=models.BigIntegerField(default=0, verbose_name='Размер файла'),
        ),
        migrations.AlterField(
            model_name='genericfile',
            name='folder',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pan.genericfile', to_field='file_uuid', verbose_name='Улучшенный каталог'),
        ),
        migrations.AlterField(
            model_name='genericfile',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='limit',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель'),
        ),
        migrations.AlterField(
            model_name='limit',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='message',
            name='action',
            field=models.CharField(choices=[('0', 'сообщение'), ('1', 'заявление')], max_length=1, verbose_name='тип'),
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.TextField(verbose_name='Содержание сообщения'),
        ),
        migrations.AlterField(
            model_name='message',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель'),
        ),
        migrations.AlterField(
            model_name='message',
            name='state',
            field=models.CharField(choices=[('0', 'Неподтвержденный'), ('1', 'Принятый'), ('2', 'Неудачный')], default='0', max_length=1, verbose_name='состояние'),
        ),
        migrations.AlterField(
            model_name='message',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='content',
            field=models.TextField(verbose_name='Содержание уведомления'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='title',
            field=models.CharField(max_length=50, verbose_name='подпись'),
        ),
        migrations.AlterField(
            model_name='notice',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('0', 'Жен'), ('1', 'Муж')], max_length=1, verbose_name='пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.ForeignKey(on_delete=models.SET(pan.models.get_deleted_role), to='pan.role', verbose_name='роль'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.AlterField(
            model_name='role',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_key',
            field=models.CharField(max_length=50, unique=True, verbose_name='Характер'),
        ),
        migrations.AlterField(
            model_name='role',
            name='role_name',
            field=models.CharField(max_length=50, verbose_name='Имя персонажа'),
        ),
        migrations.AlterField(
            model_name='role',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='rolelimit',
            name='create_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Cоздатель'),
        ),
        migrations.AlterField(
            model_name='rolelimit',
            name='limit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pan.limit', verbose_name='ограничение'),
        ),
        migrations.AlterField(
            model_name='rolelimit',
            name='update_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(pan.models.get_deleted_user), related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Средство обновления'),
        ),
        migrations.AlterField(
            model_name='rolelimit',
            name='value',
            field=models.BigIntegerField(verbose_name='значение'),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='action',
            field=models.CharField(choices=[('0', 'войти'), ('1', 'опубликовывать'), ('2', 'Ошибка входа')], max_length=1, verbose_name='действия'),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='action_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='время'),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='ipaddress',
            field=models.GenericIPAddressField(verbose_name='IP-адрес :'),
        ),
        migrations.AlterField(
            model_name='userlog',
            name='os',
            field=models.CharField(max_length=30, verbose_name='операционная система'),
        ),
    ]