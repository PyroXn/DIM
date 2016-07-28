from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

class Patient(models.Model):
    MASCULIN = 1
    FEMININ = 2
    INDEFINI = 3
    SEXE_CHOICES = (
        (MASCULIN, 'Masculin'),
        (FEMININ, 'Féminin'),
        (INDEFINI, 'Indéfini'),
    )

    MR = 1
    MME = 2
    CIVILITY_CHOICES = (
        (MR, 'Mr'),
        (MME, 'Mme'),
    )

    OTHERS = 'ZZ'
    ID_CARD = 'CI'
    ID_CHECK = 'VE'
    DRIVING_LICENCE = 'PC'
    TYPE_DOC_CHOICES = (
        (OTHERS, 'Autres'),
        (ID_CARD, 'Carte d''identif'),
        (ID_CHECK, 'Identif. A vérif'),
        (DRIVING_LICENCE, 'Permi conduire'),
    )

    #personnal data
    surname = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    maiden_name = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField()
    sexe = models.IntegerField(choices=SEXE_CHOICES, default=INDEFINI)
    pseudo = models.CharField(max_length=200, blank=True)
    civility = models.IntegerField(choices=CIVILITY_CHOICES, blank=True)
    title = models.CharField(max_length=20, blank=True)
    affix_name = models.CharField(max_length=200, blank=True)
    particule_name = models.CharField(max_length=20, blank=True)
    nationality = models.CharField(max_length=2, default='LU', blank=True)

    #others data
    language = models.CharField(max_length=2, default='LU', blank=True)
    ssn = models.IntegerField(validators=MaxLengthValidator(13))
    number_doc = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999999)])
    type_doc = models.CharField(max_length=2, choices=TYPE_DOC_CHOICES, blank=True)
    commentary = models.CharField(max_length=500, blank=True)

    class Meta:
        db_table = 'patient'
        app_label = 'rescue'