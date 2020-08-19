from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    website = models.CharField(max_length=250)

class Adress(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    suite = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    lat = models.FloatField()
    lng = models.FloatField()

class Company(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    catchPhrase = models.CharField(max_length=250)
    bs = models.CharField(max_length=250)

class Posts(models.Model):
    post_id = models.IntegerField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    username = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.CharField(max_length=250)
    def __srt__(self):
        data = [self.post_id, self.user_id, self.title, self.body]
        return data