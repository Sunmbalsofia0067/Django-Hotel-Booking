from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save


class UserManager(BaseUserManager):

    def create_user(self, email, full_name, phone_no, password=None):
        if not email:
            raise ValueError("Email field is required!")
        user = self.model(
            email = self.normalize_email(email),
            full_name = full_name,
            phone_no = phone_no
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_staffuser(self, email, password):
        user = self.model(
            email = email,
            password = password
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.model(
            email = email,
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=255, unique=True, verbose_name='email address')
    phone_no = models.CharField(max_length=30, default='')


    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
         return True
    
    def has_module_perms(self, app_label):
     return True




    Objects = UserManager()


class ProfileManager(models.Manager):
    pass

class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)

    card_holder_name = models.CharField(max_length=100, blank=True, null=True)
    card_number = models.CharField(max_length=100, blank=True, null=True)
    cvv = models.CharField(max_length=10, blank=True, null=True)
    card_expiry = models.CharField(max_length=100, blank=True, null=True)
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    billing_address2 = models.CharField(max_length=255, blank=True, null=True)
    billing_city = models.CharField(max_length=100, blank=True, null=True)
    billing_state = models.CharField(max_length=100, blank=True, null=True)
    billing_zip = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.email

def createProfile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.created(user=kwargs['instance'])

        post_save.connect(createProfile, sender=User)