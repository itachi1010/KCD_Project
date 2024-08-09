from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, matric_number, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            matric_number=matric_number,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            matric_number='1234',  # Default matriculation number for admins
            email=email,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    matric_number = models.CharField(max_length=20, unique=True, default='1234')
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email and password are required by default

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_year_of_study = models.IntegerField( default='2024')
    gender = models.CharField(max_length=10)
    school_fees_receipt = models.ImageField(upload_to='receipts/')
    dept_fees_receipt = models.ImageField(upload_to='receipts/')
    faculty_fees_receipt = models.ImageField(upload_to='receipts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.matric_number}'s profile"

class CourseRegistration(models.Model):
    session = models.CharField(max_length=20)
    reference_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    current_year_of_study = models.IntegerField()
    gender = models.CharField(max_length=10)

class ConfirmFees(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school_fees_receipt = models.ImageField(upload_to='receipts/')
    dept_fees_receipt = models.ImageField(upload_to='receipts/')
    faculty_fees_receipt = models.ImageField(upload_to='receipts/')
