import sys
import random 
import csv
import os

def vtest():
	
	word_bank = select_module()
	lang = choose_test()
	questions(word_bank, lang)

	

def select_module():
	
	file_found = False
	while file_found is False:
		try:
			module_choice = raw_input('Enter the file name. ex. module1.csv \n')
			module = open(module_choice)
			csv_f = csv.reader(module)
			file_found = True
		except Exception: 
			print ("Cannot Find file ") + module_choice + ("\n")

	word_bank =[]
	for row in csv_f:
  		word_bank.append(row)
  	return word_bank
			
def choose_test():
	lang = False
	while lang is False:
		lang = input('For Terms to Definition enter 0, For Definition to Term enter 1 \n')

		if lang == 0 or lang == 1:
			return lang

		else:
			print ('Please enter 0 for Terms to Definition or 1 for Definition to Terms \n')
			lang = False
			
def questions(word_bank, lang):
	answer = 'answer'
	quit = False
	# print word_bank
	number_of_words = len(word_bank)
	correct_answers = 0
	number_of_questions =0
	print ('\nTo quit, enter q or quit')
	print ('\nThere are '+ str(number_of_words) +' terms for you to figure out!')

	if lang == 0:
		print ('The term is given, enter the correct definition \n')
		lang_answer = 1

	if lang == 1:
		print ('The definition is given, please enter the term \n')
		lang_answer = 0 

	while quit is False:
		if len(word_bank) == 0:
			quit = True
			print "You got them all right! "
			print "You got " + str(correct_answers) + " correct out of " + str(number_of_questions)

		else:
			rand = random.randint(0, number_of_words-1)
			question = word_bank[rand]

			a = random.randint(0, number_of_words-1)
			b = random.randint(0, number_of_words-1)
			c = random.randint(0, number_of_words-1)
			d = random.randint(0, number_of_words-1)

			seta = word_bank[a]
			setb = word_bank[b]
			setc = word_bank[c]
			setd = word_bank[d]

			answera = seta[lang_answer]
			answerb = setb[lang_answer]
			answerc = setc[lang_answer]
			answerd = setd[lang_answer]
			answere = question[lang_answer]


			answer_array = [answera, answerb, answerc, answerd, answere]
			random.shuffle(answer_array)

			answer = raw_input('Question: '+question[lang] + '\n\nA:' + str(answer_array[0])+ '\n\nB:' + str(answer_array[1])+ '\n\nC:' + str(answer_array[2])+ '\n\nD:' + str(answer_array[3])+ '\n\nE:' + str(answer_array[4])+ '\n\nEnter your answer:')

			
			if answer == 'q' or answer == 'quit':	
				quit = True
				print "You got " + str(correct_answers) + " correct out of " + str(number_of_questions)

			elif answer == 'a' or answer =='b' or answer =='c' or answer =='d' or answer =='e':
				real_answer = 'f'
				if  answer == 'a':
					real_answer = answer_array[0]
				elif  answer == 'b':
					real_answer = answer_array[1]
				elif  answer == 'c':
					real_answer = answer_array[2]
				elif  answer == 'd':
					real_answer = answer_array[3]
				elif  answer == 'e':
					real_answer = answer_array[4]


				if  question[lang_answer]== real_answer:
					print "Correct! \n"
					correct_answers = correct_answers + 1 
					number_of_questions = number_of_questions + 1
					number_of_words = number_of_words - 1
					word_bank.pop(rand)
					wait = raw_input("Enter to continue...")
					os.system('cls')
			
				else:
					print "Wrong! The answer is: " +question[lang_answer] + "\n"
					wait = raw_input("Enter to continue...")
					os.system('cls')
					number_of_questions = number_of_questions + 1
				
			
			else:
				print "Wrong! The answer is: " +question[lang_answer] + "\n"
				number_of_questions = number_of_questions + 1
				wait = raw_input("Enter to continue...")
				os.system('cls')


vtest()