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


