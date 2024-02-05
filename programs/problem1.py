# Loop until \end
# add question marks to question and full stop to end of statments.
# Capitalise the first letter in every sentence.

user_input = ''
end = "\end"
question = ["how","who","why"]
while user_input != end:
    user_input = input("Say Something: ")
    if "how" or "who" or "why" in user_input:
        user_input += "?"
    elif user_input != end:
        user_input.title()
        user_input += "."
    
    print(user_input)