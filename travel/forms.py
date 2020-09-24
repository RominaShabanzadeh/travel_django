from django import forms

from travel.models import travel_mdl


class travel_frm(forms.ModelForm):
    class Meta():
        model=travel_mdl
        fields=['name','origin','destination','date','time','price']