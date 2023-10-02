from django import forms


class CommentForm(forms.Form):

    body = forms.CharField(max_length=300, min_length=25, widget=forms.Textarea(attrs={
        "class": "form-control",
        "placeholder": "متن نظر خود را بنویسید ..",
        "rows": "5"
    }))
