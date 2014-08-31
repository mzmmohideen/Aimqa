from valuation import models as valuation_models
from django.contrib import admin
from django.db.models.base import ModelBase
from valuation.models import Family,FamilyMember,Class
import datetime
# Very hacky!

# admin.site.register(Family)
# admin.site.register(FamilyMember)
# admin.site.register(Class)



for name, var in valuation_models.__dict__.items():
    if type(var) is ModelBase:
        admin.site.register(var)


# from django.contrib import admin



# # admin.site.register(Attendace)

# # Register your models here.
