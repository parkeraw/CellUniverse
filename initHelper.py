



from Tkinter import * # Tk , Label, Button, Entry, IntVar, END, W, E
import cv2 
from math import atan2, pi, sqrt


class LookupGenerator:

    def __init__(self, master):
        self.master = master
        master.title("Init Helper")
        self.rowCount = 5
        self.stateCount = 1
        
        self.sectionNamePrompt = Label(master,text = "Init file name: ")
        self.sectionNameEntry = Entry(master)
        
        self.selectBacteria = Button(master, text="Select Bacteria", command=lambda: self.update("select"))

        self.generateTable = Button(master, text="Save init file", command=lambda: self.update("generate"))
        
        

        LookupGenerator.reDraw(self)
        self.update("addState")
        
    def reDraw(self):
      
        self.sectionNamePrompt.grid(row=0, column=0, sticky=E)
        self.sectionNameEntry.grid(row=0, column=1,columnspan=5,sticky=W)
        
     
        
        
        self.selectBacteria.grid(row=11,column=2)
        self.generateTable.grid(row=11,column=3)
        
    def draw_circle(event,f,x,y,isClick,b):
        global mouseX,mouseY
        if isClick:
            
            mouseX,mouseY = x,y
            #print x,y

    
    def update(self, method):
        if method == "select":
            self.cellPositions = []
            self.image = cv2.imread('frames/0.png')
            self.image = cv2.resize(self.image, (0,0), fx=2, fy=2)
            cv2.namedWindow('init frame')
            cv2.setMouseCallback('init frame',self.draw_circle)
            cv2.putText(self.image,'left click the ends of each bacterium',(2,12),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,0,255),1)
            cv2.putText(self.image,'confirm each click by pressing ENTER',(2,25),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,0,255),1)
            cv2.putText(self.image,'press \'ESC\' before exiting the window.',(2,37),cv2.FONT_HERSHEY_SIMPLEX,0.45,(0,0,255),1)


            while 1:
                cv2.imshow('init frame',self.image)
                k = cv2.waitKey(20) & 0xFF
                
                if k == 27:
                    break
                elif k == 13:
                    try:
                        print mouseX//2,mouseY//2
                        cv2.circle(self.image,(mouseX,mouseY),3,(0,0,255),-1)
                        self.cellPositions.append((mouseX//2,mouseY//2))
                    except:
                        pass
                
                

        
        elif method == "generate":
            self.fileName = self.sectionNameEntry.get()+'.init.txt'

            #generate cell params
            if len(self.cellPositions)%2 != 0:
                print 'ODD number of cell ends have been selected, exiting..'
                quit()
            if len(self.cellPositions) == 0:
                print 'Please select the ends of each cell before creating the file'
                return
            cells = []
            
            for i in range(0,len(self.cellPositions)-1,2):
                px = (self.cellPositions[i][0] + self.cellPositions[i+1][0])//2
                py = (self.cellPositions[i][1] + self.cellPositions[i+1][1])//2
                l = sqrt(abs(self.cellPositions[i][0] - self.cellPositions[i+1][0])**2 + abs(self.cellPositions[i][1] - self.cellPositions[i+1][1])**2) + 6
                rot = atan2(self.cellPositions[i+1][1] - self.cellPositions[i][1], self.cellPositions[i+1][0] - self.cellPositions[i][0]) 
                cells.append((px,py,l,rot))
            file_text = ''
            for param in [self.dtEntry,            self.initLengthEntry,            self.initWidthEntry,            self.maxSpeedEntry,            self.maxSpinEntry,            self.kUniversesEntry,            self.maxXmotionEntry,            self.maxYmotionEntry,            self.maxXresolutionEntry,            self.maxYresolutionEntry,            self.maxRotationEntry,            self.maxRotationResolutionEntry,            self.minimumHeightIncreaseEntry,            self.maxHeightIncreaseEntry,            self.heightIncreaseResolutionEntry,            self.maxLengthBeforeSplittingEntry,            self.minimumLengthEntry,            self.beginSplitRatiopEntry,            self.endSplitRatioEntry,            self.splitRatioResolutionEntry]:
                file_text += param.get() + '\n'

            file_text += 'pos:x   pos:y   length  rotation \n'
            for cell in cells:
                file_text += str(cell[0]) + ' ' + str(cell[1]) + ' ' + str(cell[2]) + ' ' + str(cell[3]) + '\n' 
            
            f = open(self.sectionNameEntry.get() + '.init.txt','w')
            f.write(file_text)
            f.close()
            print 'saved init file at ' + self.sectionNameEntry.get() + '.init.txt'
            
        elif method == "addState":

            #row 1
            self.dtprompt = Label(self.master,text = "dt:")
            self.dtprompt.grid(row=1,column = 0)
            
            self.dtEntry = Entry(self.master)
            self.dtEntry.grid(row=1,column = 1)

            self.dtEntry.insert(0,'0.33')

            self.initLengthprompt = Label(self.master,text = "init length:")
            self.initLengthprompt.grid(row=1,column = 2)
            
            self.initLengthEntry = Entry(self.master)
            self.initLengthEntry.grid(row=1,column = 3)

            self.initLengthEntry.insert(0,'26')


            #row2
            self.initWidthprompt = Label(self.master,text = "init width:")
            self.initWidthprompt.grid(row=2,column = 0)
            
            self.initWidthEntry = Entry(self.master)
            self.initWidthEntry.grid(row=2,column = 1)

            self.initWidthEntry.insert(0,'6')

            self.maxSpeedprompt = Label(self.master,text = "max speed:")
            self.maxSpeedprompt.grid(row=2,column = 2)
            
            
            self.maxSpeedEntry = Entry(self.master)
            self.maxSpeedEntry.grid(row=2,column = 3)

            self.maxSpeedEntry.insert(0,'26')

            #row3
            
            self.maxSpinprompt = Label(self.master,text = "max spin:")
            self.maxSpinprompt.grid(row=3,column = 0)
            
            self.maxSpinEntry = Entry(self.master)
            self.maxSpinEntry.grid(row=3,column = 1)

            self.maxSpinEntry.insert(0,'0.3141592653589793')

           
            self.kUniversesprompt = Label(self.master,text = "K universes:")
            self.kUniversesprompt.grid(row=3,column = 2)
            
            
            self.kUniversesEntry = Entry(self.master)
            self.kUniversesEntry.grid(row=3,column = 3)

            self.kUniversesEntry.insert(0,'20')

            #row4
            
            
            self.maxXmotionprompt = Label(self.master,text = "max x motion:")
            self.maxXmotionprompt.grid(row=4,column = 0)
            
            self.maxXmotionEntry = Entry(self.master)
            self.maxXmotionEntry.grid(row=4,column = 1)

            self.maxXmotionEntry.insert(0,'3')

           
            self.maxYmotionprompt = Label(self.master,text = "max y motion:")
            self.maxYmotionprompt.grid(row=4,column = 2)
            
            self.maxYmotionEntry = Entry(self.master)
            self.maxYmotionEntry.grid(row=4,column = 3)

            self.maxYmotionEntry.insert(0,'3')
            
            #row5
            
            self.maxXresolutionprompt = Label(self.master,text = "max x resolution:")
            self.maxXresolutionprompt.grid(row=5,column = 0)
            
            self.maxXresolutionEntry = Entry(self.master)
            self.maxXresolutionEntry.grid(row=5,column = 1)

            self.maxXresolutionEntry.insert(0,'7')

           
            self.maxYresolutionprompt = Label(self.master,text = "max y resolution:")
            self.maxYresolutionprompt.grid(row=5,column = 2)
            
            self.maxYresolutionEntry = Entry(self.master)
            self.maxYresolutionEntry.grid(row=5,column = 3)

            self.maxYresolutionEntry.insert(0,'7')

            #row6
            
            self.maxRotationprompt = Label(self.master,text = "max rotation:")
            self.maxRotationprompt.grid(row=6,column = 0)
            
            self.maxRotationEntry = Entry(self.master)
            self.maxRotationEntry.grid(row=6,column = 1)

            self.maxRotationEntry.insert(0,'0.3141592653589793')

        
            self.maxRotationResolutionprompt = Label(self.master,text = "max rotation resolution:")
            self.maxRotationResolutionprompt.grid(row=6,column = 2)
            
            self.maxRotationResolutionEntry = Entry(self.master)
            self.maxRotationResolutionEntry.grid(row=6,column = 3)

            self.maxRotationResolutionEntry.insert(0,'7')

            #row7
            
            self.minimumHeightIncreaseprompt = Label(self.master,text = "minimum height increase:")
            self.minimumHeightIncreaseprompt.grid(row=7,column = 0)
            
            self.minimumHeightIncreaseEntry = Entry(self.master)
            self.minimumHeightIncreaseEntry.grid(row=7,column = 1)

            self.minimumHeightIncreaseEntry.insert(0,'0')

           
            self.maxHeightIncreaseprompt = Label(self.master,text = "max height increase:")
            self.maxHeightIncreaseprompt.grid(row=7,column = 2)
            
            self.maxHeightIncreaseEntry = Entry(self.master)
            self.maxHeightIncreaseEntry.grid(row=7,column = 3)

            self.maxHeightIncreaseEntry.insert(0,'3')

            #row7
            
            self.heightIncreaseResolutionprompt = Label(self.master,text = "height increase resolution:")
            self.heightIncreaseResolutionprompt.grid(row=8,column = 0)
            
            self.heightIncreaseResolutionEntry = Entry(self.master)
            self.heightIncreaseResolutionEntry.grid(row=8,column = 1)

            self.heightIncreaseResolutionEntry.insert(0,'4')

           
            self.maxLengthBeforeSplittingprompt = Label(self.master,text = "max length if bacterua before splitting:")
            self.maxLengthBeforeSplittingprompt.grid(row=8,column = 2)
            
            self.maxLengthBeforeSplittingEntry = Entry(self.master)
            self.maxLengthBeforeSplittingEntry.grid(row=8,column = 3)

            self.maxLengthBeforeSplittingEntry.insert(0,'31')

            #row8
            
            self.minimumLengthprompt = Label(self.master,text = "minimum length of any bacteria:")
            self.minimumLengthprompt.grid(row=9,column = 0)
            
            self.minimumLengthEntry = Entry(self.master)
            self.minimumLengthEntry.grid(row=9,column = 1)

            self.minimumLengthEntry.insert(0,'13')

           
            self.beginSplitRatioprompt = Label(self.master,text = "beginning of split ratio:")
            self.beginSplitRatioprompt.grid(row=9,column = 2)
            
            self.beginSplitRatiopEntry = Entry(self.master)
            self.beginSplitRatiopEntry.grid(row=9,column = 3)

            self.beginSplitRatiopEntry.insert(0,'0.25')


            #row9

            self.endSplitRatioprompt = Label(self.master,text = "end of split ratio:")
            self.endSplitRatioprompt.grid(row=10,column = 0)
            
            self.endSplitRatioEntry = Entry(self.master)
            self.endSplitRatioEntry.grid(row=10,column = 1)

            self.endSplitRatioEntry.insert(0,'0.75')

            self.splitRatioResolutionprompt = Label(self.master,text = "split ratio resolution:")
            self.splitRatioResolutionprompt.grid(row=10,column = 2)
            
            self.splitRatioResolutionEntry = Entry(self.master)
            self.splitRatioResolutionEntry.grid(row=10,column = 3)

            self.splitRatioResolutionEntry.insert(0,'20')
            

            
        
            
    
           

root = Tk()


my_gui = LookupGenerator(root)

root.mainloop()
