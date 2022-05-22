############################################################################################################################################################################
#Τσάμπρας Ιωάννης
#Στάικος Θεόδωρος
#Λυκουργιώτης Γενναίος
#Πολίτης Παναγιώτης
#Πολίτη Τατιανή
#Τζανάτος Μιχαήλ

#################################################################################################################################
def sunarthseis_creation(x=1):
    global leksiko_sunarthseis
    leksiko_sunarthseis={}
    if x==1:
        f=open('resources/functions.txt','r',encoding='utf-8-sig')
    else:
        f=open('resources/functionsdefault.txt','r',encoding='utf-8-sig')
    for line in f:
        linE=line.strip()
        try:
            if linE[0]=="N":
                if linE[4]==":":
                    fName=linE.replace("Name:","").strip() 
                else:
                    fNameGUI=linE.replace("NameGUI:","").strip()
            elif linE[0]=="I":
                fInfo=linE.replace("Info:","").strip()
            elif linE[0]=="V":
                fVariables=linE.replace("Variables:","").strip()
            elif linE[0]=="D":
                fDef=linE.replace("Def:","").strip()
            elif linE[0]=="C":
                fCheck=linE.replace("Check:","").strip()
            elif linE[0]==">":
                s=0
                for i in leksiko_sunarthseis:
                    if s<leksiko_sunarthseis[i].GUIrow:
                        s=leksiko_sunarthseis[i].GUIrow
                leksiko_sunarthseis["{}". format(fName)] = Sunarthsh(fName,fNameGUI,fInfo,fVariables,fDef,fCheck,s+1,0)
        except:
            pass
        
    
    f.close()


#################################################################################################################################


#################################################################################################################################           
class Sunarthsh:
    def __init__(self,Name,NameGUI,Info,Variables,Def,Check,GUIrow,ap):
        self.Name=Name
        self.Variables=int(Variables)
        self.NameGUI=NameGUI
        self.Info=Info
        self.Def=Def
        self.Check=Check
        self.GUIrow=GUIrow

        if ap==0:
            self.bonoma=Button(eastFrame,text="  {}  ".format(self.NameGUI),bg="orange",width=15, command=self.execute)
            self.bonoma.grid(column=0,row=GUIrow)
            self.bdelete=Button(eastFrame,text="Hide",bg="purple",width=5,command=self.click_delete_function,cursor='X_cursor',)
            self.bdelete.grid(column=2,row=GUIrow)
            self.bview=Button(eastFrame,text="Info",bg="green",command=self.click_info,cursor='question_arrow',bitmap='info')
            self.bview.grid(column=1,row=GUIrow)
            self.bdeletep=Button(eastFrame,text="Hide",bg="brown",command=self.click_delete_functionp,cursor='X_cursor',bitmap="error",height=20)
            self.bdeletep.grid(column=3,row=GUIrow)           
        else:
            pass
    def execute(self):
        global lista4
        self.window4=Tk()
        self.window4.title("{}".format(self.NameGUI))
        ypsos=self.Variables*20+70
        self.window4.geometry("350x{}+500+500".format(ypsos))
        self.window4.configure(bg="orange")
        if self.Variables==1:
            Label(self.window4,text="Type the name of table you want for  {}".format(self.NameGUI),bg="orange").grid(row=0,column=0,columnspan=3)
        else:
            Label(self.window4,text="Type the names of tables you want for  {}".format(self.NameGUI),bg="orange").grid(row=0,column=0,columnspan=3)
        lista4=[]
        for i in range(self.Variables):
            lista4.append(Entry(self.window4,width=10))
            lista4[i].grid(row=i+1,column=1,sticky=W)
            Label(self.window4,text="{} Table".format(i+1),width=10).grid(column=0,row=i+1)

        btnCancel=Button(self.window4,text="Cancel",width=8,bg="purple",command=self.cancel_it).grid(row=self.Variables+1,column=2,sticky=E)
        btnEnter=Button(self.window4,text="Enter",width=8,bg="brown",command=self.execute_it).grid(row=self.Variables,column=2,sticky=E)



    def cancel_it(self):
        
        self.window4.destroy()

    def execute_it(self):
        global leksiko_main,lista4
        lista5=[]
        for i in lista4:
            entered=i.get()
            lista5.append(entered)
        
        for p in lista5:
            g=0
            for i in leksiko_main:
                if p==i:
                    g=1
            if g==0:
                try:
                    self.w12.grid_remove()
                except:
                    pass
                self.w12=Label(self.window4,text="{} is not defined".format(p),bg="red")
                self.w12.grid(row=self.Variables+1,column=0)
                    
                        
                
                break
        if g==1:
            s=self.Check
            for i in range(1,self.Variables+1):
                s=s.replace("#{}#".format(i),"leksiko_main['{}'].array".format(lista5[i-1]))
            s="import numpy as np\nimport scipy as scipy\nimport scipy.linalg\n"+"if "+s+" :\n\tok=1\nelse:\n\tok=0"
            exec(s,globals())
            if ok==1:
                self.exec_it(lista5)
            else:
                try:
                    self.w12.grid_remove()
                except:
                    pass
                self.w12=Label(self.window4,text="Unsupported operation for these tables".format(p),bg="red")
                self.w12.grid(row=self.Variables+1,column=0)

    def exec_it(self,lista5):
        global results,apotelesma,apotelesma1
        s=self.Def
        display=self.Def
        for i in range(1,self.Variables+1):
            s=s.replace("#{}#".format(i),"leksiko_main['{}'].array".format(lista5[i-1]))
        s="import numpy as np\nimport scipy as scipy\nimport scipy.linalg\n"+"result="+s
        exec(s,globals())
        apotelesma=result
        if str(type(apotelesma))=="<class 'numpy.ndarray'>":
            apotelesma1=0
        else:
            apotelesma1=1
        for i in range(1,self.Variables+1):
            display=display.replace("#{}#".format(i),"{}".format(lista5[i-1]))
        display=display+"=\n\n\n"
        
        results.delete('1.0', END)
        results.insert(END,display)
        k=0
        try:  
            for i in result:
                for g in i:
                    if len(str(int(g)))>k:
                        k=len(str(int(g)))
                     
            for i in result:
                results.insert(END,"[")
                for g in i:
                    
                    gap="0"
                    gap=gap*(k-len(str(int(g))))
                    results.insert(END,"{}{:.2f},  ".format(gap,g))
                    
                    
                results.insert(END,"]\n\n")
        except:
            results.insert(END,"{}".format(result))
            
            
        self.cancel_it()

