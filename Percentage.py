#Take input from user on 4 subjects

math = int(input("Enter your marks in Math"))
english = int(input("Enter your marks in English"))
hindi = int(input("Enter your marks in Hindi"))
science = int(input("Enter your mark in Science"))

#Lets calculate the percentage of your grade

sum = math+english+hindi+science

print("sum of Math, English, Science, and Hindi:")
perc = (sum/400)*100

print(end= "Percentage mark = ")
print(perc)