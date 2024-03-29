# Functions with Outputs

def formatName(firstName, lastName):
    if firstName == '' or lastName == '':
        return "An empty string was provided as Input."
    formatedFirstName = firstName.title()
    formatedLastName = lastName.title()
    formatedFullName = formatedFirstName + ' ' +formatedLastName
    return formatedFullName

myName = formatName("Robert", "HoHeNeSTEr")
print(myName)