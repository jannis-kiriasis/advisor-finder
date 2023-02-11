from django.contrib import admin
from .models import AdvisorUserProfile


@admin.register(AdvisorUserProfile)
class AdvisorAdmin(admin.ModelAdmin):

    actions = [
        'approve_advisor',
        'not_approve_advisor'
        ]

    def approve_advisor(self, request, queryset):
        queryset.update(approved=1)

    def not_approve_advisor(self, request, queryset):
        queryset.update(approved=2)
