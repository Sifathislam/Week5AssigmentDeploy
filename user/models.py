from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserAccount(models.Model):
     user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
     balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
     def __str__(self):
        return str(self.user.first_name)


class publisherInfo(models.Model):
    image = models.ImageField(upload_to='user/media/uploads', height_field=None, width_field=None, max_length=None,default='')
    user = models.OneToOneField(UserAccount, on_delete=models.CASCADE, related_name='publisherAccount')
    spaciality = models.CharField(max_length=150)
    about = models.TextField()
    soldBookCount = models.IntegerField(null = True, blank = True, default='0')
    adminPermission = models.BooleanField(null = True, blank = True, default = False)

    def __str__(self):
        return str(self.user.user.first_name)