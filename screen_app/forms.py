# forms.py
from django import forms
from .models import Station, ProductMedia

class StationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ['name', 'products', 'manager', 'selected_media']
        widgets = {
            'products': forms.CheckboxSelectMultiple(),
            'selected_media': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(StationForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields['selected_media'].queryset = ProductMedia.objects.filter(product__in=self.instance.products.all())
        else:
            self.fields['selected_media'].queryset = ProductMedia.objects.none()
