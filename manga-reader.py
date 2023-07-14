import sys, os, time

"""
Usage:
manga.py [folder]
"""

#to do:
#    -Create help output


#this could be implemented with argv... DO SO!!
#update: I did so. 
path = sys.argv[1]

try: #check whether the user specified a chapter number to start at
    indice = int(sys.argv[2])
except IndexError:
    indice = 1
    
ti = 0


print("Using path: " + path)


while True:

    ti = time.monotonic_ns() #start quit-detection-stopwatch
    
    #The following three blocks load the chapter based off of the variable 'indice'
    #Since not all chapter numbers are unique (i.e., the 95 in chapter 95 is also in chapter 195, 295, 395, etc)
    #, the program detects the order in order of the chapter number so it can
    #prefix it with the proper amount of zeroes. This, of course, only works
    #for manga whose chapters are all four digits, but this is the standard
    #mangal naming scheme, and thus is somewhat reasonable.
    if indice < 10:
        var = os.system("viewnior " + path + "/*000" + str(indice) + "*")
        print("Using command: viewnior " + path + "/*000" + str(indice) + "*")
        
    elif (10 <= indice) & (indice < 100):
        var = os.system("viewnior " + path + "/*00" + str(indice) + "*")
        print("Using command: viewnior " + path + "/*00" + str(indice) + "*")

    else:
        var = os.system("viewnior " + path + "/*0" + str(indice) + "*")
        print("Using command: viewnior " + path + "/*0" + str(indice) + "*")

    if time.monotonic_ns() - ti <= 3000000000: #if the stopwatch has counted out less than three seconds, 
        break
    
    #error detection! I also put the ticker in here. I could put it outside
    #of this function. I could definitely do that, as it's completely within
    #my power.
    if var == 0:
        print("iteration sucessful")
        indice += 1
    else:
        print("Error \"" + var + "\" was retruned by viewnior, exiting...")
        break
