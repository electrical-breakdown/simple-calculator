import tkinter as tk
import tkinter.font as tk_font


#Initialize root window

root = tk.Tk()


#Initialize main variables

accent_btn_bg = "#f19812"
std_btn_bg = "#b4b4b4"
accent_text_color = "#ffffff"
std_text_color = "#242424"
bg_color = "#242424"
std_font = tk_font.Font(family="Arial", size=14)  #weight=tkFont.BOLD
display_font = tk_font.Font(family="Arial", size=18)
display_color = "#e1e1e1"
command_list = []
del_icon = tk.PhotoImage(file = r"del_btn.png")   
window_icon = tk.PhotoImage(file =r"calculator_icon.png")


#configure and display GUI components

root.geometry("328x488")
root.configure(background="#242424")
root.title("Calculator v1.0")
root.resizable(width=False, height=False)
root.iconphoto(False, window_icon)
    
display_frame=tk.Frame(root, width=276, height=52, bg=display_color)
display_frame.propagate(False)
display_frame.place(x=26, y=26)

display=tk.Entry(display_frame, font=(display_font), fg=std_text_color, bg=display_color, highlightthickness=0, borderwidth=0)
display.pack(expand=True, fill=tk.BOTH, padx=12)


#Define functions

def button_click(val):
    
    """The main function that runs when a button is clicked. The buttons value is passed in as an argument and used to determine which operation to perform"""

    if val in "/*-+":

        command_list.append(display.get())
        command_list.append(val)
        display.delete(0, tk.END)  

    elif val=="+/-":

        if display.get()[0] != "-":

            display.insert(0, "-")

        else:

            display.delete(-1)

    elif val == "del":

        #calculate the length of the characters on the display, then subtract one. Starting at that index, delete everything until the end (will just be the last character)
        display.delete(len(display.get())-1, tk.END)

    elif val == "C":

        display.delete(0, tk.END)
        command_list.clear()

    elif val == "=":

        command_list.append(display.get())
        display.delete(0, tk.END)          
        result = eval(" ".join(command_list))

        #display the result
        display.insert(0, result)

        #empty the command list to get ready for the next round of calculations
        command_list.clear()

    else:

        display.insert(tk.END, val)



def generate_buttons():

    """Generates the buttons by iterating through the buttons list and then using the character as an argument to the button_click function"""

    y_coord = 114
    buttons = [["+/-", "C", "del", "/"],[7, 8, 9, "*"], [4, 5, 6, "-"], [1, 2, 3, "+"], [0, ".", "="]]

    for row in buttons:

        x_coord = 26
        
        for char in row:
            
            #set the size of the buttons. The equals button wlll be double width at 132x60, all other buttons will be 60x60. Frames are used to hold the buttons so that they can be sized in pixels rather than tpye units.

            if char == "=":

                button_frame = tk.Frame(root, height=60, width=132)            

            else:

                button_frame = tk.Frame(root, height=60, width=60)

            #The operator buttons will have a special color, all other buttons will be the default color. The delete button has an icon rather than a text label

            if str(char) in ("+-*/="):            
                
                button = tk.Button(button_frame, text=str(char), font=(std_font), bg=accent_btn_bg, fg=accent_text_color, command=lambda val=char: button_click(str(val)))
            
            elif char == "del":

                button = tk.Button(button_frame, font=(std_font), image=del_icon, bg=std_btn_bg, fg=accent_text_color, command=lambda val=char: button_click(str(val)))

            else:

                button = tk.Button(button_frame, text=str(char), font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda val=char: button_click(str(val)))


            button_frame.propagate(False)
            button_frame.place(x=x_coord, y=y_coord)
            button.pack(expand=True, fill=tk.BOTH)

            #increment the x coordinates for the next iteration through the row. 60px button width + 12px padding = 72px increase for each iteration
            x_coord += 72
            
        #increment the x coordinates to move on to the next row. 60px button height + 12px padding = 72px increase for each iteration
        y_coord += 72



#Generate buttons and run the main loop

generate_buttons()
root.mainloop()