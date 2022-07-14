# Monte Carlo Simulator
Levi Davis (ljd3frf)

### Install

To install the montecarlo module to your machine, download the "module" folder in my github MonteCarlo repository at this link. https://github.com/levijb/MonteCarlo/tree/main/module


### Import

To import the module


```python
from MonteCarlo import montecarlo as m
```

## Using the module

There are three classes in the module: Die, Game, and Analyze

First you want to create a die
- Paramter: a list of strings or a list of ints that will be the faces of the die.
- You can create any type of die, but they must have the same faces to use in the same game.


```python
die1 = m.Die([1,2,3,4,5,6])
die2 = m.Die([1,2,3,4,5,6])
```

You can roll a die 
- Parameter: number of times to roll


```python
die1.roll(5)
```




    [3, 3, 4, 4, 3]



You can change the weight of a die face (change the probabilty). All die faces starts with equal probability with value 1
- Parameters: (face to change, new weight)


```python
die1.change_weight(1, 10)
```

Use show() to display the current faces and weights of a die


```python
die1.show()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>faces</th>
      <th>weights</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>10.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>6</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>



You can create a game with a list of die already created


```python
game = m.Game([die1, die2])
```

And then play the game 
- Parameter: Number of times each die is rolled


```python
game.play(100)
```

Using show() with an instance of the game class will show the roll results


```python
game.show()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>die number</th>
      <th>0</th>
      <th>1</th>
    </tr>
    <tr>
      <th>roll number</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>95</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>96</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>97</th>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>98</th>
      <td>1</td>
      <td>3</td>
    </tr>
    <tr>
      <th>99</th>
      <td>2</td>
      <td>6</td>
    </tr>
  </tbody>
</table>
<p>100 rows × 2 columns</p>
</div>



Next, use the Analyzer class to calculate some statistics about the game
- Parameter: a game object that has been 'played'


```python
analyzer = m.Analyzer(game)
```

jackpot() shows how many rolls had all the same face, ie all 6's


```python
analyzer.jackpot()
```




    18



combo() shows all the different combonations of the previous game with a tally for the number of occurances (not permuations, so order doesnt matter) 


```python
analyzer.combo()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>n</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>1</td>
      <td>14</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>5</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>4</td>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>2</td>
      <td>11</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>3</td>
      <td>11</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>6</td>
      <td>10</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>8</th>
      <td>3</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>3</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>10</th>
      <td>3</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>11</th>
      <td>4</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>12</th>
      <td>5</td>
      <td>5</td>
      <td>2</td>
    </tr>
    <tr>
      <th>13</th>
      <td>6</td>
      <td>6</td>
      <td>2</td>
    </tr>
    <tr>
      <th>14</th>
      <td>2</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>15</th>
      <td>2</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>4</td>
      <td>5</td>
      <td>1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>5</td>
      <td>6</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



face_count() shows the tallys for total occurances of each die face


```python
analyzer.face_counts()
```




    1    87
    6    25
    2    24
    5    23
    3    22
    4    19
    dtype: int64



# API description

### Die class:
To initialize Die takes 1 parameter - a list of ints or a list of strings that will be the faces of the die
- Methods:
    - roll:  
        - A method to roll the die one or more times.
        - 1 parameter: int, number of times the die is to be rolled, defaults to 1
        - Returns a list of outcomes.
    - change_weights: 
        - A method to change the weight of a single die face
        - 2 parameters: first is the face name (int or string), second is the desired new weight
        - returns nothing
    - show:
        - returns a pandas dataframe of the current die faces and weights
        - Takes no parameters

### Game class
To initialize Game takes 1 parameter - a list of already created Die
- Attributes:
    - die: the list of die used to create the object
- Methods:
    - play:
        - A method that will roll each die x number of times
        - 1 parameter: int, number of times to roll each die, defaults to 1
        - returns nothing
    - show:
        - A method that shows the results of the previous game
        - 1 parameter: string, either 'narrow' or 'wide', defualt is wide. refers to narrow or wide dataframe format
        - returns pandas dataframe

### Analyzer class
To intialize, Analyzer takes 1 parameter, a game object on which the play method has already been called
- Attributes:
    - jack_tally: the total number of jackpots in a game
- Methods:
    - jackpot:
        - no parameters
        - returns the number(an int) of jackpots in a game
    - combo:
        - no parameters
        - returns a pandas dataframe of all different roll combinations of a game with the count of total occurances for each combo
    - face_counts:
        - no parameters
        - returns a pandas dataframe with the total number of occurances for each die face
        

## Manifest
- files in github repo:
- montecarlo.py
- montecarlo_test.py
- Scenarios.ipynb
- setup.py
- LICENSE
- README
- .gitignore
- module (folder for installing module)
    - montecarlo.py
    - montecarlo_test.py
    - setup.py



```python

```
