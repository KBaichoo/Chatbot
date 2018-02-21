#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PA6, CS124, Stanford, Winter 2018
# v.1.0.2
# Original Python code by Ignacio Cases (@cases)
######################################################################
import csv
import math
import re
import numpy as np
from collections import defaultdict
from movielens import ratings
from random import randint

class Chatbot:
    """Simple class to implement the chatbot for PA 6."""

    #############################################################################
    # `moviebot` is the default chatbot. Change it to your chatbot's name       #
    #############################################################################
    def __init__(self, is_turbo=False):
      self.name = 'reelbot'
      self.is_turbo = is_turbo
      self.read_data()
      self.rated = defaultdict(lambda: 0)

    #############################################################################
    # 1. WARM UP REPL
    #############################################################################

    def greeting(self):
      """chatbot greeting message"""
      #############################################################################
      # TODO: Write a short greeting message                                      #
      #############################################################################

      greeting_message = """
      Hi there! Let\'s talk about movies so I can recommend one to you. Tell me about
      a movie you have seen, and if you liked it!
      """


      #############################################################################
      #                             END OF YOUR CODE                              #
      #############################################################################

      return greeting_message

    def goodbye(self):
      """chatbot goodbye message"""
      #############################################################################
      # TODO: Write a short farewell message                                      #
      #############################################################################

      goodbye_message = 'Bye for now!'

      #############################################################################
      #                             END OF YOUR CODE                              #
      #############################################################################

      return goodbye_message


    #############################################################################
    # 2. Modules 2 and 3: extraction and transformation                         #
    #############################################################################

    def process(self, input):
      """Takes the input string from the REPL and call delegated functions
      that
        1) extract the relevant information and
        2) transform the information into a response to the user
      """

      sentiments = defaultdict(lambda: 0)
      word_list = open("data/sentiment.txt").read().split()
      for item in word_list:
          pairing = item.split(',')
          if pairing[1]=='neg':
              sentiments[pairing[0]] = -1
          else:
              sentiments[pairing[0]] = 1

      supplemental_pos = open("deps/liked").read().split()
      pos_set = set(supplemental_pos)

      supplemental_neg = open("deps/disliked").read().split()
      neg_set = set(supplemental_neg)

      movie = r"\"(\w+)\""

      if self.is_turbo == True:
        response = 'processed %s in creative mode!!' % input
      else:
          if len(self.rated)==5:

              # recommendation = self.

              response = '''
              Thanks so much! I think you will like \"%s\" based on our chat.
              If you'd like to hear another recommendation, tell me about another movie!
              Otherwise, enter :quit to exit :)
              ''' % recommendation

              rated.clear()
              return response

          while len(self.rated)<6:

            title = ' '
            parses = []
            parses = re.findall(movie, input)

            if not parses:
                response = "Sorry, I\'m not sure which movie you're talking about. Can you try again?"
                return response
            else:
                if len(parses) > 1:
                    response = "Can you tell me about movies one at a time?"
                    return response
                title = parses[0]

            words = input.split(' ')
            for word in words:
                if word in pos_set:
                    self.rated[title] = 1
                    break
                elif word in neg_set:
                    self.rated[title] = -1
                    break
                elif word in sentiments:
                    self.rated[title] = sentiments[word]
                    break

            if self.rated[title] == ' ':
                response = 'I\'m sorry, I can\'t tell if you liked \"%s\". Can you tell me more about \"%s\"?' % title
                return response
            else:
                sentiment = ' '
                if self.rated[title]==1:
                    sentiment = 'liked'
                else:
                    sentiment = 'disliked'
                response = "I see you %s \"%s\". Can you tell me about another movie?" % (sentiment, title)
                return response

      return response


    #############################################################################
    # 3. Movie Recommendation helper functions                                  #
    #############################################################################

    def read_data(self):
      """Reads the ratings matrix from file"""
      # This matrix has the following shape: num_movies x num_users
      # The values stored in each row i and column j is the rating for
      # movie i by user j
      self.titles, self.ratings = ratings()
      reader = csv.reader(open('data/sentiment.txt', 'rb'))
      self.sentiment = dict(reader)


    def binarize(self):
      """Modifies the ratings matrix to make all of the ratings binary"""

      pass


    def distance(self, u, v):
      """Calculates a given distance function between vectors u and v"""
      # TODO: Implement the distance function between vectors u and v]
      # Note: you can also think of this as computing a similarity measure

      pass


    def recommend(self, u):
      """Generates a list of movies based on the input vector u using
      collaborative filtering"""
      # TODO: Implement a recommendation function that takes a user vector u
      # and outputs a list of movies recommended by the chatbot

      pass


    #############################################################################
    # 4. Debug info                                                             #
    #############################################################################

    def debug(self, input):
      """Returns debug information as a string for the input string from the REPL"""
      # Pass the debug information that you may think is important for your
      # evaluators
      debug_info = 'debug info'
      return debug_info


    #############################################################################
    # 5. Write a description for your chatbot here!                             #
    #############################################################################
    def intro(self):
      return """
      Your task is to implement the chatbot as detailed in the PA6 instructions.
      Remember: in the starter mode, movie names will come in quotation marks and
      expressions of sentiment will be simple!
      Write here the description for your own chatbot!
      """


    #############################################################################
    # Auxiliary methods for the chatbot.                                        #
    #                                                                           #
    # DO NOT CHANGE THE CODE BELOW!                                             #
    #                                                                           #
    #############################################################################

    def bot_name(self):
      return self.name


if __name__ == '__main__':
    Chatbot()
