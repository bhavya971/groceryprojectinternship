from django import forms
from .models import ContactMessage,Review  # Make sure to import your ContactMessage model


class CartForm(forms.Form):
    quantity=forms.IntegerField(initial='1')
    product_id=forms.IntegerField(widget=forms.HiddenInput)

    def __init__(self,request,*args,**Kwargs):
       self.request=request
       super(CartForm,self).__init__(*args,**Kwargs)

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['review']
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']