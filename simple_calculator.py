import tkinter as tk
import tkinter.font as tk_font

###------------------------------------Initialize variables---------------------------------------###

#-----------tkinter root window--------#

root = tk.Tk()


#-----------main variables-------------#

accent_btn_bg = "#f19812"
std_btn_bg = "#b4b4b4"
accent_text_color = "#ffffff"
std_text_color = "#242424"
bg_color = "#242424"
std_font = tk_font.Font(family="Arial", size=14, weight=tk_font.BOLD)  
display_font = tk_font.Font(family="Arial", size=18)
display_color = "#e1e1e1"
del_icon = tk.PhotoImage(file = r"del_btn.png")   
window_icon = tk.PhotoImage(file =r"calculator_icon.png")
command_list = []
finished_calculation = False



###------------------------------Define functions-------------------------------------------###


def validate_entry(action_type, val):

    """Validate entry in the display widget to only allow numbers 0-9 and the following strings: (*/+-=cC)"""

    valid_values = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+/-", "C", "del", "/", "*", "-", "+", ".", "=")
    
    #if the action type is an insertion, make sure it's a valid value
    if action_type == "1":        
        
        if all(i in valid_values for i in val):                   
            return True
        
    #if the action is a deletion, always allow it
    elif action_type == "0":
        return True

    
    return False



def number_click(val):

    """The main function that runs when pressing a number button/key. Returns "break" to prevent the built-in key handler from running. 
    Otherwise the number would be inserted twice on every key press"""

    global finished_calculation

    #if current cacluation is completed, clear the display before inserting new numbers. This way new numbers aren't appended to the previous value   
    #don't insert zero if the display is empty

    if finished_calculation:

        if val == 0:
            
            display.delete(0, tk.END)  
            finished_calculation = False                   
            return "break"
           
        else:

            display.delete(0, tk.END)  
            display.insert(tk.END, val)
            finished_calculation = False           
            return "break"

    else:

        if val == 0:
            
            if display.get():

                display.insert(tk.END, val)   
                return "break"

        else:

            display.insert(tk.END, val) 
            return "break"
    


def pos_neg_click():

    """Toggles the current value in the display between positive and negative"""

    if display.get():

        if display.get()[0] != "-":

            display.insert(0, "-")

        else:

            display.delete(-1)

    #if the display is empty, just insert - at the beginning so the subsequent entry will be negative
    else:
        
        display.insert(0, "-")


def clear_click():

    """Clears all data from the display and command list"""

    display.delete(0, tk.END)
    command_list.clear()
   


def backspace_click():

    """Deletes the last number in the dislplay"""

    #calculate the length of the characters on the display, then subtract one. Starting at that index, delete everything until the end (will just be the last character)

    display.delete(len(display.get())-1, tk.END)



def operator_click(val):

    """Runs when any of the operator (/*-+) buttons are pressed"""

    #make sure the display isn't empty
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
                    
                #if the last value is an operator, replace that operator with the newly-pressed operator 
                else:
                    command_list[-1] = val

            #if the command list is empty, just append the current value and the operator that was pressed
            else:
                
                command_list.append(current_value)
                command_list.append(val)
                



def equals_click():

    """Evaluates everything in the command list and displays the result"""

    global finished_calculation

    #make sure command list isn't empty
    if command_list:

        if display.get():     
                
            command_list.append(display.get())
            display.delete(0, tk.END)          
            result = eval(" ".join(command_list))
            display.insert(0, result)

            #empty the command list to get ready for the next round of calculations
            command_list.clear()

        else:

            #if the display is empty, add the previous value to the end of the list
            
            command_list.append(command_list[-2])
           
            display.delete(0, tk.END)          
            result = eval(" ".join(command_list))

            #display the result
            display.insert(0, result)
            command_list.clear()
                
    #the current calculation has been completed. Set vairable to True and begin a new set of calculations
    finished_calculation = True


def bind_keys():

    """overrides default keybindings and binds keyboard keys to custom functions"""

    root.bind("<plus>", lambda x: operator_click("+"))
    root.bind("<minus>", lambda x: operator_click("-"))
    root.bind("<asterisk>", lambda x: operator_click("*"))
    root.bind("<slash>", lambda x: operator_click("/"))
    root.bind("<Return>", lambda x: equals_click())    
    root.bind("<c>", lambda x: clear_click())
    root.bind("<period>", lambda x: number_click("."))

    for i in range(10):
        display.bind(str(i), lambda x: number_click(int(x.char)))




###------------------------------------configure and display GUI components------------------------------------###

root.geometry("328x488")
root.configure(background="#242424")
root.title("Calculator v1.1")
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


