from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password = None):
        if not email:
            raise ValueError('Email is required')
        if not username:
            raise ValueError("Username is required")
        user = self.model(
            email = self.normalize_email(email),
            username = username
        )
        user.set_password(password)
        user.save(using = self._db)
        return user


    def create_staffuser(self, email, username, password = None):
        user = self.create_user(
            email = email,
            username = username,
            password = password
        )
        user.is_staff = True
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, username,password = None):
        user = self.create_user(
            email = email,
            username = username,
            password= password
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using = self._db)
        return user



class Account(AbstractBaseUser):
    email = models.EmailField(max_length = 30, unique =True, verbose_name = "Email")
    username = models.CharField(max_length = 50, unique= True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default= False)
    is_admin = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now= True)

    joined_date = models.DateTimeField(auto_now_add= True)


    def __str__(self):
        return self.email

    class Meta:
        db_table = 'Account'

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    objects = AccountManager()

    def has_perm(self, perm, object = None):
        return True

    def has_module_perms(self, app_label):
        return True


class ProfileFeed(models.Model):
    feed_user = models.ForeignKey(Account, on_delete= models.CASCADE)
    feed_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.feed_text

    class Meta:
        db_table = 'Profile Feed'

    