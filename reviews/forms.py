from django.forms import ModelForm, Textarea
from reviews.models import Review, Landlord

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['address','rating',  'apt_condition', 'communication','maintenance_eff', 'rent_again', 'comment']
 		widgets = {
            'comment': Textarea(),
        }
class AddLandlord(ModelForm):
	class Meta:
		model = Landlord
		fields = ['name']