####---------------------------------------------Create Buttons---------------------------------------------------------###

#The equals button wlll be double width at 132x60, all other buttons will be 60x60. Frames are used to hold the buttons so that they can be sized in pixels rather than tpye units.


#-----------------------First Row--------------------------------#

pos_neg_frame = tk.Frame(root, height=60, width=60)
pos_neg_button = tk.Button(pos_neg_frame, text="+/-", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=pos_neg_click)

clear_frame = tk.Frame(root, height=60, width=60)
clear_button = tk.Button(clear_frame, text="C", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=clear_click)

del_frame = tk.Frame(root, height=60, width=60)
del_button = tk.Button(del_frame, font=(std_font), image=del_icon, bg=std_btn_bg, fg=std_text_color, command=backspace_click)

divide_frame = tk.Frame(root, height=60, width=60)
divide_button = tk.Button(divide_frame, text="/", font=(std_font), bg=accent_btn_bg, fg=accent_text_color, command=lambda: operator_click("/"))



#-----------------------Second Row--------------------------------#

seven_frame = tk.Frame(root, height=60, width=60)
seven_button = tk.Button(seven_frame, text="7", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(7))

eight_frame = tk.Frame(root, height=60, width=60)
eight_button = tk.Button(eight_frame, text="8", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(8))

nine_frame = tk.Frame(root, height=60, width=60)
nine_button = tk.Button(nine_frame, text="9", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(9))

multiply_frame = tk.Frame(root, height=60, width=60)
multiply_button = tk.Button(multiply_frame, text="*", font=(std_font), bg=accent_btn_bg, fg=accent_text_color, command=lambda: operator_click("*"))



#-----------------------Third Row--------------------------------#

four_frame = tk.Frame(root, height=60, width=60)
four_button = tk.Button(four_frame, text="4", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(4))

five_frame = tk.Frame(root, height=60, width=60)
five_button = tk.Button(five_frame, text="5", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(5))

six_frame = tk.Frame(root, height=60, width=60)
six_button = tk.Button(six_frame, text="6", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(6))

minus_frame = tk.Frame(root, height=60, width=60)
minus_button = tk.Button(minus_frame, text="-", font=(std_font), bg=accent_btn_bg, fg=accent_text_color, command=lambda: operator_click("-"))



#-----------------------Fourth Row--------------------------------#

one_frame = tk.Frame(root, height=60, width=60)
one_button = tk.Button(one_frame, text="1", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(1))

two_frame = tk.Frame(root, height=60, width=60)
two_button = tk.Button(two_frame, text="2", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(2))

three_frame = tk.Frame(root, height=60, width=60)
three_button = tk.Button(three_frame, text="3", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(3))

plus_frame = tk.Frame(root, height=60, width=60)
plus_button = tk.Button(plus_frame, text="+", font=(std_font), bg=accent_btn_bg, fg=accent_text_color, command=lambda: operator_click("+"))


       
#-----------------------Fifth Row---------------------------------#

zero_frame = tk.Frame(root, height=60, width=60)
zero_button = tk.Button(zero_frame, text="0", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click(0))

decimal_frame = tk.Frame(root, height=60, width=60)
decimal_button = tk.Button(decimal_frame, text=".", font=(std_font), bg=std_btn_bg, fg=std_text_color, command=lambda: number_click("."))

equal_frame = tk.Frame(root, height=60, width=132)
equal_button = tk.Button(equal_frame, text="=", font=(std_font), bg=accent_btn_bg, fg=accent_text_color, command=equals_click)



###------------------------lay out frames in a grid and pack buttons into frames--------------------####


frames = [pos_neg_frame, clear_frame, del_frame, divide_frame, seven_frame, eight_frame, nine_frame, multiply_frame, four_frame, five_frame, six_frame, minus_frame, one_frame, two_frame, three_frame, plus_frame, zero_frame, decimal_frame, equal_frame]

buttons = [pos_neg_button, clear_button, del_button, divide_button, seven_button, eight_button, nine_button, multiply_button, four_button, five_button, six_button, minus_button, one_button, two_button, three_button, plus_button, zero_button, decimal_button, equal_button]


x_coord = 26
y_coord = 114

for frame, button in zip(frames, buttons):

    frame.propagate(False)
    frame.place(x=x_coord, y=y_coord)
    button.pack(expand=True, fill=tk.BOTH)

    #if x_coord is 242 we've reached the end of the row and will need to start a new row

    if x_coord == 242:

        x_coord = 26
        y_coord += 72

    else:

        x_coord += 72




###-------------------------Run the main loop and give focus to the display---------------------------###

bind_keys()
display.focus()
root.mainloop()