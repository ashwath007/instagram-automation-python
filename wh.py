import pywhatkit as pwk
 
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     pwk.sendwhatmsg("+916364250724", "Hi, how are you?",1, 48)
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")
     