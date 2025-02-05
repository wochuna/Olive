from django import forms
from .models import Data

class MyForm(forms.ModelForm):
    gender = [('Male', 'Male'), ('Female', 'Female')]
    month = [
        ('January', 'January'), ('February', 'February'),
        ('March', 'March'), ('April', 'April'),
        ('May', 'May'), ('June', 'June'),
        ('July', 'July'), ('August', 'August'),
        ('September', 'September'), ('October', 'October'),
        ('November', 'November'), ('December', 'December')
    ]
    month = forms.MultipleChoiceField(
    choices=month,
    widget=forms.CheckboxSelectMultiple,
    required=False,
    )
    experience = [
        ('4', 'Very Satisfied'),
        ('3', 'Satisfied'),
        ('2', 'Unsatisfied'),
        ('1', 'Very Unsatisfied')
    ]
    class Meta:
        model = Data
        fields = ['gender', 'month', 'experience']

 