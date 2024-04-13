import random

def check(comp, user):
  if comp ==user:
    return 0
    
  if(comp == "snake" and user =="water"):
    return -1
    
  if(comp == "water" and user =="gun"):
    return -1
    
  if(comp == "gun" and user == "snake"):
    return -1

  return 1
    
options = ["snake", "water", "gun"]
comp = random.choice(options)
user = input("choose from snake,water and gun: ")

score = check(comp, user)

print("You: ", user)
print("Computer: ", comp)

if(score == 0):
  print("Its a draw")
elif (score == -1):
  print("You Lose")
else:
  print("You Won")
