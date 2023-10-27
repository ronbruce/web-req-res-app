from flask import Flask
from random import randint

app = Flask(__name__)
# URL of my webpage
@app.route('/')
def homepage():
# Docstring describes a route in a readable way for a human.
    return 'Are you there, world? It\'s, me, Ducky!'

# Route for favorite animal
# Any value the user type in will be available in the <user_animal> variable
@app.route('/animal/<users_animal>')
# My function for the route that takesmy variable as a parameter.
def favorite_animal(users_animal):
    return f'Wow, {users_animal} is my favorite animal, too!'

# Route for favorite desset
@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def funny_story(adjective,noun):
    return f'{noun} is the {adjective} of all Saiyans!'

# Multiply 2 Numbers
# Hence I placed the variables number1 and number2 into a variable called multiplication_answer
# # When I perform my multiplication operation in the url, the numbers will know they have to multiply.
# That answer will be shown in my browser, just like magic.
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2): 
    multiplication_answer = int(number1) * int(number2)
    return f'{number1} times {number2} is {multiplication_answer}'

# Say N Times route: Say a word a particular number of times
@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    repeated_word = " ".join([word] * int(n))
    return repeated_word

# Dice game that utlizes randint()
# Returns a random dice roll when you refresh the page.
@app.route('/dicegame')
def roll_dice():
    random_dice_roll = randint(1, 6)
    if random_dice_roll == 6:
        return(f'You rolled a {random_dice_roll}. You won!')
    else:
        return(f'You rolled a {random_dice_roll}. You lost') 

# Tell Python how to run the server
if __name__ == '__main__':
    app.run(debug=True)



