from django import forms
from .models import contact_support
from django.core.exceptions import ValidationError

class ContactForm(forms.Form):
	categoria_choices = [('Общий вопрос','Общий вопрос'), ('Финансовый вопрос','Финансовый вопрос')]
	otvet_choices = [('По e-mail','По e-mail'), ('По телефону','По телефону')]
	name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=100)
	tel = forms.CharField(max_length=14)
	cat = forms.ChoiceField(widget=forms.Select, choices=categoria_choices)
	text = forms.CharField(widget=forms.Textarea)
	otvet = forms.ChoiceField(widget=forms.RadioSelect, choices=otvet_choices)

	name.widget.attrs.update({'class':'form-control required', 'placeholder':'Введите ваше имя'})
	email.widget.attrs.update({'class':'form-control required', 'placeholder':'user@mail.ru'})
	tel.widget.attrs.update({'class':'form-control required', 'placeholder':'+7(000)000 00 00'})
	cat.widget.attrs.update({'class':'form-control required'})
	text.widget.attrs.update({'class':'form-control required', 'col':'30', 'rows':'5'})
#	otvet.widget.attrs.update({'class':'btn btn-outline-secondary ls0 nott'})

	def clean_text(self):
		new_text = self.cleaned_data['text']
		if len(new_text) < 10:
			raise ValidationError('Очень короткое сообщение')
		return new_text


	def save(self):
		new_contact_support = contact_support.objects.create(
		supp_name=self.cleaned_data['name'],
		supp_email=self.cleaned_data['email'],
		supp_tel=self.cleaned_data['tel'],
		supp_cat=self.cleaned_data['cat'],
		supp_text=self.cleaned_data['text'],
		supp_otvet=self.cleaned_data['otvet'],
		)
		return new_contact_support