#################################################################################################################################
    def click_delete_function(self):
        self.confirm=Tk()
        self.confirm.geometry('230x80+400+400')
        self.confirm.config(bg='cyan')
        self.confirm.title('Confirm')
        def yes():
            self.click_delete_function_silent()
            self.confirm.destroy()
            
        def no():
            self.confirm.destroy()
        l1=Label(self.confirm,text='Are you sure you want to hide {}?'.format(self.NameGUI))
        l1.pack(anchor=CENTER)
        b1=Button(self.confirm,text='Yes',bg='yellow',command=yes)
        b1.pack()
        b2=Button(self.confirm,text='No',bg='yellow',command=no)
        b2.pack()
        
    def click_delete_function_silent(self):
        try:
            leksiko_sunarthseis.pop("{}".format(self.Name))
            self.bonoma.grid_remove()
            self.bview.grid_remove()
            self.bdelete.grid_remove()
            self.bdeletep.grid_remove()
        except:
            pass
    def click_delete_functionp(self):
        self.confirm=Tk()
        self.confirm.geometry('230x80+400+400')
        self.confirm.config(bg='cyan')
        self.confirm.title('Confirm')
        def yes():
            self.click_delete_function_silentp()
            self.confirm.destroy()
            
        def no():
            self.confirm.destroy()
        l1=Label(self.confirm,text='Are you sure you want to delete {}?'.format(self.NameGUI))
        l1.pack(anchor=CENTER)
        b1=Button(self.confirm,text='Yes',bg='yellow',command=yes)
        b1.pack()
        b2=Button(self.confirm,text='No',bg='yellow',command=no)
        b2.pack()

    def click_delete_function_silentp(self):
        try:
            leksiko_sunarthseis.pop("{}".format(self.Name))
            self.bonoma.grid_remove()
            self.bview.grid_remove()
            self.bdelete.grid_remove()
            self.bdeletep.grid_remove()
        except:
            pass
        f=open('resources/functions.txt','r',encoding='utf-8-sig')
        z=""
        
        for line in f:
            try:
                linE=line.strip()
                if linE[0]=="N":
                    if linE[4]==":":
                        fName=linE.replace("Name:","").strip()
                        if fName!=self.Name:
                            z=z+line
                            w=0
                        else:
                            w=1
                    else:
                        if w==0:
                            z=z+line
                elif linE[0]=="I":
                    if w==0:
                        z=z+line
                elif linE[0]=="V":
                    if w==0:
                        z=z+line
                elif linE[0]=="D":
                    if w==0:
                        z=z+line
                elif linE[0]=="C":
                    if w==0:
                        z=z+line
                elif linE[0]==">":
                    if w==0:
                        z=z+line

                else:
                    z=z+line
            except:
                pass




        f.close()
        
        f=open("resources/functions.txt","w",encoding="utf-8-sig")
        f.write(z)
        f.close()
        
###################################################################################################################################
    def click_info(self):
        self.windowInfo=Tk()
        self.windowInfo.title("{}".format(self.NameGUI))
        x=7*len(self.Info)
        self.windowInfo.geometry("{}x80+600+300". format(x))
        self.windowInfo.configure(bg="lime green")
        Label(self.windowInfo,text="{}".format(self.Info),bg="light yellow").grid(row=0,column=0,columnspan=2)
        Button(self.windowInfo,text="Close",bg="brown",command=self.close_Info).grid(row=1,column=1)
    def close_Info(self):
        self.windowInfo.destroy()
        
