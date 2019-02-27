from django import forms


class NameForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
