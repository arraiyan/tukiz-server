from django.contrib import admin
from .models import post
from .models import profile
from .models import comment
from .models import postphotos
from .models import postbody
# Register your models here.

admin.site.register(post)
admin.site.register(profile)
admin.site.register(comment)
admin.site.register(postphotos)
admin.site.register(postbody)