import customtkinter as CTK
import tkinterDnD 
from tkinter import END
import pandas as pd
import tkinter as tk
import re


# Some standard themes for Custom tkinter
CTK.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
CTK.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(tkinterDnD.Tk):

    WIDTH = 500
    HEIGHT = 500

    def __init__(self):
        super().__init__()


        
        # ======== Create Main Meta ==========
        self.title( "Kounter" )
        self.geometry( f"{App.WIDTH}x{App.HEIGHT}" )
        self.protocol( "WM_DELETE_WINDOW", self.on_closing )
        # Will change when file is dropped on
        self.stringvar = tk.StringVar()
        # Will change when file is dropped on
        self.stringvar_count = tk.StringVar()
        self.stringvar_count.set('Total Count:')
        # ======== Create Main Layout Grid ==========
        self.grid_columnconfigure( 1, weight=1 ) 
        self.grid_rowconfigure( 0, weight=1 )
        # ====== VARS FOR APP ==============
        self.file_list = []
        self.total_counts_from_files = []
        self.my_entries = []
        self.sub_total_count = []
        self.record_count = 0
         # ========= LEFT FRAME =======
        self.frame_left = tk.Frame( master=self, relief="solid")
        self.frame_left.register_drop_target(tkinterDnD.FILE)
        self.frame_left.register_drag_source("*")
        self.frame_left.bind("<<Drop>>", self.drop)
        self.frame_left.grid(row=0, rowspan=5,column=0,columnspan=1, sticky="nswe")

        self.left_label = CTK.CTkLabel(master=self.frame_left,text_font=('Sans-serif',15),text="Drop files below to begin")
        self.left_label.grid( row=0, column=0, sticky="we")
        self.left_list_box = tk.Listbox(master=self.frame_left, bd=0, height=20)
        self.left_list_box.grid(row=1,column=0,columnspan=1, padx=5,sticky='nsew')
        self.exit_button = CTK.CTkButton(master=self.frame_left, text="Close", command=self.on_closing,text_color='#fff')
        self.exit_button.grid( row=3, column=0,columnspan=1, sticky="ew", pady=50,padx=5)

        # ========= RIGHT FRAME =======
        self.frame_right = CTK.CTkFrame( master=self )
        self.frame_right.grid( row=0, column=1, sticky="nswe", padx=10, pady=10 )
        self.frame_right_bottom = CTK.CTkLabel( master=self,textvariable=self.stringvar_count ,text_font=('Sans-serif',20))
        self.frame_right_bottom.grid( row=2, column=1, sticky='w', padx=5, pady=5 )


    #Close App
    def on_closing(self):
        self.destroy()



    #DROP EVENT FOR FILE LOADED
    def drop(self,event):
        # Reading rows
        file_path = re.sub("[{}]", "", event.data)
        counts = self.read_rows(file_path)
        self.display_counts(counts)
        self.total_counts(counts)
        file_name = file_path.split("/")[-1]
        self.file_list.append(file_name)
        self.left_list_box.insert(END,file_name)
 


    # read all rows from dropped on file
    def read_rows(self,data):

        # Reverse string to work around emplyee's name containing a .
        file_extension = data[::-1].split(".")

        # TXT files,string is in reverse
        if file_extension[0] == 'txt':
            result = []
            df = pd.read_csv(data, delimiter='\t', quotechar='"', quoting=0, dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False)
            rows_count = len(df)
            result.append(f"Sheet1: {rows_count}")
            return result
        # XLSX files,string is in reverse
        if file_extension[0] == 'xslx':
            full_df = pd.ExcelFile(data)
            result = []
            # Logic for multi sheets
            for sheet in full_df.sheet_names:
                df = pd.read_excel(full_df, sheet,header=0)
                rows_count = len(df)
                result.append(f"{sheet}: {rows_count}")
            return result
        # CSV files, string is in reverse
        if file_extension[0] == 'vsc':
            result = []
            df = pd.read_csv(data, delimiter=',', quotechar='"', quoting=0, dtype=str, skip_blank_lines=True, skiprows=0, keep_default_na=False,encoding='cp1252',header=None)
            rows_count = len(df)
            result.append(f"Sheet1: {rows_count}")
            return result
        else:
            print('File type not supported')

    # Counts function displayed bottom right
    def total_counts(self,counts):
        for num in counts:
            x = int(num.split(" ")[1])
            self.total_counts_from_files.append(x)
        total_counts = sum(self.total_counts_from_files)
        self.stringvar_count.set(f"Total Counts: {total_counts}")

    # display counts per file in right frame
    def display_counts(self,counts):
        self.sub_total_count.clear()
        for count in counts:
            self.record_count +=1
            x = int(count.split(" ")[1])
            self.sub_total_count.append(int(x))
            self.sub_total = tk.StringVar()
            self.sub_total.set(x)
            self.entry_string = tk.StringVar()
            self.entry_string.set(count)
            ent = CTK.CTkLabel(master=self.frame_right,textvariable=self.entry_string,width=20,text_font=('Sans-serif',13))
            ent.grid(row=self.record_count, column=0,columnspan=2, sticky="ew",padx=8)
        self.record_count +=1



if __name__ == "__main__":
    app = App()
    app.mainloop()

