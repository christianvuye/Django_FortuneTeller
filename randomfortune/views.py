from multiprocessing import context
from django.shortcuts import render
import random

# Create your views here.
fortuneList = [
    "All will go well with your new project.",
    "If you continually give, you will continually have.",
    "Self-knowledge is a life long process.",
    "You are busy, but you are happy.",
    "Your abilities are unparalleled.",
    "Those who care will make the effort.",
    "Now is the time to try something new.",
    "Miles are covered one step at a time.",
    "Don’t just think, act!"
]

nameList = [
    "Christian",
    "Pablo",
    "Sebastian",
    "Zishan"
]


def fortune(request):
    fortune = random.choice(fortuneList)
    name = random.choice(nameList)
    context = {"fortune": fortune, "name": name}
    return render(request, "randomfortune/fortune.html", context)
