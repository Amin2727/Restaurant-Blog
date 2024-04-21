from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
	"""This form is related to restaurant reservations."""
	
	class Meta:
		model = Reservation
		fields = "__all__"