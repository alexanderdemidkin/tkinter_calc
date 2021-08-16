
def click_ins(elem,text):
   elem.insert("end",text)

def click_clr(elem):
    elem.delete(len(elem.get())-1)

def click_clr_all(elem):
    elem.delete(0, "end") 

def click_close(elem):
    elem.destroy()

def click_get(elem):
    st = elem.get()
    it = eval(st)
    elem.delete(0, "end") 
    elem.insert("end",it)

def click_add_mem(elem, mem,ct):
    st = elem.get()
    mem.append(st)
    i = len(mem)
    ct.delete(0, "end") 
    ct.insert("end",i)

def click_clear_mem(mem,ct):
    mem.clear()
    i = len(mem)
    ct.delete(0, "end") 
    ct.insert("end",i)

def click_del_mem(mem,ct):
    i = int(ct.get()) - 1
    mem.pop(i)
    i = len(mem)
    ct.delete(0, "end") 
    ct.insert("end",i)

def click_del_min(mem,ct,elem):
    i = int(ct.get())
    if i > 1 and i <= len(mem):
        i -= 1
        ct.delete(0, "end") 
        ct.insert("end",i)
        elem.delete(0, "end") 
        elem.insert("end",mem[i-1])
    else:
        elem.delete(0, "end") 
        elem.insert("end",mem[i-1])

def click_del_plus(mem,ct,elem):
    i = int(ct.get()) 
    if i >= 0 and i < len(mem) :
        i += 1
        ct.delete(0, "end") 
        ct.insert("end",i)

        elem.delete(0, "end") 
        elem.insert("end",mem[i - 1])
    else:
        elem.delete(0, "end") 
        elem.insert("end",mem[i - 1])

