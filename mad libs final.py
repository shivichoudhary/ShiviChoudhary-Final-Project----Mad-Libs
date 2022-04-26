#Shivi Choudhary
#Final project: Mad Libs Generator

from tkinter import * #upon doing research I learned that Tkinter is an interface used with Python to the "Tk GUI toolkit" which is what essentially creates the window


root = Tk() #creates the window
root.geometry('420x420') #creates the size of the window in which the options to choose the madlib pop up
root.title('DataFlair-Mad Libs Generator')
Label(root, text= 'Shivi the Great - Mad Libs Generator \n Fill out at your own risk' , font = 'arial 20 bold').pack()
Label(root, text = 'Click The Most Intriguing One :', font = 'arial 15 bold').place(x=40, y=80)

def madlib1():
    adjective1 = input('enter adjective : ')
    adjective2 = input('enter adjective : ')
    animal1 = input('enter a animal name : ')
    verb1 = input('enter a verb in the past tense : ')
    verb2 = input('enter a verb name : ')
    adjective3 = input('enter adjective : ')
    animal2 = input('enter a animal name : ')
    verb3 = input('enter a verb name ending in ing : ')
    bodypart = input('enter a bodypart : ')
    animal3 = input('enter a animal name : ')
    verb4 = input('enter a verb in the past tense : ')
    print('It was a ' +adjective1+ ' gloomy December evening. I woke up to the ' +adjective2+ ' aroma of ' +animal1+ ' rotting away in our fireplace. No one else seemed to notice so I did not bring it up. I ' +verb1+ ' down the stairs to see if I could help ' +verb2+ ' with dinner. My mom asked me to place firewood in the fireplace to start a fire for the dinner table. So I made my way to the back shed where the ' +adjective3+ ' smell only became worse. I crept to the shed to open the doors and there lay hundreds of ' +animal2+ ' eggs. I was terrified that they had invaded my home. I ran away ' +verb3+ ' .I couldnt believe my ' +bodypart+ ' .Suddenly I woke up. It was all a dream thank god. I got out of bed when suddenly I smell the scent of ' +animal3+ ' all over again. Oh no I ' +verb4+ ' here we go again!')
def madlib2():
    comichero = input('enter a comic book hero name : ')
    unrealisticprofession = input('enter an unrealistic profession : ')
    comichero = input('enter a comic book hero name :')
    verb1 = input('enter a verb of a violent action : ')
    villain= input('enter a name of a villain : ')
    verb2 = input('enter a verb name : ')
    person= input('enter a person name : ')
    noun1 = input('enter a noun : ')
    cityname = input('enter a name of a city : ')
    noun2 = input('enter a noun : ')
    verb3 = input('enter a verb name ending in ing : ')
    noun3 = input('enter a noun : ')
    thing = input('enter a thing name :')
    print('Meet our hero ' +comichero+ ' , a super intelligent ' +unrealisticprofession+ ' .He only leaves his house at night to pursue his hidden identity. Many years ago ' +comichero+ ' had ' +verb1+ ' his face while fighting ' +villain+ ' .He does not like for people to see his face because they ' +verb2+ ' away screaming. Eventually it is discovered that our heros long time colleague ' +person+ ' is trying to turn ' +noun1+ ' into a weapon, leading to a battle in downtown ' +cityname+ ' threatening the lives of hundreds of ' +noun2+ ' .However, hour hero does not step down from this battle, instead he went ' +verb3+ ' to the top of a ' +noun3+ ' so that he could throw ' +thing+ ' at the weapon and save the day.')
def madlib3():
    adjective1 = input('enter adjective : ')
    verb1 = input('enter a verb name ending in ing : ')
    verb2 = input('enter a verb name ending in ing : ')
    animal = input('enter a animal name : ')
    person1 = input('enter a person name : ')
    noun1 = input('enter a noun : ')
    thing = input('enter a thing name :')
    adjective2 = input('enter adjective : ')
    noun2 = input('enter a noun : ')
    instrument = input('enter an instrument name : ')
    verb3 = input('enter a verb name ending in ing : ')
    person2 = input('enter a person name : ')
   
    print('I adore long ' +adjective1+ ' walks on the beach ' +verb1+ ' in the rain, and ' +verb2+ ' with my pet ' +animal+ ' .His name is ' +person1+ ' .I like music and Champagne mixed with ' +noun1+ ' when I am not busy with work. I am looking for love and beauty in the form of a ' +thing+ ' goddess. It is very important that anyone looking to fulfill the role of being my girlfriend makes sure she has the ' +adjective2+ ' of a ' +noun2+ ' .I prefer that she knows how to play the ' +instrument+ ' .Now I know you might think I dont look that good in my picture. Trust me it was taken right after I was done ' +verb3+ ' but I assure you I look better in person. I will wait for your reply. Sincerily ' +person2+ ' Hope to hear from my future girlfriend soon. ')
                
Button(root, text= 'An Invasive Species', font ='arial 15', command= madlib1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'Comic Book Hero', font ='arial 15', command = madlib2, bg = 'ghost white').place(x=80, y=240)
Button(root, text= 'Craigslist Girlfriend Ad', font ='arial 15', command = madlib3 , bg = 'ghost white').place(x=70, y=180)

root.mainloop()
