from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import FileExtensionValidator
# Create your models here.


class MyAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, avatar, username, password=None):
        if not email:
             raise ValueError('Users must have an email')
        if not avatar:
             raise ValueError('Users must have an avatar')
        if not username:
             raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            avatar=avatar,
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, avatar, username, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            avatar=avatar,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=60, unique=True, verbose_name='email', blank=False)
    avatar = models.ImageField(upload_to='', validators=[FileExtensionValidator(allowed_extensions=['jpg'])])
    username = models.CharField(max_length=15)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'avatar']

    objects = MyAccountManager()

    def __str__(self):
        return self.email
