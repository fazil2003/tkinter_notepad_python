from tkinter import *
from tkinter import filedialog
###photoimage
from tkinter.ttk import *

class text_editor:
    
    current_open_file="no file"
    def open_file(self):
        open_return=filedialog.askopenfile(initialdir="/",title="select file to open",filetypes=(("text files","*.txt"),("rich text file","*.rtf"),("all files","*.*")))
        if(open_return!=None):
            self.text_area.delete(1.0,END)
            for line in open_return:
                self.text_area.insert(END,line)
        self.current_open_file=open_return.name
        open_return.close()

        self.master.title(self.current_open_file+" - Notepad in Python")
        
    def save_as_file(self):
        f=filedialog.asksaveasfile(mode="w",defaultextension=".rtf")
        if f is None:
            return
        text2save=self.text_area.get(1.0,END)
        self.current_open_file=f.name
        f.write(text2save)
        f.close()

    def save_file(self):
        if self.current_open_file=="no file":
            self.save_as_file()
        else:
            f=open(self.current_open_file,"w+")
            f.write(self.text_area.get(1.0,END))
            f.close()

    def new_file(self):
        self.text_area.delete(1.0,END)
        self.current_open_file="no file"

    def normal_text(self):
        self.text_area.tag_add("normal","sel.first","sel.last")
    def bold_text(self):
        self.text_area.tag_add("bold","sel.first","sel.last")
    def italic_text(self):
        self.text_area.tag_add("italic","sel.first","sel.last")
    def underline_text(self):
        self.text_area.tag_add("underline","sel.first","sel.last")
        
    def copy_text(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.text_area.selection_get())
        

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")
        
        
    def paste_text(self):
        self.text_area.insert(INSERT,self.text_area.clipboard_get())
        #pyperclip.paste()

    def font_fn(self):
        self.text_area.config(foreground='green',font='Helvetica 18 bold italic underline')

    def font_fn_arial(self,font):
        self.font=font
        if(font=='Arial'):
            self.text_area.tag_add("font_arial","sel.first","sel.last")
        if(font=='Verdana'):
            self.text_area.tag_add("font_verdana","sel.first","sel.last")
        if(font=='Courier'):
            self.text_area.tag_add("font_courier","sel.first","sel.last")
        if(font=='Times'):
            self.text_area.tag_add("font_times","sel.first","sel.last")
        if(font=='Georgia'):
            self.text_area.tag_add("font_georgia","sel.first","sel.last")
        if(font=='Tahoma'):
            self.text_area.tag_add("font_tahoma","sel.first","sel.last")
        if(font=='Jokerman'):
            self.text_area.tag_add("font_jokerman","sel.first","sel.last")
        if(font=='Impact'):
            self.text_area.tag_add("font_impact","sel.first","sel.last")
        
    def font_fn_color(self,font):
        #self.text_area.config(foreground=font)
        if(font=='red'):
            self.text_area.tag_add("color_red","sel.first","sel.last")
        if(font=='blue'):
            self.text_area.tag_add("color_blue","sel.first","sel.last")
        if(font=='green'):
            self.text_area.tag_add("color_green","sel.first","sel.last")
        if(font=='yellow'):
            self.text_area.tag_add("color_yellow","sel.first","sel.last")
        if(font=='lightblue'):
            self.text_area.tag_add("color_lightblue","sel.first","sel.last")
        if(font=='lightgreen'):
            self.text_area.tag_add("color_lightgreen","sel.first","sel.last")
        if(font=='orange'):
            self.text_area.tag_add("color_orange","sel.first","sel.last")
        if(font=='brown'):
            self.text_area.tag_add("color_brown","sel.first","sel.last")
        if(font=='black'):
            self.text_area.tag_add("color_black","sel.first","sel.last")
        if(font=='violet'):
            self.text_area.tag_add("color_violet","sel.first","sel.last")
        
    
    def __init__(self,master):

        self.font="Courier"
        self.size="10"
        
        self.master=master
        master.title("NotePad in Python")
        self.text_area=Text()
        self.text_area.pack(fill=BOTH,expand=1)

        self.text_area.tag_config("normal",font=(self.font,self.size,"normal"))
        self.text_area.tag_config("bold",font=(self.font,self.size,"bold"))
        self.text_area.tag_config("italic",font=(self.font,self.size,"italic"))
        self.text_area.tag_config("underline",font=(self.font,self.size,"underline"))

        self.text_area.tag_config("color_red",foreground="red")
        self.text_area.tag_config("color_blue",foreground="blue")
        self.text_area.tag_config("color_green",foreground="green")
        self.text_area.tag_config("color_yellow",foreground="yellow")
        self.text_area.tag_config("color_lightblue",foreground="lightblue")
        self.text_area.tag_config("color_lightgreen",foreground="lightgreen")
        self.text_area.tag_config("color_violet",foreground="violet")
        self.text_area.tag_config("color_orange",foreground="orange")
        self.text_area.tag_config("color_brown",foreground="brown")
        self.text_area.tag_config("color_black",foreground="black")


        self.text_area.tag_config("font_arial",font="Arial")
        self.text_area.tag_config("font_verdana",font="Verdana")
        self.text_area.tag_config("font_courier",font="Courier")
        self.text_area.tag_config("font_times",font="Times")
        self.text_area.tag_config("font_georgia",font="Georgia")
        self.text_area.tag_config("font_tahoma",font="Tahoma")
        self.text_area.tag_config("font_jokerman",font="Jokerman")
        self.text_area.tag_config("font_impact",font="Impact")
        

        
        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)

        #creating file menu
        self.file_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="File",menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open",command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save as",command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit",command=self.master.quit)


        #creating edit menu
        self.edit_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Edit",menu=self.edit_menu)
        self.edit_menu.add_command(label="Normal", command=self.normal_text)
        self.edit_menu.add_command(label="Bold", command=self.bold_text)
        self.edit_menu.add_command(label="Italic", command=self.italic_text)
        self.edit_menu.add_command(label="Underline", command=self.underline_text)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)


        #creating Format menu
        self.format_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Format",menu=self.format_menu)
        self.format_menu.add_command(label="Font", command=self.font_fn)

        #creating Font menu
        self.font_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Fonts",menu=self.font_menu)
        
        self.font_menu.add_command(label="Arial", command=lambda:self.font_fn_arial("Arial"))
        self.font_menu.add_command(label="Verdana", command=lambda:self.font_fn_arial("Verdana"))
        self.font_menu.add_command(label="Courier", command=lambda:self.font_fn_arial("Courier"))
        self.font_menu.add_command(label="Times", command=lambda:self.font_fn_arial("Times"))
        self.font_menu.add_command(label="Georgia", command=lambda:self.font_fn_arial("Georgia"))
        self.font_menu.add_command(label="Tahoma", command=lambda:self.font_fn_arial("Tahoma"))
        self.font_menu.add_command(label="Jokerman", command=lambda:self.font_fn_arial("Jokerman"))
        self.font_menu.add_command(label="Impact", command=lambda:self.font_fn_arial("Impact"))

        #creating Colors menu
        self.color_menu=Menu(self.main_menu,tearoff=False)
        self.main_menu.add_cascade(label="Colors",menu=self.color_menu)
        
        self.color_menu.add_command(label="Red", command=lambda:self.font_fn_color("red"))
        self.color_menu.add_command(label="Blue", command=lambda:self.font_fn_color("blue"))
        self.color_menu.add_command(label="Green", command=lambda:self.font_fn_color("green"))
        self.color_menu.add_command(label="Yellow", command=lambda:self.font_fn_color("yellow"))
        self.color_menu.add_command(label="Orange", command=lambda:self.font_fn_color("orange"))
        self.color_menu.add_command(label="Brown", command=lambda:self.font_fn_color("brown"))
        self.color_menu.add_command(label="Violet", command=lambda:self.font_fn_color("violet"))
        self.color_menu.add_command(label="Light Green", command=lambda:self.font_fn_color("lightgreen"))
        self.color_menu.add_command(label="Light Blue", command=lambda:self.font_fn_color("lightblue"))
        self.color_menu.add_command(label="Black ( Default )", command=lambda:self.font_fn_color("black"))
        
                

root=Tk()
photo=PhotoImage(file=r"logo.png")
root.iconphoto(False,photo)
te=text_editor(root)
root.mainloop()