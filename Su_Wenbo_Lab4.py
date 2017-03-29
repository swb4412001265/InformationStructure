# Wenbo Su's Lab4
#define a class inheitance from Exception
class ExpectionHandler (Exception) :
    def __init__(self):
        pass
    def __str__(self):
        return ("Exception raised because '#' found.")


def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if name_input.find('#') > -1:
        raise (ExpectionHandler)

try:
    get_name()
except ExpectionHandler:
    print(ExpectionHandler.__str__(ExpectionHandler))


