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

VALID_KEYS = ("<plus>", "<minus>", "<asterisk>", "<slash>", "<Return>", "<period>", "<c>")
VALID_VALUES = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+/-", "C", "del", "/", "*", "-", "+", ".", "=")
#VALID_VALUES = ("+/-", "c", "C", "del", "/", "*", "-", "+", ".", "=")


#Define functions

last_operation = ""

def button_click(val):
    
    """The main function that runs when a button is clicked. The buttons value is passed in as an argument and used to determine which operation to perform"""
    
    global last_operation
    # print("start of button click function")
    # print(f"val is: {val}")
  
  

    
        
    
    if val in "/*+-":

        if display.get():

            #split the display content on "<" and grab just the first portion so that the keypress data isn't added to the command list

            current_value = display.get().split(val)[0]

            
            #clear the display once an operator key is pressed
            display.delete(0, tk.END)  

            #if the command list isn't empty, make sure the last value isn't already an operator, then append the current value of the display, and the operator that was pressed
            if command_list:

                
                if command_list[-1] not in "/*-+":
                    command_list.append(current_value)
                    command_list.append(val)
                    

                    print(f"command list: {command_list}")

                #if the last value is an operator, change that value to the newly-pressed operator 
                else:
                    command_list[-1] = val

            #if the command list is empty, just append the current value and the operator that was pressed
            else:
                
                command_list.append(current_value)
                command_list.append(val)
                print(f"command list: {command_list}")


    elif val=="+/-":

        #check to make sure there is a value before trying to make it negative
        if display.get():

            if display.get()[0] != "-":

                display.insert(0, "-")

            else:

                display.delete(-1)

        #if the display is empty, just insert - at the beginning so the subsequent entry will be negative
        else:
            display.insert(0, "-")

    elif val == "del":

        #calculate the length of the characters on the display, then subtract one. Starting at that index, delete everything until the end (will just be the last character)
        display.delete(len(display.get())-1, tk.END)

    elif val == "c" or val == "C":

        display.delete(0, tk.END)
        command_list.clear()
        print(f"command list: {command_list}")

    elif val in ("=", "\r"):
        
        if display.get():
            # if command_list[-1] in "+-\*":
            print("inside the elif if")
            if display.get():
                command_list.append(display.get())
                display.delete(0, tk.END)          
                result = eval(" ".join(command_list))
                display.insert(0, result)
                    #empty the command list to get ready for the next round of calculations
                command_list.clear()

        else:
            #if the display is empty, add the previous value to the end of the list
            print("in the equals else")
            command_list.append(command_list[-2])
            print(f"updated command_list: {command_list}")
            display.delete(0, tk.END)          
            result = eval(" ".join(command_list))
            #display the result
            display.insert(0, result)
            command_list.clear()
               

        print(f"command list: {command_list}")

    elif val == ".":

        if command_list:
            #check to make sure display isn't empty
            if display.get():

                if last_operation == "=":
                    display.delete(0, tk.END)  
                    display.insert(tk.END, val)

                #insert . ONLY if the previous character isn't already a .
                if display.get()[-1] !=".":
                    display.insert(tk.END, val)

            #if the display is empty, just insert . at the beginning so the subsequent entry will be a float
            else: 
                display.insert(tk.END, val)

    else:
        
        
        #check to see if the last operation was equals. If so, we want to clear the display and insert new values rather than append them to the number current displayed
        print("inside the last operation section")
        if last_operation == "=" or not last_operation:
            print("inside the last operation section")
            display.delete(0, tk.END)  
            display.insert(tk.END, val)

        else:
            display.insert(tk.END, val)

        
    
    last_operation = val
    print(f"last operation: {last_operation}")
    print("end of button click function")


def validate_entry(action_type, val):
    """Validate entry in the display widget to only allow numbers 0-9 and the following strings: (*/+-=cC)"""
    
    #if the action type is an insertion, make sure it's a valid value
    if action_type == "1":
        
        
        if all(i in VALID_VALUES for i in val):
            
            # print(f"val: {val}")
            # print(f"action type before true: {action_type}")
            return True
        
    #if the action is a deletion, always allow it
    elif action_type == "0":
        return True

    # print("-----before the false------")
    # print(f"action type before false: {action_type}")
    
    # print(f"val before false: {val}")
    # print(f"type of val: {type(val)}")
    return False


def bind_keys():

    """Bind keyboard keys to the button_click function and pass in their char attribute"""

    for key in VALID_KEYS:
    #for key in ("+", "-", "/", "*", "<Return>", "."):

        root.bind(key, lambda x: button_click(x.char))
       

def generate_buttons():

    """Generates the buttons by iterating through the buttons list and then using the character as an argument to the button_click function"""

    y_coord = 114
    button_layout = [["+/-", "C", "del", "/"],[7, 8, 9, "*"], [4, 5, 6, "-"], [1, 2, 3, "+"], [0, ".", "="]]

    for row in button_layout:

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

vcmd = root.register(validate_entry)
display.configure(validate="key", validatecommand=(vcmd, "%d", "%S") )
display["validatecommand"] = (display.register(validate_entry), "%d", "%S")

display.pack(expand=True, fill=tk.BOTH, padx=12)





#---------------------------------------------------------------------------------------------
#Generate buttons and run the main loop


generate_buttons()
bind_keys()


root.mainloop()