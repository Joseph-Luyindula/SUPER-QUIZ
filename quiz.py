import json 

# ouverture du fichier json
with open('questionnaire.json') as file:
  question = json.load(file)

score  = 0 # initialisation du score à 0

def quiz(question,q1,q2,q3,q4,reponse):
	global score
	print(question)
	print("a :",q1)
	print("b :",q2)
	print("c :",q3)
	print("d :",q4)
	print("Quel est votre choix .")
	don = input(">>>")
	if don == reponse:
		score += 1

	
def run_quiz():
	for i in range(len(question)):
		quiz(*question[str(i+1)])
	print(f"score : {score}/{len(question)}")
	
# exécution du quiz
run_quiz()