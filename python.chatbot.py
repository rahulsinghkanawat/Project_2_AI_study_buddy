   ##Rule Based AI Python Chatbot


import datetime
import time

name= input("welcome hai,enter your name:")
presenthour= datetime.datetime.now().hour

if 5<= presenthour <12:
   print("good morning", name)
elif 12<= presenthour <17:
   print("good afternoon", name)

elif 17<= presenthour <21:
   print("good evening", name)

else:
   print("good night", name)



print("hello! i am a chatbot. welcome to my world. how can i help you today?")
print("you can ask me anything about python programming language.")


#Chatbot Memory Creation [dictionary of responses]
chatbot_memory = { 
    "hello": "radhe radhe! how are you?",
    "hi": "hello! how can i help you today?",
    "what is python?": "python is a high-level, interpreted programming language known for its simplicity and  readability.",
   " what is the features of python?": "python has several features, including easy-to-read syntax, dyanamic typing, automatic memory management, and a large standard library.",
   "what is the difference between python 2 and python 3?": "python 2 is an older version of python, while python 3 is the latest version. python 3 has several improvements and new features compared to python 2.",
   "what is the use of python?": "python is used for a wide range of applications, including web development, data analysis, artificial intelligence, scientific computing, and more.",
   "what is the best way to learn python?": "the best way to learn python is through practice and hands-on experience. you can start by working on small projects, reading tutorials, and participating in online coding communities.",
   "what are the popular python frameworks?": "some popular python frameworks include django, flask, pyramid, and bottle.",
   "what is the difference between list and tuple in python?": "a list is a mutable data structure that can be modified after creation, while a tuple is an immutable data structure that cannot be modified after creation.",
   "what is the difference between python and java?": "python is a dynamically typed language , while java is a statically typed language. python is known for its simplicity and ease of use, while java is known for its performance and scalability.",
   "which python library is used for data analysis?": "pandas is a popular python library used for data analysis and monipulation. it provides data structures and functions for working with structured data."

}


##method /function to get response from chatbot memory
def get_response(user_input):
    user_input = user_input.lower() 
    for key in chatbot_memory:
      if key in user_input:
        return chatbot_memory[key]
    return "i am sorry, i don't understand. can you please rephrase your question?"

#take user input and get respnse from chatbot memory
while True:
   
    user_input= input("please ask me a question about pythonp programming language: ")
    response= get_response(user_input)
    print(response)

    if "bye" in user_input.lower():
        print(" goodbye! have a great day!")
        break


