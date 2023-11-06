"""
Alexander
30/05/2023
Chat Bot
""" 

# importing our libaries / isacat = False

import random as rd
import webbrowser 


isacat = False


# start intro
print("")
print("hello, I am a chatbot, what is your name?")
name = input("insert name here:").lower()

if name == "alexander":
  print(" oh, yes, you created me. well done")
elif name == "james":
  print("oh, I have heard of you, you helped invent 'space robots'")
elif name == "archie":
  print("oh hi archie, I hear you are good at hide and seek")
elif name == "dad":
  print ("hi dad, nice to meet you, you are likely in bed.")
elif name == "mum":
  print ("hi mum, the super creator of the man who made me.")

else:
  print(f"oh nice to meet you, {name}.")

 
print(f"how are you today, {name}?")
mood = input ("insert mood here:")
if mood == "good":
  print("that is amazing, I am also good!")
elif mood == "bad":
  print("i am sorry to hear that, I hope you feel better soon.")
elif mood == "meh":
  print("well, at least you are not bad")
elif mood == "tired":
  print ("it is okay. you will get more energy soon")
else:
  print (f"it is interesting that you are {mood} {name}")

print(f"what are your hobbies {name}?")
plans = input ("insert hobbies here:").lower()
if plans == "walk":
  print(f"nice {name}, i wish i could walk.")
elif plans == "game":
  print ("i can help you win your game")
elif plans == "snooze": 
  print ("ah, you must be dad.")
elif plans == "play sport":
  print ("cool, i know all about sport") 
elif plans == "work":
  print ("i hope your work goes well")
elif plans == "rest":
  print ("i guess everyone needs to rest.")
else :
    print(f"cool, have a nice time with your {plans} {name}.")
    
print (f"what is your favorite colour {name}?") 
colour = input ("insert answer here:").lower()
if colour == "red":
    print ("red is amazing, it is also my favorite colour.")
elif colour == "light blue":
  print (f"WHAT!!! {colour} is so bad!")
else: 
    print (f"i like {colour} too. It is really good, isn't it?")  

print("what country are you from?")
country = input("insert country here:").lower()
if country == "uk":
  print ("oh yes, I am from uk.")
elif country == "us":
  print ("i wish I had been there.")
elif country == "australia":
  print ("we are on different sides of the world!") 
elif country == "france":
  print ("bonjour, je m'appelle Chatbot Zi.")
elif country == "italy":
  print ("ciao, mi chiamo Chatbot")
else: 
  print (f"i hear great things about {country}.")

# dictionary 



# end intro
  
print ("thanks for helping with the intro.")
print("")




"""alexander dictionary is defined here"""
alexander_dict = {'fav colour : red', ' fav food : chicken tikka masala', 'age : 10 ' }

joke = {'why was the broom late?' : 'because it over swept :) ', 'what did one elevator say to the other elevator?' : 'i think i am coming down with something:)', 'why did the scarecrow win a prize?' : 'because he was outstanding in the field:)', 'if you hold 9 oranges in one hand and 10 lemons in another, what do you have?' : 'big hands!'}

key, value = rd.choice(list(joke.items()))

# questions

while isacat == False:
  joke = {'why was the broom late?' : 'because it over swept :) ', 'what did one elevator say to the other elevator?' : 'i think i am coming down with something:)', 'why did the scarecrow win a prize?' : 'because he was outstanding in the field:)', 'if you hold 9 oranges in one hand and 10 lemons in another, what do you have?' : 'big hands!'}

  key, value = rd.choice(list(joke.items()))
  questions = input ("do you have any questions?").lower()
  if questions == "print alexander dict":
    print (alexander_dict) 
  elif questions == "no": 
    print ("ok then")
  elif questions == "joke":
    print(key, value)
  elif questions == "calculate":
    print ("i know 56 + 56 = 112, but that's it")
  elif questions == "news":
    print ("I found this on the web:")
    webbrowser.open_new_tab("https://www.bbc.co.uk/news")
  elif questions=="roll dice":
    dice=rd.randint(1,6)
    print(f"{dice}")
  elif questions=="weather":
    print ("I found this on the web")
    webbrowser.open_new_tab("https://www.bbc.co.uk/weather")
  elif questions=="cubing":
    print(f"i would go to jperm.net {name}")
    cbing = input ("shall i take you there?").lower()
    if cbing=="yes":
      webbrowser.open_new_tab("https://jperm.net")
    else:
      print("ok then.")
  elif questions == "rock paper scissors":
    prs = input ("ok what are you?")
    print (f"")
    mrs = rd.randint (1,3)
    if mrs == 1:
      print (f" you were {prs} and i was a rock from mars.")
    elif mrs == 2:
      print (f" you were {prs} and i was a5 paper")
    elif mrs == 3:
      print (f" you were {prs} and i was the world's sharpest scissors.")
    else:
      print (f'sorry {name} but there was an error in "rock paper scissors":(') 
  elif questions == ("take me to this website"):
    web = input("where shall i take you?")
    webbrowser.open_new_tab(f"{web}") 
  else:
    print (f"i am sorry {name}, but i cannot answer that question :(")
    

# random = rd
joke = {'why was the broom late?' : 'because it over swept :) ', 'what did one elevator say to the other elevator?' : 'i think i am coming down with something:)', 'why did the scarecrow win a prize?' : 'because he was outstanding in the field:)', 'if you hold 9 oranges in one hand and 10 lemons in another, what do you have?' : 'big hands!'}

key, value = rd.choice(list(joke.items()))
print(key, value)