##################################################################################################################################

#THE CLASS PINAKAS
#######################################################################################################################################
class Pinakas:
    def __init__(self,name,array,rows,columns,GUIrow,ap):
        self.name=name
        self.array=array
        self.rows=rows
        self.columns=columns
        self.GUIrow=GUIrow
        if ap==0:    
            self.bview=Button(westFrame,text="{}".format(self.name),bg="yellow",command=self.click_view,cursor='target',width=12)
            self.bview.grid(column=0,row=GUIrow)
            self.bedit=Button(westFrame,text="Edit",bg="cyan",command=self.edit_click_edit,cursor='pencil')
            self.bedit.grid(column=1,row=GUIrow)
            self.bdelete=Button(westFrame,text="Delete",bg="purple",command=self.click_delete,cursor='X_cursor',bitmap="error",height=20)
            self.bdelete.grid(column=2,row=GUIrow)
        else:
            pass
        






        

#DELETE IN CLASS PINAKAS
############################################################################################################################################################################


    def click_delete(self):
        self.confirm=Tk()
        self.confirm.geometry('230x80+400+400')
        self.confirm.config(bg='cyan')
        self.confirm.title('Confirm')
        def yes():
            self.silent_delete()
            self.confirm.destroy()
            
        def no():
            self.confirm.destroy()
        l1=Label(self.confirm,text='Are you sure you want to delete Table?')
        l1.pack(anchor=CENTER)
        b1=Button(self.confirm,text='Yes',bg='yellow',command=yes)
        b1.pack()
        b2=Button(self.confirm,text='No',bg='yellow',command=no)
        b2.pack()
        



    def silent_delete(self):
        leksiko_main.pop("{}".format(self.name))
        self.bedit.grid_remove()
        self.bview.grid_remove()
        self.bdelete.grid_remove()

        

            


#EDIT IN CLASS PINAKAS
###########################################################################################################################################################################
    def edit_click_submit(self):
        global edited_name,lista1,lblOr1
        k=1
        try:
            for i in lista1:
                entered=i.get()

                if entered=="":
                    entered="0"
                    l=float(entered)
                else:
                    l=float(entered)
        except:
            k=0
        entered=""
        if k==1:
            lista2=[]
            for i in lista1:
                entered=i.get()
                if entered=="":
                    entered="0"
                    lista2.append(entered)
                else:
                    lista2.append(entered)
            new_final = matrix(new_rows,new_columns,lista2)
            leksiko_main["{}".format(edited_name)]=Pinakas(edited_name,new_final,self.rows,self.columns,self.GUIrow,0)
            self.silent_delete()
            self.window3.destroy()
            
        else:
            lblOr1.grid_remove()
            lblOr2=Label(self.window3,text="Unacceptable\nitem type",bg='brown').grid(row=new_rows+1,column=0,sticky=E)
            
            

    
    
    
    
   

    def edit_click_enter(self):
        global editedname,edited_name,lista1,leksiko_main,lblName1,lblOr1
        edited_name=editedname.get()
        y=0
        for i in leksiko_main:
            if edited_name==i :
                if self.name!=i:
                    y=1
        if y==0:   
            lista1=[]   
            rows=self.rows
            columns=self.columns
            rows=int(rows)
            columns=int(columns)
            y=rows*21+85
            x=columns*64+110
            self.window3 = Tk()
            self.window3.title("import chart")
            self.window3.geometry("{}x{}+100+200". format(x,y))
            self.window3.configure(background="lime green")
            for p in range(0,rows):
                for i in range(0,columns):
                    lista1.append(Entry(self.window3,width=10))
                    lista1[p*columns+i].grid(row=p+1,column=i+1)
                    lista1[p*columns+i].insert(0,"{}".format(round(1000*self.array[p,i])/1000))
            for j in range(0,columns):
                Label(self.window3,text="column {}". format(j),bg='lime green').grid(row=0,column=j+1,sticky=E)
            for j in range(0,rows):
                Label(self.window3,text="row {}". format(j),bg='lime green').grid(row=j+1,column=0,sticky=E)
            btn3=Button(self.window3, text="Submit", width=8,bg="orange", command=self.edit_click_submit) .grid(row=rows+1, column=columns, sticky=E)
            self.window2.destroy()
            btn4=Button(self.window3, text="Return", width=4,bg="blue",fg="violet", command=self.edit_click_edit) .grid(row=0, column=0, sticky=E)
            lblOr1=Label(self.window3,text="You must enter\nnumbers only",bg='lightyellow')
            lblOr1.grid(row=new_rows+1,column=0,sticky=E)
        else:
            lblName1.grid_remove()
            lblName2=Label(self.window2, text="Name exists",  bg="green").grid(row=2, column=1, sticky=E)
            
                    
            



    def edit_click_edit(self):
        global editedname,lblName1
        try:
            self.window3.destroy()
        except:
            pass 
        self.window2 = Tk()
        self.window2.title("import dimensions")
        self.window2.geometry("160x92+100+200")
        self.window2.configure(background="lime green")

        lblName1=Label(self.window2, text="     Name    ",  bg="green")
        lblName1.grid(row=2, column=1, sticky=E)

        global editedname
        editedname=Entry(self.window2,width=11)
        editedname.insert(0,"{}".format(self.name))
        editedname.grid(row=3,column=1)
        btn2=Button(self.window2, text="Enter", width=8,bg="orange", command=self.edit_click_enter) .grid(row=3, column=3, sticky=E)
        btn3=Button(self.window2, text="Cancel", width=8,bg="purple", command=self.window2.destroy) .grid(row=4, column=3, sticky=E)

################################################################################################################################################################################


#VIEW IN CLASS PINAKAS
################################################################################################################################################################################
    def click_view(self): 
        lista3=[]   
        rows=self.rows
        columns=self.columns
        rows=int(rows)
        columns=int(columns)
        y=rows*21+55
        x=columns*64+40
        window3 = Tk()
        window3.title("view chart {}".format(self.name))
        window3.geometry("{}x{}". format(x,y))
        window3.configure(background="lime green")
        for p in range(0,rows):
            for i in range(0,columns):
                Label(window3,width=8,text="{}".format(round(1000*self.array[p,i])/1000)).grid(row=p+1,column=i+1)
        for j in range(0,columns):
            Label(window3,text="column {}". format(j),bg='lime green').grid(row=0,column=j+1,sticky=E)
        for j in range(0,rows):
            Label(window3,text="row {}". format(j),bg='lime green').grid(row=j+1,column=0,sticky=E)
        def cancel():
            window3.destroy()
        buttonCancel=Button(window3,text='Close',bg='orange',command=cancel)
        buttonCancel.grid(row=p+2,column=i+1)
################################################################################################################################################################################       
         




#NEW TABLE
#################################################################################################################################################################################
def click_submit():
    global lista1,new_name,leksiko_main,new_rows,new_columns,lblOr1
    k=1
    try:
        for i in lista1:
            entered=i.get()
            if entered=="":
                entered="0"
                l=float(entered)
            else:
                l=float(entered)
    except:
        k=0
    entered=""
    if k==1:
        lista2=[]
        for i in lista1:
            entered=i.get()
            if entered=="":
                entered="0"
                lista2.append(entered)
            else:
                lista2.append(entered)
        new_final = matrix(new_rows,new_columns,lista2)
        s=3
        for i in leksiko_main:
            if s<leksiko_main[i].GUIrow:
                s=leksiko_main[i].GUIrow
        leksiko_main["{}".format(new_name)]=Pinakas(new_name,new_final,new_rows,new_columns,s+1,0)
        window3.destroy()
        
        if new_name=="PAPAS":
            listara=[]
            for i in range(100):
                v=Tk()
                v.title("PATERAS SAS")
                v.geometry("200x100+500+500")
                Label(v,text="PAPAS PANTOU RE\nAKOUTE? PAPOUS SAS",bg="blue").pack()
                
    else:
        lblOr1.grid_remove()
        lblOr2=Label(window3,text="Unacceptable\nitem type",bg='brown').grid(row=new_rows+1,column=0,sticky=E)
        
        
    
    
    
   


def click_enter():
    global window3,lista1,new_rows,new_columns,newname,new_name,leksiko_main,lblOr1,lblName1
    new_name=newname.get()
    y=0
    for i in leksiko_main:
        if new_name==i :
            y=1
    r=1
    try:
        new_rows=enter1.get()
        new_columns=enter2.get()
        new_rows=int(new_rows)
        new_columns=int(new_columns)
    except:
        r=0
    if r==1 and new_rows<=10 and new_columns<=10:
        if y==0:
            lista1=[]   
            y=new_rows*21+85
            x=new_columns*64+110
            window3 = Tk()
            window3.title("import chart")
            window3.geometry("{}x{}+100+200". format(x,y))
            window3.configure(background="lime green")
            for p in range(0,new_rows):
                for i in range(0,new_columns):
                    lista1.append(Entry(window3,width=10))
                    lista1[p*new_columns+i].grid(row=p+1,column=i+1)
            for j in range(0,new_columns):
                Label(window3,text="column {}". format(j),bg='lime green').grid(row=0,column=j+1,sticky=E)
            for j in range(0,new_rows):
                Label(window3,text="row {}". format(j),bg='lime green').grid(row=j+1,column=0,sticky=E)
            btn3=Button(window3, text="Submit", width=8,bg="orange", command=click_submit) .grid(row=new_rows+1, column=new_columns, sticky=E)
            window2.destroy()
            btn4=Button(window3, text="Return", width=4,bg="blue",fg="violet", command=click_new) .grid(row=0, column=0, sticky=E)
            lblOr1=Label(window3,text="You must enter\nnumbers only",bg='lightyellow')
            lblOr1.grid(row=new_rows+1,column=0,sticky=E)
        else:
            lblName1.grid_remove()
            lblName2=Label(window2, text="Name exists",  bg="brown").grid(row=2, column=1, sticky=E)
    else:
        Label(window2,text="Wrong\ndimensions",bg="brown").grid(row=4,column=1)
        
    



def click_new():
    global window2,window3,lblName1
    try:
        window3.destroy()
    except:
        pass  
    window2 = Tk()
    window2.title("import dimensions")
    window2.geometry("260x130+100+200")
    window2.configure(background="lime green")
    lblName1=Label(window2, text="     Name    ",  bg="green")
    lblName1.grid(row=0, column=1, sticky=E)
    Label(window2, text="        rows   ",  bg="green") .grid(row=2, column=0, sticky=E)
    Label(window2, text="  columns ",  bg="green") .grid(row=2, column=2, sticky=E)
    Label(window2, text="   ",  bg="lime green").grid(row=2, column=1, sticky=E)
    global newname
    newname=Entry(window2,width=10)
    newname.grid(row=1,column=1)
    global enter1
    enter1=Entry(window2, width=10)
    enter1.grid(row=3, column=0, sticky=E)
    label2=Label(window2, text="X         ",bg="lime green")
    label2.grid(row=3, column=1, sticky=E)
    global enter2
    enter2=Entry(window2, width=10)
    enter2.grid(row=3, column=2, sticky=E)
    btn2=Button(window2, text="Enter", width=8,bg="orange", command=click_enter) .grid(row=3, column=3, sticky=E)
    btn3=Button(window2, text="Cancel", width=8,bg="purple", command=window2.destroy) .grid(row=4, column=3, sticky=E)

####################################################################################################################################################
               #NEW FUNC
def enter_new_func():
    global windownewfunc,Entry1,Entry2,Entry4,Entry5,Entry6
    f=open('resources/functions.txt','a',encoding='utf-8-sig')
    f.write(str("\n"+("Name: {}".format(Entry1.get()))+"\n"+("NameGUI: {}".format(Entry2.get()))+"\n"+("Info: {}".format(Entry3.get()))+"\n"+("Variables: {}".format(Entry4.get()))+"\n"+("Def: {}".format(Entry5.get()))+"\n"+("Check: {}".format(Entry6.get()))+"\n>"))
    f.close
    listara=[]
    for i in leksiko_sunarthseis:
        listara.append(i)
    for i in listara:
        leksiko_sunarthseis[i].click_delete_function_silent()
    f=open('resources/functions.txt','a',encoding='utf-8-sig')
    f.close
    sunarthseis_creation()
    windownewfunc.destroy()
    

def guide():
    windowguide=Tk()
    windowguide.title("Help")
    windowguide.geometry("700x170+300+300")
    windowguide.configure(background="green")

    Label(windowguide,text="Name:  Το όνομα της συνάρτησης που χρησημοποιεί το πρόγραμμα",bg="lime green").grid(row=1,column=0,sticky=W)
    Label(windowguide,text="NameGUI: Το όνομα της συνάρτησης που εμφανίζεται",bg="lime green").grid(row=2,column=0,sticky=W)
    Label(windowguide,text="Info:  Πληροφορίες για τη συνάρτηση         ",bg="lime green").grid(row=3,column=0,sticky=W)
    Label(windowguide,text="Variables: Το πλήθως των πινάκων που εισάγονται  ",bg="lime green").grid(row=4,column=0,sticky=W)
    Label(windowguide,text="Def:   Ο τύπος της πράξης σε Python",bg="lime green").grid(row=5,column=0,sticky=W)
    Label(windowguide,text="Check:  H συνθήκη για να ορίζεται η πράξη σε Python (Aν δέν υπάρχει αναγκαία συνθήκη εισάγεται True)",bg="lime green").grid(row=6,column=0,sticky=W)
    Label(windowguide,text="(οι πίνακες να εισάγονται με τη μορφή #1# , #2# ... με βάση τη σειρά εισαγωγής και η βιβλιοθήκη Numpy αναφέρεται ως np)",bg="lime green").grid(row=7,column=0,sticky=W)
    







    
def click_new_func():
    global windownewfunc,Entry1,Entry2,Entry3,Entry4,Entry5,Entry6
    windownewfunc=Tk()
    windownewfunc.title("New Function")
    windownewfunc.geometry("360x200+100+200")
    windownewfunc.configure(background="green")
    Label(windownewfunc,text="Define your function",bg="lime green").grid(row=0,column=0,columnspan=2)
    Label(windownewfunc,text="Name:       ",bg="lime green").grid(row=1,column=0,sticky=W)
    Label(windownewfunc,text="NameGUI: ",bg="lime green").grid(row=2,column=0,sticky=W)
    Label(windownewfunc,text="Info:           ",bg="lime green").grid(row=3,column=0,sticky=W)
    Label(windownewfunc,text="Variables:  ",bg="lime green").grid(row=4,column=0,sticky=W)
    Label(windownewfunc,text="Def:            ",bg="lime green").grid(row=5,column=0,sticky=W)
    Label(windownewfunc,text="Check:       ",bg="lime green").grid(row=6,column=0,sticky=W)
    Entry1=Entry(windownewfunc,width=50)
    Entry1.grid(row=1,column=1)
    Entry2=Entry(windownewfunc,width=50)
    Entry2.grid(row=2,column=1)
    Entry3=Entry(windownewfunc,width=50)
    Entry3.grid(row=3,column=1)
    Entry4=Entry(windownewfunc,width=50)
    Entry4.grid(row=4,column=1)
    Entry5=Entry(windownewfunc,width=50)
    Entry5.grid(row=5,column=1)
    Entry6=Entry(windownewfunc,width=50)
    Entry6.grid(row=6,column=1)
    btnenternewfunc1=Button(windownewfunc,text="Enter",bg="brown",width=7,height=1,command=enter_new_func).grid(row=7,column=1,sticky=E)
    btnenternewfunc2=Button(windownewfunc,text="Cancel",bg="purple",width=6,height=1,command=windownewfunc.destroy).grid(row=7,column=0)
    btnenternewfunc3=Button(windownewfunc,bg="yellow",width=20,height=20,bitmap='question',command=guide).grid(row=7,column=1,sticky=W)
def click_default_funcs():
    listara=[]
    for i in leksiko_sunarthseis:
        listara.append(i)
    for i in listara:
        leksiko_sunarthseis[i].click_delete_function_silent()
    sunarthseis_creation(0)
    f=open('resources/functions.txt','w',encoding='utf-8-sig')
    f.close
    f=open('resources/functions.txt','a',encoding='utf-8-sig')
    k=open('resources/functionsdefault.txt','r',encoding='utf-8-sig')
    for line in k:
        f.write(line)
    f.close
    k.close
#######################################################################################################################################################
#COPY RESULTS





def click_enter2():
    global newname,apotelesma,leksiko_main,window2
    new_name=newname.get()
    y=0
    for i in leksiko_main:
        if new_name==i :
            y=1
    if y==1:
        Label(window2,text="Name exists",bg="Red").grid(row=5,column=0)
    else:
        s=0
        for i in leksiko_main:
            if s<leksiko_main[i].GUIrow:
                s=leksiko_main[i].GUIrow
        shape=str(apotelesma.shape)
        shape=shape.replace("(","")
        shape=shape.replace(")","")
        columns,rows=shape.split(",")
        
        leksiko_main["{}".format(new_name)]=Pinakas(new_name,apotelesma,rows,columns,s+1,0)
        window2.destroy()
        
        






    
    
def click_copy():
    global apotelesma,window2
    if apotelesma1==1:
        pass
    else:
        window2 = Tk()
        window2.title("import Name")
        window2.geometry("0x120+100+200")
        window2.configure(background="lime green")
        lblName1=Label(window2, text="               Name              ",  bg="green")
        lblName1.grid(row=0, column=0)
        global newname
        newname=Entry(window2,width=20)
        newname.grid(row=1,column=0)
        btn2=Button(window2, text="Enter", width=8,bg="orange", command=click_enter2) .grid(row=3, column=0)
        btn3=Button(window2, text="Cancel", width=8,bg="purple", command=window2.destroy) .grid(row=4, column=0)
    
    
    
    


def click_clear():
    global apotelesma
    results.delete('1.0', END)
    apotelesma1=1



def matrix(rows,columns,lista):
    rows=int(rows)
    columns=int(columns)
    a=np.zeros((rows,columns),dtype=np.float64)
    s=0
    for i in range(rows):
        a[i]=lista[s:s+columns]
        s+=columns
    return a
    
#MAIN ΠΡΟΓΡΑΜΜΑ
#######################################################################################################################################################

from tkinter import *                              #εισαγωγη της tkinter και αλλων βιβλιοθηκων                
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
import random
from scipy import linalg


global leksiko_main
global leksiko_sunarthseis
leksiko_main={}
global apotelesma,apotelesma1

global main,results
import numpy as np
apotelesma1=1
import time as time
start=time.time()

main=Tk()
main.geometry("800x400+300+100")
main.title("Gram")
westFrame=Frame(main)
westFrame.grid(column=0,row=1,sticky=NW)
eastFrame=Frame(main)
eastFrame.grid(column=2,row=1,sticky=NE)
centerFrame=Frame(main,height=380,width=330)
centerFrame.grid(column=1,row=1,sticky=N)
centerFrame.grid_propagate(False)
centerFrame1=Frame(centerFrame,height=300,width=330)
centerFrame1.grid(column=1,row=1,sticky=N)
centerFrame1.grid_propagate(False)
centerFrame2=Frame(centerFrame,height=26,width=330)
centerFrame2.grid(column=1,row=2,sticky=N)
centerFrame2.grid_propagate(False)
global resultscolor
resultscolor='light green'
results = Text(centerFrame1, font=("arial", "14"),bg="{}".format(resultscolor))
results.grid(row=0,column=0,columnspan=2)
results.grid_propagate(False)
global labelTables,labelResults,labelFunctions
def labels(size):
    global labelTables,labelResults,labelFunctions
    try:
        labelTables.grid_remove()
        labelFunctions.grid_remove()
        labelResults.grid_remove()
    except:
        pass
    labelTables=Label(main,text="Tables",width=round(size/(100/4)),bg="lime green")
    labelTables.grid(row=0,column=0)
    labelResults=Label(main,text="Results",width=round(size/(67/4)),bg="lime green")
    labelResults.grid(row=0,column=1)
    labelFunctions=Label(main,text="Functions",width=round(size/(100/4)),bg="lime green")
    labelFunctions.grid(row=0,column=2)
labels(800)

def change_color():                                   
    color_list3=[]
    for line in open('resources/light_colors.txt','r'):
        color_list3.append(line.strip())
        randcolor3=random.choice(color_list3)
    main.configure(bg='{}'.format(randcolor3))
    eastFrame.configure(bg='{}'.format(randcolor3))
    westFrame.configure(bg='{}'.format(randcolor3))
    centerFrame.configure(bg='{}'.format(randcolor3))
    

btnNew=Button(westFrame, text="New Table", width=8,bg="brown",cursor="plus", command=click_new).grid(row=100, column=0, sticky=NW)
btnCopy=Button(centerFrame2, text="Copy Table", width=15,bg="green",cursor="exchange", command=click_copy).grid(row=2, column=0,sticky=N)
btnClear=Button(centerFrame2, text="Clear", width=14,bg="light blue",cursor="X_cursor", command=click_clear).grid(row=2, column=1,sticky=N)
btnColor=Button(centerFrame2, text="Change Color", width=14,bg="yellow",command=change_color).grid(row=2, column=2,sticky=N,columnspan=2)

                                                                                                                 

menubar = Menu(main)
sunarthseis_creation()
zhtoumeno=0

zhtoumeno=0







##########################################################    -----ΜΕΝΟΥ------   #######################################################################################################





##############    ΧΡΩΜΑΤΑ ΚΑΙ RELIEF   ##################################################################################################################################


color_list1=[]
for line in open('resources/basic_colors.txt','r'):                       #λιστα με 11 βασικα χρωματα σε ξεχωριστο αρχειο basic_colors.txt για να προσθετει ο χρηστης δικα του
    color_list1.append(line.strip())
randcolor1=random.choice(color_list1)


                                               #λιστα με 17 χρωματα σε ξεχωριστο αρχειο light_colors.txt για να προσθετει ο χρηστης δικα του
color_list2=[]
for line in open('resources/light_colors.txt','r'):
    color_list2.append(line.strip())
randcolor2=random.choice(color_list2)


results.configure(bg='{}'.format(randcolor1))                  
main.configure(bg='{}'.format(randcolor2))
eastFrame.configure(bg='{}'.format(randcolor2))
westFrame.configure(bg='{}'.format(randcolor2))
centerFrame.configure(bg='{}'.format(randcolor2))

relief1=RAISED                                                     #ψευτο3D-effect των κουμπιων, RAISED και FLAT τα πιο συνηθισμενα
relief2=FLAT
relief3=SUNKEN
relief4=GROOVE
relief5=RIDGE

   

######################    1ο Μενου   #######################################################################################################################################

def Exit():
    confirm=Tk()
    confirm.geometry('230x80+400+400')
    confirm.config(bg='cyan')
    confirm.title('Confirm')
    def yes():
        confirm.destroy()
        main.destroy()
    def no():
        confirm.destroy()
    l1=Label(confirm,text='Are you sure you want to exit?')
    l1.pack(anchor=CENTER)
    b1=Button(confirm,text='Yes',bg='yellow',command=yes)
    b1.pack()
    b2=Button(confirm,text='No',bg='yellow',command=no)
    b2.pack()


filemenu = Menu(menubar, tearoff=0)


filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

menubar.add_cascade(label="File", menu=filemenu)




#####################     2ο Μενου     ####################################################################################################################################





editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Add your own function", command=click_new_func)

menubar.add_cascade(label="Edit", menu=editmenu)




        
#####################   3ο Μενου    ########################################################################################################################################
def Manual():
    manual=Tk()
    manual.geometry("350x100")
    manual.title("Tutorial")
    Entrym=Entry(manual,bg="yellow",width=150)
    Entrym.pack()
    Entrym.insert(END,"https://www.youtube.com/watch?v=ZaFkOlGct44")
    b=Button(manual,text='Close',bg='purple',command=manual.destroy).pack(anchor=SE)
def Info():
    #from tkinter import messagebox
    a=messagebox.showinfo('Software Information','Το παρον λογισμικο αφορα την\nεπιλυση προβληματων γραμμικης αλγεβρας')



def Credits():
    k=open('resources/credits.txt','r',encoding='utf-8-sig')
    creditsw=Tk()
    creditsw.title=("Credits")
    creditsw.geometry("1500x780+10+10")
    creditsw.configure(bg="light green")
    b=Button(creditsw,text='Close',bg='purple',command=creditsw.destroy).grid(row=40,column=0)
    x=0
    y=0
    for line in k:
        x=x+1
        Label(creditsw,text=line.strip(),bg="light green").grid(row=x,column=y,sticky=W)
        if x==40:
            y=y+1
    


    
helpmenu = Menu(menubar, tearoff=0)

helpmenu.add_command(label="Manual", command=Manual)
helpmenu.add_command(label="Info", command=Info)
helpmenu.add_command(label="Credits", command=Credits)


menubar.add_cascade(label="Help", menu=helpmenu)

#####################   4ο Μενου   #########################################################################################################################################

#συναρτησεις διαστασεων

def change1():
    main.geometry('1366x768+50+0')
    labels(1366)
def change2():
    main.geometry('1280x720+50+0')
    labels(1280)
def change3():
    main.geometry('1024x768+50+0')
    labels(1022)
def change4():
    dimensions_window=Tk()
    dimensions_window.title("display")
    dimensions_window.geometry("200x130+900+400")
    Label(dimensions_window, text="Import display dimensions").grid(column=0,row=0,columnspan=2)
    entry_dimensions=Entry(dimensions_window,width=10)
    entry_dimensions2=Entry(dimensions_window,width=10)
    entry_dimensions.grid(row=1,column=0)
    entry_dimensions2.grid(row=1,column=1)
    entry_dimensions.insert(0,"x")
    entry_dimensions2.insert(0,"y")
    def display():
        k=entry_dimensions.get()
        l=entry_dimensions2.get()
        u=0
        try:
            k=int(k)
            l=int(l)
            u=1
        except:
            u=0
        
        if u==1:
            if k<=7680 and k>=750 and l<=4320 and l>=300:
                main.geometry('{}x{}+100+100'.format(k,l))
                labels(int(k))
                dimensions_window.destroy()
        else:
            Label(dimensions_window, text="Wrong Dimensions\n750<x<1920\n300<y<1080").grid(column=1,row=2)
            
    btnEnterDimensionsWindow=Button(dimensions_window,text="Enter",bg="brown",command=display).grid(row=2,column=0)
    btnCancelDimensionsWindow=Button(dimensions_window,text="Cancel",bg="purple",command=dimensions_window.destroy).grid(row=3,column=0)


###################################################   
    
def WindowColours():
    #from tkinter import colorchooser
    col=colorchooser.askcolor(color="",title ="Colour Chooser")
    main.configure(bg=col[1])
    eastFrame.configure(bg=col[1])
    westFrame.configure(bg=col[1])
    centerFrame.configure(bg=col[1])

def ResultsColours():
    global resultscolor
    #from tkinter import colorchooser
    col=colorchooser.askcolor(color="",title ="Results Colour Chooser")
    try:
        results.configure(bg='{}'.format(col[1]))
    except:
        pass
    
    


def Display():
    var=IntVar()
    a=Tk()
    a.title('Window Size')
    a.geometry('300x160+900+200')
    
    c=Label(a,text='Suggested Window Sizes:')
    c.pack()
    
    R1 = Radiobutton(a, text="1366x768", variable=var, value=1,command=change1)
    R1.pack( anchor = W )
    
    R2 = Radiobutton(a, text="1280x720", variable=var, value=2,command=change2)
    R2.pack( anchor = W)

    R3 = Radiobutton(a, text="1024x768", variable=var, value=3,command=change3)
    R3.pack( anchor = W)

    R4 = Button(a, text="Customize",bg="green",command=change4)
    R4.pack( anchor = W)



    def exit_display():
        a.destroy()
    btnCancelDimensionsWindow=Button(a,text="Close",bg="purple",command=a.destroy).pack()


settingsmenu = Menu(menubar, tearoff=0)

settingsmenu.add_command(label="Window Colours", command=WindowColours)
settingsmenu.add_command(label="Results Colours", command=ResultsColours)
settingsmenu.add_command(label="Reset Functions", command=click_default_funcs)
settingsmenu.add_command(label="Display", command=Display)

menubar.add_cascade(label="Settings", menu=settingsmenu)


#####################   Τελος προγραμματος---Κλεισιμο main παραθυρου   ##################################################################################################

main.config(menu=menubar)
main.mainloop()




