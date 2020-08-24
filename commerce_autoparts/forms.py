from django.forms import ModelForm
from .models import OrderRequest, PurchaseUpdate

class CreateRequestForm(ModelForm):
    class Meta:
        model = OrderRequest
        fields = '__all__'
        exclude = [
            'user',
            'ref_code'
                   ]

class PurchaseUpdateForm(ModelForm):
    class Meta:
        model = PurchaseUpdate
        fields = '__all__'