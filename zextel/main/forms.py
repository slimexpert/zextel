from django import froms

class ContactForm(forms.Form):
	name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	tel = forms.CharField(max_length=14)
	cat = forms.ChoiceField(widget=forms.Select, choices=('Общий вопрос','Финансовый вопрос'))
	text = forms.CharField(widget=forms.Textrea)
	otvet = forms.CharField(widget=forms.CheckboxInput, check_test='True')

	