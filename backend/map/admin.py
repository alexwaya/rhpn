from django.contrib import admin
from mapbox_location_field.admin import MapAdmin

from .models import Facility

class FacilityAdmin(admin.ModelAdmin):
    list_display = [
			'facility_name',
            'partner_instituition',
            'health_facility_contact',

            'district_or_county',
            'sub_county',
            'mfl_code',

            'facility_type',
            'level',
            'facility_ownership',
    ]

# class CategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Facility, FacilityAdmin)
#admin.site.register(Category, CategoryAdmin)