from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # TODO закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    first_name =
    last_name =
    phone =
    email =
    role =
    image =
    # TODO переопределение пользователя.
    # TODO подробности также можно поискать в рекоммендациях к проекту
    pass


first_name — имя пользователя (строка).
last_name — фамилия пользователя (строка).
phone — телефон для связи (строка).
email — электронная почта пользователя (email) (используется в качестве логина).
role — роль пользователя, доступные значени
image - аватарка пользователя