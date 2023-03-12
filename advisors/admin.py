from django.contrib import admin
from .models import AdvisorUserProfile


@admin.register(AdvisorUserProfile)
class AdvisorAdmin(admin.ModelAdmin):
    """
    Create action to approve advisor.
    Choose fields to display at preview level.
    """
    actions = [
        'approve_advisor',
        'not_approve_advisor'
        ]

    list_display = ('business_name', 'user', 'approved')

    def approve_advisor(self, request, queryset):
        queryset.update(approved=1)

    def not_approve_advisor(self, request, queryset):
        queryset.update(approved=2)
