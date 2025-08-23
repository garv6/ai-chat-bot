# chatbot/views.py
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .farmerbot import load_intents_farmer, train_chatbot_farmer, get_response_farmer
from .educationbot import load_intents_education, train_chatbot_education, get_response_education
from .womenbot import load_intents_women, train_chatbot_women, get_response_women
from .healthbot import load_intents_health, train_chatbot_health, get_response_health

# Load intents and train your models separately for each domain
# Farmer model variables
farmer_file_path = 'farmer.json'  # Path to your intents file for Farmer
farmer_intents = load_intents_farmer(farmer_file_path)
farmer_vectorizer, farmer_label_encoder, farmer_model = train_chatbot_farmer(farmer_intents)

# Education model variables
education_file_path = 'education.json'  # Path to your intents file for Education
education_intents = load_intents_education(education_file_path)
education_vectorizer, education_label_encoder, education_model = train_chatbot_education(education_intents)

# Women model variables
women_file_path = 'women.json'  # Path to your intents file for Women
women_intents = load_intents_women(women_file_path)
women_vectorizer, women_label_encoder, women_model = train_chatbot_women(women_intents)

# Health model variables
health_file_path = 'health.json'  # Path to your intents file for Health
health_intents = load_intents_health(health_file_path)
health_vectorizer, health_label_encoder, health_model = train_chatbot_health(health_intents)

# Views for rendering HTML templates for each domain
def farmer_view(request):
    return render(request, 'farmer.html')  # Render the Farmer chatbot template

def education_view(request):
    return render(request, 'education.html')  # Render the Education chatbot template

def women_view(request):
    return render(request, 'women.html')  # Render the Women chatbot template

def health_view(request):
    return render(request, 'health.html')  # Render the Health chatbot template

# Response functions for each chatbot model
@csrf_exempt
def farmer_response(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get('message')
        # Use farmer-specific model, vectorizer, and label encoder
        response = get_response_farmer(user_input, farmer_vectorizer, farmer_label_encoder, farmer_model, farmer_intents)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def education_response(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get('message')
        # Use education-specific model, vectorizer, and label encoder
        response = get_response_education(user_input, education_vectorizer, education_label_encoder, education_model, education_intents)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def women_response(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get('message')
        # Use women-specific model, vectorizer, and label encoder
        response = get_response_women(user_input, women_vectorizer, women_label_encoder, women_model, women_intents)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def health_response(request):
    if request.method == 'POST':
        user_input = json.loads(request.body).get('message')
        # Use health-specific model, vectorizer, and label encoder
        response = get_response_health(user_input, health_vectorizer, health_label_encoder, health_model, health_intents)
        return JsonResponse({'response': response})
    return JsonResponse({'error': 'Invalid request'}, status=400)
