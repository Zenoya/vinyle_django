from django.forms import ModelForm, TextInput, EmailInput
from django.forms.utils import ErrorList
from .models import Contact

class ParagrapheErrorList(ErrorList):

    def __str__(self):
        return self.as_div()

    def as_div(self):
        if not self: return ''
        return '<div class="errorList">%s</div>' % ''.join(['<p class="smallerror">%s</p>' % e for e in self])


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email"]
        widget = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'})
        }
