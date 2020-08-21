from django.forms import ModelForm
from .models import OrderRequest

class CreateRequestForm(ModelForm):
    class Meta:
        model = OrderRequest
        fields = '__all__'
        exclude = [
            'user',
            'ref_code'
                   ]

