# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 18:11:35 2022

@author: ljd3frf - Levi Davis
"""
import numpy as np
import pandas as pd

class Die:
    
    '''
    A die has N sides, or “faces”, and W weights, and can be rolled to select a face. 
    W defaults to 1.0 for each face but can be changed after the object is created.
    The weights are just numbers, not a normalized probability distribution.
    The die has one behavior, which is to be rolled one or more times.

    Methods
    
        __init__:     
            An initializer
            Takes an array of faces as an argument. The array's data type (dtype) 
            may be strings or numbers.
            Internally iInitializes the weights to 1.0 for each face.
            Saves both faces and weights into a private dataframe that is to be 
            shared by the other methods.
        
        change_weight:
            A method to change the weight of a single side.
            A method to change the weight of a single side.
            Takes two arguments: the face value to be changed and the new weight.
            Checks to see if the face passed is in the array of weights.
            Checks to see if the weight is a float or if it be converted to one.
            
        roll:
            A method to roll the die one or more times.
            Takes a parameter of how many times the die is to be rolled; defaults to 1. 
            Returns a list of outcomes.
            Does not store internally these results.
            
        show:
            A method to show the user the die’s current set of faces and weights
            Returns the dataframe created in the initializer.
    '''
    
    def __init__(self, names):
        self._df = pd.DataFrame({'faces': [], 'weights': []})
        self._df['faces'] = names
        self._df['weights'] = np.ones(len(names))
        
        
    def change_weight(self, face, val):
        if face not in self._df.faces.values:
            print(self._df.faces.values)
            print("The face entered does not match any current faces")
        else:
            if type(float(val)) != float:
                print(float(val))
                print("Cannot convert to a float")
            else:
                self._df.loc[self._df['faces'] == face,'weights'] = val
    
    
    def roll(self, times=1):
        probs = self._df['weights'] / self._df['weights'].sum()
        rolls = []
        for i in range(0,times):
            outcome = np.random.choice(self._df['faces'], p=probs)
            rolls.append(outcome)
        return rolls
    
    def show(self):
        return self._df
        

class Game:
    '''
    A game consists of rolling of one or more dice of the same kind one or more
    times.
    
    Each game is initialized with one or more of similarly defined dice (Die objects).
    
    By “same kind” and “similarly defined” we mean that each die in a given game has
    the same number of sides and associated faces, but each die object may have
    its own weights.
    
    The class has a behavior to play a game, i.e. to rolls all of the dice a given
    number of times.
        
    The class keeps the results of its most recent play. 
    
    Methods:
        __init__:
            An initializer
            Takes a single parameter, a list of already instantiated similar Die
            objects.
            
        play:
            Takes a parameter to specify how many times the dice should be rolled.
            Saves the result of the play to a private dataframe of shape N rolls
            by M dice.
            The private dataframe has the roll number is a named index.
            
        show:
            A method to show the user the results of the most recent play.
            This method passes the private dataframe to the user.
            Takes a parameter to return the dataframe in narrow or wide form.
            This parameter defaults to wide form.
            This parameter raises an exception of the user passes an invalid option.
    '''
    def __init__(self, die):
        self.die = die
        

    def play(self, times):
        self._gdf = pd.DataFrame()
        for dice in self.die:
            results = dice.roll(times)
            self._gdf[self.die.index(dice)] = results
            self._gdf.index.name = 'roll number'
            self._gdf = self._gdf.rename_axis('die number', axis ='columns')            
    
    def show(self, view = 'wide'):
        if view.lower() == 'wide': 
            return (self._gdf)
        elif view.lower() == 'narrow':
            print(self._gdf.stack())
        else:
            print('Please enter "wide" or "narrow"')
        return self._gdf
        print(self._gdf)


class Analyzer:
    
    '''
    An analyzer takes the results of a single game and computes various descriptive 
    statistical properties about it. These properties results are available as 
    attributes of an Analyzer object.
    
    Methods:
        __init__:
            An initializer
            Takes a game object as its input parameter. 
            
        jackpot:
            A jackpot method to compute how many times the game resulted in all 
            faces being identical.
            Returns an integer for the number times to the user.
            Stores the results as a dataframe of jackpot results in a public 
            attribute.
            
        combo:
            A combo method to compute the distinct combinations of faces rolled, 
            along with their counts.
            Combinations should be sorted and saved as a multi-columned index.
            Stores the results as a dataframe in a public attribute.
            
        facecounts:
            A face counts per roll method to compute how many times a given face 
            is rolled in each event.
            Stores the results as a dataframe in a public attribute.
            The dataframe has an index of the roll number and face values as 
            columns (i.e. it is in wide format).
    '''
    
    
    
    def __init__(self, game):
        self.game = game

    def jackpot(self):
        self.jack_tally = 0
        self.df_jackpot = pd.DataFrame()
        for row in self.game._gdf.index:
            set_check = set()
            for col in self.game._gdf.iloc[[row]]:
                set_check.add(self.game._gdf.iloc[row][col])
            if len(set_check) == 1:
                self.jack_tally += 1
                self.df_jackpot = self.df_jackpot.append(self.game._gdf.iloc[[row]])
        return self.jack_tally

    def combo(self):
        self.combo = self.game._gdf.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')
        return self.combo.reset_index()
            
        
    def face_counts(self):
        self.fc_df = self.game._gdf.stack().value_counts()
        print(self.fc_df)
        return self.fc_df
        