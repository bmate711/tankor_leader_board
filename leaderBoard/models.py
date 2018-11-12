from django.db import models


class Team(models.Model):
    TEAMS = (
        ('FEKETE','Fekete'),
        ('SARGA','Sárga'),
        ('PIROS','Piros'),
        ('KEK','Kék'),
        ('FEHER','Fehér'),
    )
    name = models.CharField(max_length=100)
    team_id = models.CharField(max_length=8)
    color = models.CharField(max_length=10, choices=TEAMS)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
