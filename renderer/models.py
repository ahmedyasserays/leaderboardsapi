from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def validate_length(password):
    if len(password) < 8:
        raise ValidationError("password must be at least 8 characters")
        
class leaderBoard(models.Model):
    name = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=15, validators=[validate_length])



    def __str__(self):
        return self.name


class score(models.Model):
    leader_board = models.ForeignKey(leaderBoard, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    score = models.IntegerField()

    def __str__(self):
        return self.name