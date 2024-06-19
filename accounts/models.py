from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .managers import UserManager

GENDER = (
    ('men', _('Men')),
    ('women', _('Women')),
)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(
            verbose_name=_("phone number"),
            max_length=20,
            unique=True,
            blank=True,
            validators=[
                RegexValidator(
                    regex=r'^\+998\d{9}$',
                    message=_('Invalid phone number. Please enter in the format +998901234567')
                ),
            ]
    )    
    full_name = models.CharField(
        verbose_name=_("Full name"),
        max_length=255
    )
    username = models.CharField(
        verbose_name=_("Username"),
        max_length=255,
        blank=True,
    )
    telegram_id = models.IntegerField(
        verbose_name=_("Telegram ID"),
        blank=True,
        null=True
    )
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=GENDER,
        max_length=5,
        default='men'
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True
    )
    is_staff = models.BooleanField(
        verbose_name="is staff",
        default=False
    )
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']
    
    objects = UserManager()

    def __str__(self) -> str:
        return self.full_name
    
    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
