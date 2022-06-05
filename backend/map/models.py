from django.db import models
from mapbox_location_field.models import LocationField, AddressAutoHiddenField


from staff.models import CustomUser

class Facility(models.Model):
    location = LocationField(
        map_attrs={"style": "mapbox://styles/mightysharky/cjwgnjzr004bu1dnpw8kzxa72", "center": [-1.292066, 36.821946], "marker_color": "blue"})
    address = AddressAutoHiddenField()

    facility_name = models.CharField(max_length=255) #Facility Name (Open-ended)
    partner_instituition = models.CharField(max_length=255) #Partner Institution (Open-ended)
    health_facility_contact = models.CharField(max_length=255) #Health Facility Contact (Open-ended)

    district_or_county = models.CharField(max_length=255) #District/ County (Open-ended)
    sub_county = models.CharField(max_length=255) #Sub County (Open-ended)
    mfl_code = models.CharField(max_length=255) #MFL Code (Open-ended)

    facility_type = models.CharField(max_length=255) #Facility Type (Drop down)
    level = models.CharField(max_length=255) #Level (Drop down)
    facility_ownership = models.CharField(max_length=255) # Facility Ownership (Drop down)

    catchment_population = models.CharField(max_length=255) #Catchment Population (Open-ended)
    wra_population = models.CharField(max_length=255) #WRA Population (15-49 yrs) (Open-ended)
    adolescent_population = models.CharField(max_length=255) #Adolescent Population (10-24yrs) (Open-ended)

    work_with_yfc = models.CharField(max_length=255) #Do you work with a YFC? (Drop down)
    work_with_yfs = models.CharField(max_length=255) #Do you work with YFS? (Drop down)
    work_with_vht_or_chw = models.CharField(max_length=255) #Do you work with VHT/ CHW? (Drop down)

    provide_short_term_fp = models.CharField(max_length=255) #Do you provide short term FP? (Drop down)
    provide_larc = models.CharField(max_length=255) #Do you provide LARC? (Drop down)
    service_provider_trained_and_offering_larc_services = models.CharField(max_length=255) #Service provider trained and offering LARC services? (Drop down)
    provide_permanent_family_planning = models.CharField(max_length=255) #Provision of permanent family planning methods? (Drop down)

    where_you_refer_on_fp_cases = models.CharField(max_length=255) #Where do you refer on FP cases? (Open-ended)

    service_provider_trained_and_offering_fp_services = models.CharField(max_length=255) #Service provider trained and offering FP services?
    provide_pac_medical_abortion = models.CharField(max_length=255) #Do you provide PAC medical abortion?
    provide_pac_manual_evacuation = models.CharField(max_length=255) #Do you provide PAC manual evacuation?

    where_you_refer_on_pac_cases = models.CharField(max_length=255) #Where do you refer on PAC cases? (Open-ended)

    service_provider_trained_and_offering_pac_services = models.CharField(max_length=255) #Service provider trained and offering PAC services? (Drop down)
    provide_cervical_screening_services_pap_smear = models.CharField(max_length=255) # Do you provide cervical screening services (Pap Smear)? (Drop down)
    provide_cervical_screening_services_via_or_vili = models.CharField(max_length=255) #Do you provide cervical screening services (VIA/VILI)? (Drop down)
    service_provide_train_and_offer_cervix_services = models.CharField(max_length=255) # Service provider trained and offering cervical screening services? (Drop down)

    where_you_refer_on_fp_cervical_cancer_screening = models.CharField(max_length=255) # Where do you refer on cervical cancer screening cases? (Open-ended)
    partners_in_the_area_doing_similar_work = models.CharField(max_length=255) #Names of partners in the area doing similar work (Open-ended)
    partner_in_the_area_working_with = models.CharField(max_length=255) #Name of the partner in the area you are working with (Open-ended

    country = models.CharField(max_length=255) #Country (Drop down)
    attachments_photos_gallery = models.ImageField(upload_to='attachements/', default='') # Attachments (Photos from Camera or Gallery)

    other_questions = models.CharField(max_length=255, blank=True)

    #staff = models.ForeignKey(CustomUser, related_name='posts', on_delete=models.CASCADE)
    
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    #categories = models.CharField(max_length=255, default='')

    class Meta:
        verbose_name = "Facility"
        verbose_name_plural = "Facilities"

    def __str__(self):
        return self.facility_name