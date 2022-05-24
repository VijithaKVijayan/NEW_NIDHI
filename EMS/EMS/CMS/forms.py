from CMS.models import Admin, LevelOne, LevelTwo, LevelThree, Customer
from django.forms import ModelForm

class AdminHeadForm(ModelForm):
     class Meta:
        model = Admin
        fields = '__all__'


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class LevelOneHeadForm(ModelForm):
    class Meta:
        model = LevelOne
        fields = '__all__'


class LevelTwoHeadForm(ModelForm):
    class Meta:
        model = LevelTwo
        fields = '__all__'


class LevelThreeHeadForm(ModelForm):
    class Meta:
        model = LevelThree
        fields = '__all__'
