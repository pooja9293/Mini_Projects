# Mad Libs Game

# Story template with placeholders
story = """
Once upon a time in a [adjective] [place], there lived a [noun]. This [noun] had a [adjective] [pet] named [name]. 
One day, they decided to go on an adventure to find the [adjective] [treasure]. On their way, they encountered a [adjective] [animal]. 
It was a [size] and [color] [animal] that made a [sound]. It tried to [verb] them, but they managed to escape.
Finally, they reached the [place] and found the [treasure], which was full of [plural_noun]. They were [emotion] and [verb] all day long.
The end.
"""

# Ask the player for words to fill in the placeholders
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
noun = input("Enter a noun: ")
pet = input("Enter a type of pet: ")
name = input("Enter a name: ")
treasure_adjective = input("Enter an adjective for the treasure: ")
animal_adjective = input("Enter an adjective for the animal: ")
size = input("Enter a size (e.g., small, large): ")
color = input("Enter a color: ")
animal_sound = input("Enter a sound the animal makes: ")
verb = input("Enter a verb: ")
plural_noun = input("Enter a plural noun: ")
emotion = input("Enter an emotion: ")

# Fill in the story with the player's words
filled_story = story.replace("[adjective]", adjective)
filled_story = filled_story.replace("[place]", place)
filled_story = filled_story.replace("[noun]", noun)
filled_story = filled_story.replace("[pet]", pet)
filled_story = filled_story.replace("[name]", name)
filled_story = filled_story.replace("[treasure]", treasure_adjective)
filled_story = filled_story.replace("[animal]", animal_adjective)
filled_story = filled_story.replace("[size]", size)
filled_story = filled_story.replace("[color]", color)
filled_story = filled_story.replace("[sound]", animal_sound)
filled_story = filled_story.replace("[verb]", verb)
filled_story = filled_story.replace("[plural_noun]", plural_noun)
filled_story = filled_story.replace("[emotion]", emotion)

# Display the filled-in story
print("\nHere's your Mad Libs story:\n")
print(filled_story)
