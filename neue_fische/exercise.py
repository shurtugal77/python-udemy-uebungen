# Force definition of global variables in functions
def forceGlobal():
    global var
    var = "ick bin global"

forceGlobal()

print(var)


# Change (global) variables within functions
x = "super toller Wert"

def uiToll():
    global x
    x = "ein anderer Wert"

print(x)
uiToll()
print(x)

