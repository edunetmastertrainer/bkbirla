from django import forms

class MealPlanForm(forms.Form):
    dchoice=[
        ('vegetarian', 'Vegetarian'), 
        ('non-vegetarian', 'Non-Vegetarian'),
        ('vegan', 'Vegan')
    ]
    purpose = [
        ('weight_loss', 'Weight Loss'),
        ('muscle_gain', 'Muscle Gain'),
        ('maintenance', 'Maintenance'),
        ('weight_gain', 'Weight Gain')
    ]
    age = forms.IntegerField(label='Age', min_value=0)
    weight = forms.FloatField(label='Weight (kg)', min_value=0)
    height = forms.FloatField(label='Height (cm)', min_value=0)
    dietary_preferences = forms.ChoiceField(label='Dietary Preferences',choices=dchoice)
    fitness_goal = forms.ChoiceField(label='Fitness Goal', choices=purpose)
    location = forms.CharField(label='Location', max_length=100)
    