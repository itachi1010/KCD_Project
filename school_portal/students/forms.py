from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, CourseRegistration, ConfirmFees


# Define the choices for school years
SCHOOL_YEAR_CHOICES = [
    ('1', '1st Year'),
    ('2', '2nd Year'),
    ('3', '3rd Year'),
    ('4', '4th Year'),
    ('5', '5th Year'),
]

# Define the choices for sessions
SESSION_CHOICES = [
    ('2022/2023', '2022/2023'),
    ('2021/2022', '2021/2022'),
    ('2020/2021', '2020/2021'),
    ('2019/2020', '2019/2020'),
]



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('matric_number', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('current_year_of_study', 'gender', 'school_fees_receipt', 'dept_fees_receipt', 'faculty_fees_receipt')


     


class CourseRegistrationForm(forms.ModelForm):
    current_year_of_study = forms.ChoiceField(
        choices=SCHOOL_YEAR_CHOICES,
        error_messages={'required': 'Please select your current year of study.'}
    )
    session = forms.ChoiceField(
        choices=SESSION_CHOICES,
        error_messages={'required': 'Please select a session.'}
    )

    class Meta:
        model = CourseRegistration
        fields = ['session', 'reference_number', 'name', 'reg_number', 'current_year_of_study', 'gender']

    def clean_reference_number(self):
        ref_num = self.cleaned_data.get('reference_number')
        if not ref_num.isdigit():
            raise forms.ValidationError('Reference number must be numeric.')
        return ref_num

        

class ConfirmFeesForm(forms.ModelForm):
    class Meta:
        model = ConfirmFees
        fields = ['school_fees_receipt', 'dept_fees_receipt', 'faculty_fees_receipt']
