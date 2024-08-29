from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, CourseRegistration, ConfirmFees, Course


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



from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile, CourseRegistration, ConfirmFees

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Enter your email'
        })
    )
    matric_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Matriculation Number'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Enter your password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control custom-input',
            'placeholder': 'Confirm your password'
        })
    )

    class Meta:
        model = User
        fields = ('matric_number', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('current_year_of_study', 'gender', 'school_fees_receipt', 'dept_fees_receipt', 'faculty_fees_receipt')


     



from django import forms
from .models import Course, CourseRegistration

class CourseRegistrationForm(forms.ModelForm):
    courses = forms.ModelMultipleChoiceField(
        queryset=Course.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Select Courses"
    )

    class Meta:
        model = CourseRegistration
        fields = ['session', 'reference_number', 'name', 'reg_number', 'current_year_of_study', 'gender', 'courses']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['courses'].label_from_instance = self.label_from_instance

    def label_from_instance(self, obj):
        return f"{obj.course_code} - {obj.course_title} ({obj.credit_load} credits)"

    def clean_courses(self):
        selected_courses = self.cleaned_data.get('courses')
        total_credit_load = sum(course.credit_load for course in selected_courses)
        
        # if not (8 <= len(selected_courses) <= 9):
        #     raise forms.ValidationError("You must register between 8 and 9 courses.")
        
        if total_credit_load > 24:
            raise forms.ValidationError("Total credit load cannot exceed 24.")

        return selected_courses

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.total_credit_load = sum(course.credit_load for course in self.cleaned_data['courses'])
        if commit:
            instance.save()
            self.save_m2m()  # Save the many-to-many field (courses)
        return instance



        

class ConfirmFeesForm(forms.ModelForm):
    class Meta:
        model = ConfirmFees
        fields = ['school_fees_receipt', 'dept_fees_receipt', 'faculty_fees_receipt']
