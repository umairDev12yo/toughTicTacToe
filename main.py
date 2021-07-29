import random
import time
def exchange(listValue,intValue,Value):
	listValue[intValue]=Value
	return listValue
def search(character,value,position):
	for i in range(len(value)):
		curIndex=i
		if(value[curIndex]==position):
			value[curIndex]=character
	return(value)




time.sleep(1)
print("preparing game")
time.sleep(1)
print("Generating lists")
time.sleep(1)
print("Laiunching")

ticTacToeList=['1:1','1:2','1:3',
				'2:1','2:2','2:3',
				'3:1','3:2','3:3']


characterInput=input("please tell us your character: ")
i=1

opChar=input("plese enter opponent's character: ")

while(i<9):
	move=input("Give us the Positional Argument: ")
	randomTicTacToe=random.choice(ticTacToeList)
	wurstAIEver=search(opChar,ticTacToeList,randomTicTacToe)
	process=search(characterInput,ticTacToeList,move)
	print(ticTacToeList)
	i+=i
	if(ticTacToeList[0] and ticTacToeList[1] and ticTacToeList[2]== characterInput):
		print("You won")
		 
	elif(ticTacToeList[3]and ticTacToeList[4]and ticTacToeList[5]==characterInput):
		print("You won")
		 
	elif(ticTacToeList[6]and ticTacToeList[7]and ticTacToeList[8]==characterInput):
		print("You won")
		 
	elif(ticTacToeList[2]and ticTacToeList[5]and ticTacToeList[8]==characterInput):
		print("YOU WON!!")
		 
	elif(ticTacToeList[1]and ticTacToeList[4] and ticTacToeList[7]==characterInput):
		print("You won")
		 
	elif(ticTacToeList[0] and ticTacToeList[3] and ticTacToeList[6]==characterInput):
		print("You won")
		 
	elif(ticTacToeList[0]and ticTacToeList[4]and ticTacToeList[8]==characterInput):
		print("You won")
		 
	elif(ticTacToeList[2] and ticTacToeList[4] and ticTacToeList[6]==characterInput):
		print("You won")
		 
	elif(ticTacToeList[0] and ticTacToeList[1] and ticTacToeList[2]== opChar):
		print("Opponent Won")
		 
	elif(ticTacToeList[3]and ticTacToeList[4]and ticTacToeList[5]==opChar):
		print("Opponent won")
		 
	elif(ticTacToeList[6]and ticTacToeList[7]and ticTacToeList[8]==opChar):
		print("Opponet Won")
		 
	elif(ticTacToeList[2]and ticTacToeList[5]and ticTacToeList[8]==opChar):
		print("Opponent Won")
		 
	elif(ticTacToeList[1]and ticTacToeList[4] and ticTacToeList[7]==opChar):
		print("Opponent Won")
		 
	elif(ticTacToeList[0] and ticTacToeList[3] and ticTacToeList[6]==opChar):
		print("Opponent Wins")
		 
	elif(ticTacToeList[0]and ticTacToeList[4]and ticTacToeList[8]==opChar):
		print("Opponent Won, {'sensitive content'}")
		 
	elif(ticTacToeList[2] and ticTacToeList[4] and ticTacToeList[6]==opChar):
		print("Opponent Won")
		 
	elif(ticTacToeList[2] and ticTacToeList[4] and ticTacToeList[6]==opChar):
		print("Opponent won")
		 
	else:
		print("Umair: Both of you Won")
		 








#array=["3","6","0","2"]
#arraySearch=input("Please input to change variable: ")
#process=search(character,array,arraySearch)
#print(array)