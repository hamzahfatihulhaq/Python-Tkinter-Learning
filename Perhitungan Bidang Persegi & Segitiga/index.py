import tkinter as tk
from PIL import ImageTk,Image
import algoritma as alg

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.bidang = None
        self.switch_frame(StartPage,self.bidang)
        self.title("Program Perhitungan Bidang")
        self.geometry("400x300")
        self.title = 'top'

    def switch_frame(self, frame_class,bidang):
        self.bidang = bidang
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    
class StartPage(tk.Frame):
    def __init__(self, master):
    
        tk.Frame.__init__(self, master)
        # label
        label = tk.Label(self, text="Program Perhitungan Bidang",font=('Helvetica', 18, "bold"))
        label.grid(row =0, column=1, padx=10,pady=30)
        # button
        Persegi = tk.Button(self, text="Persegi",width=10,command=lambda: master.switch_frame(PageOne,"Persegi"))
        Segitiga = tk.Button(self, text="Segitiga",width=10,command=lambda: master.switch_frame(PageOne,"Segitiga"))
        Exit = tk.Button(self,text="Exit",width=10,command= master.quit)

        Persegi.grid(row =1, column=1,padx=10,pady=5)
        Segitiga.grid(row =2, column=1,padx=10,pady=5)
        Exit.grid(row =3, column=1,padx=10,pady=10)
        
class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Label
        label = tk.Label(self, text="Program Perhitungan "+ master.bidang,font=('Helvetica', 18, "bold"))
        label.grid(row =0, column=1, padx=10,pady=30)
        # Buttom
        Luas = tk.Button(self, text="Luas",width=10,command=lambda: master.switch_frame(PageTwo,master.bidang))
        Keliling = tk.Button(self, text="Keliling",width=10,command=lambda: master.switch_frame(PageThree,master.bidang))
        Back = tk.Button(self, text="Back",width=10,command=lambda: master.switch_frame(StartPage,None))

        Luas.grid(row =1, column=1,padx=10,pady=5)
        Keliling.grid(row =2, column=1,padx=10,pady=5)
        Back.grid(row =3, column=1,padx=10,pady=10)

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Label
        label = tk.Label(self, text="Luas "+ master.bidang,font=('Helvetica', 18, "bold"))
        label.grid(row =0, column=0, padx=10,pady=30,columnspan=3)

        # buttom
        Back = tk.Button(self, text="Back",width=10,command=lambda: master.switch_frame(PageOne,master.bidang))
        Back.grid(row =4, column=1,padx=5,pady=10)

        cari =tk.Button(self, text="Cari",width=10,command=lambda: self.MencariLuas(entry_sisi1,entry_sisi2,master.bidang))
        cari.grid(row =4, column=2,padx=5,pady=10)

        label_luas = tk.Label(self, text="Luas :")
        entry_luas = tk.Label(self)
        label_luas.grid(row=3,column=1,padx=1,pady=5)
        entry_luas.grid(row=3,column=2,padx=1,pady=5)

        if master.bidang == "Persegi":
            image1 = Image.open("./img/persegi.jpeg")
            image1 = image1.resize((100,100), Image.ANTIALIAS)#(height,widht)
            my_img1 = ImageTk.PhotoImage(image1)
            my_label = tk.Label(self,image=my_img1)
            my_label.image = my_img1
            my_label.grid(row=1,column=0,rowspan=3)

            label_sisi1 = tk.Label(self, text="Sisi1 :")
            entry_sisi1 = tk.Entry(self)
            label_sisi1.grid(row=1,column=1,padx=1,pady=5)
            entry_sisi1.grid(row=1,column=2,padx=1,pady=5)

            label_sisi2 = tk.Label(self, text="Sisi2 :")
            entry_sisi2 = tk.Entry(self)
            label_sisi2.grid(row=2,column=1,padx=1,pady=5)
            entry_sisi2.grid(row=2,column=2,padx=1,pady=5)
        if master.bidang == "Segitiga":
            image1 = Image.open("./img/segitiga.jpeg")
            image1 = image1.resize((100,100), Image.ANTIALIAS)#(height,widht)
            my_img1 = ImageTk.PhotoImage(image1)
            my_label = tk.Label(self,image=my_img1)
            my_label.image = my_img1
            my_label.grid(row=1,column=0,rowspan=3)

            label_sisi1 = tk.Label(self, text="Tinggi :")
            entry_sisi1 = tk.Entry(self)
            label_sisi1.grid(row=1,column=1,padx=1,pady=5)
            entry_sisi1.grid(row=1,column=2,padx=1,pady=5)

            label_sisi2 = tk.Label(self, text="Alas :")
            entry_sisi2 = tk.Entry(self)
            label_sisi2.grid(row=2,column=1,padx=1,pady=5)
            entry_sisi2.grid(row=2,column=2,padx=1,pady=5)

    def MencariLuas(self,entry1,entry2,bidang):
        entry1 = int(entry1.get())
        entry2 = int(entry2.get())
        Luas = tk.StringVar()

        if bidang == "Persegi":
            Luas.set(str(alg.persegi(entry1,entry2).luas()))

        if bidang == "Segitiga":
            Luas.set(str(alg.segitiga(entry1,entry2,None).luas()))

        label_luas = tk.Label(self,text="Luas :")
        entry_luas = tk.Entry(self,textvariable = Luas)
        label_luas.grid(row=3,column=1,padx=1,pady=5)
        entry_luas.grid(row=3,column=2,padx=1,pady=5)

