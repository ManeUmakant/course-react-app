from django import forms
from django.core.exceptions import ValidationError
from employee.models import Student,Teacher


class teacherForm(forms.ModelForm):
    ch = (
        ('', '--Select Option--'),
        ('pn', 'Pune'),
        ('bng', 'Bangalore')

    )

    gn = (

        ('m', 'Male'),
        ('f', 'Female')
    )
    is_active = forms.CharField(widget=forms.CheckboxInput())
    city = forms.ChoiceField(choices=ch)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect())
    class Meta:
        model = Teacher
        fields = ('name', 'student', 'email', 'city', 'gender', 'is_active')

class formEXample(forms.Form):

    ch = (
        ('', '--Select Option--'),
        ('pn', 'Pune'),
        ('bng', 'Bangalore')

    )

    gn = (

        ('m', 'Male'),
        ('f', 'Female')
    )
    name = forms.CharField(disabled=True,min_length=5, max_length=20,label="UserName", initial='xyz', required=True,)
    email = forms.EmailField()
    city = forms.ChoiceField(choices=ch)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect())
    address = forms.CharField(max_length=250, widget=forms.Textarea)
    is_active = forms.CharField(widget=forms.CheckboxInput())


    def clean(self):

        form_data = self.cleaned_data
        if 'email' in form_data and form_data['email'].find('mytectra.com') == -1:
            self.errors['email'] = ['Please provide mytectra.com email!']

        return form_data


class studentForm(forms.ModelForm):

    class Meta:

        model = Student
        fields = ('name', 'email', 'address')