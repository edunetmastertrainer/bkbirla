from django.shortcuts import render
from .forms import MealPlanForm
import google.generativeai as genai
# Create your views here.

def meal_plan_view(request):
    if request.method == 'POST':
        form = MealPlanForm(request.POST)
        if form.is_valid():
            # Process the form data here
            age = form.cleaned_data['age']
            weight = form.cleaned_data['weight']
            height = form.cleaned_data['height']
            dietary_preferences = form.cleaned_data['dietary_preferences']
            fitness_goal = form.cleaned_data['fitness_goal']
            location = form.cleaned_data['location']
            #Prompt
            prompt = f"Create a weekly meal plan for a {age} years old person, whose weight is {weight} and heightn is {height}.The person is following a {dietary_preferences} diet and has a fitness goal of {fitness_goal}. The person lives in {location}. I need response in a table format with days of the week and meals for each day. generate only table using html tags and border of table will be 2."
            #configurse API key
            genai.configure(api_key="AIzaSyAKouGm88-mTo6MxDqD-Ljp_-GAINizNLA")
            #model
            model = genai.GenerativeModel("gemini-2.5-flash")
            response = model.generate_content(prompt)
            
            return render(request, 'meal_plan_result.html', {'response': response.text})
    else:
        form = MealPlanForm()
    
    return render(request, 'meal_plan_form.html', {'form': form})
