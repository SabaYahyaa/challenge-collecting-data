import numpy as np
import pdb


#     # ask to the player to enter a letter
#     def play (self):
#
#         while True:
#             x=input("Please, enter a letter")
#
#             if len(x) == 1 and x.isalpha():
#                 print("yyes")
#             else:
#                 print("please, enter a letter to continue playing")
#                 return
#
#     def start_game(self):
#         print(self.life)
#         # while self.life>0:
#         #     x=self.play()
#         #     print(" here")
#         return

class Hangman:
    def __init__(self, life=0, good_word=[], well_guessed_letters=[],bad_guessed_letters=[], turn_count=0, error_count=0,good_answers=0):
        self.__life=5
        self.__good_word=['H','E','L','L','O']
        self.__well_guessed_letters=["-" for x in range(5)]
        self.__bad_guessed_letters=bad_guessed_letters
        self.__turn_count=0
        self.__error_count=0
        self.__good_answers=0

    # this is a property that returns the good word
    def getgood_word(self):
        return self.__good_word
    good_word= property(getgood_word)

    #this is a property that returns the bad letter list,
    def getbad_guessed_letters(self):
        return self.__bad_guessed_letters
    def setbad_guessed_letters(self, letter):
        if letter not in self.__good_word:
            self.__bad_guessed_letters.append(letter)
    bad_guessed_letters=property(getbad_guessed_letters, setbad_guessed_letters)

    # this is a property that returns  and set the number of life,
    def getlife(self):
        print('getname() called')
        return self.__life - 1
    def setlife(self, life):
        print('setname() called')
        self.__life = life
    life = property(getlife, setlife)

    #this is a property that returns well_guessed_letters,
    def getwell_guessed_letters(self):
        return self.__well_guessed_letters
    def setwell_guessed_letters(self, input_letter):
        input_letter_capital = input_letter.capitalize()
        if input_letter_capital in self.__good_word: #if the input letter inside, update
             z = np.where(np.array(self.__good_word) == input_letter_capital)
             if len(z[0]) >= 1:
                 for i in z[0]:
                     self.__well_guessed_letters[i] = input_letter_capital
    #         return (initial_guess)
    #
        else: #do not update
             self.__well_guessed_letters

    well_guessed_letters=property(getwell_guessed_letters, setwell_guessed_letters)

   # # ###############################
   # # ###############################
   # # ###############################
   # # ##########         well_guessed_letters as a method
   # # ###############################
   # # ###############################
   # # ###############################
   # # takes the good_word list, the input letter by player, the initial well_guessed_letters list
   # # and returns the updated well_guessed_letters
   #  def well_guessed_letters(self, input_letter, initial_guess, good_word):
   #     input_letter_capital = input_letter.capitalize()
   #
   #     if input_letter_capital in good_word: #if the input letter inside, update
   #         z = np.where(np.array(good_word) == input_letter_capital)
   #         if len(z[0]) >= 1:
   #             for i in z[0]:
   #                 initial_guess[i] = input_letter_capital
   #         return (initial_guess)
   #
   #     else: #do not update
   #         return (initial_guess

    # this is a property that returns the turn_count (number of playing)
    def getturn_count(self):
        self.__turn_count +=1
        return self.__turn_count
    def setturn_count(self):
        return self.__turn_count
    turn_count = property(getturn_count,setturn_count)

    # this is a property that computes the error_count,
    def geterror_count(self):
        return self.__error_count
    def seterror_count(self, letter):
        if letter not in self.__good_word:
            self.__error_count +=1
    error_count = property(geterror_count, seterror_count)

    # this is a property that computes the good_answers,
    def getgood_answers(self):
        return self.__good_answers
    def setgood_answers(self, letter):
        if letter in self.__good_word:
            self.__good_answers += 1
    good_answers = property(getgood_answers, setgood_answers)

    def play(self):
        x=input("Please, enter a letter")
        if len(x) == 1 and x.isalpha():
            print("correct enter")
            return (x)
        else:
            print("please, enter a letter to continue playing")
            return

if __name__ == '__main__':
    #### To DO: use input, while later
    #the following code have to be in the start_game
    han=Hangman() #create an instance
    first_call=han.life #each time you play, get the number of lifes that you have which shoul not be bigger than the number of playing
    print(first_call)
    #set, after finishing playing, set the lif
    han.life=4
    print(han.life)
    print(han.good_word) #get the good_word only, this is fixed

    # print(han.bad_guessed_letters) #get bad_guessed_letters
    han.bad_guessed_letters='p'

    print(han.bad_guessed_letters)
    print("-------------")
    han.well_guessed_letters='p'
    print(han.well_guessed_letters)

    print(han.turn_count)
    pdb.set_trace()
    # print("--------------- checking well_guessed_letters method-----------------")
    # input_letter='l'
    # #initialize the guessed_letters
    # initial_guess=["-" for x in range(5)]
    # # good_word=['H','E','L','L','O']
    # print(han.well_guessed_letters(input_letter,initial_guess,han.good_word))



    #
    # print("--------------- checking well_guessed_letters property-----------------")
    # input_letter='l'
    # # initialize the guessed_letters
    # initial_guess=["-" for x in range(5)]
    # good_word=['H','E','L','L','O']
    #
    # han.well_guessed_letters=(input_letter,initial_guess,good_word)
    # print(han.well_guessed_letters)


