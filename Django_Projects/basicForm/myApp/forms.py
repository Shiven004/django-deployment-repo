from django import forms
from django.core import validators

#Custom validator
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name must start with Z")

class FormName(forms.Form):
    #name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email agin...')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vemail = all_clean_data['verify_email']


        if email != vemail:
            raise forms.ValidationError("Make Sure Email Match!!!")

    """
    #Bot catcher fn.
    
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if botcatcher:
            raise forms.ValidationError('Gotcha Bot!!!!')
        return botcatcher
    """
