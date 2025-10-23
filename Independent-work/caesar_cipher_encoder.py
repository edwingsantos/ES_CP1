#ES 1  Caesar Cipher Encoder and Decoder


#make an input for the user to choose a letter 
letter = input("choose a lower case letter: ")
#make the text variable and make the letter input = ord(letter), so it turns into a number 
text = ord(letter)
#make a num variable and make it a interger, then make text = chr(text)
num = (f"{text} = {chr(text)}")
print(num)