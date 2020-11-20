from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

window = Tk()
window.title("Student Management System")
class Student():
	"""docstring for Student"""
	def __init__(self, window):
		self.window = window
		self.window.title("Student Management System")
		self.window.geometry("1350x700+0+0")
		mybg = "#C8F902"

		title=Label(self.window,text="Student Management System",font=('arial',40,'bold'),bg=mybg)
		title.pack(side=TOP,fill=X)
	#---------all variables-----------
		self.roll_var=StringVar()
		self.name_var=StringVar()
		self.name_var=StringVar()
		self.email_var=StringVar()
		self.gender_var=StringVar()
		self.gender_var=StringVar()
		self.gender_var=StringVar()
		self.contact_var=StringVar()
		self.dob_var=StringVar()

		self.search_by=StringVar()
		self.search_txt=StringVar()
		




	#-------manage_frame--------------
		Manage_Frame=Frame(self.window,bg=mybg)
		Manage_Frame.place(x=20,y=100,width=450,height=580)

		m_title=Label(Manage_Frame,text="Manage Students",font=('arial',30,'bold'),bg=mybg)
		m_title.grid(row=0,columnspan=2,pady=20)

		lbl_roll=Label(Manage_Frame,text="Roll No.",font=('arial',20),bg=mybg)
		lbl_roll.grid(row=1,column=0,padx=20,pady=10,sticky='w')

		txt_Roll=Entry(Manage_Frame,textvariable=self.roll_var, font=('arial',15))
		txt_Roll.grid(row=1,column=1,padx=20,pady=10,sticky='w')

		lbl_name=Label(Manage_Frame,text="Name",font=('arial',20),bg=mybg)
		lbl_name.grid(row=2,column=0,padx=20,pady=10,sticky='w')

		txt_Name=Entry(Manage_Frame,textvariable=self.name_var, font=('arial',15))
		txt_Name.grid(row=2,column=1,padx=20,pady=10,sticky='w')

		lbl_email=Label(Manage_Frame,text="Email ID",font=('arial',20),bg=mybg)
		lbl_email.grid(row=3,column=0,padx=20,pady=10,sticky='w')

		txt_Email=Entry(Manage_Frame,textvariable=self.email_var, font=('arial',15))
		txt_Email.grid(row=3,column=1,padx=20,pady=10,sticky='w')

		lbl_gender=Label(Manage_Frame,text="Gender",font=('arial',20),bg=mybg)
		lbl_gender.grid(row=4,column=0,padx=20,pady=10,sticky='w')

		combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var, font=('arial',14),state='readonly')
		combo_Gender['values']=('Male','Female','Other')
		combo_Gender.grid(row=4,column=1,padx=10,pady=10)

		lbl_contact=Label(Manage_Frame,text="Contact No.",font=('arial',20),bg=mybg)
		lbl_contact.grid(row=5,column=0,padx=20,pady=10,sticky='w')

		txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var, font=('arial',15))
		txt_Contact.grid(row=5,column=1,padx=20,pady=10,sticky='w')

		lbl_dob=Label(Manage_Frame,text="D.O.B",font=('arial',20),bg=mybg)
		lbl_dob.grid(row=6,column=0,padx=20,pady=10,sticky='w')

		txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var, font=('arial',15))
		txt_DOB.grid(row=6,column=1,padx=20,pady=10,sticky='w')

		lbl_address=Label(Manage_Frame,text="Address",font=('arial',20),bg=mybg)
		lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky='w')

		self.txt_Address=Text(Manage_Frame,width=25,height=5,font=15)
		self.txt_Address.grid(row=7,column=1,padx=20,pady=10,sticky='w')
		

		#------button----------
		btn_Frame=Frame(Manage_Frame,bg=mybg)
		btn_Frame.place(x=15,y=525,width=450)

		Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students)
		Addbtn.grid(row=0,column=0,padx=10,pady=10)


		Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data)
		Updatebtn.grid(row=0,column=1,padx=10,pady=10)

		Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data)
		Deletebtn.grid(row=0,column=2,padx=10,pady=10)

		Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear)
		Clearbtn.grid(row=0,column=3,padx=10,pady=10)


	#--------detail_frame-------------
		Detail_Frame=Frame(self.window,bg=mybg)
		Detail_Frame.place(x=500,y=100,width=800,height=580)

		lbl_search=Label(Detail_Frame,text="Search By",font=('arial',20),bg=mybg)
		lbl_search.grid(row=0,column=0,padx=20,pady=10,sticky='w')

		combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=('arial',16),state='readonly')
		combo_search['values']=('Roll','Name','Contact')
		combo_search.grid(row=0,column=1,padx=10,pady=10)

		txt_Search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=('arial',16))
		txt_Search.grid(row=0,column=2,padx=20,pady=10,sticky='w')

		searchbtn=Button(Detail_Frame,width=10,text="Search",command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
		shownbtn=Button(Detail_Frame,width=10,text="Show All",command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

		#---------table_frame-----------
		Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg=mybg)
		Table_Frame.place(x=10,y=70,width=760,height=500)

		scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
		self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)
		self.Student_table.heading("roll",text="Roll No.")
		self.Student_table.heading("name",text="Name")
		self.Student_table.heading("name",text="Name")
		self.Student_table.heading("email",text="Email")
		self.Student_table.heading("gender",text="Gender")
		self.Student_table.heading("contact",text="Contact")
		self.Student_table.heading("dob",text="D.O.B")
		self.Student_table.heading("address",text="Address")
		self.Student_table['show']='headings'
		self.Student_table.column("roll",width=100)
		self.Student_table.column("name",width=100)
		self.Student_table.column("email",width=100)
		self.Student_table.column("gender",width=100)
		self.Student_table.column("contact",width=100)
		self.Student_table.column("dob",width=100)
		self.Student_table.column("address",width=150)
		self.Student_table.pack(fill=BOTH,expand=1)
		self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()

	def add_students(self):
		if self.roll_var.get()=="" or self.name_var.get()=="":
			messagebox.showerror("Error","All fields are required")
		else:
			con=pymysql.connect(host="localhost",user="root",database="stm")
			cur=con.cursor()
			cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get("1.0",END)))
			con.commit()
			self.fetch_data()
			self.clear()
			con.close()
			messagebox.showinfo("Succes","Records have been inserted")


	def fetch_data(self):
		con=pymysql.connect(host="localhost",user="root",database="stm")
		cur=con.cursor()
		cur.execute("select * from students")
		rows=cur.fetchall()
		# print(rows)
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			index = 0;
			for row in rows:
				# print(type(row))
				# print(row[1])
				self.Student_table.insert("","end", values=row)    		                                                            
			con.commit()
		con.close()

	def clear(self):
		self.roll_var.set("")
		self.name_var.set("")
		self.email_var.set("")
		self.gender_var.set("")
		self.contact_var.set("")
		self.dob_var.set("")
		self.txt_Address.delete("1.0",END)

	def get_cursor(self,ev):
		cursor_row=self.Student_table.focus()
		contents=self.Student_table.item(cursor_row)
		row=contents['values']
		self.roll_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.contact_var.set(row[4])
		self.dob_var.set(row[5])
		self.txt_Address.delete("1.0",END)
		self.txt_Address.insert(END,row[6])

	def update_data(self):
		con=pymysql.connect(host="localhost",user="root",database="stm")
		cur=con.cursor()
		cur.execute("update students set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get("1.0",END),self.roll_var.get()))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
	def delete_data(self):
		con=pymysql.connect(host="localhost",user="root",database="stm")
		cur=con.cursor()
		cur.execute("delete from students where roll_no=%s" %self.roll_var.get())
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()

	def search_data(self):
		con=pymysql.connect(host="localhost",user="root",database="stm")
		cur=con.cursor()
		cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
		# cur.execute("select * from students where "+str(self.search_by.get())+"LIKE %"+str(self.search_txt.get())+"%")
		rows=cur.fetchall()
		# print(rows)
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			index = 0;
			for row in rows:
				# print(type(row))
				# print(row[1])
				self.Student_table.insert("","end", values=row)    		                                                            
			con.commit()
		con.close()

		


ob = Student(window)
window.mainloop()
