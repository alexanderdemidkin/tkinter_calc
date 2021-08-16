from tkinter import Tk, W, E
from tkinter.ttk import Frame, Button, Entry, Style
import btn_act


class Example(Frame):
    
    def __init__(self,rt,mem):
        super().__init__()
        self.root = rt
        self.mem = mem
        self.initUI()
        

    def initUI(self):
        self.master.title("Калькулятор на Tkinter")
        ct = Entry(self)
        ct.insert(0,0)
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        def validate(new_value):   
            if new_value.isnumeric():
                value = new_value
            elif ord(new_value) == 42:
                value = new_value
            elif ord(new_value) == 43:
                value = new_value
            elif ord(new_value) == 45:
                value = new_value
            elif ord(new_value) == 47:
                value = new_value
            elif ord(new_value) == 61:
                value = new_value
            else:
                value = ""
            return value 

        vcmd = (self.root.register(validate), '%P') 
        entry = Entry(self,validate='key',validatecommand=vcmd)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        cls = Button(self, text="Clear",command=lambda:btn_act.click_clr_all(entry))
        cls.grid(row=1, column=0)
        bck = Button(self, text="Delete",command=lambda:btn_act.click_clr(entry))
        bck.grid(row=1, column=1)
        lbl = Button(self,text="In mem",command=lambda:btn_act.click_add_mem(entry,self.mem,ct))
        lbl.grid(row=1, column=2)
        clo = Button(self, text="Close", command=lambda:btn_act.click_close(self.root))
        clo.grid(row=1, column=3)

        cls = Button(self, text="Clr mem",command=lambda:btn_act.click_clear_mem(self.mem,ct))
        cls.grid(row=2, column=0)
        bck = Button(self, text="Mem +",command=lambda:btn_act.click_del_plus(self.mem,ct,entry))
        bck.grid(row=2, column=1)
        lbl = Button(self,text= "Mem -",command=lambda:btn_act.click_del_min(self.mem,ct,entry))
        lbl.grid(row=2, column=2)
        clo = Button(self, text="Del mem", command=lambda:btn_act.click_del_mem(self.mem,ct))
        clo.grid(row=2, column=3)


        sev = Button(self, text="7",command=lambda:btn_act.click_ins(entry,'7'))
        sev.grid(row=3, column=0)
        eig = Button(self, text="8",command=lambda:btn_act.click_ins(entry,'8'))
        eig.grid(row=3, column=1)
        nin = Button(self, text="9",command=lambda:btn_act.click_ins(entry,'9'))
        nin.grid(row=3, column=2)
        div = Button(self, text="/",command=lambda:btn_act.click_ins(entry,'/'))
        div.grid(row=3, column=3)

        fou = Button(self, text="4",command=lambda:btn_act.click_ins(entry,'4'))
        fou.grid(row=4, column=0)
        fiv = Button(self, text="5",command=lambda:btn_act.click_ins(entry,'5'))
        fiv.grid(row=4, column=1)
        six = Button(self, text="6",command=lambda:btn_act.click_ins(entry,'6'))
        six.grid(row=4, column=2)
        mul = Button(self, text="*",command=lambda:btn_act.click_ins(entry,'*'))
        mul.grid(row=4, column=3)

        one = Button(self, text="1",command=lambda:btn_act.click_ins(entry,'1'))
        one.grid(row=5, column=0)
        two = Button(self, text="2",command=lambda:btn_act.click_ins(entry,'2'))
        two.grid(row=5, column=1)
        thr = Button(self, text="3",command=lambda:btn_act.click_ins(entry,'3'))
        thr.grid(row=5, column=2)
        mns = Button(self, text="-",command=lambda:btn_act.click_ins(entry,'-'))
        mns.grid(row=5, column=3)

        zer = Button(self, text="0",command=lambda:btn_act.click_ins(entry,'0'))
        zer.grid(row=6, column=0)
        dot = Button(self, text=".",command=lambda:btn_act.click_ins(entry,'.'))
        dot.grid(row=6, column=1)
        equ = Button(self, text="=",command=lambda:btn_act.click_get(entry))
        equ.grid(row=6, column=2)
        pls = Button(self, text="+",command=lambda:btn_act.click_ins(entry,'+'))
        pls.grid(row=6, column=3)

        self.pack()

