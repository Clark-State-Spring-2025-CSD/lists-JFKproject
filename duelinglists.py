#Create two seperate lists for player one and player two. 
#Each one should contain 10 random numbers between 1 and 50.
#Do NOT sort the lists.
#Compare the lists in order. Whichever list has the higher number wins.
#Keep track of how many times each list wins.
#Find the highest number in each list and it's index. If the number occers multiple times take the first instsance.
#Find the lowest number in each list and it's index. If the number occers multiple times take the first instsance.
#A tie is not record as a win for either player
#Display the lists
#Report to the user how many times each player won and the information from lines 6 and 7.
#For the example output I am limiting the range to 1 to 9 to keep it more readable.

#Player One = [5,7,2,9,1,1,3,8,6,9]
#Player Two = [3,8,5,5,8,1,4,7,4,7]
#Player one won 5 times
#Player two won 4 times
#Player one's highest number is 9 at index 3
#Player two's highest number is 8 at index 1
#Player one's lowest number is 1 at index 4
#Player two's lowest number is 1 at index 5

import random

#Lists for both players
first_Player = [random.randint(1, 50) for _ in range(10)]
second_Player = [random.randint(1, 50) for _ in range(10)]

#Win Record/Counters
first_Player_wins = 0
second_Player_wins = 0

for i in range(10):
    if first_Player[i] > second_Player[i]:
        first_Player_wins += 1
    elif second_Player[i] > first_Player[i]:
        second_Player_wins += 1

#First Player's high/low number record
highest_first_Player = max(first_Player)
highest_FirstPlayer_index = first_Player.index(highest_first_Player)
lowest_first_Player = min(first_Player)
lowest_FirstPlayer_index = first_Player.index(lowest_first_Player)

#Second Player's high/low number record
highest_second_Player = max(second_Player)
highest_SecondPlayer_index = second_Player.index(highest_second_Player)
lowest_second_Player = min(second_Player)
lowest_SecondPlayer_index = second_Player.index(lowest_second_Player)

#Display to players
print(f"Player 1 = {first_Player}")
print(f"Player 2 = {second_Player}")
print(f"Player 1 has won {first_Player_wins} times.")
print(f"Player 2 has won {second_Player_wins} times.")
print(f"Player 1's highest number is {highest_first_Player} at index {highest_FirstPlayer_index}.")
print(f"Player 2's highest number is {highest_second_Player} at index {highest_SecondPlayer_index}.")
print(f"Player 1's lowest number is {lowest_first_Player} at index {lowest_FirstPlayer_index}.")
print(f"Player 2's lowest number is {lowest_second_Player} at index {lowest_SecondPlayer_index}.")

#End of script