{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "85d85ede-04bb-42ee-9584-1ce02dac5cd4",
   "metadata": {},
   "source": [
    "# Monte Carlo Simulator\n",
    "Levi Davis (ljd3frf)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cba006a7-4674-4315-9202-300af143c113",
   "metadata": {},
   "source": [
    "### Install"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb0f1fbc-18b5-4fc7-8c83-de85e38d3ff5",
   "metadata": {},
   "source": [
    "To install the montecarlo module to your machine, download the \"module\" folder in my github MonteCarlo repository at this link. https://github.com/levijb/MonteCarlo/tree/main/module\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45d9a344-0d84-4ea0-9ad6-f0de955c3897",
   "metadata": {},
   "source": [
    "### Import"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7333d4ae-decd-4814-bf0e-04b854d48d5d",
   "metadata": {},
   "source": [
    "To import the module"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "39137228-1d2a-4df5-aa47-4d586e963118",
   "metadata": {},
   "outputs": [],
   "source": [
    "from MonteCarlo import montecarlo as m"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5fcee04f-6161-4a0d-b300-ee3b7330efea",
   "metadata": {},
   "source": [
    "## Using the module"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f41ab94-014c-4868-a0ba-dbf349f7d9ed",
   "metadata": {},
   "source": [
    "There are three classes in the module: Die, Game, and Analyze"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "694bf1e9-85cf-40d8-a315-4728657c97b5",
   "metadata": {},
   "source": [
    "First you want to create a die\n",
    "- Paramter: a list of strings or a list of ints that will be the faces of the die.\n",
    "- You can create any type of die, but they must have the same faces to use in the same game."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e440085f-a00c-41a8-81ef-fdbdc4b3ca2b",
   "metadata": {},
   "outputs": [],
   "source": [
    "die1 = m.Die([1,2,3,4,5,6])\n",
    "die2 = m.Die([1,2,3,4,5,6])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f70c133c-c6d5-40c1-b867-d232cb58b35f",
   "metadata": {},
   "source": [
    "You can roll a die \n",
    "- Parameter: number of times to roll"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "d75dbc15-b9e4-432e-964c-cab74f7ce344",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 3, 4, 4, 3]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "die1.roll(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd286773-ee23-4358-92c9-bbd2ba098b5a",
   "metadata": {},
   "source": [
    "You can change the weight of a die face (change the probabilty). All die faces starts with equal probability with value 1\n",
    "- Parameters: (face to change, new weight)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6024ae3b-1ad2-4089-9498-a343ea741050",
   "metadata": {},
   "outputs": [],
   "source": [
    "die1.change_weight(1, 10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71c9269f-1eb3-4d20-8839-6cdabf2b8442",
   "metadata": {},
   "source": [
    "Use show() to display the current faces and weights of a die"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c01f4a73-3575-4734-b05d-c8b7c3512039",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>faces</th>\n",
       "      <th>weights</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>6</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   faces  weights\n",
       "0      1     10.0\n",
       "1      2      1.0\n",
       "2      3      1.0\n",
       "3      4      1.0\n",
       "4      5      1.0\n",
       "5      6      1.0"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "die1.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5cac1a71-c05d-4ecb-b189-11a21ba0ccbc",
   "metadata": {},
   "source": [
    "You can create a game with a list of die already created"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ad2a32a6-a1ec-4c20-9ef5-793e2c1dea36",
   "metadata": {},
   "outputs": [],
   "source": [
    "game = m.Game([die1, die2])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8604f75b-4970-40d2-9c31-19cca553bf5a",
   "metadata": {},
   "source": [
    "And then play the game \n",
    "- Parameter: Number of times each die is rolled"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a8e0bf1b-6887-41c6-b6bf-0812fe38e68c",
   "metadata": {},
   "outputs": [],
   "source": [
    "game.play(100)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52cadc27-fa49-4ec6-a4a3-557dc0613cc6",
   "metadata": {},
   "source": [
    "Using show() with an instance of the game class will show the roll results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "8ef4b7c5-fcc9-42c7-882a-5bbbb52ee057",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th>die number</th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>roll number</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>95</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>96</th>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>97</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>98</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>99</th>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>100 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "die number   0  1\n",
       "roll number      \n",
       "0            5  2\n",
       "1            2  6\n",
       "2            4  1\n",
       "3            1  5\n",
       "4            5  1\n",
       "...         .. ..\n",
       "95           1  2\n",
       "96           3  5\n",
       "97           1  4\n",
       "98           1  3\n",
       "99           2  6\n",
       "\n",
       "[100 rows x 2 columns]"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "game.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f4834d85-1d3c-477e-b121-deb2ad992134",
   "metadata": {},
   "source": [
    "Next, use the Analyzer class to calculate some statistics about the game\n",
    "- Parameter: a game object that has been 'played'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "02f7cd16-af3e-463b-bae3-bce0af211dcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "analyzer = m.Analyzer(game)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c3923c64-2d47-44da-929d-17f4805e8382",
   "metadata": {},
   "source": [
    "jackpot() shows how many rolls had all the same face, ie all 6's"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8a50e749-6041-4940-a23b-7516b817bc36",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "18"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "analyzer.jackpot()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a14c4851-ab6d-4c00-a11c-880cc37a77db",
   "metadata": {},
   "source": [
    "combo() shows all the different combonations of the previous game with a tally for the number of occurances (not permuations, so order doesnt matter) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1bfda738-97b5-4acc-8ccc-17f79035f9fb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>n</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>2</td>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>3</td>\n",
       "      <td>4</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>3</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>3</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>4</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>5</td>\n",
       "      <td>5</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>6</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>2</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>2</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>4</td>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>5</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    0  1   n\n",
       "0   1  1  14\n",
       "1   1  5  14\n",
       "2   1  4  13\n",
       "3   1  2  11\n",
       "4   1  3  11\n",
       "5   1  6  10\n",
       "6   2  6   6\n",
       "7   2  3   5\n",
       "8   3  4   2\n",
       "9   3  5   2\n",
       "10  3  6   2\n",
       "11  4  6   2\n",
       "12  5  5   2\n",
       "13  6  6   2\n",
       "14  2  4   1\n",
       "15  2  5   1\n",
       "16  4  5   1\n",
       "17  5  6   1"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "analyzer.combo()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2439f0a2-0e32-4d99-a9cc-cbbcdbe99e3e",
   "metadata": {},
   "source": [
    "face_count() shows the tallys for total occurances of each die face"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "1b4cc696-dc04-4349-bf8d-17367a4b6f94",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1    87\n",
       "6    25\n",
       "2    24\n",
       "5    23\n",
       "3    22\n",
       "4    19\n",
       "dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "analyzer.face_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b7ac73c-8699-4a40-94fc-9b427f2966dc",
   "metadata": {},
   "source": [
    "# API description"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c7e9e4c-22f7-4b96-9b19-03ca5bfcbaf1",
   "metadata": {
    "tags": []
   },
   "source": [
    "### Die class:\n",
    "\n",
    "- Methods:\n",
    "    - __init: \n",
    "        - initializer\n",
    "        - Takes 1 parameter - a list of ints or a list of strings that will be the faces of the die\n",
    "    - roll:  \n",
    "        - A method to roll the die one or more times.\n",
    "        - 1 parameter: int, number of times the die is to be rolled, defaults to 1\n",
    "        - Returns a list of outcomes.\n",
    "    - change_weights: \n",
    "        - A method to change the weight of a single die face\n",
    "        - 2 parameters: first is the face name (int or string), second is the desired new weight\n",
    "        - returns nothing\n",
    "    - show:\n",
    "        - returns a pandas dataframe of the current die faces and weights\n",
    "        - Takes no parameters\n",
    "\n",
    "### Game class\n",
    "\n",
    "- Attributes:\n",
    "    - die: the list of die used to create the object\n",
    "- Methods:\n",
    "    - __init:\n",
    "        - Initializer\n",
    "        - To initialize Game takes 1 parameter - a list of already created Die\n",
    "    - play:\n",
    "        - A method that will roll each die x number of times\n",
    "        - 1 parameter: int, number of times to roll each die, defaults to 1\n",
    "        - returns nothing\n",
    "    - show:\n",
    "        - A method that shows the results of the previous game\n",
    "        - 1 parameter: string, either 'narrow' or 'wide', defualt is wide. refers to narrow or wide dataframe format\n",
    "        - returns pandas dataframe\n",
    "\n",
    "### Analyzer class\n",
    "- Attributes:\n",
    "    - jack_tally: the total number of jackpots in a game\n",
    "    - combo: pandas datframe containing combo info\n",
    "    - fc_df: pandas dataframe containing face count values\n",
    "- Methods:\n",
    "    - __init:\n",
    "        - Initializer\n",
    "        - Takes 1 parameter, a game object on which the play method has already been called\n",
    "    - jackpot:\n",
    "        - no parameters\n",
    "        - returns the number(an int) of jackpots in a game\n",
    "    - combo:\n",
    "        - no parameters\n",
    "        - returns a pandas dataframe of all different roll combinations of a game with the count of total occurances for each combo\n",
    "    - face_counts:\n",
    "        - no parameters\n",
    "        - returns a pandas dataframe with the total number of occurances for each die face\n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "781e42ed-2d94-460f-800a-c5551a0ca7ba",
   "metadata": {},
   "source": [
    "## Manifest\n",
    "- files in github repo:\n",
    "- montecarlo.py\n",
    "- montecarlo_test.py\n",
    "- Scenarios.ipynb\n",
    "- setup.py\n",
    "- LICENSE\n",
    "- README\n",
    "- .gitignore\n",
    "- module (folder for installing module)\n",
    "    - montecarlo.py\n",
    "    - montecarlo_test.py\n",
    "    - setup.py\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
