from django.db import models
from django.utils import timezone



class Info(models.Model):
    patient_id = models.AutoField(primary_key=True)
    crf_filled_by = models.CharField(max_length=300, default="", )
    date_crf = models.DateField()
    Location = models.CharField(max_length=300, default="")
    name = models.CharField(max_length=300, default="")
    uhid = models.IntegerField()
    husband_name = models.CharField(max_length=300, default="")
    contact_number = models.IntegerField()
    blood_group = models.CharField(max_length=300, default="")
    age = models.IntegerField()
    dob = models.DateField()
    diagnosis = models.CharField(max_length=300, default="")
    gestation_week = models.IntegerField()
    lmp = models.CharField(max_length=300, default="")
    pre_preg_weight = models.CharField(max_length=300, default="")
    height = models.IntegerField()
    bmi = models.IntegerField()
    permanent_address = models.CharField(max_length=500, default="")
    temporary_address = models.CharField(max_length=500, default="")
    def __str__(self):
        return str(self.patient_id)


class Screening_form(models.Model):
    id = models.AutoField(primary_key=True)
    age_18_to_40 = models.CharField(max_length=500, default="")
    GDM_diagnosis = models.CharField(max_length=100, default="")
    singleton_gestation = models.CharField(max_length=100, default="")
    receiving_of_antenatal = models.CharField(max_length=200, default="")
    use_smartphone = models.CharField(max_length=100, default="")
    do_not_participate = models.CharField(max_length=100, default="")
    type1_type1_diabetes = models.CharField(max_length=100, default="")
    hearing_vision_problem = models.CharField(max_length=100, default="")
    literacy = models.CharField(max_length=100, default="")

    def __str__(self):
        return str(self.id)

class randomization(models.Model):
    id = models.AutoField(primary_key=True)
    group = [('Intervention', 'Intervention'), ('Comparator', 'Comparator')]
    randomization_date = models.DateField()
    patient_code = models.IntegerField()
    randomization_to_group = models.CharField(max_length=1000, choices=group)
    indicate_the_reason = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.id)

class patient_demographic(models.Model):
    id = models.AutoField(primary_key=True)
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
    Num_children = models.CharField(max_length=1000, choices=children)
    Education_level = models.CharField(max_length=1000, choices=level)
    occuption_status = models.CharField(max_length=1000, choices=status)
    occuption_specify = models.CharField(max_length=2000, default="")
    family_type = models.CharField(max_length=1000, choices=family)
    religion = models.CharField(max_length=1000, choices=rel)
    Residence = models.CharField(max_length=1000, choices=settings)
    mode_of_travel = models.CharField(max_length=1000, choices=travel)
    public_mode_specify = models.CharField(max_length=2000, default="")
    time_to_travel = models.CharField(max_length=1000, choices=travel_Time)
    avg_timein_hospital = models.CharField(max_length=1000, choices=hospital_Time)

    def __str__(self):
        return str(self.id)

