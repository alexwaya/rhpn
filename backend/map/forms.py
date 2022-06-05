from django import forms

from .models import Facility


class FacilityForm(forms.ModelForm):

    class Meta:
        model = Facility
        fields = (

            "location",
            "address",
            
            'facility_name',
            'partner_instituition',
            'health_facility_contact',

            'district_or_county',
            'sub_county',
            'mfl_code',

            'facility_type',
            'level',
            'facility_ownership',

            'catchment_population',
            'wra_population',
            'adolescent_population',

            'work_with_yfc',
            'work_with_yfs',
            'work_with_vht_or_chw',

            'provide_short_term_fp',
            'provide_larc',
            'service_provider_trained_and_offering_larc_services',
            'provide_permanent_family_planning',

            'where_you_refer_on_fp_cases',

            'service_provider_trained_and_offering_fp_services',
            'provide_pac_medical_abortion',
            'provide_pac_manual_evacuation',

            'where_you_refer_on_pac_cases',

            'service_provider_trained_and_offering_pac_services',
            'provide_cervical_screening_services_pap_smear',
            'provide_cervical_screening_services_via_or_vili',
            'service_provide_train_and_offer_cervix_services',

            'where_you_refer_on_fp_cervical_cancer_screening',
            'partners_in_the_area_doing_similar_work',
            'partner_in_the_area_working_with',

            'country',
            'attachments_photos_gallery',
            
            'other_questions',
            
            )