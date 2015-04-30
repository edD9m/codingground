print "Hi, my name is Python! I'm a programming language that's intelligent but simple! Enjoy your stay!"
print "Soo, please answer my questions."
myname=raw_input("What's your name? >>> ")
print "Nice to meet you, " + " " + myname
if myname == "myname" :
    print "Oh, by the way, don't enter the name of the variable, thanks."
if myname == "name" :
    print "Yes, I know it's a name, but what IS your name?"
print "Good! Let's move on forward! How about I calculate a sum of two variables?"
calc=raw_input("So, shall  I? You can answer either yes or no in downcase so my script will work properly! ")
if calc == "yes." :
    a=20
    b=30
    print a+b,"is the answer."
else :
    print "Well, I can't complain, so, shall we go on? "
shallwe=raw_input("So, shall we go on? Answer yes or no in downcase. ")
if shallwe == "yes" :
    print "Well, let's go on! Now, let me calculate a complex mathematical equation!"
else :
    print "I can't complain, but shall we go forward?"
shallwe2=raw_input("Shall we? ")
if shallwe2 == "yes" :
    print "Haha, you are interested already!"
else :
    print "Well, well, well."


v=30
c=20
numbers=v+c

print ("My calculations say: %i meters." % numbers)

print "Well, I think you are enjoying this! Shall we go on?"
go_on=raw_input("Shall we?")
if go_on == "yes" :
    print "So, let's go on!"
else :
    print "Well, that's fine by me!"
shallweend=raw_input("So, shall we end your first course or shall we continue? ")
if shallweend == "yes" :
    print "Goodbye!"
else :
    print "Well, if you want to continue the ride, let's go on!"
print "Now, let me show ya simple lists."
list = ["cats", "bong", "hey!", "hockey"]
print list
del list[2]
print list

print "This is the end of course 1, goodbye!"
print "INTERACTIVE PYTHON"
print "by edD."
print "------------------------------------"


print "Well, shall we start course 2?"
shallwe3=raw_input("Shall we or no? ")
if shallwe3 == "yes" :
    print "Alright!"
else :
    print "Well, that's fine."
print "Course 2 will be exclusive to some more fun script."
print "So, let me show you how to print out all the letters in Python."
for letter in "Python":
    print "Current letter: ", letter
print "Here is an another example."
vegetables = ['tomato', 'potato', 'carrot']
for vegetable in vegetables:
    print "Current vegetable: ", vegetable
    
print "Well, this is the short end of the first part of the guide."