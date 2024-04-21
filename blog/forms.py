from django import forms


class CommentForm(forms.Form):
    """This form is related to posting comments on posts."""
    
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=254, required=True)
    message = forms.CharField(widget=forms.Textarea)