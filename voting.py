# Aaron Morgenegg, A02072659
# Voting program comparing different voting methods

import random

# ----- CONST DECLARATIONS -----

CANDIDATES = ['A', 'B', 'C', 'D']
MIN_WEIGHT = 1
MAX_WEIGHT = 10
MIN_VOTERS = 3
MAX_VOTERS = 10

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

    def restrict(self, a, b):
        """
        Enforces the restriction that a > b in all cases if a and b are candidates
        Enforces the restriction that a is always in bth place if b is an index
        :param a:
        :param b:
        :return:
        """
        if isinstance(b, int):
            for voter in self.voters:
                index_a = voter.ordering.index(a)
                if index_a != b:
                    voter.ordering[index_a], voter.ordering[b] = voter.ordering[b], voter.ordering[index_a]
        else:
            for voter in self.voters:
                index_a = voter.ordering.index(a)
                index_b = voter.ordering.index(b)
                if index_a > index_b:
                    voter.ordering[index_a], voter.ordering[index_b] = voter.ordering[index_b], voter.ordering[index_a]

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

    threshold = getThreshold(society)

    while True:
        resetCounts(counts)
        for voter in society.voters:
            for i in range(len(voter.ordering)):
                if voter.ordering[i] in candidates:
                    counts[candidates.index(voter.ordering[i])] += voter.weight
                    break
        min_count = min(counts)
        max_count = max(counts)
        min_candidate = candidates[counts.index(min_count)]
        max_candidate = candidates[counts.index(max_count)]
        if max_count > threshold:
            sorted_candidates.append(max_candidate)
            sorted_candidates.reverse()
            for candidate in candidates:
                if candidate not in sorted_candidates:
                    sorted_candidates.insert(1,candidate)
            return sorted_candidates
        else:
            sorted_candidates.append(min_candidate)
            candidates.remove(min_candidate)
            counts.remove(min_count)

def bucklin(society):
    """
    Given a society of voters, computes the bucklin ranking candidate
    :param society:
    :return:
    """
    k = 1
    threshold = getThreshold(society)
    candidates = list(CANDIDATES)
    counts = []
    for i in range(len(candidates)):
        counts.append(0)

    while k < len(society.voters):
        resetCounts(counts)
        for voter in society.voters:
            for i in range(0, k):
                counts[candidates.index(voter.ordering[i])] += voter.weight

        for i in range(len(candidates)):
            if counts[i] > threshold and counts[i] == max(counts):
                return (candidates[i], k)
        k += 1

    print("Error: No bucklin ranking found.")

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

def getThreshold(society):
    threshold = 0
    for voter in society.voters: threshold += voter.weight
    return (threshold / 2 + 1)

def resetCounts(counts):
    for i in range(len(counts)):
        counts[i] = 0

def getRandomWeight():
    return random.randint(MIN_WEIGHT, MAX_WEIGHT)

def getRandomOrdering():
    """
    Gets a random ordering of the candidates
    :return:
    """
    candidates_copy = list(CANDIDATES)
    random.shuffle(candidates_copy)
    return candidates_copy

def tallyVotes(society):
    """
    runs the given society through each of the voting schemes and prints results
    :param society:
    :return:
    """
    print("----------")

    print("Tallying votes for given society of voters...")
    print(society)

    print("Borda ranking...")
    print(borda(society))

    print("\nBucklin ranking...")
    print(bucklin(society))

    print("\nSTV ranking...")
    print(singleTransferableVote(society))

    print("----------")

if __name__ == '__main__':
    print("Test 1: Predefined society of voters")
    test1 = Society()
    test1.addVoter(Voter(8, ['A', 'B', 'C', 'D']))
    test1.addVoter(Voter(6, ['C', 'D', 'B', 'A']))
    test1.addVoter(Voter(1, ['C', 'D', 'A', 'B']))
    test1.addVoter(Voter(1, ['B', 'D', 'C', 'A']))
    test1.addVoter(Voter(4, ['B', 'C', 'D', 'A']))
    tallyVotes(test1)

    print("Test 2: Random society of voters")
    test2 = Society()
    for i in range(random.randint(MIN_VOTERS, MAX_VOTERS)):
        test2.addVoter(Voter(None, None))
    tallyVotes(test2)

    print("Test 3: Random society of voters with restriction that C > A")
    test3 = Society()
    for i in range(random.randint(MIN_VOTERS, MAX_VOTERS)):
        test3.addVoter(Voter(None, None))
    test3.restrict('C', 'A')
    tallyVotes(test3)

    print("Test 4: Random society of voters with restriction that B is always ranked 2nd")
    test4 = Society()
    for i in range(random.randint(MIN_VOTERS, MAX_VOTERS)):
        test4.addVoter(Voter(None, None))
    test4.restrict('B', 1)
    tallyVotes(test4)

    print("Test 5: Random society of voters with restrictions that A is always ranked 2nd, D > C, and B < C")
    test5 = Society()
    for i in range(random.randint(MIN_VOTERS, MAX_VOTERS)):
        test5.addVoter(Voter(None, None))
    test5.restrict('A', 1)
    test5.restrict('D', 'C')
    test5.restrict('C', 'B')
    tallyVotes(test5)
