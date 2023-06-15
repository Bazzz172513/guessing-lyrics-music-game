import pyttsx3
import time
import random

# Define the verses of the songs
verses_just_the_way_you_are = [
    "When I see your face",
    "There's not a thing that I would change",
    "Cause you're amazing",
    "Just the way you are"
]

verses_shake_it_off = [
    "Cause the players gonna play, play, play, play, play",
    "And the haters gonna hate, hate, hate, hate, hate",
    "Baby, I'm just gonna shake, shake, shake, shake, shake",
    "I shake it off, I shake it off"
]

verses_baby = [
    "You know you love me, I know you care",
    "Just shout whenever, and I'll be there",
    "You are my love, you are my heart",
    "And we will never, ever, ever be apart"
]

verses_set_fire_to_the_rain = [
    "Sometimes I wake up by the door",
    "That heart you caught must be waiting for you",
    "Even now, when we're already over",
    "I can't help myself from looking for you"
]

verses_easy_on_me = [
    "Go easy on me, baby",
    "I was still a child",
    "Didn't get the chance to",
    "Feel the world around me"
]

verses_glimpe_of_us = [
    "Cause sometimes I look in her eyes",
    "And that's where I find a glimpse of us",
    "And I try to fall for her touch",
    "But I'm thinking of the way it was"
]

verses_let_me_down_slowly = [
    "Don't cut me down, throw me out, leave me here to waste",
    "I once was a man with dignity and grace",
    "Now I'm slippin' through the cracks of your cold embrace",
    "So please, please"
]

verses_when_i_was_your_man = [
    "I hope he buys you flowers",
    "I hope he holds your hand",
    "Give you all his hours",
    "When he has the chance"
]

verses_somewhere_only_we_know = [
    "Oh, simple thing, where have you gone?",
    "I'm gettin' old, and I need something to rely on",
    "So, tell me when you're gonna let me in",
    "I'm gettin' tired, and I need somewhere to begin"
]

verses_you_belong_with_me = [
    "If you could see that I'm the one",
    "Who understands you",
    "Been here all along",
    "So, why can't you see?"
]

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to play a verse
def play_verse(verse):
    engine.say(verse)
    engine.runAndWait()
    time.sleep(1)  # Add a pause between verses

# Function to select a random song
def select_song():
    song = random.choice(["just_the_way_you_are", "shake_it_off", "baby", "set_fire_to_the_rain", "easy_on_me", "glimpe_of_us", "let_me_down_slowly", "when_i_was_your_man", "somewhere_only_we_know", "you_belong_with_me"])
    return song

# Game loop
while True:
    # Select a random song
    song = select_song()

    # Play the verses based on the selected song
    if song == "just_the_way_you_are":
        for verse in verses_just_the_way_you_are:
            play_verse(verse)
    elif song == "shake_it_off":
        for verse in verses_shake_it_off:
            play_verse(verse)
    elif song == "baby":
        for verse in verses_baby:
            play_verse(verse)
    elif song == "set_fire_to_the_rain":
        for verse in verses_set_fire_to_the_rain:
            play_verse(verse)
    elif song == "easy_on_me":
        for verse in verses_easy_on_me:
            play_verse(verse)
    elif song == "glimpe_of_us":
        for verse in verses_glimpe_of_us:
            play_verse(verse)
    elif song == "let_me_down_slowly":
        for verse in verses_let_me_down_slowly:
            play_verse(verse)
    elif song == "when_i_was_your_man":
        for verse in verses_when_i_was_your_man:
            play_verse(verse)
    elif song == "somewhere_only_we_know":
        for verse in verses_somewhere_only_we_know:
            play_verse(verse)
    elif song == "you_belong_with_me":
        for verse in verses_you_belong_with_me:
            play_verse(verse)

    # Ask the player to guess the song's name
    guess = input("Guess the name of the song: ")

    # Check if the guess is correct
    if song == "just_the_way_you_are" and guess.lower() == "just the way you are":
        print("Congratulations! You guessed it right!")
    elif song == "shake_it_off" and guess.lower() == "shake it off":
        print("Congratulations! You guessed it right!")
    elif song == "baby" and guess.lower() == "baby":
        print("Congratulations! You guessed it right!")
    elif song == "set_fire_to_the_rain" and guess.lower() == "set fire to the rain":
        print("Congratulations! You guessed it right!")
    elif song == "easy_on_me" and guess.lower() == "easy on me":
        print("Congratulations! You guessed it right!")
    elif song == "glimpe_of_us" and guess.lower() == "glimpe of us":
        print("Congratulations! You guessed it right!")
    elif song == "let_me_down_slowly" and guess.lower() == "let me down slowly":
        print("Congratulations! You guessed it right!")
    elif song == "when_i_was_your_man" and guess.lower() == "when i was your man":
        print("Congratulations! You guessed it right!")
    elif song == "somewhere_only_we_know" and guess.lower() == "somewhere only we know":
        print("Congratulations! You guessed it right!")
    elif song == "you_belong_with_me" and guess.lower() == "you belong with me":
        print("Congratulations! You guessed it right!")
    else:
        print("Oops! That's not the correct song. The correct song is '{}'.".format(song.capitalize()))

    # Ask if the player wants to replay
    replay = input("Would you like to play again? (yes/no): ")
    if replay.lower() != "yes":
        break

# Clean up the text-to-speech engine
engine.stop()
