# Aaron Morgenegg, A02072659
# Voting program comparing different voting methods

import random

# ----- CONST DECLARATIONS -----

CANDIDATES = ['A', 'B', 'C', 'D']
MAX_WEIGHT = 100

class Voter:
    """
    Class that contains voter info, such as weight and their social preference ranking
    """
    def __init__(self, weight, ordering):
        if weight is None:
            self.weight = getRandomWeight()
        else:
            self.weight = weight
        if ordering is None:
            self.ordering = getRandomOrdering()
        else:
            self.ordering = ordering

    def __str__(self):
        return "Weight <" + str(self.weight) + "> Ordering <" + str(self.ordering) + ">"

class Society:
    """
    Class that holds many different voters
    """
    def __init__(self):
        self.voters = []

    def addVoter(self, voter):
        self.voters.append(voter)

    def __str__(self):
        retval = ""
        for i in range(len(self.voters)):
            retval += "Voter " + str(i) + " <" + str(self.voters[i]) + ">\n"
        return retval

def getRandomWeight():
    return random.randint(1, MAX_WEIGHT)

def getRandomOrdering():
    """
    Gets a random ordering of the candidates
    :return:
    """
    candidates_copy = list(CANDIDATES)
    random.shuffle(candidates_copy)
    return candidates_copy

if __name__ == '__main__':
    my_society = Society()
    guy = Voter(None, None)
    hermano = Voter(5, CANDIDATES)

    my_society.addVoter(guy)
    my_society.addVoter(hermano)
    print(my_society)

