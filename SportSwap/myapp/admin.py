from django.contrib import admin
from.models import user
from.models import country
from.models import state
from.models import city
from.models import userprofile
from.models import sportcategory
from.models import equipment
from.models import productcart
from.models import order
from.models import payment
from.models import feedback
from.models import contactus
# Register your models here.
#@admin.register(user)
class DisplayUser(admin.ModelAdmin):
    list_display = ["name", "email", "password", "date_joined"]
admin.site.register(user,DisplayUser)


class DisplayCountry(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(country,DisplayCountry)

class DisplayState(admin.ModelAdmin):
    list_display = ["country", "name"]
admin.site.register(state,DisplayState)

@admin.register(city)
class DisplayCity(admin.ModelAdmin):
    list_display = ["state", "name"]

@admin.register(userprofile)
class DisplayUserprofile(admin.ModelAdmin):
    list_display = ["user", "dob", "address", "phone", "image"]

@admin.register(sportcategory)
class DisplaySportcategory(admin.ModelAdmin):
    list_display = ["catname", "desc"]

@admin.register(equipment)
class DisplayEquipment(admin.ModelAdmin):
    list_display = ["user", "category", "price", "desc", "stock", "image"]

@admin.register(productcart)
class DisplayProductcart(admin.ModelAdmin):
    list_display = ["user", "plant", "price", "quantity", "orderid", "orderstatus"]

@admin.register(order)
class DisplayOrder(admin.ModelAdmin):
    list_display = ["user", "plant", "totalprice", "quantity", "orderdate", "deliverydate", "status"]

@admin.register(payment)
class DisplayPayment(admin.ModelAdmin):
    list_display = ["user", "booking", "amount", "paymentmode", "paymentstatus", "paymentdate"]

@admin.register(feedback)
class DisplayFeedback(admin.ModelAdmin):
    list_display = ["user", "plant", "rating", "comment", "reviewdate"]

@admin.register(contactus)
class DisplayContactus(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "message", "phone", "createdat"]

