# Simple Greetings Program

# Friends List
friends = ['blaine', 'mark', 'Jeff', 'brandon', 'Cody', 'nate', 'chris']

# Message Creation Object
def greet(friend):
    print(f'Hello {friends[friend].title()}, how are you today?')

# Greet entire Friends List
for f in friends:
    i = friends.index(f)
    greet(i)

