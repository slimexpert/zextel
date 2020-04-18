from django import froms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50)


	def save(self):
		new_contact = 