class Maternal_characterstic(models.Model):
    id = models.AutoField(primary_key=True)
    Maternal_age = models.IntegerField()
    Mcatogery = [('Sedentary', 'Sedentary'), ('Moderate', 'Moderate'), ('Heavy', 'Heavy')]
    Nulli = [('Yes', 'Yes'), ('No', 'No')]
    fasting = [('IADPSG', 'IADPSG'), ('DIPSI', 'NoDIPSI')]
    LMP = models.CharField(max_length=1000, default="")
    date_of_diagnosis = models.DateField()
    no_of_pregnancy = models.IntegerField()
    gestation_week = models.IntegerField()
    category = models.CharField(max_length=1000, choices=Nulli)
    age_at_menarche = models.IntegerField()
    gravidity = models.CharField(max_length=2000, default="")
    nulliparity = models.CharField(max_length=1000, choices=Nulli)
    chronic_hypertension = models.CharField(max_length=1000, choices=Nulli)
    family_history = models.CharField(max_length=1000, default="")
    self_medical_history = models.CharField(max_length=1000, default="")
    thrombophilia = models.CharField(max_length=1000, choices=Nulli)
    Assisted_reproductive_technology = models.CharField(max_length=1000, choices=Nulli)
    Assisted_reproductive_specify = models.CharField(max_length=1000, default="")
    previous_caesarean_case = models.CharField(max_length=1000, choices=Nulli)
    previous_GDM = models.CharField(max_length=1000, choices=Nulli)
    family_history_DM = models.CharField(max_length=1000, choices=Nulli)
    F_history_hypertension = models.CharField(max_length=1000, choices=Nulli)
    fasting_glucose_1_trim = models.IntegerField()
    Glucose_test = models.CharField(max_length=1000, choices=fasting)
    OGTT_fasting = models.IntegerField()
    OGTT_60min = models.IntegerField()
    OGTT_120min = models.IntegerField()
    smoking = models.CharField(max_length=1000, choices=Nulli)
    smoking_frequency = models.CharField(max_length=1000, default="")
    alcohol = models.CharField(max_length=2000, choices=Nulli)
    alcohol_frequency = models.CharField(max_length=2000, default="")
    tobacco = models.CharField(max_length=2000, choices=Nulli)
    tobacco_frequency = models.CharField(max_length=2000, default="")
    physical_exercise = models.CharField(max_length=2000, choices=Nulli)
    physical_frequency = models.CharField(max_length=2000, default="")
    yoga = models.CharField(max_length=1000, choices=Nulli)
    yoga_frequency = models.CharField(max_length=1000, default="")
    meditation = models.CharField(max_length=2000, choices=Nulli)
    meditation_frequency = models.CharField(max_length=2000, default="")
    walking = models.CharField(max_length=2000, choices=Nulli)
    walking_frequency = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.id)

