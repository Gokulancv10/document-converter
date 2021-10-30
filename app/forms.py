from django import forms


class UploadFileForm(forms.Form):

    image = forms.ImageField()

    class Meta:
        fields = ("image",)