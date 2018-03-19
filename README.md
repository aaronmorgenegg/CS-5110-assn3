# CS-5110-assn3
Assignment 3 for Multiagent Systems : voting

USING THE PROGRAM

Example test cases are provided in main to demonstrate the program

You may use the code to make your own voting test cases and societies.

Several functions are available to create voters, societies, and social rankings

Constants are changed at the top

a list of candidates used for voting is included at the top in the CANDIDATES list

Create a voter using Voter(weight, ordering)
    - where weight is an integer greater than 1
    - where ordering is a list containing all of the candidates from the CANDIDATES list, ordered by preference
    - ex Voter(5, ['A', 'C', 'B', 'D'])
    - passing in None for either parameter defaults them to random values
    - ex Voter(None, None), or Voter(4, None)

Create a society using Society()
    - Voters are added using member function .addVoter(voter)
    - ex my_society.addVoter(Voter(5, ['A', 'C', 'B', 'D'])

Get a borda ranking on a society with borda(society)
    - ex print(borda(my_society))
