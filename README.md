# CS-5110-assn3
Assignment 3 for Multiagent Systems : voting

USING THE PROGRAM

Example test cases are provided in main to demonstrate the program

You may use the code to make your own voting test cases and societies.

Several functions are available to create voters, societies, and social rankings

Constants are changed at the top

a list of candidates used for voting is included at the top in the CANDIDATES list. You can add more candidates, but be
aware that the 'test1' society will break since it is predefined to contain only 4 candidates. The random societies will
adjust based on the given candidates

Create a voter using Voter(weight, ordering)
    - where weight is an integer greater than 1
    - where ordering is a list containing all of the candidates from the CANDIDATES list, ordered by preference
    - ex Voter(5, ['A', 'C', 'B', 'D'])
    - passing in None for either parameter defaults them to random values
    - ex Voter(None, None), or Voter(4, None), or Voter(None, ['A', 'C', 'D', 'B'])

Create a society using Society()
    - Voters are added using member function .addVoter(voter)
    - ex my_society.addVoter(Voter(5, ['A', 'C', 'B', 'D'])
    - Restrictions are added by using member function .restrict(a, b), forces a > b
    - ex my_society.restrict('C', 'A')
    - Can also restrict the ranking of a single candidate, ie force a into 2nd place(0 indexed)
    - ex my_society.restrict('B', 1)

Get a borda ranking on a society with borda(society)
    - ex print(borda(my_society))

Get a bucklin ranking on a society with bucklin(society)
    - ex print(bucklin(my_society))i
    - returns a tuple containing the top bucklin candidate and the value of k

Get a single transferable vote on a society with singleTransferableVote(society)
    - ex print(singleTransferableVote(my_society))

Run all of the above voting schemes and print the output using tallyVotes(society)
    - ex tallyVotes(my_society)
