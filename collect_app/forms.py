from django import forms


class GetNameAge (forms.Form):
    fname = forms.CharField(label="State", widget=forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'name', 
        'required': 'true'}))
    age = forms.IntegerField(label="State", widget=forms.TextInput(attrs={
        'class':'form-control', 
        'placeholder': 'age', 
        'required': 'true'}))
