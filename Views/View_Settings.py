import customtkinter
def Settings(self, parent):
    def switch_event():
        customtkinter.set_appearance_mode(switch_var.get())

    Width = 900
    Height = 600


    window = customtkinter.CTkToplevel(self)
    window.geometry(f'{Width}x{Height}')

    window_frame = customtkinter.CTkFrame(window,width=Width-40,height=Height-40,corner_radius=15)
    window_frame.grid(row=0,column=0,padx=20,pady=10)

    window_title = customtkinter.CTkLabel(window_frame,text="Settings",width=Width-40,height=10)
    window_title.grid(row=0,column=0,pady=10)



    window_content_frame = customtkinter.CTkFrame(window,width=Width-40,height=200,corner_radius=15)
    window_content_frame.grid(row=1,column=0,padx=20,sticky=customtkinter.W)

    window_content_frame.columnconfigure(0, weight=1)
    window_content_frame.columnconfigure(1, weight=3)

    global switch_var 
    switch_var = customtkinter.StringVar(value="dark")

    switch_1 = customtkinter.CTkSwitch(master=window_content_frame, text="Screen Mode",command=switch_event,variable=switch_var, onvalue="light", offvalue="dark")
    switch_1.grid(row=10,column=0,padx=20,pady=20,sticky=customtkinter.W)

    IP_Label = customtkinter.CTkLabel(window_content_frame,text='IP Address',width=100,height=10)
    IP_Label.grid(row=0,column=2,padx=20,pady=20,sticky=customtkinter.E)

    IP_Label = customtkinter.CTkLabel(window_content_frame,text='Port',width=100,height=10)
    IP_Label.grid(row=1,column=2,padx=20,pady=20,sticky=customtkinter.E)

    IP_Address = customtkinter.CTkEntry(master=window_content_frame,
                            placeholder_text="127.0.0.1",
                            width=120,
                            height=25,
                            border_width=2,
                            corner_radius=10)
    Port_Address = customtkinter.CTkEntry(master=window_content_frame,
                            placeholder_text="20777",
                            width=120,
                            height=25,
                            border_width=2,
                            corner_radius=10)
    
    IP_Address.grid(row=0,column=3,columnspan=2,padx=20,pady=20,sticky=customtkinter.E)
    Port_Address.grid(row=1,column=3,columnspan=2,padx=20,pady=20,sticky=customtkinter.E)
    
