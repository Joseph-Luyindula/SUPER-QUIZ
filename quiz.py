import json 

# ouverture du fichier json
with open('questionnaire.json') as file:
  question = json.load(file)

score  = 0 # initialisation du score à 0

def quiz(question,q1,q2,q3,q4,reponse):
	global score
	print(f"""
{question}:
	    
	    a : {q1}
	    
	    b : {q2}
	    
	    c : {q3}
	    
	    d : {q4}
	    
	  QUEL EST VOTRE CHOIX ? 
	  """)
	don = input(">>> ").lower()
	if don == reponse:
		score += 1
	elif not don in  ("a","b","c","d"):
		print("""ERREUR : Cette question a été annulée, veuillez s'il-vous-plaît mettre une valeur comprise entre a et d (a,b,c,d) lors des prochaines question .
		
		N.B : Oui=y et Non=n""")
		poursuivre = ""
		while poursuivre != ("y","n"):
			poursuivre = input("voulez-vous continuer le quiz ? [ y/n ] ")
			if poursuivre.lower() == "y":
				break 
			elif poursuivre.lower() == "n":
				print()
				print("Merci et à la prochaine 😁")
				exit()
			else:
				print()
				print("désolé mais écrivez soit y soit n s'il-vous-plaît .")
			

	
def run_quiz():
	for i in range(len(question)):
		quiz(*question[str(i+1)])
	print(f"score : {score}/{len(question)}")
	
# exécution du quiz
run_quiz()