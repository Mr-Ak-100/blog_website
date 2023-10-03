from django import forms


class MessageForm(forms.Form):

    name = forms.CharField(
        max_length=50, widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "نام خود را بنویسید",
            "data-error": "نوشتن نام الزامی است"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "ایمیل خود را بنویسید",
            "data-error": "نوشتن ایمیل الزامی است"
        })
    )

    title = forms.CharField(
        max_length=150, widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "موضوع خود را وارد بنویسید",
            "data-error": "نوشتن موضوع الزامی است"
        })
    )

    body = forms.CharField(
        widget=forms.Textarea(attrs={
            "rows": 4,
            "class": "form-control",
            "placeholder": "متن پیام خود را بنویسید",
            "data-error": "نوشتن متن پیام الزامی است"
        })
    )
