def sentence_maker(phrase):
    interrogatives = ("how","who","why")
    capitalized = phrase.title()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    

results = []
while True:
    user_input = input("Say Something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))
    
print(" ".join(results))
