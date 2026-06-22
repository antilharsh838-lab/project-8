from tkinter import *

  
class Dashboard:
    def __init__(self, root):    #constructor
         
        self.root = root
        self.root.title("student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")       
  
  

        
     #title                                                                                                                                       
        title=Label(self.root,text="Student Result Managment System",font=("goudy old style",20,"bold"),bg="white",fg="green").place(x=0,y=0,relwidth=1,height=50)



     #main frame
        main_frame=LabelFrame(self.root,text="menu",font=("times new roman",15,"bold"),bg="white")
        main_frame.place(x=10,y=70,width=1340,height=600)

       
        btn_course=Button(main_frame,text="Course",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=50,y=70,width=200,height=40)
        btn_student=Button(main_frame,text="Student",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=50,y=130,width=200,height=40)
        btn_result=Button(main_frame,text="Result",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=50,y=190,width=200,height=40)
        btn_view=Button(main_frame,text="View Student Result",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=50,y=250,width=200,height=40)
        btn_logout=Button(main_frame,text="Logout",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=50,y=310,width=200,height=40)
        btn_exit=Button(main_frame,text="Exit",font=("goudy old style",15,"bold"),bg="green",fg="white",cursor="hand2").place(x=50,y=370,width=200,height=40)

      #   #right side image
      #   self.bg_img=PhotoImage(file="images/bg.png")
      #   self.bg_label=Label(self.root,image=self.bg_img).place(x=700,y=200,width=500,height=300)




        #update details button
        self.btn_course=Label(self.root,text="total courses\n[0]",font=("goudy old style",20,"bold"),bg="#29ba94",fg="white").place(x=490,y=530,width=200,height=70)
        self.btn_student=Label(self.root,text="total students\n[0]",font=("goudy old style",20,"bold"),bg="#03dcf4",fg="white").place(x=750,y=530,width=200,height=70)
        self.btn_result=Label(self.root,text="total results\n[0]",font=("goudy old style",20,"bold"),bg="#0367f4",fg="white").place(x=1000,y=530,width=200,height=70)




        #footer
        footer=Label(self.root,text="SRMS-Student Result Management System | Developed By: harsh antil | Contact Us: xyz123@gmail.com",font=("goudy old style",10,"bold"),bg="green",fg="white").place(x=0,y=670,relwidth=1,height=30)





if __name__ == "__main__":     #main function
    root = Tk()                #creating object of Tk class   
    obj = Dashboard(root)      #passing root as an argument to Dashboard class
    root.mainloop()