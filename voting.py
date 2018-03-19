# Aaron Morgenegg, A02072659
# Voting program comparing different voting methods

import random

# ----- CONST DECLARATIONS -----

CANDIDATES = ['A', 'B', 'C', 'D']
MAX_WEIGHT = 10

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

    def getBordaCount(self, candidate):
        """
        Returns the borda count for given candidate
        :param candidate:
        :return:
        """
        index = self.ordering.index(candidate)
        return index * self.weight

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

def borda(society):
    """
    Given a society of voters, return the borda ranking
    :param society:
    :return:
    """
    counts = []
    candidates = list(CANDIDATES)
    for i in range(len(candidates)):
        counts.append(0)

    for voter in society.voters:
        for i in range(len(candidates)):
            counts[i] += voter.getBordaCount(candidates[i])

    return sortCounts(counts, candidates)

def singleTransferableVote(society):
    """
    Given a society of voters, computes the single transferable vote candidate
    :param society:
    :return:
    """
    counts = []
    candidates = list(CANDIDATES)
    sorted_candidates = []
    for i in range(len(candidates)):
        counts.append(0)

    max_votes = 0
    for voter in society.voters: max_votes += voter.weight
    threshold = max_votes/2 + 1

    while True:
        for voter in society.voters:
            for candidate in candidates:
                if voter.ordering[0] == candidate:
                    counts[candidates.index(candidate)] += voter.weight

        min_count = min(counts)
        max_count = max(counts)
        min_candidate = candidates[counts.index(min_count)]
        max_candidate = candidates[counts.index(max_count)]
        if max_count > threshold:
            sorted_candidates.append(max_candidate)
            sorted_candidates.reverse()
            return sorted_candidates
        else:
            sorted_candidates.append(candidates[counts.index(min_count)])
            for voter in society.voters:
                if voter.ordering[0] == candidate:
                    counts[candidates.index(candidate)] += voter.weight
            del candidates[counts.index(min_count)]
            threshold -= 1

def sortCounts(counts, candidates):
    """
    returns a sorted candidates list based on counts list
    :param counts:
    :param candidates:
    :return:
    """
    indexes = list(range(len(counts)))
    indexes.sort(key=counts.__getitem__)
    sorted_candidates = map(candidates.__getitem__, indexes)
    return list(sorted_candidates)

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

    print(borda(my_society))

    test_borda = Society()
    test_borda.addVoter(Voter(8, ['A', 'B', 'C', 'D']))
    test_borda.addVoter(Voter(6, ['C', 'D', 'B', 'A']))
    test_borda.addVoter(Voter(1, ['C', 'D', 'A', 'B']))
    test_borda.addVoter(Voter(1, ['B', 'D', 'C', 'A']))
    test_borda.addVoter(Voter(4, ['B', 'C', 'D', 'A']))

    print("Testing Borda method of given society of voters...")
    print(test_borda)
    print("Borda ranking...")
    print(borda(test_borda))

    print("STV ranking...")
    print(singleTransferableVote(test_borda))
