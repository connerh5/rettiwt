from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Rett

#unregister
admin.site.unregister(Group)

#mix prof and user
class ProfileInline(admin.StackedInline):
    model = Profile

#extned useer
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]
    #unregister users
admin.site.unregister(User)

admin.site.register(User, UserAdmin)



#mix prof and user
class ProfileInline(admin.StackedInline):
    model = Profile

admin.site.register(Rett)