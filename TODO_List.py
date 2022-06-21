from tkinter import RIGHT
from tkinter import LEFT
from tkinter import Frame
from tkinter import Label
from tkinter import X
import tkinter.messagebox
import pickle  # konwertowanie obiektu Pythona na strumień bajtów

root = tkinter.Tk()
root.overrideredirect(True)


def move_app(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")


def quitter(e):
    root.quit()


def minimizer(e):
    root.minimize()


def add_task(event=None):
    task = entry_task.get()  # dodanie zadania do okna zadań

    if task != "":  # brak odstępu między zadaniami
        listbox_task.insert(tkinter.END, task)  # dodanie do okna
        entry_task.delete(0, tkinter.END)  # dodanie do okna zadania pozycji 0
    else:  # brak wpisania zadania wyrzuci błąd
        tkinter.messagebox.showwarning(title="Waring!", message="You must enter a task.")


def delete_task():
    try:
        task_index = listbox_task.curselection()  # index 0,ponieważ chcemy tylko 1 element z listy a,nie wiele na raz
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="Waring!", message="You must select a task.")


def load_task():
    try:
        tasks = pickle.load(open("task.data", "rb"))  # "rb" - został napisany w trybie binarnym
        listbox_task.delete(0, tkinter.END)  # - zapobiega ponownemu wczytaniu tego samego zapisanego pliku
        for task in tasks:
            listbox_task.insert(tkinter.END, task)
    except:
        tkinter.messagebox.showwarning(title="Waring!", message="You must find a task.")


def save_task():
    task = listbox_task.get(0, listbox_task.size())
    pickle.dump(task, open("task.data", "wb"))
    # "wb" - plik jest zapisany w trybie binarnym(nie wprowadza żadnych zmian, ponieważ "task" jest zapisany w pliku)


# fejkowy pasek zadań
title_bar = Frame(root, bg="gray11", relief="raised", bd=2)
title_bar.pack(expand=1, fill=X)

# slowa na pasku taki sam kolor jak pasek
title_label = Label(title_bar, anchor="center", text="To Do List", font=("Forte", 12, "bold"), bg="gray11", fg="gray80")
title_label.pack(side=LEFT, pady=2, expand=True)

# binding - ruchomosc okna
title_bar.bind("<B1-Motion>", move_app)

# okno zamykania X
close_label = Label(title_bar, text=" X ", font=("Arial", 9, "bold"), bg="red", fg="black", relief="raised", bd=2)
close_label.pack(side=RIGHT, pady=4)
close_label.bind("<Button- 1>", quitter)

# okno minimalizacji _

minimize_label = Label(title_bar, text=" _ ", font=("Arial", 9, "bold"), bg="red", fg="black", relief="raised", bd=2)
minimize_label.pack(side=RIGHT, pady=4)
minimize_label.bind("<Button- 2>", minimizer)

# graficzny interfejs użytkownika
frame_task = tkinter.Frame(root)
frame_task.pack(expand=1, fill=X)

listbox_task = tkinter.Listbox(frame_task, height=10, width=55)
listbox_task.pack(side=tkinter.LEFT)

# pasek przesuwania
scrollbar_task = tkinter.Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand=scrollbar_task.set)  # yscrollcommand lub xscrollcommand - widżet paska przewijania
scrollbar_task.config(
    command=listbox_task.yview())  # x/yview-obsługuje przewijanie odpowiednio w kierunku poziomym i pionowym.

# okno dodania zadania
entry_task = tkinter.Entry(root, width=50)
entry_task.pack()
entry_task.bind('<Return>', add_task)

# przycisk dodania zadania do To-DO listy
button_add_task = tkinter.Button(root, text="Add task", width=48, command=add_task)
button_add_task.pack()

# przycisk usunięcia zadania
button_delete_task = tkinter.Button(root, text="Delete task", width=48, command=delete_task)
button_delete_task.pack()

# przycisk wczytania zapisanego zadania
button_load_task = tkinter.Button(root, text="Load task", width=48, command=load_task)
button_load_task.pack()

# przycisk zapisania listy zadań
button_save_task = tkinter.Button(root, text="Save task", width=48, command=save_task)
button_save_task.pack()

root.mainloop()
