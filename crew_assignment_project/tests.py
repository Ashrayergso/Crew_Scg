```python
from django.test import TestCase
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance
from .views import assignCrewToShips

class CrewMemberModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John Doe', position='Captain', contract_duration=12, vacation_time=30)

    def test_crew_member_content(self):
        crew_member = CrewMember.objects.get(id=1)
        expected_object_name = f'{crew_member.name}'
        self.assertEquals(expected_object_name, 'John Doe')

class AssignCrewToShipsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        CrewMember.objects.create(name='John Doe', position='Captain', contract_duration=12, vacation_time=30)
        Ship.objects.create(name='Titanic', capacity=2000)

    def test_assign_crew_to_ships(self):
        assignCrewToShips()
        assignment = Assignment.objects.get(id=1)
        self.assertEquals(assignment.crew_member.name, 'John Doe')
        self.assertEquals(assignment.ship.name, 'Titanic')

class MessageTest(TestCase):
    def test_crew_fetch_success(self):
        response = self.client.get('/crew_members/')
        self.assertContains(response, 'CREW_FETCH_SUCCESS')

    def test_ship_fetch_success(self):
        response = self.client.get('/ships/')
        self.assertContains(response, 'SHIP_FETCH_SUCCESS')

    def test_assignment_success(self):
        response = self.client.post('/assignments/', {'crew_member': 1, 'ship': 1})
        self.assertContains(response, 'ASSIGNMENT_SUCCESS')

    def test_assignment_failure(self):
        response = self.client.post('/assignments/', {'crew_member': 1, 'ship': 2})
        self.assertContains(response, 'ASSIGNMENT_FAILURE')
```