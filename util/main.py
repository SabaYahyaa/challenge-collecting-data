from game import Hangman

#create a function that will run the class and its property, and play method
def start_game():
    number_of_allowed_playing=5
    han=Hangman()
    #if the number of turn less than 5, play and update all the property
    while han.turn_count < number_of_allowed_playing:
        letter=han.play()
        #set the bad guess
        han.bad_guessed_letters = letter
        # set the well guess
        han.well_guessed_letters=letter
        #compute if there is an error
        han.error_count=letter
        #compute the number of good answers
        han.good_answers=letter

        #after playing, a turn print the following
        print("good answers=", han.good_answers)
        print("bad_guessed_letters_list", han.bad_guessed_letters )
        print("well_guessed_letters list=", han.well_guessed_letters)
        print("error_count=", han.error_count)
        print("number of available playing", han.life)
        print("number of turn playing", han.turn_count)

        return

print(start_game.__doc__)




   