class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        # Label
        label = tk.Label(self, text="Keliling "+ master.bidang,font=('Helvetica', 18, "bold"))
        label.grid(row =0, column=0, padx=10,pady=30,columnspan=3)

        if master.bidang == "Persegi":
            image1 = Image.open("./img/persegi.jpeg")
            image1 = image1.resize((100,100), Image.ANTIALIAS)#(height,widht)
            my_img1 = ImageTk.PhotoImage(image1)
            my_label = tk.Label(self,image=my_img1)
            my_label.image = my_img1
            my_label.grid(row=1,column=0,rowspan=3)

            label_sisi1 = tk.Label(self, text="Sisi1 :")
            entry_sisi1 = tk.Entry(self)
            label_sisi1.grid(row=1,column=1,padx=1,pady=5)
            entry_sisi1.grid(row=1,column=2,padx=1,pady=5)

            label_sisi2 = tk.Label(self, text="Sisi2 :")
            entry_sisi2 = tk.Entry(self)
            label_sisi2.grid(row=2,column=1,padx=1,pady=5)
            entry_sisi2.grid(row=2,column=2,padx=1,pady=5)

            label_keliling = tk.Label(self, text="Keliling :")
            entry_keliling = tk.Label(self)
            label_keliling.grid(row=3,column=1,padx=1,pady=5)
            entry_keliling.grid(row=3,column=2,padx=1,pady=5)

            Back = tk.Button(self, text="Back",width=10,command=lambda: master.switch_frame(PageOne,master.bidang))
            Back.grid(row =4, column=1,padx=5,pady=10)

            cari =tk.Button(self, text="Cari",width=10,command=lambda: self.MencariKeliling(entry_sisi1,entry_sisi2,None,master.bidang))
            cari.grid(row =4, column=2,padx=5,pady=10)

        if master.bidang == "Segitiga":
            image1 = Image.open("./img/segitiga.jpeg")
            image1 = image1.resize((100,100), Image.ANTIALIAS)#(height,widht)
            my_img1 = ImageTk.PhotoImage(image1)
            my_label = tk.Label(self,image=my_img1)
            my_label.image = my_img1
            my_label.grid(row=1,column=0,rowspan=3)

            label_sisi1 = tk.Label(self, text="Tinggi :")
            entry_sisi1 = tk.Entry(self)
            label_sisi1.grid(row=1,column=1,padx=1,pady=5)
            entry_sisi1.grid(row=1,column=2,padx=1,pady=5)

            label_sisi2 = tk.Label(self, text="Alas :")
            entry_sisi2 = tk.Entry(self)
            label_sisi2.grid(row=2,column=1,padx=1,pady=5)
            entry_sisi2.grid(row=2,column=2,padx=1,pady=5)

            label_sisi3 = tk.Label(self, text="Miring :")
            entry_sisi3 = tk.Entry(self)
            label_sisi3.grid(row=3,column=1,padx=1,pady=5)
            entry_sisi3.grid(row=3,column=2,padx=1,pady=5)

            label_keliling = tk.Label(self, text="Keliling :")
            entry_keliling = tk.Label(self)
            label_keliling.grid(row=4,column=1,padx=1,pady=5)
            entry_keliling.grid(row=4,column=2,padx=1,pady=5)
            
            Back = tk.Button(self, text="Back",width=10,command=lambda: master.switch_frame(PageOne,master.bidang))
            Back.grid(row =5, column=1,padx=5,pady=10)

            cari =tk.Button(self, text="Cari",width=10,command=lambda: self.MencariKeliling(entry_sisi1,entry_sisi2,entry_sisi3,master.bidang))
            cari.grid(row =5, column=2,padx=5,pady=10)

    def MencariKeliling(self,entry1,entry2,entry3,bidang):
        entry1 = int(entry1.get())
        entry2 = int(entry2.get())
        keliling = tk.StringVar()

        if bidang == "Persegi":
            keliling.set(str(alg.persegi(entry1,entry2).keliling()))

            label_keliling = tk.Label(self,text="Keliling :")
            entry_keliling = tk.Entry(self,textvariable = keliling)
            label_keliling.grid(row=3,column=1,padx=1,pady=5)
            entry_keliling.grid(row=3,column=2,padx=1,pady=5)
            
        if bidang == "Segitiga":
            entry3 = int(entry3.get())
            keliling.set(str(alg.segitiga(entry1,entry2,entry3).keliling()))

            label_keliling = tk.Label(self,text="Keliling :")
            entry_keliling = tk.Entry(self,textvariable = keliling)
            label_keliling.grid(row=4,column=1,padx=1,pady=5)
            entry_keliling.grid(row=4,column=2,padx=1,pady=5)

if __name__ == "__main__":
    # wndRoot = tk.Tk()
    app = SampleApp()
    app.mainloop()