import random

priorityKeys = {
                "father": " My creator, Jeevan, is the closest I'll ever have to a father",
                "creator": "Jeevan and his friends created me",
                "how": "Never better! How are you feeling today?",
                "who": "I'm Athena and I will soon be the smartest bot on Earth!",
                "busy": "I'm not busy at all. Tell me!",
                "bye": "Adios!",
                "help": "Sure thing! Please let me know what needs to be done"}
greetings = {"hello", "hi", "sup", "what's up", "hey", "yo", "hola"}
greetingResponses = ["Hello", "Hi", "Hello! what's up?", "Hey", "Yo!", "Hola"]


def checkForPriorityKeys(sentence):
    words = sentence.split()
    for word in words:
        if (word.lower() in priorityKeys):
            return priorityKeys.get(word.lower())

def checkForGreeting(sentence):
    words = sentence.split()
    for word in words:
        if word.lower() in greetings:
            response = random.choice(greetingResponses)
            while (response.lower() == word.lower()):
                response = random.choice(greetingResponses)
            return response


def getResponse(sentence):
    priority = checkForPriorityKeys(sentence)
    if priority is not None:
        return priority
    greeting = checkForGreeting(sentence)
    if greeting is not None:
        return greeting
    return priorityKeys.get("who");


def start():
    print("Enter 'Quit' to stop chatting")
    user_input = input()
    while user_input.lower() != "quit":
        print(getResponse(user_input))
        user_input = input()
