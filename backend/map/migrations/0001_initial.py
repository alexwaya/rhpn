# Generated by Django 4.0.4 on 2022-06-03 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=255)),
                ('partner_instituition', models.CharField(max_length=255)),
                ('health_facility_contact', models.CharField(max_length=255)),
                ('district_or_county', models.CharField(max_length=255)),
                ('sub_county', models.CharField(max_length=255)),
                ('mfl_code', models.CharField(max_length=255)),
                ('facility_type', models.CharField(max_length=255)),
                ('level', models.CharField(max_length=255)),
                ('facility_ownership', models.CharField(max_length=255)),
                ('catchment_population', models.CharField(max_length=255)),
                ('wra_population', models.CharField(max_length=255)),
                ('adolescent_population', models.CharField(max_length=255)),
                ('work_with_yfc', models.CharField(max_length=255)),
                ('work_with_yfs', models.CharField(max_length=255)),
                ('work_with_vht_or_chw', models.CharField(max_length=255)),
                ('provide_short_term_fp', models.CharField(max_length=255)),
                ('provide_larc', models.CharField(max_length=255)),
                ('service_provider_trained_and_offering_larc_services', models.CharField(max_length=255)),
                ('provide_permanent_family_planning', models.CharField(max_length=255)),
                ('where_you_refer_on_fp_cases', models.CharField(max_length=255)),
                ('service_provider_trained_and_offering_fp_services', models.CharField(max_length=255)),
                ('provide_pac_medical_abortion', models.CharField(max_length=255)),
                ('provide_pac_manual_evacuation', models.CharField(max_length=255)),
                ('where_you_refer_on_pac_cases', models.CharField(max_length=255)),
                ('service_provider_trained_and_offering_pac_services', models.CharField(max_length=255)),
                ('provide_cervical_screening_services_pap_smear', models.CharField(max_length=255)),
                ('provide_cervical_screening_services_via_or_vili', models.CharField(max_length=255)),
                ('service_provider_trained_and_offering_cervical_screening_services', models.CharField(max_length=255)),
                ('where_you_refer_on_fp_cervical_cancer_screening', models.CharField(max_length=255)),
                ('partners_in_the_area_doing_similar_work', models.CharField(max_length=255)),
                ('partner_in_the_area_working_with', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('attachments_photos_gallery', models.ImageField(default='', upload_to='attachements/')),
                ('other_questions', models.CharField(blank=True, max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Facility',
                'verbose_name_plural': 'Facilities',
            },
        ),
    ]
