
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
        )
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)
        user.save(using=self._db)

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    first_name = models.CharField(max_length=150, verbose_name='имя')
    last_name = models.CharField(max_length=150, verbose_name='фамилия')
    phone = models.CharField(max_length=35, verbose_name='Номер телефона')
    img = models.ImageField(upload_to='media/', verbose_name='Аватар')
    is_verificated = models.BooleanField(default=False, verbose_name='Подтверждение почты')
    is_active = models.BooleanField(default=False, verbose_name='Статус пользователя')
    is_staff = models.BooleanField(default=False, verbose_name='Статус менеджера')
    is_superuser = models.BooleanField(default=False, verbose_name='Статус администратора')


    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []



