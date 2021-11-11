from django import forms

CAT_CHOICES = {
    ('RPG', 'RPG'),
    ("FPS", "FPS")
}


class AuctionAddForm(forms.Form):
    name = forms.CharField(label="name")
    start_date = forms.DateField(label="start_date", widget=forms.DateInput)
    end_date = forms.DateField(label="end_date")
    product = forms.CharField(label="product")
