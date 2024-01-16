from django import forms
from django.core.validators import RegexValidator, ValidationError
from .models import User


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["fullname", "phone", "message"]

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        phone_validator = RegexValidator(
            regex=r'^\+998[123456789]\d{8}$',
            message='Telefon raqamingizni to\'g\'ri kiriting, masalan: +998901234567',
            code='invalid_phone_number'
        )
        try:
            phone_validator(phone)
        except ValidationError as e:
            raise forms.ValidationError(e.messages)

        return phone
