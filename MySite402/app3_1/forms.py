from django import forms

class Form1(forms.Form):
    id = forms.IntegerField(label='ID')
    name = forms.CharField(label="NAME", max_length=50)
    address = forms.CharField(label="ADDRESS", max_length=50)


# News Form
class Form2(forms.Form):
    nid = forms.IntegerField(label="ID")
    title = forms.CharField(label="TITLE")
    content = forms.CharField(label="CONTENTS")