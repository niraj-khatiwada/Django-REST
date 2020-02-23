from django.db import models


from django.core.exceptions import ValidationError
from django.contrib.auth.models import  AbstractBaseUser, BaseUserManager


# Create your models here

class AccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email must be provided')
        if not username:
            raise ValidationError("Username must be provided")
        user = self.model(
        email = self.normalize_email(email),
        username = username
        )  
        user.set_password(password)
        user.save(using= self._db)
        return user


    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email =email,
            username= username,
            password = password,

        )
        user.is_staff = True
        user.save(using = self._db  )
        return user

    def create_superuser(self, email, username,  password=None):
        user = self.create_user(
            email = email,
            username = username,
            password = password,
           
        )
        user.is_staff = True
        user.is_admin = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    email =         models.EmailField(max_length=255, unique=True, verbose_name='Email')
    username =      models.CharField(max_length = 50)
    is_active =     models.BooleanField(default=True, verbose_name='Active')
    is_staff =      models.BooleanField(default=False, verbose_name='Staff')
    is_admin =      models.BooleanField(default=False, verbose_name='Admin')
    date_joined     = models.DateTimeField(verbose_name='Date Joined',auto_now_add= True)
    last_login      = models.DateTimeField(verbose_name='Last Active', auto_now=True)
        
    class Meta:
        db_table = 'Account'

    def __str__(self):
        return self.email
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = AccountManager()

    def has_perm(self, perm, object=None):
        return True

    def has_module_perms(self, app_label):
        return True

class ProfileFeed(models.Model):
    feed_user = models.ForeignKey(Account, on_delete= models.CASCADE)
    feed_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add= True)

    class Meta:
        db_table = 'Feed Details'

    def __str__(self):
        return self.feed_text
