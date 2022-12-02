import customtkinter

def Race_Director(self, parent_frame):
    global activated

    self.frame_5 = customtkinter.CTkFrame(parent_frame,width=500)
    self.frame_5.grid(row=0,column=1,padx=20,pady=20,sticky='news')


    self.label = customtkinter.CTkLabel(self.frame_5,text='Race Director',width=800)
    self.label.grid(row=1, column=0,padx=10,pady=10)

    self.label2 = customtkinter.CTkLabel(self.frame_5,textvariable=activated,width=800)
    self.label2.grid(row=2, column=0,padx=10,pady=10)