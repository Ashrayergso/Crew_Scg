```python
from django import forms
from .models import CrewMember, Cert, Qualification, Ship, Positions, Assignment, ShipCrewAllowance

class CrewMemberForm(forms.ModelForm):
    class Meta:
        model = CrewMember
        fields = '__all__'

class CertForm(forms.ModelForm):
    class Meta:
        model = Cert
        fields = '__all__'

class QualificationForm(forms.ModelForm):
    class Meta:
        model = Qualification
        fields = '__all__'

class ShipForm(forms.ModelForm):
    class Meta:
        model = Ship
        fields = '__all__'

class PositionsForm(forms.ModelForm):
    class Meta:
        model = Positions
        fields = '__all__'

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'

class ShipCrewAllowanceForm(forms.ModelForm):
    class Meta:
        model = ShipCrewAllowance
        fields = '__all__'
```