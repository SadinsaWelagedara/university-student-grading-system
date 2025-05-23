# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
#Student Name :W.A.S.Himsari
# Date :14.12.2023

from graphics import *   #import the graphics.py  

countProgress = 0
countTrailer = 0
countExclude = 0
countMretriever = 0
outcomesList =[]

print("Part 1\n")  #Part 1

def getCredit(credit):                        #creating a function to get user input
    creditsRange =[0,20,40,60,80,100,120]
    while True:
        try:
            marks = int(input(f"Please enter your credits at {credit} :"))
            if marks not in  creditsRange:                    #checking if inputs are given range
                print("Out of range")   
                continue
            else:
                break
        except ValueError:                   #handling non-integer values
            print("Integer required") 
    return marks
while True:
    while True:        
        passCredits = getCredit("pass")
        deferCredits = getCredit("defer")
        failCredits = getCredit("fail")
                
        total = passCredits +deferCredits +failCredits       # calculate total marks
        if total == 120:
            if passCredits == 120:
                outcome = "Progress"
                countProgress += 1
            elif passCredits == 100:
                outcome = "Progress(module trailer)"
                countTrailer += 1
            elif failCredits >= 80:
                outcome = "Exclude"
                countExclude += 1
            else:
                outcome = "Module retriever"
                countMretriever += 1
            print(outcome)
            break
        else:
            print("Total incorrect")
            continue
        
    outcomesList.append([outcome,passCredits ,deferCredits ,failCredits]) #append the list items

#Part C - Multiple outcomes
    
    while True:
        multipleOutcomes = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results :").lower()
        print()        #to get a space between lines
        if multipleOutcomes != "y" and multipleOutcomes != "q":  
            print("invalid input")                      # if user input integer ,symbol or different letter
            continue
        else:
            break
    if multipleOutcomes == "y":
        continue
    else:
        break
      

#Part D - Histogram
    
#OPEN THE WINDOW
graph = GraphWin("Histogram", 950, 700)               #open a window object called "graph"  
graph.setBackground("ivory2")                         # Set the background colour of the window

#Set topic of the histogram
topic1 = Text(Point(150 , graph.getHeight() - 650) , "Histogram Results")
topic1.setSize(25) , topic1.setStyle("bold") , topic1.setTextColor("gray12")
topic1.draw(graph)

#Set total count of students
studentCount = countProgress +countTrailer +countExclude +countMretriever  

topic2 = Text(Point(150 , graph.getHeight() - 30) ,f"{studentCount} outcomes in total.")
topic2.setSize(25), topic2.setStyle("bold") , topic2.setTextColor("burlywood4")
topic2.draw(graph)

lines=Line(Point(50, 600) ,Point(900, 600)) 
lines.draw(graph)

maxlength = 450    #maximum bar length
width = 150        #bar width
gap = 50           #gap between 2 bars

#finding the maximum progression outcome
maxcount= max(countProgress ,countTrailer ,countExclude ,countMretriever)

def histogram(length,barpoint,color,text):
    #creating rectangles
    bar = Rectangle(Point(50 +gap +barpoint , graph.getHeight() - 100),
                    Point(50 +gap +barpoint +width ,graph.getHeight()-100 -(maxlength /maxcount) *length))
    bar.setFill(color)
    bar.draw(graph)
    
    #student count of each rectangle
    count = Text(Point(50 +gap +barpoint+ width/2 , graph.getHeight()-100 -(maxlength /maxcount *length)-20),str(length))
    count.setSize(20) , count.setTextColor("bisque4")
    count.draw(graph)
    
    text1 = Text(Point(50 +gap +barpoint+ width/2 , graph.getHeight()-80),text)  #progression outcome of each rectangle
    text1.setSize(20) , text1.setTextColor("bisque4")
    text1.draw(graph)
    
histogram(countProgress , 0*(width+gap) , "cadetblue" , "progress")
histogram(countTrailer , 1*(width+gap) , "darkolivegreen3" , "Trailer")
histogram(countMretriever , 2*(width+gap) , "plum3" , "Retriever")
histogram(countExclude , 3*(width+gap) , "lightpink3" , "Excluded")

graph.getMouse()             # Pause to view result
graph.close()                # Close window when done

#part 2 - To print the list
print("\nPart 2\n")

for value in outcomesList:
    print(f"{value[0]} - {value[1]}, {value[2]}, {value[3]}")
print("----------------------------------------")              #to separate the lines    

#Part 3 - Writing outputs to the text file
print("\nPart 3\n")

with open("outcomes.txt", "w") as textFile:
    for item in outcomesList:
        textFile.write(f"{item[0]} - {item[1]}, {item[2]}, {item[3]}\n")
textFile.close() ##Opening and automatic file closing through context manager

file =open("outcomes.txt", "r")         #read the file
for record in file:
    print(record,end="")
file.close() ###file close 2nd type-because it write in context manager (with open   as)


    
