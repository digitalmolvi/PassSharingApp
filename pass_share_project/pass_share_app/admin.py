from django.contrib import admin
from .models import User, Property, Compound, PassType, PassRequest, Payment, Notification, PropertyOwnerVerification, NationalIDVerification

admin.site.register(User)
admin.site.register(Property)
admin.site.register(Compound)
admin.site.register(PassType)
admin.site.register(PassRequest)
admin.site.register(Payment)
admin.site.register(Notification)
admin.site.register(PropertyOwnerVerification)
admin.site.register(NationalIDVerification)
