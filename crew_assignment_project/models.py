```python
from django.db import models

class CrewMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    contract_duration = models.IntegerField()
    vacation_time = models.IntegerField()

    def __str__(self):
        return self.name

class Cert(models.Model):
    name = models.CharField(max_length=200)
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Qualification(models.Model):
    name = models.CharField(max_length=200)
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=200)
    crew_allowance = models.IntegerField()

    def __str__(self):
        return self.name

class Positions(models.Model):
    name = models.CharField(max_length=200)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Assignment(models.Model):
    crew_member = models.ForeignKey(CrewMember, on_delete=models.CASCADE)
    ship = models.ForeignKey(Ship, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.crew_member.name} assigned to {self.ship.name}"

class ShipCrewAllowance(models.Model):
    ship = models.OneToOneField(Ship, on_delete=models.CASCADE)
    crew_allowance = models.IntegerField()

    def __str__(self):
        return f"{self.ship.name} allowance: {self.crew_allowance}"
```