from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm, UserChangeForm
from .models import User

# from input_mask.widgets import InputMask

# admin.site.register(User, auth_admin.UserAdmin)

# class PhoneNumberMask(InputMask):
#     mask = {'phoneNumber': '88 99999-9999'}

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        # ("Campos personalizados", {"fields": ("bio", "phoneNumber")}),
        ("Campos personalizados", {"fields": ("bio",)}),
    )
