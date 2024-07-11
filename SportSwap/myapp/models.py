from django.db import models
from django.utils.safestring import mark_safe


# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=16)
    date_joined = models.DateField()

    def __str__(self):
        return self.name


class country(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class state(models.Model):
    country = models.ForeignKey(country, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class city(models.Model):
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)


class userprofile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    dob = models.DateField()
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="userprofile")

    def userimage(self):
        return mark_safe('<img src="{}" width="100"/>'.format(self.image.url))

class sportcategory(models.Model):
    catname = models.CharField(max_length=20)
    desc = models.CharField(max_length=30)

class equipment(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    category = models.ForeignKey(sportcategory, on_delete=models.CASCADE)
    price = models.IntegerField()
    desc = models.CharField(max_length=40)
    stock = models.IntegerField()
    image = models.ImageField(upload_to="equipment")

    def __str__(self):
        return self.name


class productcart(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    plant = models.ForeignKey(equipment, on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField()
    orderid = models.IntegerField()
    orderstatus = models.IntegerField()

class order(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    plant = models.ForeignKey(equipment, on_delete=models.CASCADE)
    totalprice = models.IntegerField()
    quantity = models.IntegerField()
    orderdate = models.DateField()
    deliverydate = models.DateField()
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('shipped', 'Shipped'),('delivered', 'Delivered')], default='pending')

    def __str__(self):
        return self.name

class payment(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    booking = models.ForeignKey(order, on_delete=models.CASCADE)
    amount = models.IntegerField()
    paymentmode = models.CharField(max_length=10)
    paymentstatus = models.CharField(max_length=50, choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'),
    ('paypal', 'PayPal'), ('other', 'Other')])
    paymentdate = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'),
    ('failed', 'Failed')], default='pending')


class feedback(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    plant = models.ForeignKey(equipment, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.CharField(max_length=100)
    reviewdate = models.DateField()


class contactus(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    createdat = models.CharField(max_length=10)

