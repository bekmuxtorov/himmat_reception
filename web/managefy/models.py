from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser

FOR_WHOM = (
    ('man', _('Man')),
    ('woman', _("Woman")),
    ('all', _('All'))
)


class TelegramGroups(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255
    )
    telegram_id = models.IntegerField(verbose_name=_("telegram_id"),)
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Telegram Group'
        verbose_name_plural = 'Telegram Groups'


class Courses(models.Model):
    name = models.CharField(
        verbose_name=_("name"),
        max_length=255
    )
    description = models.TextField(verbose_name=_("description"))
    created_at = models.DateTimeField(
        verbose_name=_("created_at"),
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'


class Groups(models.Model):
    organiser = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='organised_groups',
        verbose_name=_("Organiser"),
    )
    telegram_group = models.ForeignKey(
        to=TelegramGroups,
        on_delete=models.CASCADE,
        verbose_name=_("Telegram Group"),
        related_name="groups"
    )
    course = models.ForeignKey(
        to=Courses,
        on_delete=models.CASCADE,
        verbose_name=_("Course"),
        related_name="groups"
    )
    for_whom = models.CharField(
        verbose_name=_("for whom"),
        max_length=255,
        choices=FOR_WHOM
    )
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255
    )
    start_date = models.DateTimeField(verbose_name=_("Start date"))
    end_date = models.DateTimeField(verbose_name=_("End date"))
    created_at = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'


class Applications(models.Model):
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        verbose_name=_("User")
    )
    group = models.ForeignKey(
        to=Groups,
        on_delete=models.CASCADE,
        verbose_name=_("Group")
    )
    is_accepted = models.BooleanField(
        verbose_name=_("is accepted"),
        default=False
    )
    is_enter_group = models.BooleanField(
        default=False,
        verbose_name=_("is enter group")
    )
    enter_group_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name=_("enter group date")
    )
    created_at = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.user.full_name} || {self.group.name}'

    class Meta:
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'


class UserMessage(models.Model):
    application = models.ForeignKey(
        to=Applications,
        on_delete=models.CASCADE,
        related_name='user_messages',
        verbose_name=_("Application")
    )
    text = models.TextField(verbose_name=_("text"))
    created_at = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.application.user}: {self.text[:20]}...'

    class Meta:
        verbose_name = 'UserMessage'
        verbose_name_plural = 'UserMessages'


class AdminMessage(models.Model):
    application = models.ForeignKey(
        to=Applications,
        on_delete=models.CASCADE,
        related_name='admin_messages',
        verbose_name=_("Application")
    )
    text = models.TextField(verbose_name=_("text"))
    created_at = models.DateTimeField(
        verbose_name=_("Created date"),
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.application.user}: {self.text[:20]}...'

    class Meta:
        verbose_name = 'AdminMessage'
        verbose_name_plural = 'AdminMessages'
