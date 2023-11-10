# myapp/views.py
import json

from datetime import datetime, timedelta
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from .forms import CustomUserCreationForm
from .models import *
@csrf_exempt
def register(request):
    print(request.method)
    if request.method == 'POST':
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)

            # Extract username, password, and email from the JSON data
            username = data["username"]
            password = data["password"]
            email = data["email"]

            # Create a form with the extracted data
            form = CustomUserCreationForm(data={'username': username, 'password': password, 'email': email})

            if form.is_valid():
                user = form.save()
                login(request, user)
                return JsonResponse({'message': 'User registered and logged in successfully'})
            else:
                return JsonResponse({'error': 'Invalid form data'}, status=400)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def create_game_view(request):
    # Create a new game object
    try:
        # Create a new game object
        current_time = datetime.now()

        # Calculate the end time as 60 minutes from the start time
        end_time = current_time + timedelta(minutes=60)

        # Create a new game object with the current time and end time
        new_game = Game(start_time=current_time, end_time=end_time)

        # Save the game object to the database
        new_game.save()

        game_json = serializers.serialize("json", [new_game])

        # Parse the serialized JSON
        game_data = json.loads(game_json)[0]

        # Return a success response
        return JsonResponse(game_data)

    except Exception as e:
        # Handle any exceptions or errors
        return JsonResponse({'error': str(e)}, status=500)

    

def join_game(request, game_id):
    try:
        game = Game.objects.get(pk=game_id)
        default_starting_balance = game.starting_balance

        # Create a new player profile with the default starting balance
        player_profile = PlayerProfile(starting_balance=default_starting_balance, current_balance=default_starting_balance)
        player_profile.save()

        payload_json = serializers.serialize("json", [game, player_profile])

        payload_data = json.loads(payload_json)

        # Associate the player profile with the game
        game.player_profiles.add(player_profile)

        return JsonResponse(payload_data)
    except Game.DoesNotExist:
        return JsonResponse({'error': 'Game not found'}, status=404)

