#Create a function, yell, which accepts a single string argument.
# It should return(not print) an uppercased version of the string
# with an exclamation point added at the end.
# For example: yell("go away") # "GO AWAY!"   yell("leave me alone") # "LEAVE ME ALONE!"


def yell (phrase):
    loud_phrase = (phrase.upper()+"!")
    return loud_phrase

phrase = input("What are you saying? ")

noisy = yell (phrase)

print (noisy)

