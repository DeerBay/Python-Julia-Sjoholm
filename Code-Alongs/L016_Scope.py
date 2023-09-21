# In python we have two kind of Scope, life-time of variable.
# Local scope: Only available locally insida a fucktion
# Global scope: Available through execution of program

name = "Fredrik"

def main():
    name = "Kalle"
    print(name)

print(name)
main()
print(name)

# if name == "Fredrik":
#     last_name = "Johansson"

# print(last_name)

# for i in range(2):
#     print(i)

# print(f"i = {i}")

