import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import *
import PIL
from PIL import Image, ImageTk
from datetime import datetime
now = datetime.now()
formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        load = Image.open("foodbank.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
def logoutdb():
    Username.delete(0,END)
    password.delete(0,END)
def logintodb():
    user=int(Username.get())
    passw=int(password.get())
    db = mysql.connector.connect(host="localhost",user='dnya',password='dnya1234',db="Food_Bank")
    cursor = db.cursor()
    savequery = "select e_name from Employee where e_id='%d' and pwd='%d'" % (user,passw)
    cursor.execute(savequery)
    list_id_pd=cursor.fetchall()
    if not list_id_pd:
        messagebox.showerror("Error !","Invalid Employee Id or Password")
    else:
        messagebox.showinfo("login_alert","successfully logged in to ANNADATA!!")
        window = tk.Toplevel(root)
        window.geometry("1600x900")
        window.title("Employee Profile")
        def clswin():
            window.destroy()
        def opnwin():
            win2=tk.Toplevel(root)
            win2.geometry("1600x900")
            win2.title("Donation")

            lbnm = tk.Label(win2, text ="Mail")
            lbnm.place(x=500,y=300)

            usr = tk.Entry(win2,width=35)
            usr.place(x=700,y=300,width=100)



            def checkdr():
                dbb = mysql.connector.connect(host="localhost",user='dnya',password='dnya1234',db="Food_Bank")
                cursor2 = db.cursor()
                savequery="select donr_name from Donor where d_email='%s'" % (usr.get())
                cursor2.execute(savequery)
                list_id_pd=cursor.fetchall()

                if len(list_id_pd)==0:
                    messagebox.showinfo("New","New Donor")
                    win4=tk.Toplevel(root)
                    win4.geometry("1600x900")
                    win4.title("Add New Donor")

                    lbm1 = tk.Label(win4, text ="Donor Name")
                    lbm1.place(x=500,y=100)
                    mpbn1=tk.Entry(win4,width=35)
                    mpbn1.place(x=600,y=100,width=100)

                    lbm2 = tk.Label(win4, text ="Donor Mail")
                    lbm2.place(x=500,y=200)
                    mpbn2=tk.Entry(win4,width=35)
                    mpbn2.place(x=600,y=200,width=100)

                    lbm3 = tk.Label(win4, text ="Donor Phone")
                    lbm3.place(x=500,y=300)
                    mpbn3=tk.Entry(win4,width=35)
                    mpbn3.place(x=600,y=300,width=100)

                    lbm4 = tk.Label(win4, text ="Donor Address")
                    lbm4.place(x=500,y=400)
                    mpbn4=tk.Entry(win4,width=35)
                    mpbn4.place(x=600,y=400,width=100)

                    lbm5 = tk.Label(win4, text ="Donor Occupation")
                    lbm5.place(x=500,y=500)
                    mpbn5=tk.Entry(win4,width=35)
                    mpbn5.place(x=600,y=500,width=100)

                    lbm6 = tk.Label(win4, text ="Donor Age")
                    lbm6.place(x=500,y=600)
                    mpbn6=tk.Entry(win4,width=35)
                    mpbn6.place(x=600,y=600,width=100)

                    def savednrnw():
                        cursor3 = db.cursor()
                        savequery="insert into donor(donr_name,e_id,donr_age,d_phone,d_email,d_addr,donr_occu) values('%s','%d','%d','%s','%s','%s','%s')" % (mpbn1.get(),user,int(mpbn6.get()),mpbn3.get(),mpbn2.get(),mpbn4.get(),mpbn5.get())
                        cursor3.execute(savequery)
                        db.commit()

                        messagebox.showinfo("Updated","New Donor is added")
                        win4.destroy()
                        win6=tk.Toplevel(root)
                        win6.geometry("1600x1200")
                        win6.title("Donation Details")
                        lbm8 = tk.Label(win6, text ="Select the Food to be donated")
                        lbm8.place(x=500,y=800)
                        l = tk.Label(win6, bg='white', width=20, text='empty')
                        l.place(x=600,y=300)
                        #to store food with its qty
                        food_donated_dic=dict()


                        def print_selection():
                            if(var1.get()==1):
                                n1=m1.get()
                                l.config(text='Rice:')
                                food_donated_dic['Rice']=n1

                                #print(food_donated_dic)
                            if(var2.get()==1):
                                n2=m2.get()
                                l.config(text='Wheat')
                                food_donated_dic['Wheat']=n2

                            if(var3.get()==1):
                                n3=m3.get()
                                l.config(text='Jowar')
                                food_donated_dic['Wheat']=n3

                            if(var4.get()==1):
                                n4=m4.get()
                                l.config(text='Bajra')
                                food_donated_dic['Bajra']=n4


                            if(var5.get()==1):
                                n5=m5.get()
                                l.config(text='Maize')
                                food_donated_dic['Maize']=n5



                            if(var6.get()==1):
                                n6=m6.get()
                                l.config(text='Poha')
                                food_donated_dic['Poha']=n6

                            if(var7.get()==1):
                                n7=m7.get()
                                l.config(text='Ragi')
                                food_donated_dic['Ragi']=n7

                            if(var8.get()==1):
                                n8=m8.get()
                                l.config(text='Oats')
                                food_donated_dic['Oats']=n8

                            if(var9.get()==1):
                                n9=m9.get()
                                l.config(text='Daliya')
                                food_donated_dic['Daliya']=n9

                            if(var10.get()==1):
                                n10=m10.get()
                                l.config(text='Barley')
                                food_donated_dic['Barley']=n10

                            if(var11.get()==1):
                                n11=m11.get()
                                l.config(text='Chickpea')
                                food_donated_dic['Chickpea']=n11

                            if(var12.get()==1):
                                n12=m12.get()
                                l.config(text='Lentils')
                                food_donated_dic['Lentils']=n12

                            if(var13.get()==1):
                                n13=m13.get()
                                l.config(text='Moong Dal')
                                food_donated_dic['Moong Dal']=n13

                            if(var14.get()==1):
                                n14=m14.get()
                                l.config(text='Urad Dal')
                                food_donated_dic['Urad Dal']=n14

                            if(var15.get()==1):
                                n15=m15.get()
                                l.config(text='Red Lentil')
                                food_donated_dic['Red Lentil']=n15

                            if(var16.get()==1):
                                n16=m16.get()
                                l.config(text='Green Gram')
                                food_donated_dic['Green Gram']=n16

                            if(var17.get()==1):
                                n17=m17.get()
                                l.config(text='Black Gram')
                                food_donated_dic['Black Gram']=n17

                            if(var18.get()==1):
                                n18=m18.get()
                                l.config(text='Rajma')
                                food_donated_dic['Rajma']=n18


                        var1 = tk.IntVar()
                        var2 = tk.IntVar()
                        var3 = tk.IntVar()
                        var4 = tk.IntVar()
                        var5 = tk.IntVar()
                        var6 = tk.IntVar()
                        var7 = tk.IntVar()
                        var8 = tk.IntVar()
                        var9 = tk.IntVar()
                        var10 = tk.IntVar()
                        var11 = tk.IntVar()
                        var12= tk.IntVar()
                        var13 = tk.IntVar()
                        var14= tk.IntVar()
                        var15= tk.IntVar()
                        var16 = tk.IntVar()
                        var17= tk.IntVar()
                        var18 = tk.IntVar()



                        c1=tk.Checkbutton(win6,text='Rice',variable=var1,onvalue=1,offvalue=0,command=print_selection)
                        c1.place(x=400,y=400)
                        m1=tk.Entry(win6,width=30)
                        m1.place(x=470,y=400,width=40,height=15)


                        c2=tk.Checkbutton(win6,text='Wheat',variable=var2,onvalue=1,offvalue=0,command=print_selection)
                        c2.place(x=400,y=420)
                        m2=tk.Entry(win6,width=30)
                        m2.place(x=470,y=420,width=40,height=15)

                        c3=tk.Checkbutton(win6,text='Jowar',variable=var2,onvalue=1,offvalue=0,command=print_selection)
                        c3.place(x=400,y=440)
                        m3=tk.Entry(win6,width=30)
                        m3.place(x=470,y=440,width=40,height=15)


                        c4=tk.Checkbutton(win6,text='Bajra',variable=var4,onvalue=1,offvalue=0,command=print_selection)
                        c4.place(x=400,y=460)
                        m4=tk.Entry(win6,width=30)
                        m4.place(x=470,y=460,width=40,height=15)

                        c5=tk.Checkbutton(win6,text='Maize',variable=var5,onvalue=1,offvalue=0,command=print_selection)
                        c5.place(x=400,y=480)
                        m5=tk.Entry(win6,width=30)
                        m5.place(x=470,y=480,width=40,height=15)

                        c6=tk.Checkbutton(win6,text='Poha',variable=var6,onvalue=1,offvalue=0,command=print_selection)
                        c6.place(x=400,y=500)
                        m6=tk.Entry(win6,width=30)
                        m6.place(x=470,y=500,width=40,height=15)

                        c7=tk.Checkbutton(win6,text='Ragi',variable=var7,onvalue=1,offvalue=0,command=print_selection)
                        c7.place(x=400,y=520)
                        m7=tk.Entry(win6,width=30)
                        m7.place(x=470,y=520,width=40,height=15)

                        c8=tk.Checkbutton(win6,text='Oats',variable=var8,onvalue=1,offvalue=0,command=print_selection)
                        c8.place(x=400,y=540)
                        m8=tk.Entry(win6,width=30)
                        m8.place(x=470,y=540,width=40,height=15)

                        c9=tk.Checkbutton(win6,text='Daliya',variable=var9,onvalue=1,offvalue=0,command=print_selection)
                        c9.place(x=400,y=560)
                        m9=tk.Entry(win6,width=30)
                        m9.place(x=470,y=560,width=40,height=15)

                        c10=tk.Checkbutton(win6,text='Barley',variable=var10,onvalue=1,offvalue=0,command=print_selection)
                        c10.place(x=700,y=400)
                        m10=tk.Entry(win6,width=30)
                        m10.place(x=800,y=400,width=40,height=15)

                        c11=tk.Checkbutton(win6,text='Chickpea',variable=var11,onvalue=1,offvalue=0,command=print_selection)
                        c11.place(x=700,y=420)
                        m11=tk.Entry(win6,width=30)
                        m11.place(x=800,y=420,width=40,height=15)

                        c12=tk.Checkbutton(win6,text='Lentils',variable=var12,onvalue=1,offvalue=0,command=print_selection)
                        c12.place(x=700,y=440)
                        m12=tk.Entry(win6,width=30)
                        m12.place(x=800,y=440,width=40,height=15)

                        c13=tk.Checkbutton(win6,text='Moong Dal',variable=var13,onvalue=1,offvalue=0,command=print_selection)
                        c13.place(x=700,y=460)
                        m13=tk.Entry(win6,width=30)
                        m13.place(x=800,y=460,width=40,height=15)

                        c14=tk.Checkbutton(win6,text='Urad Dal',variable=var14,onvalue=1,offvalue=0,command=print_selection)
                        c14.place(x=700,y=480)
                        m14=tk.Entry(win6,width=30)
                        m14.place(x=800,y=480,width=40,height=15)

                        c15=tk.Checkbutton(win6,text='Red Lentil',variable=var15,onvalue=1,offvalue=0,command=print_selection)
                        c15.place(x=700,y=500)
                        m15=tk.Entry(win6,width=30)
                        m15.place(x=800,y=500,width=40,height=15)

                        c16=tk.Checkbutton(win6,text='Green Gram',variable=var16,onvalue=1,offvalue=0,command=print_selection)
                        c16.place(x=700,y=520)
                        m16=tk.Entry(win6,width=30)
                        m16.place(x=800,y=520,width=40,height=15)

                        c17=tk.Checkbutton(win6,text='Black Gram',variable=var17,onvalue=1,offvalue=0,command=print_selection)
                        c17.place(x=700,y=540)
                        m17=tk.Entry(win6,width=30)
                        m17.place(x=800,y=540,width=40,height=15)

                        c18=tk.Checkbutton(win6,text='Rajma',variable=var18,onvalue=1,offvalue=0,command=print_selection)
                        c18.place(x=700,y=560)
                        m18=tk.Entry(win6,width=30)
                        m18.place(x=800,y=560,width=40,height=15)


                        def savetodntn2():
                            cursor5 = db.cursor()
                            svqry="select max(donr_id) as maxd from donor"
                            cursor5.execute(svqry)
                            listd=cursor5.fetchall()
                            dnrid=listd[0][0]
                            for dntion in food_donated_dic:
                                formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                                savequery="insert into donation(food_item,food_qty,donation_date_time,donr_id) values('%s','%s','%s','%s')" % (dntion,food_donated_dic[dntion],formatted_date,dnrid)
                                cursor5.execute(savequery)
                                db.commit()
                            sveqry="update donation set food_id=(select food_id from food where food.food_item=donation.food_item)"
                            cursor5.execute(sveqry)
                            db.commit()
                            sq2="update food set total_qty=(select sum(food_qty) from donation where food.food_id=donation.food_id)"
                            cursor5.execute(sq2)
                            db.commit()
                            sq22="update food set total_qty=total_qty-(select sum(supplied_qty) from donation_supplied where food.food_id=donation_supplied.food_id)"
                            cursor5.execute(sq22)
                            db.commit()
                            messagebox.showinfo("Donated","Food has been donated")

                        end2=tk.Button(win6,text="Save Donation",command=savetodntn2)
                        end2.place(x=1000,y=500,width=150)




                    savebttn=tk.Button(win4,text="Save",bg='mistyrose3',command=savednrnw)
                    savebttn.place(x=700,y=700,width=100)

                else:
                    messagebox.showinfo("Exist","Donor already exist")
                    win7=tk.Toplevel(root)
                    win7.geometry("1600x1200")
                    win7.title("Donation Details")
                    lbm9 = tk.Label(win7, text ="Select the Food to be donated")
                    lbm9.place(x=500,y=800)
                    l = tk.Label(win7, bg='white', width=20, text='empty')
                    l.place(x=600,y=300)

                    food_donated_dic=dict()


                    def print_selectionn():
                        if(var11.get()==1):
                            nn1=m11.get()
                            l.config(text='Rice:')
                            food_donated_dic['Rice']=nn1

                                #print(food_donated_dic)
                        if(var22.get()==1):
                            nn2=m22.get()
                            l.config(text='Wheat')
                            food_donated_dic['Wheat']=nn2

                        if(var33.get()==1):
                            nn3=m33.get()
                            l.config(text='Jowar')
                            food_donated_dic['Wheat']=nn3

                        if(var44.get()==1):
                            nn4=m44.get()
                            l.config(text='Bajra')
                            food_donated_dic['Bajra']=nn4


                        if(var55.get()==1):
                            nn5=m55.get()
                            l.config(text='Maize')
                            food_donated_dic['Maize']=nn5



                        if(var66.get()==1):
                            nn6=m66.get()
                            l.config(text='Poha')
                            food_donated_dic['Poha']=nn6

                        if(var77.get()==1):
                            nn7=m77.get()
                            l.config(text='Ragi')
                            food_donated_dic['Ragi']=nn7

                        if(var88.get()==1):
                            nn8=m88.get()
                            l.config(text='Oats')
                            food_donated_dic['Oats']=nn8

                        if(var99.get()==1):
                            nn9=m99.get()
                            l.config(text='Daliya')
                            food_donated_dic['Daliya']=nn9

                        if(var101.get()==1):
                            nn10=m101.get()
                            l.config(text='Barley')
                            food_donated_dic['Barley']=nn10

                        if(var102.get()==1):
                            nn11=m102.get()
                            l.config(text='Chickpea')
                            food_donated_dic['Chickpea']=nn11

                        if(var103.get()==1):
                            nn12=m103.get()
                            l.config(text='Lentils')
                            food_donated_dic['Lentils']=nn12

                        if(var104.get()==1):
                            nn13=m104.get()
                            l.config(text='Moong Dal')
                            food_donated_dic['Moong Dal']=nn13

                        if(var105.get()==1):
                            nn14=m105.get()
                            l.config(text='Urad Dal')
                            food_donated_dic['Urad Dal']=nn14

                        if(var106.get()==1):
                            nn15=m106.get()
                            l.config(text='Red Lentil')
                            food_donated_dic['Red Lentil']=nn15

                        if(var107.get()==1):
                            nn16=m107.get()
                            l.config(text='Green Gram')
                            food_donated_dic['Green Gram']=nn16

                        if(var108.get()==1):
                            nn17=m108.get()
                            l.config(text='Black Gram')
                            food_donated_dic['Black Gram']=nn17

                        if(var109.get()==1):
                            nn18=m109.get()
                            l.config(text='Rajma')
                            food_donated_dic['Rajma']=nn18
                        print(food_donated_dic)
                    var11 = tk.IntVar()
                    var22 = tk.IntVar()
                    var33 = tk.IntVar()
                    var44 = tk.IntVar()
                    var55 = tk.IntVar()
                    var66 = tk.IntVar()
                    var77 = tk.IntVar()
                    var88 = tk.IntVar()
                    var99 = tk.IntVar()
                    var101 = tk.IntVar()
                    var102 = tk.IntVar()
                    var103= tk.IntVar()
                    var104 = tk.IntVar()
                    var105 = tk.IntVar()
                    var106= tk.IntVar()
                    var107 = tk.IntVar()
                    var108 = tk.IntVar()
                    var109 = tk.IntVar()




                    c11=tk.Checkbutton(win7,text='Rice',variable=var11,onvalue=1,offvalue=0,command=print_selectionn)
                    c11.place(x=400,y=400)
                    m11=tk.Entry(win7,width=30)
                    m11.place(x=470,y=400,width=40,height=15)

                    c22=tk.Checkbutton(win7,text='Wheat',variable=var22,onvalue=1,offvalue=0,command=print_selectionn)
                    c22.place(x=400,y=420)
                    m22=tk.Entry(win7,width=30)
                    m22.place(x=470,y=420,width=40,height=15)

                    c33=tk.Checkbutton(win7,text='Jowar',variable=var33,onvalue=1,offvalue=0,command=print_selectionn)
                    c33.place(x=400,y=440)
                    m33=tk.Entry(win7,width=30)
                    m33.place(x=470,y=440,width=40,height=15)

                    c44=tk.Checkbutton(win7,text='Bajra',variable=var44,onvalue=1,offvalue=0,command=print_selectionn)
                    c44.place(x=400,y=460)
                    m44=tk.Entry(win7,width=30)
                    m44.place(x=470,y=460,width=40,height=15)

                    c55=tk.Checkbutton(win7,text='Maize',variable=var55,onvalue=1,offvalue=0,command=print_selectionn)
                    c55.place(x=400,y=480)
                    m55=tk.Entry(win7,width=30)
                    m55.place(x=470,y=480,width=40,height=15)

                    c66=tk.Checkbutton(win7,text='Poha',variable=var66,onvalue=1,offvalue=0,command=print_selectionn)
                    c66.place(x=400,y=500)
                    m66=tk.Entry(win7,width=30)
                    m66.place(x=470,y=500,width=40,height=15)

                    c77=tk.Checkbutton(win7,text='Ragi',variable=var77,onvalue=1,offvalue=0,command=print_selectionn)
                    c77.place(x=400,y=520)
                    m77=tk.Entry(win7,width=30)
                    m77.place(x=470,y=520,width=40,height=15)

                    c88=tk.Checkbutton(win7,text='Oats',variable=var88,onvalue=1,offvalue=0,command=print_selectionn)
                    c88.place(x=400,y=540)
                    m88=tk.Entry(win7,width=30)
                    m88.place(x=470,y=540,width=40,height=15)

                    c99=tk.Checkbutton(win7,text='Daliya',variable=var99,onvalue=1,offvalue=0,command=print_selectionn)
                    c99.place(x=400,y=560)
                    m99=tk.Entry(win7,width=30)
                    m99.place(x=470,y=560,width=40,height=15)

                    c101=tk.Checkbutton(win7,text='Barley',variable=var101,onvalue=1,offvalue=0,command=print_selectionn)
                    c101.place(x=700,y=400)
                    m101=tk.Entry(win7,width=30)
                    m101.place(x=800,y=400,width=40,height=15)

                    c102=tk.Checkbutton(win7,text='Chickpea',variable=var102,onvalue=1,offvalue=0,command=print_selectionn)
                    c102.place(x=700,y=420)
                    m102=tk.Entry(win7,width=30)
                    m102.place(x=800,y=420,width=40,height=15)

                    c103=tk.Checkbutton(win7,text='Lentils',variable=var103,onvalue=1,offvalue=0,command=print_selectionn)
                    c103.place(x=700,y=440)
                    m103=tk.Entry(win7,width=30)
                    m103.place(x=800,y=440,width=40,height=15)

                    c104=tk.Checkbutton(win7,text='Moong Dal',variable=var104,onvalue=1,offvalue=0,command=print_selectionn)
                    c104.place(x=700,y=460)
                    m104=tk.Entry(win7,width=30)
                    m104.place(x=800,y=460,width=40,height=15)

                    c105=tk.Checkbutton(win7,text='Urad Dal',variable=var105,onvalue=1,offvalue=0,command=print_selectionn)
                    c105.place(x=700,y=480)
                    m105=tk.Entry(win7,width=30)
                    m105.place(x=800,y=480,width=40,height=15)

                    c106=tk.Checkbutton(win7,text='Red Lentil',variable=var106,onvalue=1,offvalue=0,command=print_selectionn)
                    c106.place(x=700,y=500)
                    m106=tk.Entry(win7,width=30)
                    m106.place(x=800,y=500,width=40,height=15)

                    c107=tk.Checkbutton(win7,text='Green Gram',variable=var107,onvalue=1,offvalue=0,command=print_selectionn)
                    c107.place(x=700,y=520)
                    m107=tk.Entry(win7,width=30)
                    m107.place(x=800,y=520,width=40,height=15)

                    c108=tk.Checkbutton(win7,text='Black Gram',variable=var108,onvalue=1,offvalue=0,command=print_selectionn)
                    c108.place(x=700,y=540)
                    m108=tk.Entry(win7,width=30)
                    m108.place(x=800,y=540,width=40,height=15)

                    c109=tk.Checkbutton(win7,text='Rajma',variable=var109,onvalue=1,offvalue=0,command=print_selectionn)
                    c109.place(x=700,y=560)
                    m109=tk.Entry(win7,width=30)
                    m109.place(x=800,y=560,width=40,height=15)

                    def savetodntn1():
                        cursor6 = db.cursor()
                        id=list_id_pd[0][0]
                        ssveqry1="select donr_id from donor where donr_name='%s'" % (id)
                        cursor6.execute(ssveqry1)
                        list_dnr_id=cursor6.fetchall()
                        donor_id=list_dnr_id[0][0]
                        for dntion in food_donated_dic:
                            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
                            savequery1="insert into donation(food_item,food_qty,donation_date_time,donr_id) values('%s','%s','%s','%s')" % (dntion,food_donated_dic[dntion],formatted_date,donor_id)
                            cursor6.execute(savequery1)
                            db.commit()
                            sveqry1="update donation set food_id=(select food_id from food where food.food_item=donation.food_item)"
                            cursor6.execute(sveqry1)
                            db.commit()
                            sq1="update food set total_qty=(select sum(food_qty) from donation where food.food_id=donation.food_id)"
                            cursor6.execute(sq1)
                            db.commit()
                            sq11="update food set total_qty=total_qty-(select sum(supplied_qty) from donation_supplied where food.food_id=donation_supplied.food_id)"
                            cursor6.execute(sq11)
                            db.commit()
                        messagebox.showinfo("Donated","Food has been donated")

                    end1=tk.Button(win7,text="Save Donation",command=savetodntn1)
                    end1.place(x=1000,y=500,width=150)




#riya@gmail.com 12345 1  a 2

            dtn=tk.Button(win2,text="Check Donor",bg='mistyrose3',command=checkdr)
            dtn.place(x =500, y=500, width = 100,height=60)
            def bcking():
                win2.destroy()

            btn=tk.Button(win2,text="Back",bg='mistyrose3',command=bcking)
            btn.place(x =700, y =500, width = 100,height=60)

        def upwin():
            win3=tk.Toplevel(root)
            win3.geometry("1600x900")
            win3.title("Donor details")
            nameety=tk.Entry(win3,width=10)
            nameety.place(x=600,y=200,width=100)
            phnety=tk.Entry(win3,width=10)
            phnety.place(x=600,y=300,width=100)
            mailety=tk.Entry(win3,width=10)
            mailety.place(x=600,y=400,width=100)
            addety=tk.Entry(win3,width=10)
            addety.place(x=600,y=500,width=100)

            lblfrstrow = tk.Label(win3, text ="Name")
            lblfrstrow.place(x=500,y=200)
            lbsrw = tk.Label(win3, text ="Mobile Number")
            lbsrw.place(x=500,y=300)
            lbtrw = tk.Label(win3, text ="Email")
            lbtrw.place(x=500,y=400)
            lbfrw = tk.Label(win3, text ="Address")
            lbfrw.place(x=500,y=500)
            cursor=db.cursor()
            # store updated values in database
            def saving():
                nwname=nameety.get()
                if nwname:
                    upqury="update Employee set e_name='%s' where pwd='%d'" % (nwname,passw)
                    cursor.execute(upqury)

                nwphn=phnety.get()
                if nwphn:
                    upqury="update Employee set phone='%s' where pwd='%d'" % (nwphn,passw)
                    cursor.execute(upqury)

                nwm=mailety.get()
                if nwm:
                    upqury="update Employee set email='%s' where pwd='%d'" % (nwm,passw)
                    cursor.execute(upqury)

                nadd=addety.get()
                if nadd:
                    upqury="update Employee set addr='%s' where pwd='%d'" % (nadd,passw)
                    cursor.execute(upqury)



                db.commit()
                messagebox.showinfo("Updated","Profile is updated")
                win3.destroy()


            savebtn=tk.Button(win3,text="Save & Update",bg='mistyrose3',command=saving)
            savebtn.place(x=600,y=700)


        lblfrstrow = tk.Label(window, text ="Employee Id")
        lblfrstrow.place(x=400,y=200)
        lbsrw = tk.Label(window, text ="Name")
        lbsrw.place(x=400,y=250)
        lbtrw = tk.Label(window, text ="Mobile Number")
        lbtrw.place(x=400,y=300)
        lbfrw = tk.Label(window, text ="Email")
        lbfrw.place(x=400,y=350)
        lbffrw = tk.Label(window, text ="Address" )
        lbffrw.place(x=400,y=400)
            #name = tk.Entry(window, width = 35)
            #name.place(x = 750, y = 330, width = 100)
            # get emp details
        equery = "select e_id,e_name,phone,email,addr from Employee where e_id='%d' and pwd='%d'" % (user,passw)
        cursor.execute(equery)
        list_id_pd=cursor.fetchall()
        frstrow = tk.Label(window, text =list_id_pd[0][0] )
        frstrow.place(x=500,y=200)
        srow = tk.Label(window, text =list_id_pd[0][1] )
        srow.place(x=500,y=250)
        trow = tk.Label(window, text =list_id_pd[0][2] )
        trow.place(x=500,y=300)
        frow = tk.Label(window, text =list_id_pd[0][3] )
        frow.place(x=500,y=350)
        ffrow = tk.Label(window, text =list_id_pd[0][4] )
        ffrow.place(x=500,y=400)

        def ngodetail():
            # display tables on canvas
            my_w = tk.Tk()
            my_w.geometry("1200x300")
            cursor=db.cursor()
            cursor.execute("select ngo_id,ngo_name,ngo_phone,ngo_email,ngo_addr,vol_name,v_phone from ngo inner join volunteer on ngo.volun_id=volunteer.volun_id;")

            e=Entry(my_w,width=30)
            e.grid(row=0,column=0)
            e.insert(END,'ngo_id')
            e.config(state=DISABLED)

            e=Entry(my_w,width=30)
            e.grid(row=0,column=1)
            e.insert(END,'ngo_name')
            e.config(state=DISABLED)

            e=Entry(my_w,width=30)
            e.grid(row=0,column=2)
            e.insert(END,'ngo_phone')
            e.config(state=DISABLED)

            e=Entry(my_w,width=30)
            e.grid(row=0,column=3)
            e.insert(END,'ngo_email')
            e.config(state=DISABLED)

            e=Entry(my_w,width=30)
            e.grid(row=0,column=4)
            e.insert(END,'ngo_addr')
            e.config(state=DISABLED)

            e=Entry(my_w,width=30)
            e.grid(row=0,column=5)
            e.insert(END,'vol_name')
            e.config(state=DISABLED)

            e=Entry(my_w,width=30)
            e.grid(row=0,column=6)
            e.insert(END,'v_phone')
            e.config(state=DISABLED)


            i=1
            for ngo in cursor:
                for j in range(7):
                    e=Entry(my_w,width=30)
                    e.grid(row=i,column=j)
                    e.insert(END,ngo[j])
                    e.config(state=DISABLED)
                i=i+1

            #my_w.mainloop()


        btnn=tk.Button(window,text="Ngo Details",bg='mistyrose3',command=ngodetail)
        btnn.place(x =1200, y =400, width = 100,height=60)
        def dontdet():
            # display tables on canvas
            myw = tk.Tk()
            myw.geometry("1200x900")
            cursor=db.cursor()
            cursor.execute("select * from donation")
            e=Entry(myw,width=30)
            e.grid(row=0,column=0)
            e.insert(END,'donation_id')
            e.config(state=DISABLED)

            e=Entry(myw,width=30)
            e.grid(row=0,column=1)
            e.insert(END,'donr_id')
            e.config(state=DISABLED)

            e=Entry(myw,width=30)
            e.grid(row=0,column=2)
            e.insert(END,'donation_date_time')
            e.config(state=DISABLED)

            e=Entry(myw,width=30)
            e.grid(row=0,column=3)
            e.insert(END,'food_id')
            e.config(state=DISABLED)

            e=Entry(myw,width=30)
            e.grid(row=0,column=4)
            e.insert(END,'food_item')
            e.config(state=DISABLED)

            e=Entry(myw,width=30)
            e.grid(row=0,column=5)
            e.insert(END,'food_qty')
            e.config(state=DISABLED)

            i=1
            for dnt in cursor:
                for j in range(6):
                    e=Entry(myw,width=30)
                    e.grid(row=i,column=j)
                    e.insert(END,dnt[j])
                    e.config(state=DISABLED)
                i=i+1

        bttn=tk.Button(window,text="Donation Details",bg='mistyrose3',command=dontdet)
        bttn.place(x =1200, y =250, width = 100,height=60)

        def fooddet():
            # display tables on canvas
            mw = tk.Tk()
            mw.geometry("1200x600")
            cursor=db.cursor()
            cursor.execute("select * from food")
            e=Entry(mw,width=30)
            e.grid(row=0,column=0)
            e.insert(END,'food_id')
            e.config(state=DISABLED)

            e=Entry(mw,width=30)
            e.grid(row=0,column=1)
            e.insert(END,'food_item')
            e.config(state=DISABLED)

            e=Entry(mw,width=30)
            e.grid(row=0,column=2)
            e.insert(END,'total_qty')
            e.config(state=DISABLED)
            i=1
            for fd in cursor:
                for j in range(3):
                    e=Entry(mw,width=30)
                    e.grid(row=i,column=j)
                    e.insert(END,fd[j])
                    e.config(state=DISABLED)
                i=i+1

        bttnn=tk.Button(window,text="Food Catlog",bg='mistyrose3',command=fooddet)
        bttnn.place(x =1200, y =550, width = 100,height=60)

        dbtn=tk.Button(window, text ="Donate",
                              bg ='mistyrose3', command=opnwin)
        dbtn.place(x =300, y =500, width = 100,height=60)
        upbtn = tk.Button(window, text ="Update",
                              bg ='mistyrose3',command=upwin)
        upbtn.place(x = 500, y =500, width = 100,height=60)
        logoutbtn = tk.Button(window, text ="Logout",
                              bg ='mistyrose3', command =clswin)
        logoutbtn.place(x = 700, y =500, width = 100,height=60)
        #lblsecrow = tk.Label(window, text ="Name")
        #lblsecrow.place(x=600,y=370)

root=Tk()
app = Window(root)
root.geometry("1600x900")
root.wm_title("ANNADATA")
root.title("Login Page")

# Definging the first row
text=Label(root,text="Kick out the hunger!",relief="solid",font="Times 32",background="Springgreen4",width=80,height=1,anchor=S)
text.pack()
lblfrstrow = tk.Label(root, text ="Employee Id", )
lblfrstrow.place(x=680,y=330)

Username = tk.Entry(root, width = 35)
Username.place(x = 750, y = 330, width = 100)

lblsecrow = tk.Label(root, text ="Password -")
lblsecrow.place(x = 680, y = 370)

password = tk.Entry(root, width = 35,show="*")
password.place(x = 750, y = 370, width = 100)

submitbtn = tk.Button(root, text ="Login",
                      bg ='whitesmoke', command = logintodb)
submitbtn.place(x = 600, y =450,width = 100,height=60)
cancelbtn = tk.Button(root, text ="Cancel",
                      bg ='whitesmoke', command = logoutdb)
cancelbtn.place(x = 800, y =450,width = 100,height=60)

root.mainloop()
