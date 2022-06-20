from django.db import models

# Create your models here.


class Question(models.Model):
    OTHERS = 'OTHERS'
    MATH = 'MATHEMATICS'
    ENG = 'ENGLISH STUDIES'
    GEO = 'GOEGRAPHY'
    CHEM = 'CHEMISTRY'
    PHY = 'PHYSICS'
    HISTORY = 'HISTORY'
    COMP = 'COMPUTER STUDIES'
    CRS = 'CHRISTIAN RELIGIOUS STUDIES'
    FMATH = 'FURTHER MATHEMATICS'
    ECON = 'ECONOMICS'
    BIO = 'BIOLOGY'
    CIVIC = 'CIVIC EDUCATION'
    NONE = 'NONE'

    SUBJECTS = [

        (MATH, 'MATHEMATICS'),
        (ENG, 'ENGLISH STUDIES'),
        (PHY, 'PHYSICS'),
        (CHEM, 'CHEMISTRY'),
        (GEO, 'GOEGRAPHY'),
        (BIO, 'BIOLOGY'),
        (FMATH, 'FURTHER MATHEMATICS'),
        (HISTORY, 'HISTORY'),
        (COMP, 'COMPUTER STUDIES'),
        (CRS, 'CHRISTIAN RELIGIOUS STUDIES'),
        (ECON, 'ECONOMICS'),
        (CIVIC, 'CIVIC EDUCATION'),
        (OTHERS, 'OTHERS'),
        (NONE, 'NONE'),
    ]

    question = models.CharField(max_length=300)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    answer = models.IntegerField()
    domain = models.CharField(max_length=30, choices=SUBJECTS, default=NONE)

    def __str__(self):
        return self.question
