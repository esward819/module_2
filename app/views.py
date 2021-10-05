from typing import List
from django.shortcuts import render
from django.http import HttpResponse
from dataclasses import dataclass
# Create your views here.
@dataclass
class Team:
    team_name: str
    description: str
    team_members: List


def hello_world(request, name):
    context = {
        "name": name, 
        "teams": {"Management": Team("Management", "The Management Team Handles all of the base structure of Base Camp Coding Academy! The main responsibilities of this team is to delegate chores, assign structure and communication within the teams, and overall help Base Camp Coding Academy grow further.", ["Rylee Chisholm", "Logan Coley", "Dylan Goad", "Will Collins", "Daelan Hollingsworth", "Michelle Rankin"]),
        "Community": Team("Community", "Community team helps with planning events, handling birthdays and overall making Base Camp Coding Academy feel more welcoming", ["Jacen Barefoot", "RJay Pickering", "Justin Ashmore", "Logan Wilkins", "Ariyana Neal"]), 
        "Documentation": Team("Documentation", "Documentation team handles the social media aspect of base camp such as posting our guest speakers and the many events the students and faculty alike.", ["Randy Trullet", "Makyla Person", "Isaac Jones", "Ben Crosby", "Ryan Bennett"]),
        "Procurement": Team("Procurement", "Procurement Teams handles the budget and food from a week to week basis. Also factoring in new and diverse ways to spend the budget while saving money and making the people at base camp satisfied", ["Richard Tutor", "Mariann McCord", "Quinton Summerford", "Gary Lane", "Ethan Ward"]) }
    } 
    return render(request, "details.html", context)

def hello_world2(request):
    context = {
        "teams": ["Management", "Procurement", "Documentation", "Community"]
    } 
    return render(request, "Teams.html", context)