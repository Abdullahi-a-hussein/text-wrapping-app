
from tkinter import *

MINUTE = 60
FONT_NAME = 'MS Serif'
BACKGROUND_COLOR = "#FFFFFF"
FOREGROUND = "#000000"
COLOR_LIST = ["#FDF1F0", "#F6DBD9", "#EABAB6", "#E59D88", "#E66B49"]
OPTIONS = [5, 15, 30, 45, 60]
STARTED_TYPING = False
KEY_PRESSED = None


def duration_selected(choice=None):
    """Get the duration the clients wants to work 
        duration options: 5minutes, 15 minutes, 30 minutes, 45 minutes or 60 minutes
    """
    choice = working.get()
    text.focus()
    return choice


def timer(count):
    if count > 0:
        window.after(1000, timer, count - 1)
    else:
        text.config(state=DISABLED)
    
        

def timer_call(event=None):
    global STARTED_TYPING, MINUTE
    if not STARTED_TYPING:
        working = int(duration_selected())
        print(working)
        timer(working*MINUTE)
        STARTED_TYPING = True
        
def pause(paused):
    def stop_start(event=None):
        window.after_cancel(running)
    if paused > 0:
        text.bind("<Key>", stop_start)
        running = window.after(1000, pause, paused - 1)
        if paused < 5:
            text.config(fg=COLOR_LIST[paused])
    else:
        text.delete('1.0', END)
        text.config(fg=FOREGROUND)
    running = window.after(1000, pause, paused - 1)
        
    


# ----------------------------------------- UI SET UP ------------------------------- #
window = Tk()
window.title('Dispearing Text Wrapping App')
window.config(width=1000, height=800, padx=30, pady=30, bg=BACKGROUND_COLOR)
time_description = Label(text="Select Time you want to work in Minutes:", font=(FONT_NAME, 32))

time_description.grid(row=0, column=0)
working = StringVar(window)
working.set(5)
select_time = OptionMenu(window, working, *OPTIONS, command=duration_selected)
select_time.config(font=(FONT_NAME, 24))
select_time.grid(row=1, column=0)
text = Text(width=100, height=30, padx=30, pady=30, font=(FONT_NAME, 24), bg=BACKGROUND_COLOR, wrap='word', fg=FOREGROUND)
text.grid(column=0, row=2,columnspan=2)


text.bind("<Key>", timer_call)
pause(10)





window.mainloop()