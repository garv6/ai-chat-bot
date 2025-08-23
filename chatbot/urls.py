# chatbot/urls.py
from django.urls import path
from .views import farmer_view,farmer_response,education_view,women_view,health_view,education_response,women_response,health_response

urlpatterns = [
    path('farmer/', farmer_view, name='farmer_chatbot_view'),  # Route for farmer chatbot page
    path('farmer/response/', farmer_response, name='farmer_response'),  # Route for farmer chatbot responses

    path('education/', education_view, name='education_chatbot_view'),  # Route for education chatbot page
    path('education/response/', education_response, name='education_response'),  # Route for education chatbot responses

    path('health/', health_view, name='health_chatbot_view'),  # Route for health chatbot page
    path('health/response/', health_response, name='health_response'),  # Route for health chatbot responses

    path('women/', women_view, name='women_chatbot_view'),  # Route for women chatbot page
    path('women/response/', women_response, name='women_response'),  # Route for women chatbot responses
]
