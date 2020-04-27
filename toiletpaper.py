
print("One of the most interesting phenomenon in the beginning of this global health crisis is the hoarding of toilet paper.\n"
      "Discussions on the amount of toilet paper used per day between London based Software Developer Ben Sasson and Artist Sam Harris gave birth to howmuchtoiletpaper.com.\n"
      "In it, users can input the amount of rolls users have and the mount of toilet visit per day. \n"
      "The two inputs then get calculated into the equation:\n       160 sheets per roll × rolls users have / (6 sheets per visit × toilet visits per day)\n"
      "to produce the output on how long will the supply of their toilet paper last.\n"
      "The website has garnered over 12 million visitors and many publicities. \n"
      "Just for fun, I'm writing a program that reads in the amount of rolls users have and the amount of toilet visit per day and outputs the number of days will their supply of toilet paper last for.")

roll = int(input("Enter the no. of toilet rolls you have: "))
visit = int(input("Enter the no.of visits to bathroom per day: "))
result = int(((160*roll)/(6*visit)))
print("You will last for "+str(result)+" days!")