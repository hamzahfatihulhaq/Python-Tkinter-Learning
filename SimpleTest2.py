import tkinter as tk

root = tk.Tk()

def ButtonClick(Sisi1,Sisi2):
    sisi1 = int(Sisi1.get())
    sisi2 = int(Sisi2.get())
    Luas = tk.StringVar()
    Luas.set(str(sisi1*sisi2))
    label_luas = tk.Label(root, text="Luas : ")
    entry_luas = tk.Entry(root, textvariable =Luas)
    label_luas.grid(row=3,column=1,padx=1,pady=5)
    entry_luas.grid(row=3,column=2,padx=1,pady=5)

cari =tk.Button(root, text="Cari",width=10, command= lambda: ButtonClick(entry_sisi1,entry_sisi2))
cari.grid(row =4, column=2,padx=5,pady=10)

label_sisi1 = tk.Label(root, text="Sisi1 :")
entry_sisi1 = tk.Entry(root)
label_sisi1.grid(row=1,column=1,padx=1,pady=5)
entry_sisi1.grid(row=1,column=2,padx=1,pady=5)

label_sisi2 = tk.Label(root, text="Sisi2 :")
entry_sisi2 = tk.Entry(root)
label_sisi2.grid(row=2,column=1,padx=1,pady=5)
entry_sisi2.grid(row=2,column=2,padx=1,pady=5)

label_luas = tk.Label(root, text="Luas :")
entry_luas = tk.Label(root)
label_luas.grid(row=3,column=1,padx=1,pady=5)
entry_luas.grid(row=3,column=2,padx=1,pady=5)

root.mainloop()