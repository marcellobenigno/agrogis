from django import forms


class SearchForm(forms.Form):
    nome = forms.CharField(label='Nome do Imóvel Rural',
                           required=False,
                           widget=forms.TextInput(
                               attrs={
                                   'class': 'form-control',
                                   'placeholder': 'Ex.: Fazenda Alegria'
                               }
                           )
                           )

    proprietario = forms.CharField(label='Nome do Proprietário',
                                   required=False,
                                   widget=forms.TextInput(
                                       attrs={
                                           'class': 'form-control',
                                           'placeholder': 'Ex.: João dos Santos'
                                       }
                                   )
                                   )

    cpf = forms.CharField(label='CPF',
                          required=False,
                          widget=forms.TextInput(
                              attrs={
                                  'class': 'form-control',
                                  'placeholder': 'Ex.: 12345678901'
                              }
                          )
                          )
