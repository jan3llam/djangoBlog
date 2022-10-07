from django.contrib import admin
from .models import Post
from django.contrib.auth.models import User

# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title','author','description','created_at','updated_at')



class UserCustomize(admin.ModelAdmin):
	def group(self, user):
		groups = []
		for group in user.groups.all():
			groups.append(group.name)
		return ' '.join(groups)

	group.short_description = 'Groups'
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'group')


admin.site.register(Post,PostAdmin)
admin.site.unregister(User)
admin.site.register(User,UserCustomize)





