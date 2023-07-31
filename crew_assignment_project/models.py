```python
from django.db import models

class CrewMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.ForeignKey('Positions', on_delete=models.CASCADE)
    contract_duration = models.IntegerField()
    vacation_time = models.IntegerField()

    def __str__(self):
        return self.name

class Cert(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Qualification(models.Model):
    crew_member = models.ForeignKey('CrewMember', on_delete=models.CASCADE)
    cert = models.ForeignKey('Cert', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.crew_member.name} - {self.cert.name}"

class Ship(models.Model):
    name = models.CharField(max_length=200)
    crew_allowance = models.ForeignKey('ShipCrewAllowance', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Positions(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Assignment(models.Model):
    crew_member = models.ForeignKey('CrewMember', on_delete=models.CASCADE)
    ship = models.ForeignKey('Ship', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.crew_member.name} - {self.ship.name}"

class ShipCrewAllowance(models.Model):
    position = models.ForeignKey('Positions', on_delete=models.CASCADE)
    allowance = models.IntegerField()

    def __str__(self):
        return f"{self.position.name} - {self.allowance}"
```