class CurrentMedication(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Drug = models.TextField()
    Dose = models.TextField()
    Timings = models.TextField()

    def __str__(self):
        return str(self.patient_id)

class Bio_chemical_profile(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Hemoglobin = models.CharField(max_length=2000, default="")
    HbA1c = models.CharField(max_length=2000, default="")
    TSH_uIU = models.CharField(max_length=2000, default="")
    Blood = models.CharField(max_length=2000, default="")
    urea = models.CharField(max_length=2000, default="")
    HIV = models.CharField(max_length=2000, default="")
    Anti = models.CharField(max_length=2000, default="")
    HCV = models.CharField(max_length=2000, default="")
    Antibodies_COI = models.CharField(max_length=2000, default="")
    HBS = models.CharField(max_length=2000, default="")
    Antigen_COI = models.CharField(max_length=2000, default="")
    VDRL = models.CharField(max_length=2000, default="")
    HPLC = models.CharField(max_length=2000, default="")
    Urine = models.CharField(max_length=2000, default="")
    Routine = models.CharField(max_length=2000, default="")
    Colour = models.CharField(max_length=2000, default="")
    Reaction = models.CharField(max_length=2000, default="")
    Sp_Gravity = models.CharField(max_length=2000, default="")
    Protein = models.CharField(max_length=2000, default="")
    Sugar = models.CharField(max_length=2000, default="")
    MICROSCOPIC = models.CharField(max_length=2000, default="")
    RBC = models.CharField(max_length=2000, default="")
    WBC = models.CharField(max_length=2000, default="")
    Epithelial = models.CharField(max_length=2000, default="")
    Cells = models.CharField(max_length=2000, default="")
    Bacteria = models.CharField(max_length=2000, default="")
    Granular = models.CharField(max_length=2000, default="")
    Ca_Oxalate = models.CharField(max_length=2000, default="")
    Tripple_Phosphate = models.CharField(max_length=2000, default="")
    Phosphate = models.CharField(max_length=2000, default="")
    Amorphous = models.CharField(max_length=2000, default="")
    Urate = models.CharField(max_length=2000, default="")
    Uric_Acid = models.CharField(max_length=2000, default="")
    Yeast = models.CharField(max_length=2000, default="")
    Mucus = models.CharField(max_length=2000, default="")
    SPECIAL = models.CharField(max_length=2000, default="")
    Ketones = models.CharField(max_length=2000, default="")
    Bile_Salts = models.CharField(max_length=2000, default="")
    Hb = models.CharField(max_length=2000, default="")
    Hematocrit = models.CharField(max_length=2000, default="")
    RedBC = models.CharField(max_length=2000, default="")
    WhiteBC = models.CharField(max_length=2000, default="")
    Platelet = models.CharField(max_length=2000, default="")
    MCV = models.CharField(max_length=2000, default="")
    MCH = models.CharField(max_length=2000, default="")
    MCHC = models.CharField(max_length=2000, default="")
    RDW_CV = models.CharField(max_length=2000, default="")
    Neutro = models.CharField(max_length=2000, default="")
    Lympho = models.CharField(max_length=2000, default="")
    Eosino = models.CharField(max_length=2000, default="")
    Mono = models.CharField(max_length=2000, default="")
    NRBC = models.CharField(max_length=2000, default="")
    Baso = models.CharField(max_length=2000, default="")
    NeutroAbsl = models.CharField(max_length=2000, default="")
    Lympho_Abs = models.CharField(max_length=2000, default="")
    Eosino_Abs = models.CharField(max_length=2000, default="")
    Mono_Abs = models.CharField(max_length=2000, default="")
    Baso_Urea = models.CharField(max_length=2000, default="")
    Creatinine = models.CharField(max_length=2000, default="")
    Uric_Acid = models.CharField(max_length=2000, default="")
    Calcium = models.CharField(max_length=2000, default="")
    Phosphorus = models.CharField(max_length=2000, default="")
    Sodium = models.CharField(max_length=2000, default="")
    Potassium = models.CharField(max_length=2000, default="")
    Chloride = models.CharField(max_length=2000, default="")
    Bilirubin_T = models.CharField(max_length=2000, default="")
    Bilirublin_D = models.CharField(max_length=2000, default="")
    Bilirubin_I = models.CharField(max_length=2000, default="")
    ALT = models.CharField(max_length=2000, default="")
    AST = models.CharField(max_length=2000, default="")
    ALP = models.CharField(max_length=2000, default="")
    Total_protein = models.CharField(max_length=2000, default="")
    Albumin = models.CharField(max_length=2000, default="")
    Globulin = models.CharField(max_length=2000, default="")
    A_G_ratio = models.CharField(max_length=2000, default="")
    Vitamin_D3 = models.CharField(max_length=2000, default="")
    Iron = models.CharField(max_length=2000, default="")
    Transferrin = models.CharField(max_length=2000, default="")
    Ferritin = models.CharField(max_length=2000, default="")
    TIBC = models.CharField(max_length=2000, default="")
    Vitamin_B12 = models.CharField(max_length=2000, default="")
    Serum_Folate = models.CharField(max_length=2000, default="")
    Lipid_Profile = models.CharField(max_length=2000, default="")
    Total_Cholesterol = models.CharField(max_length=2000, default="")
    Triglycerides = models.CharField(max_length=2000, default="")
    VLDL = models.CharField(max_length=2000, default="")
    LDL = models.CharField(max_length=2000, default="")
    HDL = models.CharField(max_length=2000, default="")
    CHOL_HDL = models.CharField(max_length=2000, default="")
    LDL_HDL = models.CharField(max_length=2000, default="")
    def __str__(self):
        return str(self.patient_id)

class Kuppuswamy_scale(models.Model):
    patient_id = models.AutoField(primary_key=True)
    occupation_head = [('10', 'Legislators, Senior Officials & Managers'), ('9', 'Professionals'),('8','Technicians and Associate Professionals'),('7', 'Clerks'),('6', 'Skilled Workers and Shop & Market Sales Workers'),('5', 'Skilled Agricultural & Fishery Workers'),('4', 'Craft & Related Trade Workers'),('3', 'Plant & Machine Operators and Assemblers'),('2', 'Elementary Occupation'),('1', 'Unemployed')]
    head_of_family = models.CharField(max_length=2000, choices=occupation_head)
    education_head = [('7', 'Profession or Honours'),('6','Graduate'),('5', 'Intermediate or diploma'), ('4','High school certificate'),('3', 'Middle school certificate'),('2','Primary school certificate Illiterate'),('1', 'Illiterate')]
    education_of_family = models.CharField(max_length=2000, choices=education_head)
    income_family = [('12', '≥ 199,862'),('10','99,931–199,861') ,('6', '74,756 –99,930'), ('4', '49,962–74,755'),('3','29,973– 49,961'),('2','10,002–29,972'),('1', '≤ 10,001')]
    income = models.CharField(max_length=2000, choices=income_family)
    socio_economic=[('26-29','Upper (I)'),('16-25','Upper Middle (II'),('11-15', 'Lower Middle (III)'),('5-10','Upper Lower (IV)'),('<5 Lower', 'Lower (V)')]
    economic = models.CharField(max_length=2000, choices=socio_economic)
    def __str__(self):
        return str(self.patient_id)

class weight_monitor(models.Model):
     patient_id = models.AutoField(primary_key=True)
     Period_gestation = [('Week 24', 'Week 24'), ('Week 25', 'Week 25'), ('Week 26', 'Week 26'), ('Week 27', 'Week 27'),
                         ('Week 28', 'Week 28'), ('Week 29', 'Week 29'), ('Week 30', 'Week 30'), ('Week 31', 'Week 31'),
                         ('Week 32', 'Week 32'), ('Week 33', 'Week 33'), ('Week 34', 'Week 34'), ('Week 35', 'Week 35'),
                         ('Week 36', 'Week 36'), ('Week 37', 'Week 37')]
     Pweight = models.CharField(max_length=2000, choices=Period_gestation)
     Patient_Weight = models.CharField(max_length=2000, default="")
     Remarks = models.TextField()

     def __str__(self):
        return self.patient_id

class Dietary_recall_24hrs(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Meal_time = models.DateTimeField()
    Food_consumed = models.ImageField(upload_to='images/', null=True,default="")
    Quantity = models.TextField(max_length=2000, default="")
    Date = models.DateField()
    weekday = models.CharField(max_length=2000, default="")
    weekend = models.CharField(max_length=2000, default="")
    Glycemic_index = models.TextField()
    Glycemic_load = models.TextField()
    nutri_supplements = models.TextField()
    Multivitimins = models.TextField()
    def __str__(self):
        return str(self.patient_id)

class Dietary_recall_outcome(models.Model):
    patient_id = models.AutoField(primary_key=True)
    weekday = models.CharField(max_length=2000, default="")
    weekend = models.CharField(max_length=2000, default="")
    Glycemic_index = models.TextField()
    Glycemic_load = models.TextField()
    Date = models.DateField()
    RDA = models.CharField(max_length=2000, default="")
    actual_intake = models.CharField(max_length=2000, default="")
    Excess_Deficit = models.CharField(max_length=2000, default="")
    Energy_RDA = models.CharField(max_length=2000, default="")
    Protein_RDA = models.CharField(max_length=2000, default="")
    CHO_RDA = models.CharField(max_length=2000, default="")
    Fat_RDA = models.CharField(max_length=2000, default="")
    Calcium_RDA = models.CharField(max_length=2000, default="")
    Iron_RDA = models.CharField(max_length=2000, default="")
    Zinc_RDA = models.CharField(max_length=2000, default="")
    Magnesium_RDA = models.CharField(max_length=2000, default="")
    Retinol_RDA = models.CharField(max_length=2000, default="")
    B_Carotene_RDA = models.CharField(max_length=2000, default="")
    Thiamin_RDA = models.CharField(max_length=2000, default="")
    Riboflavin_RDA = models.CharField(max_length=2000, default="")
    Niacin_RDA = models.CharField(max_length=2000, default="")
    VitaminB6_RDA = models.CharField(max_length=2000, default="")
    Ascorbic_acid_RDA = models.CharField(max_length=2000, default="")
    Dietray_folate_RDA = models.CharField(max_length=2000, default="")
    VitaminB12_RDA = models.CharField(max_length=2000, default="")
    Energy_AI = models.CharField(max_length=2000, default="")
    Protein_AI = models.CharField(max_length=2000, default="")
    CHO_AI = models.CharField(max_length=2000, default="")
    Fat_AI = models.CharField(max_length=2000, default="")
    Calcium_AI = models.CharField(max_length=2000, default="")
    Iron_AI = models.CharField(max_length=2000, default="")
    Zinc_AI = models.CharField(max_length=2000, default="")
    Magnesium_AI = models.CharField(max_length=2000, default="")
    Retinol_AI = models.CharField(max_length=2000, default="")
    B_Carotene_AI = models.CharField(max_length=2000, default="")
    Thiamin_AI = models.CharField(max_length=2000, default="")
    Riboflavin_AI = models.CharField(max_length=2000, default="")
    Niacin_AI = models.CharField(max_length=2000, default="")
    VitaminB6_AI = models.CharField(max_length=2000, default="")
    Ascorbic_acid_AI = models.CharField(max_length=2000, default="")
    Dietray_folate_AI = models.CharField(max_length=2000, default="")
    VitaminB12_AI = models.CharField(max_length=2000, default="")
    Energy_ED = models.CharField(max_length=2000, default="")
    Protein_ED = models.CharField(max_length=2000, default="")
    CHO_ED = models.CharField(max_length=2000, default="")
    Fat_ED = models.CharField(max_length=2000, default="")
    Calcium_ED = models.CharField(max_length=2000, default="")
    Iron_ED = models.CharField(max_length=2000, default="")
    Zinc_ED = models.CharField(max_length=2000, default="")
    Magnesium_ED = models.CharField(max_length=2000, default="")
    Retinol_ED = models.CharField(max_length=2000, default="")
    B_Carotene_ED = models.CharField(max_length=2000, default="")
    Thiamin_ED = models.CharField(max_length=2000, default="")
    Riboflavin_ED = models.CharField(max_length=2000, default="")
    Niacin_ED = models.CharField(max_length=2000, default="")
    VitaminB6_ED = models.CharField(max_length=2000, default="")
    Ascorbic_acid_ED = models.CharField(max_length=2000, default="")
    Dietray_folate_ED = models.CharField(max_length=2000, default="")
    VitaminB12_ED = models.CharField(max_length=2000, default="")
    Nutritional_Supplements = models.TextField()
    Multivitamin = models.TextField()

    def __str__(self):
        return str(self.patient_id)

class Patient_Diet_assessment(models.Model):
    patient_id = models.AutoField(primary_key=True)
    food_choice = [('Vegetarian', 'Vegetarian'),
                   ('Non-vegetarian', 'Non-vegetarian'), ('Ovo-vegetarian', 'Ovo-vegetarian')]
    Fchoice = models.CharField(max_length=2000, choices=food_choice)
    consumed_meal = [('Early', 'Early'), ('Breakfast', 'Breakfast'), ('Mid-morning', 'Mid-morning'),
                     ('Lunch', 'Lunch'),
                     ('Evening snack', 'Evening snack'), ('Dinner', 'Dinner'), ('Post-dinner', 'Post-dinner')]
    weekdays = models.CharField(max_length=2000, choices=consumed_meal)
    weekends = models.CharField(max_length=2000, choices=consumed_meal)
    often_consume = [('Everyday', 'Everyday'),
                     ('4-5 times a week', '4-5 times a week'), ('2-3 times a week', '2-3 times a week'),
                     ('Once a week', 'Once a week'), ('Once a month', 'Once a month')]
    Q3 = models.CharField(max_length=2000, choices=often_consume)
    food_place = [('Daily', 'Daily'),
                  ('Frequently', 'Frequently'), ('Occasionally', 'Occasionally'), ('Never', 'Never')]
    Street_Hawker = models.CharField(max_length=2000, choices=food_place)
    Restaurant = models.CharField(max_length=2000, choices=food_place)
    Food_Courts = models.CharField(max_length=2000, choices=food_place)
    Dhabas = models.CharField(max_length=2000, choices=food_place)
    Office_canteen = models.CharField(max_length=2000, choices=food_place)

    def __str__(self):
        return str(self.patient_id)


class P_sleep_quality_index(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Date = models.DateField()
    Clock = models.DateTimeField()
    POG = models.CharField(max_length=2000, default="")
    Subj_Code = models.CharField(max_length=2000, default="")
    Sleep_duration = models.CharField(max_length=2000, default="")
    Q1 = models.CharField(max_length=2000, default="")
    Q2 = models.CharField(max_length=2000, default="")
    Q3 = models.CharField(max_length=2000, default="")
    Q4 = models.CharField(max_length=2000, default="")
    Q5a_choice = [('Not during the past month', 'Not during the past month'),
          ('Less than once a week', 'Less than once a week'), ('Once or twice a week', 'Once or twice a week'),
          ('Three or more times a week', 'Three or more times a week')]
    Q5a = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5b = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5c = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5d = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5e = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5f = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5g = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5h = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5i = models.CharField(max_length=2000, choices=Q5a_choice)
    Q5j = models.CharField(max_length=2000, default="")
    Q6_choice = [('Not during the past month', 'Not during the past month'),
                  ('Less than once a week', 'Less than once a week'), ('Once or twice a week', 'Once or twice a week'), ('Three or more times a week', 'Three or more times a week')]
    Q6 = models.CharField(max_length=2000, choices=Q6_choice)
    Q7 = models.CharField(max_length=2000, choices=Q6_choice)
    Q8_choice = [('No problem at all', 'No problem at all'),
                 ('Only a very slight problem', 'Only a very slight problem'), ('Somewhat of a problem', 'Somewhat of a problem'),
                 ('A very big problem', 'TA very big problem')]
    Q8 = models.CharField(max_length=2000, choices=Q8_choice)
    Q9_choice=[('Very good', 'Very good'),
                 ('Fairly good', 'Fairly good'), ('Fairly bad', 'Fairly bad'),
                 ('Very bad', 'Very bad')]
    Q9 = models.CharField(max_length=2000, choices=Q9_choice)
    Q10_choice = [('No bed partner or room mate', 'No bed partner or room mate'),
                 ('Partner/roommate in other room', 'Partner/roommate in other room'), ('Partner in same room but not same bed', 'Partner in same room but not same bed'),
                 ('Partner in same bed', 'Partner in same bed')]
    Q10 = models.CharField(max_length=2000, choices=Q10_choice)
    Q10a_choice = [('Not during the past month', 'Not during the past month'),
                  ('Less than once a week', 'Less than once a week'),
                  ('Once or twice a week', 'Once or twice a week'),
                  ('Three or more times a week', 'Three or more times a week')]
    Q10a= models.CharField(max_length=2000, choices=Q10a_choice)
    Q10b = models.CharField(max_length=2000, choices=Q10a_choice)
    Q10c = models.CharField(max_length=2000, choices=Q10a_choice)
    Q10d = models.CharField(max_length=2000, choices=Q10a_choice)
    Q10e = models.CharField(max_length=2000, choices=Q10a_choice)
    Q10f = models.CharField(max_length=2000, choices=Q10a_choice)

    def __str__(self):
        return str(self.patient_id)

class EPDS(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Date = models.DateField()
    POG = models.CharField(max_length=2000, default="")
    Subj_Code = models.CharField(max_length=2000, default="")
    General_health = [('1', 'Excellent'), ('2', 'Professionals'),
                       ('3', 'Good'), ('4', 'Fair'),
                       ('5', 'Poor')]
    Ghealth = models.CharField(max_length=2000, choices=General_health)
    year_health = [('1', 'Much better now than one year ago'), ('2', 'Graduate'), ('3', 'Somewhat better now than one year ago'),
                      ('4', 'About the same'), ('5', 'Somewhat worse now than one year ago'),
                      ('5', 'Much worse now than one year ago')]
    year = models.CharField(max_length=2000, choices=year_health)
    Limitations_activity =[('1', 'Yes, Limited a Lot (1)'), ('2', 'Yes, Limited a Little (2)'),('3', 'No, Not limited at All (3)')]
    q1 = models.CharField(max_length=2000, choices=Limitations_activity)
    q2 = models.CharField(max_length=2000, choices=Limitations_activity)
    q3 = models.CharField(max_length=2000, choices=Limitations_activity)
    q4 = models.CharField(max_length=2000, choices=Limitations_activity)
    q6 = models.CharField(max_length=2000, choices=Limitations_activity)
    q7 = models.CharField(max_length=2000, choices=Limitations_activity)
    q8 = models.CharField(max_length=2000, choices=Limitations_activity)
    q9 = models.CharField(max_length=2000, choices=Limitations_activity)
    q10 = models.CharField(max_length=2000, choices=Limitations_activity)

    Physical_Problems =  [('1', 'Yes'), ('2', 'No')]
    q11 = models.CharField(max_length=2000, choices=Physical_Problems)
    q12 = models.CharField(max_length=2000, choices=Physical_Problems)
    q13 = models.CharField(max_length=2000, choices=Physical_Problems)
    Emotional_Problems = [('1', 'Yes'), ('2', 'No')]
    q14 = models.CharField(max_length=2000, choices=Physical_Problems)
    q15 = models.CharField(max_length=2000, choices=Physical_Problems)
    q16 = models.CharField(max_length=2000, choices=Physical_Problems)
    Social_activity = [('1', 'Not at all'), ('2', 'Slightly'),
                       ('3', 'Moderately'), ('4', 'Quite a bit'),
                       ('5', 'Extremely')]
    q20 = models.CharField(max_length=2000, choices=Social_activity)
    P_body_pain = [('1', 'None'), ('2', 'Very mild'),
                       ('3', 'Mild'), ('4', 'Moderate'),
                       ('5', 'Severe'), ('6', 'Very severe')]
    Q21 = models.CharField(max_length=2000, choices=P_body_pain)
    D_body_pain = [('1', 'Not at all'), ('2', 'A little bit'),
                 ('3', 'Moderately'), ('4', 'Quite a bit'),
                 ('5', 'Extremely')]
    Q22 = models.CharField(max_length=2000, choices=D_body_pain)
    Energy_emotion = [('1', 'All of the Time'), ('2', 'Most of the Time'),
                   ('3', 'A Good Bit of the Time'), ('4', 'Some of the Time'),('5', 'A Little of the Time'), ('6', 'None of the Time')]
    Q23 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q24 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q25 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q26 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q27 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q28 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q29 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q30 = models.CharField(max_length=2000, choices=Energy_emotion)
    Q31 = models.CharField(max_length=2000, choices=Energy_emotion)
    Social_activity = [('1', 'All of the time'), ('2', 'Most of the time'),
                   ('3', 'Some of the time'), ('4', 'A little of the time'),
                   ('5', 'None of the time')]
    Q31 = models.CharField(max_length=2000, choices=Social_activity)
    GH = [('1', 'Definitely True'), ('2', 'Mostly True'),('3', 'Do not Know'),('4','Mostly false'),('5','Definitely false')]
    Q32 = models.CharField(max_length=2000, choices=GH)

    def __str__(self):
        return str(self.patient_id)

class daily_Glucose_level_insuline(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Gweek = models.IntegerField()
    Date = models.DateField()
    duration = [('Breakfast', 'Breakfast'),('Lunch','Lunch'),('Dinner','Dinner')]
    duration_choice = models.CharField(max_length=2000, choices=duration)
    duration_set = [('pre', 'pre'), ('post', 'post')]
    set_choice = models.CharField(max_length=2000, choices=duration_set)
    blood_sugar = models.CharField(max_length=2000, default="")
    Timing = models.DateTimeField()
    at_2am = models.CharField(max_length=2000, default="")
    Insuline = models.CharField(max_length=2000, default="")
    actual_level = models.CharField(max_length=2000, default="")
    instructed_level = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.patient_id)

class daily_Glucose_level_drug(models.Model):
    patient_id = models.AutoField(primary_key=True)

    Gweek = models.CharField(max_length=2000, default="")
    Target = models.CharField(max_length=2000, default="")
    only_diet = models.CharField(max_length=2000, default="")
    drug_diet = models.CharField(max_length=2000, default="")
    Date = models.DateField()
    Fasting = models.CharField(max_length=2000, default="")
    Post_Breakfast = models.CharField(max_length=2000, default="")
    Post_Lunch = models.CharField(max_length=2000, default="")
    Post_Dinner = models.CharField(max_length=2000, default="")
    Note = models.TextField()
    actual_level = models.CharField(max_length=2000, default="")
    instructed_level = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.patient_id)


class daily_BP(models.Model):
    patient_id = models.AutoField(primary_key=True)

    Gweek = models.CharField(max_length=2000, default="")
    Target = models.CharField(max_length=2000, default="")
    duration = [('morning', 'morning'), ('afternoon', 'afternoon'), ('Late evening', 'Late evening')]
    duration_choice = models.CharField(max_length=2000, choices=duration)
    duration_set = [('Systolic', 'Systolic'), ('Diastolic', 'Diastolic'), ('Pulse Rate', 'Pulse Rate')]
    set_choice = models.CharField(max_length=2000, choices=duration_set)
    Date = models.DateTimeField()
    actual_level = models.CharField(max_length=2000, default="")
    instruct_level = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.patient_id)

class Physical_exercise(models.Model):
    patient_id = models.AutoField(primary_key=True)
    Date = models.DateField()
    Timing= models.DateTimeField()
    Gweek = models.CharField(max_length=2000, default="")
    Breathing = models.CharField(max_length=2000, default="")
    Leg_movement = models.CharField(max_length=2000, default="")
    Pelvic_Exercise = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.patient_id)

class preganacy_delivery(models.Model):
    patient_id = models.AutoField(primary_key=True)
    time = [('Full term birth', 'Full term birth'), ('Pre-term birth', 'Pre-term birth')]
    Delivery_mode = [('Caesarean Section', 'Caesarean Section'), ('Vaginally Delivery', 'Vaginally Delivery'), ('Forcep Delivery', 'Forcep Delivery')]
    Choice = [('Yes', 'Yes'), ('No', 'No')]
    time_select = models.CharField(max_length=1000, choices=time)
    Delivery = models.CharField(max_length=1000, choices=Choice)
    Shoulder_dystocia = models.CharField(max_length=1000, choices=Choice)
    Postpartum_hemorrhage = models.CharField(max_length=2000, choices=Choice)
    Antenatal_corticosteroids = models.CharField(max_length=2000, choices=Choice)
    Gestational_hypertension = models.CharField(max_length=2000, choices=Choice)
    Preeclampsia = models.CharField(max_length=2000, choices=Choice)
    Polyhydramnios = models.CharField(max_length=2000, choices=Choice)
    Induction_of_labour = models.CharField(max_length=2000, choices=Choice)
    Caesarean_section = models.CharField(max_length=2000,  default="")
    Gestational_age = models.CharField(max_length=2000,  default="")
    Spontaneous_abortion = models.CharField(max_length=2000,  default="")
    Miscarriage = models.CharField(max_length=2000, default="")
    Other = models.CharField(max_length=2000, default="")

    def __str__(self):
        return str(self.patient_id)

class Neonatal_outcomes(models.Model):
    patient_id = models.AutoField(primary_key=True)
    birth_weight= models.IntegerField()
    Apgar_score = models.CharField(max_length=2000, default="")
    weight_baby = [('Normal', 'Normal'), ('LBW', 'LBW'), ('VLBW', 'VLBW'), ('Macrosomia', 'Macrosomia')]
    Choice = [('Yes', 'Yes'), ('No', 'No')]
    w1 = models.CharField(max_length=2000, choices=weight_baby)
    Gestational_age = models.CharField(max_length=2000, choices=Choice)
    Neonatal = models.IntegerField()
    NICU = models.CharField(max_length=2000, choices=Choice)
    New_born = models.CharField(max_length=2000, choices=Choice)
    Respiratory = models.CharField(max_length=2000, choices=Choice)
    Phototherapy = models.CharField(max_length=2000, choices=Choice)
    Neonatal_death = models.CharField(max_length=2000, choices=Choice)

    def __str__(self):
        return str(self.patient_id)

class Feedback_forms(models.Model):
    id = models.AutoField(primary_key=True)
    Statement = [('Agree', 'Agree'), ('Disagree', 'Disagree')]
    S1 = models.CharField(max_length=2000, choices=Statement)
    S2 = models.CharField(max_length=2000, choices=Statement)
    S3= models.CharField(max_length=2000, choices=Statement)
    S4 = models.CharField(max_length=2000, choices=Statement)
    S5 = models.CharField(max_length=2000, choices=Statement)

    def __str__(self):
        return str(self.id)


















