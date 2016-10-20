# This program will ask for a user to request to view a file,
# either 'cover letter' or 'resume'.

# After user input, program will do one of three things:
    # 1) if 'resume' is entered, program will type my resume one letter at a time.
    # 2) if 'cover letter' is entered, program will type my cover letter one letter at a time.
    # 3) if entered text doesn't match either 1 or 2, program will reset with a helpful prompt.

    

import time
import sys




class docs:
    
    
    def prompt(self):
        a = input("What document would you like to view? ")

        if (a.title()=="Resume"):
            docs.resume(self)

        elif (a.title()=="Cover Letter"):
            docs.cover(self)

        elif (a.title()=="Exit"):
            docs.leave(self)

        else:
            docs.restart(self)


    
    def resume(self):
        print ("You have requested to view my resume. \n")
        print ("Please wait... \n")
        time.sleep(2.50)
        print ("\n")
        r=open('exampletext2.txt', 'r')
        r2 = r.read()
        docs.delay(self, r2)
        r.close()
        print ("\n")
        while 1<2:
            m = input("Would you like to view another document? ")

            if (m.title()=="Yes"):
                print ("\n")
                docs.prompt(self)
                break

            elif (m.title()=="No"):
                docs.leave(self)
                break

            else:
                print ("Please enter yes or no: \n")
                


    def cover(self):
        print ("You have requested to view my cover letter. \n")
        print ("Please wait... \n")
        time.sleep(2.50)
        print ("\n")
        c=open('exampletext.txt', 'r')
        c2 = c.read()
        docs.delay(self, c2)
        c.close()
        print ("\n")
        while 1<2:
            m = input("Would you like to view another document? ")

            if (m.title()=="Yes"):
                print ("\n")
                docs.prompt(self)
                break

            elif (m.title()=="No"):
                docs.leave(self)
                break

            else:
                print ("Please enter yes or no: \n")

        


    def leave(self):
        print ("Goodbye!")
        sys.exit(1)
            
            
    def restart(self):
        print ("\nPlease type either Cover Letter or Resume to view document. \nOtherwise, type exit to leave program.")
        print ("\n")
        docs.prompt(self)



    def delay(self, s):
        for i in s:
            sys.stdout.write( '%s' % i )
            sys.stdout.flush()

            if (i=='.'):
                time.sleep(0.75)

            else:
                time.sleep(0.02)





ask=docs()
ask.prompt()


