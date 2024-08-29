from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Profile, CourseRegistration, ConfirmFees


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'matric_number', 'is_admin', 'is_staff')
    list_filter = ('is_admin', 'is_staff', 'is_superuser')  # Remove 'groups' from here
    search_fields = ('email',)
    ordering = ('email',)
   
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('matric_number',)}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    filter_horizontal = ()

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'current_year_of_study', 'gender', 'created_at')
    search_fields = ('user__email', 'user__matric_number')
    ordering = ('user',)

class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ('name', 'reg_number', 'session', 'current_year_of_study', 'gender')
    search_fields = ('name', 'reg_number')
    ordering = ('session', 'name')

class ConfirmFeesAdmin(admin.ModelAdmin):
    list_display = ('user', 'school_fees_receipt', 'dept_fees_receipt', 'faculty_fees_receipt')
    search_fields = ('user__email', 'user__matric_number')
    ordering = ('user',)

# Register the models in the admin site
admin.site.register(User, UserAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CourseRegistration, CourseRegistrationAdmin)
admin.site.register(ConfirmFees, ConfirmFeesAdmin)