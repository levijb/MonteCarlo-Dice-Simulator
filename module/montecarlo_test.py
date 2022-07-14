# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 16:17:47 2022

@author: ljd3frf - Levi Davis
"""

import unittest
import montecarlo
import pandas

test_die = montecarlo.Die([1,2,3,4,5,6])
test_die2 = montecarlo.Die([1,2,3,4,5,6])
test_game = montecarlo.Game([test_die,test_die2])
test_analyzer = montecarlo.Analyzer(test_game)
test_die.change_weight(4,4)
print(test_die._df)
a = test_die.roll(2)
b = test_game.play(3)
test_game._gdf
print(test_game)

class DieTest(unittest.TestCase):
    
    def test1_init(self):
        self.assertTrue(test_die._df.iloc[0,0] == 1)
        
    def test2_change_weight(self):
        test_die.change_weight(1, 3)
        self.assertEqual(test_die._df.iloc[0,1], 3)
    
    
    def test3_roll(self):
        self.assertEqual(len(a), 2)
        
    
    def test4_show(self):
        self.assertTrue(isinstance(test_die.show(), pandas.DataFrame))
        
        
        
class GameTest(unittest.TestCase):
    
    def test5_init(self):
        self.assertTrue(isinstance(test_game, montecarlo.Game))

    def test6_play(self):
        self.assertEqual(len(test_game._gdf),3)

    def test7_show(self):
        b = test_game.show()
        self.assertTrue(isinstance(b,pandas.DataFrame))
        

class AnalyzerTest(unittest.TestCase):
    
    def test8_init(self):
        self.assertTrue(isinstance(test_analyzer.game, montecarlo.Game))

    def test9_jackpot(self):
        self.assertTrue(isinstance(test_analyzer.jackpot(), int))
        
    def test10_combo(self):
        self.assertTrue(isinstance(test_analyzer.combo(), pandas.DataFrame))

    def test11_facecounts(self):
        self.assertTrue(isinstance(test_analyzer.face_counts(), pandas.Series))


if __name__ == '__main__':
    unittest.main(verbosity=2)