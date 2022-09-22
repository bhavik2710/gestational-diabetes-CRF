from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Info_screening_randomization(models.Model):
    patient_id = models.AutoField(primary_key=True)
    crf_filled_by = models.CharField(max_length=300, default="", blank=True,null=True)

    date_crf = models.DateField(default="",blank=True, null=True,)
    place = models.CharField(max_length=300, default="",blank=True, null=True,)
    name = models.CharField(max_length=300, default="",blank=True, null=True,)
    uhid = models.IntegerField(default="",blank=True, null=True,)
    husband_name = models.CharField(max_length=300, default="",blank=True, null=True,)
    contact_number = models.IntegerField(default="",blank=True, null=True,)
    blood_group = models.CharField(max_length=300, default="",blank=True, null=True,)
    age = models.IntegerField(default="",blank=True, null=True,)
    dob = models.DateField(default="",blank=True, null=True,)
    diagnosis = models.CharField(max_length=300, default="",blank=True, null=True,)
    gestation_week = models.IntegerField(blank=True, null=True)
    lmp = models.CharField(max_length=300, default="",blank=True, null=True,)
    pre_preg_weight = models.CharField(max_length=300, default="",blank=True, null=True,)
    height = models.IntegerField(default="",blank=True, null=True,)
    bmi = models.IntegerField(default="",blank=True, null=True,)
    permanent_address = models.CharField(max_length=500, default="",blank=True, null=True,)
    temporary_address = models.CharField(max_length=500, default="",blank=True, null=True,)
    age_18_to_40 = models.CharField(max_length=500, default="",blank=True, null=True,)
    GDM_diagnosis = models.CharField(max_length=100, default="",blank=True, null=True,)
    singleton_gestation = models.CharField(max_length=100, default="",blank=True, null=True,)
    receiving_of_antenatal = models.CharField(max_length=200, default="",blank=True, null=True,)
    use_smartphone = models.CharField(max_length=100, default="",blank=True, null=True,)
    do_not_participate = models.CharField(max_length=100, default="",blank=True, null=True,)
    type1_type1_diabetes = models.CharField(max_length=100, default="",blank=True, null=True,)
    hearing_vision_problem = models.CharField(max_length=100, default="",blank=True, null=True,)
    literacy = models.CharField(max_length=100, default="",blank=True, null=True,)
    group = [('Intervention', 'Intervention'), ('Comparator', 'Comparator')]
    randomization_date = models.DateField(default="",blank=True, null=True,)
    patient_code = models.IntegerField(default="",blank=True, null=True,)
    randomization_to_group = models.CharField(max_length=1000, choices=group,blank=True, null=True,)
    indicate_the_reason = models.CharField(max_length=2000, default="",blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class demographic_data(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    children = [('None', 'None'), ('One', 'One'), ('2 or more', '2 or more')]
    Education = [('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Senior Secondary', 'Senior Secondary')]
    level = [('Diploma', 'Diploma'), ('Graduate', 'Graduate'), ('PostGraduate', 'PostGraduate'),
             ('Doctorate', 'Doctorate')]
    status = [('Working', 'Working'), ('Not-working', 'Not-working')]
    family = [('Nuclear', 'Nuclear'), ('Joint', 'Joint')]
    rel = [('Hindu', 'Hindu'), ('Muslim', 'Muslim'), ('Christian', 'Christian'), ('other', 'other')]
    settings = [('Urban', 'Urban'), ('Rural', 'Rural')]
    travel = [('Private', 'Private'), ('Walk', 'Walk'), ('Public', 'Public'), ('other', 'other')]
    travel_Time = [('<30 min', '<30 min'), ('30 to 60 min', '30 to 60 min'), ('1 to 2hr', '1 to 2hr'),
                   (' >2 hr', ' >2 hr')]
    hospital_Time = [('<30 min', '<30 min'), ('30 to 60 min', '30 to 60 min'), ('1 to 2hr', '1 to 2hr'),
                     (' >2 hr', ' >2 hr')]
    Num_children = models.CharField(max_length=1000, choices=children,blank=True, null=True,)
    Education_level = models.CharField(max_length=1000, choices=level,blank=True, null=True,)
    occuption_status = models.CharField(max_length=1000, choices=status,blank=True, null=True,)
    occuption_specify = models.CharField(max_length=2000, default="",blank=True, null=True,)
    family_type = models.CharField(max_length=1000, choices=family,blank=True, null=True,)
    religion = models.CharField(max_length=1000, choices=rel,blank=True, null=True,)
    Residence = models.CharField(max_length=1000, choices=settings,blank=True, null=True,)
    mode_of_travel = models.CharField(max_length=1000, choices=travel,blank=True, null=True,)
    public_mode_specify = models.CharField(max_length=2000, default="",blank=True, null=True,)
    time_to_travel = models.CharField(max_length=1000, choices=travel_Time,blank=True, null=True,)
    avg_timein_hospital = models.CharField(max_length=1000, choices=hospital_Time,blank=True, null=True,)
    occupation_head = [('10', 'Legislators, Senior Officials & Managers'), ('9', 'Professionals'),
                           ('8', 'Technicians and Associate Professionals'), ('7', 'Clerks'),
                           ('6', 'Skilled Workers and Shop & Market Sales Workers'),
                           ('5', 'Skilled Agricultural & Fishery Workers'), ('4', 'Craft & Related Trade Workers'),
                           ('3', 'Plant & Machine Operators and Assemblers'), ('2', 'Elementary Occupation'),
                           ('1', 'Unemployed')]
    head_of_family = models.CharField(max_length=2000, choices=occupation_head,blank=True, null=True,)
    education_head = [('7', 'Profession or Honours'), ('6', 'Graduate'), ('5', 'Intermediate or diploma'),
                          ('4', 'High school certificate'), ('3', 'Middle school certificate'),
                          ('2', 'Primary school certificate Illiterate'), ('1', 'Illiterate')]
    education_of_family = models.CharField(max_length=2000, choices=education_head,blank=True, null=True,)
    income_family = [('12', '≥ 199,862'), ('10', '99,931–199,861'), ('6', '74,756 –99,930'), ('4', '49,962–74,755'),
                         ('3', '29,973– 49,961'), ('2', '10,002–29,972'), ('1', '≤ 10,001')]
    income = models.CharField(max_length=2000, choices=income_family,blank=True, null=True,)
    socio_economic = [('26-29', 'Upper (I)'), ('16-25', 'Upper Middle (II'), ('11-15', 'Lower Middle (III)'),
                          ('5-10', 'Upper Lower (IV)'), ('<5 Lower', 'Lower (V)')]
    economic = models.CharField(max_length=2000, choices=socio_economic,blank=True, null=True,)

    def __str__(self):
         return str(self.patient_id)

class Maternal_detail(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Maternal_age = models.IntegerField(default="",blank=True, null=True,)
    Mcatogery = [('Sedentary', 'Sedentary'), ('Moderate', 'Moderate'), ('Heavy', 'Heavy')]
    Nulli = [('Yes', 'Yes'), ('No', 'No')]
    fasting = [('IADPSG', 'IADPSG'), ('DIPSI', 'NoDIPSI')]
    LMP = models.CharField(max_length=1000, default="",blank=True, null=True,)
    date_of_diagnosis = models.DateField(default="",blank=True, null=True,)
    no_of_pregnancy = models.IntegerField(default="",blank=True, null=True,)
    gestation_week = models.IntegerField(default="",blank=True, null=True,)
    category = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    age_at_menarche = models.IntegerField(default="",blank=True, null=True,)
    gravidity = models.CharField(max_length=2000, default="",blank=True, null=True,)
    nulliparity = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    chronic_hypertension = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    family_history = models.CharField(max_length=1000, default="",blank=True, null=True,)
    self_medical_history = models.CharField(max_length=1000, default="",blank=True, null=True,)
    thrombophilia = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    Assisted_reproductive_technology = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    Assisted_reproductive_specify = models.CharField(max_length=1000, default="",blank=True, null=True,)
    previous_caesarean_case = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    previous_GDM = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    family_history_DM = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    F_history_hypertension = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    fasting_glucose_1_trim = models.IntegerField(default="",blank=True, null=True,)
    Glucose_test = models.CharField(max_length=1000, choices=fasting,blank=True, null=True,)
    OGTT_fasting = models.IntegerField(default="",blank=True, null=True,)
    OGTT_60min = models.IntegerField(default="",blank=True, null=True,)
    OGTT_120min = models.IntegerField(default="",blank=True, null=True,)
    smoking = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    smoking_frequency = models.CharField(max_length=1000, default="",blank=True, null=True,)
    alcohol = models.CharField(max_length=2000, choices=Nulli,blank=True, null=True,)
    alcohol_frequency = models.CharField(max_length=2000, default="",blank=True, null=True,)
    tobacco = models.CharField(max_length=2000, choices=Nulli,blank=True, null=True,)
    tobacco_frequency = models.CharField(max_length=2000, default="",blank=True, null=True,)
    physical_exercise = models.CharField(max_length=2000, choices=Nulli,blank=True, null=True,)
    physical_frequency = models.CharField(max_length=2000, default="",blank=True, null=True,)
    yoga = models.CharField(max_length=1000, choices=Nulli,blank=True, null=True,)
    yoga_frequency = models.CharField(max_length=1000, default="",blank=True, null=True,)
    meditation = models.CharField(max_length=2000, choices=Nulli,blank=True, null=True,)
    meditation_frequency = models.CharField(max_length=2000, default="",blank=True, null=True,)
    walking = models.CharField(max_length=2000, choices=Nulli,blank=True, null=True,)
    walking_frequency = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Drug = models.TextField(default="",blank=True, null=True,)
    Dose = models.TextField(default="",blank=True, null=True,)
    Timings = models.TextField(default="",blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class Bio_chemical_profile(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Hemoglobin = models.CharField(max_length=2000, default="",blank=True, null=True,)
    HbA1c = models.CharField(max_length=2000, default="",blank=True, null=True,)
    TSH_uIU = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Blood = models.CharField(max_length=2000, default="",blank=True, null=True,)
    urea = models.CharField(max_length=2000, default="",blank=True, null=True,)
    HIV = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Anti = models.CharField(max_length=2000, default="",blank=True, null=True,)
    HCV = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Antibodies_COI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    HBS = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Antigen_COI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VDRL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    HPLC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Urine = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Routine = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Colour = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Reaction = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Sp_Gravity = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Protein = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Sugar = models.CharField(max_length=2000, default="",blank=True, null=True,)
    MICROSCOPIC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    RBC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    WBC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Epithelial = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Cells = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Bacteria = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Granular = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Ca_Oxalate = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Tripple_Phosphate = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Phosphate = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Amorphous = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Urate = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Uric_Acid = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Yeast = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Mucus = models.CharField(max_length=2000, default="",blank=True, null=True,)
    SPECIAL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Ketones = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Bile_Salts = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Hb = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Hematocrit = models.CharField(max_length=2000, default="",blank=True, null=True,)
    RedBC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    WhiteBC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Platelet = models.CharField(max_length=2000, default="",blank=True, null=True,)
    MCV = models.CharField(max_length=2000, default="",blank=True, null=True,)
    MCH = models.CharField(max_length=2000, default="",blank=True, null=True,)
    MCHC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    RDW_CV = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Neutro = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Lympho = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Eosino = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Mono = models.CharField(max_length=2000, default="",blank=True, null=True,)
    NRBC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Baso = models.CharField(max_length=2000, default="",blank=True, null=True,)
    NeutroAbsl = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Lympho_Abs = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Eosino_Abs = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Mono_Abs = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Baso_Urea = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Creatinine = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Uric_Acid = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Calcium = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Phosphorus = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Sodium = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Potassium = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Chloride = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Bilirubin_T = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Bilirublin_D = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Bilirubin_I = models.CharField(max_length=2000, default="",blank=True, null=True,)
    ALT = models.CharField(max_length=2000, default="",blank=True, null=True,)
    AST = models.CharField(max_length=2000, default="",blank=True, null=True,)
    ALP = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Total_protein = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Albumin = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Globulin = models.CharField(max_length=2000, default="",blank=True, null=True,)
    A_G_ratio = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Vitamin_D3 = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Iron = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Transferrin = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Ferritin = models.CharField(max_length=2000, default="",blank=True, null=True,)
    TIBC = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Vitamin_B12 = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Serum_Folate = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Lipid_Profile = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Total_Cholesterol = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Triglycerides = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VLDL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    LDL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    HDL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    CHOL_HDL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    LDL_HDL = models.CharField(max_length=2000, default="",blank=True, null=True,)
    def __str__(self):
        return str(self.patient_id)

class weight_monitor(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Period_gestation = [('Week 24', 'Week 24'), ('Week 25', 'Week 25'), ('Week 26', 'Week 26'), ('Week 27', 'Week 27'),
                         ('Week 28', 'Week 28'), ('Week 29', 'Week 29'), ('Week 30', 'Week 30'), ('Week 31', 'Week 31'),
                         ('Week 32', 'Week 32'), ('Week 33', 'Week 33'), ('Week 34', 'Week 34'), ('Week 35', 'Week 35'),
                         ('Week 36', 'Week 36'), ('Week 37', 'Week 37')]
    Pweight = models.CharField(max_length=2000, choices=Period_gestation,blank=True, null=True,)
    Patient_Weight = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Remarks = models.TextField(default="",blank=True, null=True,)

    def __str__(self):
        return self.patient_id

class Dietary_Data(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Meal_time = models.DateTimeField(default="",blank=True, null=True,)
    Food_consumed = models.ImageField(upload_to='images/', null=True, default="", blank=True, )
    Quantity = models.TextField(max_length=2000, default="",blank=True, null=True,)
    Date = models.DateField(default="",blank=True, null=True,)
    weekday = models.CharField(max_length=2000, default="",blank=True, null=True,)
    weekend = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Glycemic_index = models.TextField(default="",blank=True, null=True,)
    Glycemic_load = models.TextField(default="",blank=True, null=True,)
    nutri_supplements = models.TextField(default="",blank=True, null=True,)
    Multivitimins = models.TextField(default="",blank=True, null=True,)
    RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    actual_intake = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Excess_Deficit = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Energy_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Protein_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    CHO_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Fat_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Calcium_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Iron_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Zinc_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Magnesium_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Retinol_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    B_Carotene_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Thiamin_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Riboflavin_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Niacin_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VitaminB6_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Ascorbic_acid_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Dietray_folate_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VitaminB12_RDA = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Energy_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Protein_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    CHO_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Fat_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Calcium_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Iron_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Zinc_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Magnesium_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Retinol_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    B_Carotene_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Thiamin_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Riboflavin_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Niacin_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VitaminB6_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Ascorbic_acid_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Dietray_folate_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VitaminB12_AI = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Energy_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Protein_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    CHO_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Fat_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Calcium_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Iron_ED = models.CharField(max_length=2000, default="")
    Zinc_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Magnesium_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Retinol_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    B_Carotene_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Thiamin_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Riboflavin_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Niacin_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VitaminB6_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Ascorbic_acid_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Dietray_folate_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    VitaminB12_ED = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Nutritional_Supplements = models.TextField(default="",blank=True, null=True,)
    Multivitamin = models.TextField(default="",blank=True, null=True,)
    food_choice = [('Vegetarian', 'Vegetarian'),
                   ('Non-vegetarian', 'Non-vegetarian'), ('Ovo-vegetarian', 'Ovo-vegetarian')]
    Fchoice = models.CharField(max_length=2000, choices=food_choice,blank=True, null=True,)
    consumed_meal = [('Early', 'Early'), ('Breakfast', 'Breakfast'), ('Mid-morning', 'Mid-morning'),
                     ('Lunch', 'Lunch'),
                     ('Evening snack', 'Evening snack'), ('Dinner', 'Dinner'), ('Post-dinner', 'Post-dinner')]
    weekdays = models.CharField(max_length=2000, choices=consumed_meal,blank=True, null=True,)
    weekends = models.CharField(max_length=2000, choices=consumed_meal,blank=True, null=True,)
    often_consume = [('Everyday', 'Everyday'),
                     ('4-5 times a week', '4-5 times a week'), ('2-3 times a week', '2-3 times a week'),
                     ('Once a week', 'Once a week'), ('Once a month', 'Once a month')]
    Q3 = models.CharField(max_length=2000, choices=often_consume,blank=True, null=True,)
    food_place = [('Daily', 'Daily'),
                  ('Frequently', 'Frequently'), ('Occasionally', 'Occasionally'), ('Never', 'Never')]
    Street_Hawker = models.CharField(max_length=2000, choices=food_place,blank=True, null=True,)
    Restaurant = models.CharField(max_length=2000, choices=food_place,blank=True, null=True,)
    Food_Courts = models.CharField(max_length=2000, choices=food_place,blank=True, null=True,)
    Dhabas = models.CharField(max_length=2000, choices=food_place,blank=True, null=True,)
    Office_canteen = models.CharField(max_length=2000, choices=food_place,blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)


class P_sleep_quality_index(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Date = models.DateField(default="",blank=True, null=True,)
    Clock = models.DateTimeField(default="",blank=True, null=True,)
    POG = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Subj_Code = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Sleep_duration = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Q1 = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Q2 = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Q3 = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Q4 = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Q5a_choice = [('Not during the past month', 'Not during the past month'),
          ('Less than once a week', 'Less than once a week'), ('Once or twice a week', 'Once or twice a week'),
          ('Three or more times a week', 'Three or more times a week')]
    Q5a = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5b = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5c = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5d = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5e = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5f = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5g = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5h = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5i = models.CharField(max_length=2000, choices=Q5a_choice,blank=True, null=True,)
    Q5j = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Q6_choice = [('Not during the past month', 'Not during the past month'),
                  ('Less than once a week', 'Less than once a week'), ('Once or twice a week', 'Once or twice a week'), ('Three or more times a week', 'Three or more times a week')]
    Q6 = models.CharField(max_length=2000, choices=Q6_choice,blank=True, null=True,)
    Q7 = models.CharField(max_length=2000, choices=Q6_choice,blank=True, null=True,)
    Q8_choice = [('No problem at all', 'No problem at all'),
                 ('Only a very slight problem', 'Only a very slight problem'), ('Somewhat of a problem', 'Somewhat of a problem'),
                 ('A very big problem', 'TA very big problem')]
    Q8 = models.CharField(max_length=2000, choices=Q8_choice,blank=True, null=True,)
    Q9_choice=[('Very good', 'Very good'),
                 ('Fairly good', 'Fairly good'), ('Fairly bad', 'Fairly bad'),
                 ('Very bad', 'Very bad')]
    Q9 = models.CharField(max_length=2000, choices=Q9_choice,blank=True, null=True,)
    Q10_choice = [('No bed partner or room mate', 'No bed partner or room mate'),
                 ('Partner/roommate in other room', 'Partner/roommate in other room'), ('Partner in same room but not same bed', 'Partner in same room but not same bed'),
                 ('Partner in same bed', 'Partner in same bed')]
    Q10 = models.CharField(max_length=2000, choices=Q10_choice,blank=True, null=True,)
    Q10a_choice = [('Not during the past month', 'Not during the past month'),
                  ('Less than once a week', 'Less than once a week'),
                  ('Once or twice a week', 'Once or twice a week'),
                  ('Three or more times a week', 'Three or more times a week')]
    Q10a= models.CharField(max_length=2000, choices=Q10a_choice,blank=True, null=True,)
    Q10b = models.CharField(max_length=2000, choices=Q10a_choice,blank=True, null=True,)
    Q10c = models.CharField(max_length=2000, choices=Q10a_choice,blank=True, null=True,)
    Q10d = models.CharField(max_length=2000, choices=Q10a_choice,blank=True, null=True,)
    Q10e = models.CharField(max_length=2000, choices=Q10a_choice,blank=True, null=True,)
    Q10f = models.CharField(max_length=2000, choices=Q10a_choice,blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class EPDS(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Date = models.DateField(default="",blank=True, null=True,)
    POG = models.CharField(max_length=2000, default="")
    Subj_Code = models.CharField(max_length=2000, default="")
    General_health = [('1', 'Excellent'), ('2', 'Professionals'),
                       ('3', 'Good'), ('4', 'Fair'),
                       ('5', 'Poor')]
    Ghealth = models.CharField(max_length=2000, choices=General_health,blank=True, null=True,)
    year_health = [('1', 'Much better now than one year ago'), ('2', 'Graduate'), ('3', 'Somewhat better now than one year ago'),
                      ('4', 'About the same'), ('5', 'Somewhat worse now than one year ago'),
                      ('5', 'Much worse now than one year ago')]
    year = models.CharField(max_length=2000, choices=year_health)
    Limitations_activity =[('1', 'Yes, Limited a Lot (1)'), ('2', 'Yes, Limited a Little (2)'),('3', 'No, Not limited at All (3)')]
    q1 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q2 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q3 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q4 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q6 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q7 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q8 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q9 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)
    q10 = models.CharField(max_length=2000, choices=Limitations_activity,blank=True, null=True,)

    Physical_Problems =  [('1', 'Yes'), ('2', 'No')]
    q11 = models.CharField(max_length=2000, choices=Physical_Problems,blank=True, null=True,)
    q12 = models.CharField(max_length=2000, choices=Physical_Problems,blank=True, null=True,)
    q13 = models.CharField(max_length=2000, choices=Physical_Problems,blank=True, null=True,)
    Emotional_Problems = [('1', 'Yes'), ('2', 'No')]
    q14 = models.CharField(max_length=2000, choices=Physical_Problems,blank=True, null=True,)
    q15 = models.CharField(max_length=2000, choices=Physical_Problems,blank=True, null=True,)
    q16 = models.CharField(max_length=2000, choices=Physical_Problems,blank=True, null=True,)
    Social_activity = [('1', 'Not at all'), ('2', 'Slightly'),
                       ('3', 'Moderately'), ('4', 'Quite a bit'),
                       ('5', 'Extremely')]
    q20 = models.CharField(max_length=2000, choices=Social_activity,blank=True, null=True,)
    P_body_pain = [('1', 'None'), ('2', 'Very mild'),
                       ('3', 'Mild'), ('4', 'Moderate'),
                       ('5', 'Severe'), ('6', 'Very severe')]
    Q21 = models.CharField(max_length=2000, choices=P_body_pain,blank=True, null=True,)
    D_body_pain = [('1', 'Not at all'), ('2', 'A little bit'),
                 ('3', 'Moderately'), ('4', 'Quite a bit'),
                 ('5', 'Extremely')]
    Q22 = models.CharField(max_length=2000, choices=D_body_pain ,blank=True, null=True,)
    Energy_emotion = [('1', 'All of the Time'), ('2', 'Most of the Time'),
                   ('3', 'A Good Bit of the Time'), ('4', 'Some of the Time'),('5', 'A Little of the Time'), ('6', 'None of the Time')]
    Q23 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q24 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q25 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q26 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q27 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q28 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q29 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q30 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Q31 = models.CharField(max_length=2000, choices=Energy_emotion,blank=True, null=True,)
    Social_activity = [('1', 'All of the time'), ('2', 'Most of the time'),
                   ('3', 'Some of the time'), ('4', 'A little of the time'),
                   ('5', 'None of the time')]
    Q31 = models.CharField(max_length=2000, choices=Social_activity,blank=True, null=True,)
    GH = [('1', 'Definitely True'), ('2', 'Mostly True'),('3', 'Do not Know'),('4','Mostly false'),('5','Definitely false')]
    Q32 = models.CharField(max_length=2000, choices=GH,blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class daily_Glucose_level_insuline(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Gweek = models.IntegerField(default="",blank=True, null=True,)
    Date = models.DateField(default="",blank=True, null=True,)
    Timing = models.DateTimeField(default="",blank=True, null=True,)
    at_2am = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Pre_Breakfast = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Pre_Lunch = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Pre_Dinner = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Post_Breakfast = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Post_Lunch = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Post_Dinner = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Pre_time_break = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Pre_time_lun = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Pre_time_Dinner = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Post_time_break = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Post_time_lun = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Post_time_Dinner = models.CharField(max_length=2000, default="", blank=True, null=True, )
    blood_sugar = models.CharField(max_length=2000, default="", blank=True, null=True, )
    Insuline = models.CharField(max_length=2000, default="",blank=True, null=True,)
    actual_level = models.CharField(max_length=2000, default="",blank=True, null=True,)
    instructed_level = models.CharField(max_length=2000, default="",blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class daily_Glucose_level_drug(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Gweek = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Target = models.CharField(max_length=2000, default="",blank=True, null=True,)
    only_diet = models.CharField(max_length=2000, default="",blank=True, null=True,)
    drug_diet = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Date = models.DateField(default="",blank=True, null=True,)
    Fasting = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Post_Breakfast = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Post_Lunch = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Post_Dinner = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Note = models.TextField(default="",blank=True, null=True,)
    actual_level = models.CharField(max_length=2000, default="",blank=True, null=True,)
    instructed_level = models.CharField(max_length=2000, default="",blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)


class daily_BP(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Gweek = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Target = models.CharField(max_length=2000, default="",blank=True, null=True,)

    Date = models.DateTimeField(default="",blank=True, null=True,)
    Morning_Systolic = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Afternoon_Systolic = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Evening_Systolic = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Morning_Diastolic = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Afternoon_Diastolic = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Evening_Diastolic = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Morning_Pulse = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Afternoon_Pulse = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Evening_Pulse = models.CharField(max_length=2000, default="",blank=True, null=True,)
    actual_level = models.CharField(max_length=2000, default="", blank=True, null=True, )
    instruct_level = models.CharField(max_length=2000, default="", blank=True, null=True, )


    def __str__(self):
        return str(self.patient_id)

class Physical_exercise(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Date = models.DateField(default="",blank=True, null=True,)
    Timing= models.DateTimeField(default="",blank=True, null=True,)
    Gweek = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Breathing = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Leg_movement = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Pelvic_Exercise = models.CharField(max_length=2000, default="",blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class Delivery_and_Neonatal(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    time = [('Full term birth', 'Full term birth'), ('Pre-term birth', 'Pre-term birth')]
    Delivery_mode = [('Caesarean Section', 'Caesarean Section'), ('Vaginally Delivery', 'Vaginally Delivery'), ('Forcep Delivery', 'Forcep Delivery')]
    Choice = [('Yes', 'Yes'), ('No', 'No')]
    time_select = models.CharField(max_length=1000, choices=time,blank=True, null=True,)
    Delivery = models.CharField(max_length=1000, choices=Choice,blank=True, null=True,)
    Shoulder_dystocia = models.CharField(max_length=1000, choices=Choice,blank=True, null=True,)
    Postpartum_hemorrhage = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Antenatal_corticosteroids = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Gestational_hypertension = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Preeclampsia = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Polyhydramnios = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Induction_of_labour = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Caesarean_section = models.CharField(max_length=2000,  default="",blank=True, null=True,)
    Gestational_age = models.CharField(max_length=2000,  default="",blank=True, null=True,)
    Spontaneous_abortion = models.CharField(max_length=2000,  default="",blank=True, null=True,)
    Miscarriage = models.CharField(max_length=2000, default="",blank=True, null=True,)
    Other = models.CharField(max_length=2000, default="",blank=True, null=True,)
    birth_weight= models.IntegerField(default="",blank=True, null=True,)
    Apgar_score = models.CharField(max_length=2000, default="",blank=True, null=True,)
    weight_baby = [('Normal', 'Normal'), ('LBW', 'LBW'), ('VLBW', 'VLBW'), ('Macrosomia', 'Macrosomia')]
    Choice = [('Yes', 'Yes'), ('No', 'No')]
    w1 = models.CharField(max_length=2000, choices=weight_baby,blank=True, null=True,)
    Gestational_age2 = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Neonatal = models.IntegerField(default="",blank=True, null=True,)
    NICU = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    New_born = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Respiratory = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Phototherapy = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)
    Neonatal_death = models.CharField(max_length=2000, choices=Choice,blank=True, null=True,)

    def __str__(self):
        return str(self.patient_id)

class Feedback_forms(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    Info_screening_randomization = models.ForeignKey(Info_screening_randomization, max_length=200, blank=True,
                                                     null=True, on_delete=models.CASCADE)

    Statement1 = [('Agree', 'Agree'), ('Disagree', 'Disagree')]
    S1 = models.CharField(max_length=2000, choices=Statement1,blank=True, null=True,)
    S2 = models.CharField(max_length=2000, choices=Statement1,blank=True, null=True,)
    S3= models.CharField(max_length=2000, choices=Statement1,blank=True, null=True,)
    S4 = models.CharField(max_length=2000, choices=Statement1,blank=True, null=True,)
    S5 = models.CharField(max_length=2000, choices=Statement1,blank=True, null=True,)
    S6 = models.CharField(max_length=2000, choices=Statement1, blank=True, null=True,)
    Statement2 = [('Delhi', 'Delhi'), ('Ballabhgarh', 'Ballabhgarh')]
    C1 = models.CharField(max_length=2000, choices=Statement2, blank=True, null=True, )
    C2 = models.CharField(max_length=2000, choices=Statement2, blank=True, null=True, )
    C3 = models.CharField(max_length=2000, choices=Statement2, blank=True, null=True, )
    Statement3 = [('Agree', 'Agree'), ('Neutral', 'Neutral'), ('Disagree', 'Disagree')]
    D1 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )
    D2 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )
    D3 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )
    D4 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )
    D5 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )
    D6 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )
    D7 = models.CharField(max_length=2000, choices=Statement3, blank=True, null=True, )


    def __str__(self):
        return str(self.patient_id)


















