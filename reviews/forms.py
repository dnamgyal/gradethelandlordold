from django.forms import ModelForm, Textarea
from reviews.models import Review

class ReviewForm(ModelForm):
	class Meta:
		model = Review
		fields = ['rating', 'communication', 'address', 'apt_condition', 'rent_again','maintenance_eff', 'comment']
		widgets = {
			'comment': Textarea(attrs={'cols': 50, 'rows': 15})}
