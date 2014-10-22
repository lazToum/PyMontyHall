#!/usr/bin/ python2
import random
curtains = ['A','B','C']
NumOfWinsIfKeep = 0
NumOfWinsIfChange = 0
#10000 Tests to convince us
for x in range (0,10000):
	# phase 1
	Ferrari = random.choice(curtains)
	PlayerChoice = random.choice(curtains)
	#host will not open the player's choice on the phase two
	curtains.remove(PlayerChoice)
	# ... or the Ferrari....
	Discard = random.choice(curtains)
	while Discard == Ferrari:
		Discard = random.choice(curtains)
	#open one curtain:
	curtains.remove(Discard)
	#phase two
	RemainingCurtain = curtains[0]
	if RemainingCurtain == Ferrari:
		# if the player changes his choice, he wins
		NumOfWinsIfChange += 1
	else :
		# if the player keeps his choice, he wins
		NumOfWinsIfKeep += 1
	#repeat
	curtains = ['A','B','C']
print 'In 10000 Tests: \nIf player keeps his choice, he wins '+str(NumOfWinsIfKeep) + ' times('+str(float(NumOfWinsIfKeep)/float(100))+'%)\nIf he changes his option he wins: '+ str(NumOfWinsIfChange)+' times('+str(float(NumOfWinsIfChange)/float(100))+'%)'
