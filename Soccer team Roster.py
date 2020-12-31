#Mijash Ghimire Code
#student Western oregon university
#Code for soccer rooster
#2/28/2020


my_dict = {}
new_dict = {}

for i in range(1,6):
  jersey_num = int(input("Enter player %d's jersey number:\n" % i)) 
  rate_num = int(input("Enter player %d's rating:\n" % i))
  my_dict[jersey_num] = rate_num
  list_jersey = list(my_dict.keys()) 
  list_jersey = sorted(list_jersey)
  i += 1
  print()
print("ROSTER")
for i in list_jersey:
  print("Jersey number: %d, Rating: %d" % (i, my_dict[i]))
  
while True:
  list_jersey = list(my_dict.keys())
  list_jersey = sorted(list_jersey)
  print()
  print("MENU")
  print("a - Add player")
  print("d - Remove player")
  print("u - Update player rating")
  print("r - Output players above a rating")
  print("o - Output roster")
  print("q - Quit") 
  option = input("\nChoose an option:\n")
  if option == "q":
    exit()
  elif option == "o":
    print()
    print("ROSTER")
    for i in list_jersey:
      print("Jersey number: %d, Rating: %d" % (i, my_dict[i]))
  elif option == "a":
    jersey_num2 = int(input("Enter a new player's jersey number:\n"))
    rate_num2 = int(input("Enter the player's rating:"))
    new_dict[jersey_num2] = rate_num2
    my_dict.update(new_dict)
  elif option == "d":
    jersey_remove = int(input("Enter a jersey number:\n"))
    my_dict.pop(jersey_remove)
  elif option == "u":
    jersey_new = int(input("Enter a jersey number:\n"))
    rate_new = int(input("Enter a new rating for player:\n"))
    my_dict[jersey_new] = rate_new
  elif option == "r":
    rate_1 = int(input("Enter a rating:\n"))
    print()
    print("ABOVE %d" % rate_1)
    for jersey in list_jersey:
      j = my_dict[jersey]
      if j > rate_1:
        print("Jersey number: %d, Rating: %d" % (jersey, j))
      if j <= rate_1:
        continue
      
      
        

        
    

  
    
    

  
