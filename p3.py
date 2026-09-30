#L14 python -m pip install setuptools
#L14 python -m pip install pyrebase4


#gui

from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from pymongo import *

f = ("Cambria", 30, "bold")
 
def mw_to_ww():
    mw.withdraw()
    ww.deiconify()


def ww_to_mw():
    ww.withdraw()
    mw.deiconify()


def mw_to_vw():
    mw.withdraw()
    vw.deiconify()
    view()


def vw_to_mw():
    vw.withdraw()
    mw.deiconify()

def save():
       name = ww_ent_name.get()
       if name == "":
                showerror("name issue ", "please enter movie name")
                ww_ent_name.focus()
                return

       review = ww_st_review.get(0.0, END)
       if review.strip() == "":
                showerror("review issue", "please enter movie review")
                ww_st_review.focus()
                return

       con = None
       try:
              con = MongoClient("localhost", 27017)
              db = con["movie_review_3aug26"]
              coll = db["movie_review"]
              doc = {"name":name, "review":review}
              coll.insert_one(doc)
              print("thank u for the review")
              msg = "thank u for the review"
              showinfo("success", msg)
              ww_ent_name.delete(0, END)
              ww_st_review.delete(0.0, END)
              ww_ent_name.focus()
       except Exception as e:
              print("issue ", e)
       finally:
              if con != None:
                         con.close()

def view():
       vw_st_review.delete(0.0, END)
       con = None
       try:
              con = MongoClient("localhost", 27017)
              db = con["movie_review_3aug26"]
              coll = db["movie_review"]
              data = coll.find()
              info = ""
              for d in data:
                       info = info + "\nName = " + str(d["name"]) + "\nReview = " + str(d["review"]) + "\n"
              vw_st_review.insert(INSERT, info)
       except Exception as e:
              print("issue ", e)
       finally:
              if con != None:
                       con.close()

mw = Tk()
mw.title("Movie Review App")
mw.geometry("600x600+300+30")

mw_btn_write = Button(mw, text="Write Review", font=f, command=mw_to_ww)
mw_btn_view  = Button(mw, text="View Reviews", font=f, command=mw_to_vw)
mw_btn_write.pack(pady=10)
mw_btn_view.pack(pady=10)

ww = Toplevel()
ww.title("Write movie Review")
ww.geometry("600x600+300+30")
ww_lab_name = Label(ww, text = "Enter Movie Name", font=f)
ww_ent_name = Entry(ww, font=f)
ww_lab_review = Label(ww, text = "Enter Movie Review", font=f)
ww_st_review = ScrolledText(ww, font=f, width=20, height=3, wrap=WORD)
ww_btn_submit = Button(ww, text="Submit Review", font=f, command=save)
ww_btn_back = Button(ww, text="Back to main", font=f, command=ww_to_mw)

ww_lab_name.pack(pady=10)
ww_ent_name.pack(pady=10)
ww_lab_review.pack(pady=10)
ww_st_review.pack(pady=10)
ww_btn_submit.pack(pady=10)
ww_btn_back.pack(pady=10)

ww.withdraw()

vw = Toplevel()
vw.title("View Movie Reviews")
vw.geometry("600x600+300+30")
vw_st_review = ScrolledText(vw, font=f, width=20, height=10, wrap=WORD)
vw_btn_back = Button(vw, text = "Back to Main", font=f,command=vw_to_mw)

vw_st_review.pack(pady=10)
vw_btn_back.pack(pady=10)

vw.withdraw()

def on_closing():
      if askyesno("exit", "Do you want to close the program?"):
                mw.destroy()

mw.protocol("WM_DELETE_WINDOW", on_closing)
ww.protocol("WM_DELETE_WINDOW", on_closing)
vw.protocol("WM_DELETE_WINDOW", on_closing)

mw.mainloop()

              
              