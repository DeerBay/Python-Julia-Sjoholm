def input_int(prompt = ""):
    while True:
        try:
            my_int = int(input(prompt))
            #print(x)
        except ValueError:
            print("My int is not a integer")
        #except NameError:
            #print("x is not defined ")
        # except: #använd helt inte så detta är det lata sättet
            #print("Some other kind of error")
        else:
            return my_int

age = input_int('Input age: ')
length = input_int('Input length: ')
weight = input_int('Input weight ')

print(f"x = {age}, lenght = {length}, weight = {weight}")

def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

################################################################################
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def input_float(prompt = "" ):
    while True:
        try:
            my_float = float(input(prompt))
        except ValueError:
            print("My int is not a integer")
        else:
            return my_float

user_width = input_float("Input width for pokemon: ")
user_height = input_float("Input height for pokemon: ")

distances = []
# Loop through each test point
for test_point in test_points:
    closest_pokemon = None
    min_distance = 999999
    
    # Loop through each Pichu and Pikachu data point
    for pokemon_point in pokemon_data:
        distance = euclidean_distance(test_point, pokemon_point)
        if distance < min_distance:
            min_distance = distance
            closest_pokemon = pokemon_point