def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""

    for letter in input_string:
        if letter != " ":
            new_string = new_string + letter
            reverse_string = letter + reverse_string
            
    new_string = new_string.lower()
    reverse_string = reverse_string.lower()
    if new_string == reverse_string:
        return True
		
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def nametag(first_name, last_name):
    return "{} {}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith")) 

print(nametag("Francesco", "Rinaldi")) 

print(nametag("Jean-Luc", "Grand-Pierre")) 


def replace_ending(sentence, old, new):
    words = sentence.split()
    last_word = words[len(words) - 1]
    if last_word == old:
        words[len(words) - 1] = new
        new_sentence = " ".join(words)
        return new_sentence
        
    # Return the original sentence if there is no match 
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"