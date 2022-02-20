# problem_1_experience_gaining
Write a program that helps a player figure how many battles he will need to play in a battle video game to unlock the next tank in the line.
On the first line you will receive the amount of experience needed to unlock the tank. On the second line you will receive the count of battles. On the following lines , you will receive the experience the player can gain in every battle.
Calculate if he can unlock the tank. Keep in mind that he gets 15 % more experience for every third battle and 10 % less for every fifth battle , and 5 % more experience on every fifteenth. You also need to stop the program as soon as he collect the needed experience.
The possible outputs are:
•	"Player successfully collected his needed experience for {battleCount} battles."
•	"Player was not able to collect the needed experience, {neededExperience} more needed."

Input
500
5
50
100
200
100
30

Output
Player successfully collected his needed experience for 5 battles.

Comments
The first line is the amount of the wanted experience.  – "500"
The second line is the expected battles for which he has to collect the experience.  – "5"
After that is the experience received for every battle:
50 + 100 + (200 + (200 * 15 %)) + 100 + (30 – (30 * 10 %)) = 507
So on the console is printed :
"Player successfully collected his needed experience for 5 battles."

