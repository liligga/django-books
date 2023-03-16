from django import forms
from .models import Book, Author, Publisher


class BookForm(forms.ModelForm):
    # publication_date = forms.DateField(
    #     widget=forms.SelectDateWidget(
    #         # empty_label=("Choose Year", "Choose Month", "Choose Day"),
    #     ),
    # )
    class Meta:
        model = Book
        fields = ('__all__')
        widgets = {
            'publication_date': forms.DateInput(
            format=('%Y-%m-%d'),
            attrs={ 
                'placeholder': 'Select a date',
                'type': 'date'
            }),
        }


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
