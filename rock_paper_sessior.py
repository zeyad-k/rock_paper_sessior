# Start
# Player choose
# Computer choose
# If Player choose == Computer choose 
# تعادل
# If ( player = rock and computer = scissor ) or ( player = paper and computer = rock ) or ( player = scissor and computer = paper )
# >>> player wins 
# Else 
# >>> computer wins
# End

# Player choose
user = input("Choose your move movement : 'r' for Rock  , 'p' for Paper and 's' for scissor  ")

# Computer choose
import random

choices = ['r', 'p', 's']
computer = random.choice(choices)

# Show choices of player and computer
print (f"Player choice is : {user} \n ")
print (f"Computer  choice is : {computer} \n ")




# If Player choose == Computer choose
if user == computer :
	print ("The result is a tie\n ")

# If ( player = rock and computer = scissor ) or ( player = paper and computer = rock ) or ( player = scissor and computer = paper )
elif   (user == 'r' and computer =='s' )  or ( user == 'p' and computer =='r' ) or ( user == 's' and computer =='p' ):
	print("Player wins -You won-\n ")  # >>> player wins 

# Else any other choice
else :
	print("Computer wins -You lost-\n ")	# >>> computer wins

# End
print ("Game over.")

 