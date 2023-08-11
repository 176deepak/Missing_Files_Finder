import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import main

width = 400
height = 250


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Filename Changer")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        center_x = int(screen_width / 2 - width / 2)
        center_y = int(screen_height / 2 - height / 2)
        self.geometry(f"{width}x{height}+{center_x}+{center_y}")
        self.resizable(False, False)
        self.iconbitmap(r"static\favicon.ico")

        self.create_widgets()

    def choose_drt(self, btn):
        directory = filedialog.askdirectory()
        if directory:
            btn.delete(0, tk.END)  # Clear the entry field
            btn.insert(0, directory)

    def change_name(self, drt1, drt2):
        try:
            files = main.directory_files_comparer(drt1, drt2)
            frame2 = tk.Frame(self, width=400)
            frame2.pack(padx=20)

            text = ttk.Label(frame2, text=files)
            text.pack(padx=10, side=tk.LEFT)
            
            messagebox.showinfo("Sucess", "Operation Successful...")
        except:
            messagebox.showerror("Error! Something went wrong.")

    def create_widgets(self):
        drt1 = ttk.Label(self, text="Directory you compare with:")
        drt1.pack(padx=10, pady=5, anchor=tk.NW)

        frame1 = tk.Frame(self, width=400)
        frame1.pack(padx=10)

        drt_value1 = tk.StringVar()
        drt_entry1 = ttk.Entry(frame1, textvariable=drt_value1, width=50)
        drt_entry1.pack(side=tk.LEFT)

        drt_btn1 = ttk.Button(
            frame1, text="select", command=lambda: self.choose_drt(btn=drt_entry1)
        )
        drt_btn1.pack(side=tk.LEFT)

        drt2 = ttk.Label(self, text="Directory you compare against:")
        drt2.pack(padx=10, pady=5, anchor=tk.NW)

        frame1 = tk.Frame(self, width=400)
        frame1.pack(padx=10)

        drt_value2 = tk.StringVar()
        drt_entry2 = ttk.Entry(frame1, textvariable=drt_value2, width=50)
        drt_entry2.pack(side=tk.LEFT)

        drt_btn = ttk.Button(
            frame1, text="select", command=lambda: self.choose_drt(btn=drt_entry2)
        )
        drt_btn.pack(side=tk.LEFT)

        done_btn = ttk.Button(
            self,
            text="Find",
            command=lambda: self.change_name(drt_value1.get(), drt_value2.get()),
            cursor="hand2",
        )
        done_btn.pack(pady=20, ipadx=20)

        text = ttk.Label(self, text="Extra files in 2 directory:")
        text.pack(pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()
