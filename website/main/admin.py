from django.contrib import admin
from .models import Post,UserGroup
from django.contrib.auth.models import User,Group

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','description','created_at','updated_at')




admin.site.register(Post,PostAdmin)



