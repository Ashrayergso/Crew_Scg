```python
from django.test import TestCase
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance
from .views import assignCrewToShips

class CrewMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John', position='Captain', contract_duration=12, vacation_time=2)

    def test_name_label(self):
        crewmember = CrewMember.objects.get(id=1)
        field_label = crewmember._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # Add more tests for other fields and models

class AssignCrewToShipsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create some test data for the function to use
        pass

    def test_assign_crew_to_ships(self):
        # Test the assignCrewToShips function
        pass

    # Add more tests for other functions and views
```