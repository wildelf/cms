from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import Group, Permission, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext


SEX = (
    ('1', u'男'),
    ('2', u'女'),
)


class SiteUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)



class SiteGroup(Group):
    class Meta:
        proxy = True
        verbose_name = '角色'
        verbose_name_plural = '角色'


class SitePermission(Permission):
    class Meta:
        proxy = True
        verbose_name = '权限'
        verbose_name_plural = '权限'

class SiteUser(AbstractBaseUser, PermissionsMixin):
    # objects = SiteUserManager()
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    groups = models.ManyToManyField(SiteGroup, verbose_name='角色')
    user_permissions = models.ManyToManyField(
        SitePermission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_set",
        related_query_name="user",
    )

    parent = models.ForeignKey("self",verbose_name='上级用户',null=True,blank=True,on_delete=models.SET_NULL)
    mobile = models.CharField(verbose_name=u'手机', max_length=15, null=True, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )

    objects = SiteUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ ]

    class Meta:
        # db_table = 'lable'
        verbose_name = u'用户'
        verbose_name_plural = u'用户'

    def __str_(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length=256,verbose_name='标题')
    type_choices = ((0, "通告"), (1, "新闻"))
    type = models.SmallIntegerField(choices=type_choices, default=0, verbose_name='类型')
    add_index_choices = ((0, "否"), (1, "是"))
    index = models.SmallIntegerField(choices=add_index_choices, default=0, verbose_name='是否加入首页')
    add_change_show_choices = ((0, "否"), (1, "是"))
    change_show = models.SmallIntegerField(choices=add_change_show_choices, default=0, verbose_name='是否加入轮播图')
    summary = models.TextField(verbose_name='摘要',null=True,blank=True)
    content = models.TextField(verbose_name='内容',null=True,blank=True)
    update_time = models.DateTimeField(verbose_name='日期',auto_now=True)
    big_img = models.ImageField(verbose_name='大图')
    small_img = models.ImageField(verbose_name='小图')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'



