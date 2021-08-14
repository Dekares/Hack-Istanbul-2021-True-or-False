import os 

number1 = 0
number2 = 1
number3 = 1

outputBinary = ""

while True:
	try:

		output = os.popen("zsteg logs3months/{2}/{1}/{0}/flg.png".format(number1,number2,number3)).read()

		if "True" in output:
			outputBinary+= "1"
			
		if "False" in output:
			outputBinary+="0"

		number1 += 1
		
		if number1 == 24:
			number1 = 0
			number2 += 1
			
			if number2 == 6:
				number2 = 1
				number3+=1
				
				if number3 == 4:
					print(outputBinary)
					break
	except KeyboardInterrupt:
		print("Program durduruldu.")
		print(outputBinary)
		break
		pass



