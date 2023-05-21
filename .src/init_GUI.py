import tkinter as tk
from tkinter import ttk


def init_GUI(self):
    method_var1 = tk.IntVar()
    method_var2 = tk.IntVar()
    method_var3 = tk.IntVar()
    method_var4 = tk.IntVar()
    method_var5 = tk.IntVar()
    method_var6 = tk.IntVar()

    self.title("Wafer Analysis")
    self.geometry("575x450")

    self.set_data_folder_button = tk.Button(self, text="Set scale", command=self.save_choosed_data)
    self.set_data_folder_button.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    self.num_files_label = tk.Label(self, text="Number of Files: 0")
    self.num_files_label.grid(row=3, column=3, padx=5, pady=5, sticky="e")

    self.show_selected_files_button = tk.Button(self, text="Show Selected Files", command=self.show_selected_files)
    self.show_selected_files_button.grid(row=4, column=0, padx=5, pady=5, sticky="w")

    self.clear_selected_files_button = tk.Button(self, text="Clear Files", command=self.clear_selected_files)
    self.clear_selected_files_button.grid(row=4, column=3, padx=5, pady=5, sticky="e")

    self.progress_ratio_label = tk.Label(self, text="Progress ratio:  0%")
    self.progress_ratio_label.grid(row=6, column=3, padx=5, pady=5, sticky="e")

    self.progress_bar = ttk.Progressbar(self, length=110, orient="horizontal", mode="determinate")
    self.progress_bar.grid(row=7, column=3, padx=5, pady=5, sticky="e")

    self.analyze_button = tk.Button(self, text="Analyze", command=lambda: self.analyze_data([
        'ax1' if method_var1.get() else None,
        'ax2' if method_var2.get() else None,
        'ax3' if method_var3.get() else None,
        'ax4' if method_var4.get() else None,
        'save_csv' if method_var5.get() else None,
        'ax5' if method_var6.get() else None
    ]))
    self.analyze_button.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    self.xml_files = []

    self.toggle_button = tk.Checkbutton(self, text="IV_graph", padx=20, variable=method_var1)
    self.toggle_button.grid(row=7, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button2 = tk.Checkbutton(self, text="TS_graph", padx=20, variable=method_var2)
    self.toggle_button2.grid(row=8, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button3 = tk.Checkbutton(self,text="TS_fitting_8th", padx=20, variable=method_var3)
    self.toggle_button3.grid(row=9, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button4 = tk.Checkbutton(self,text="Flat_TS_graph", padx=20, variable=method_var4)
    self.toggle_button4.grid(row=10, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button5 = tk.Checkbutton(self,text="save_csv", padx=20, variable=method_var5)
    self.toggle_button5.grid(row=11, column=0, padx=5, pady=5, sticky="w")

    self.toggle_button6 = tk.Checkbutton(self,text="flat_flatgraph", padx=20, variable=method_var6)
    self.toggle_button6.grid(row=12, column=0, padx=5, pady=5, sticky="w")

    self.choose_dict = {}
    self.lot_list = []
    self.wafer_list = []
    self.coordinate_list = []
    self.date_list = []

    self.select_listbox1 = tk.Listbox(self, width=18, height=5, selectmode='multiple', exportselection=0)
    self.select_listbox1.grid(row=1, column=0, padx=5, pady=5)

    self.select_listbox2 = tk.Listbox(self, width=18, height=5, selectmode='multiple', exportselection=0)
    self.select_listbox2.grid(row=1, column=1, padx=5, pady=5)

    self.select_listbox3 = tk.Listbox(self, width=18, height=5, selectmode='multiple', exportselection=0)
    self.select_listbox3.grid(row=1, column=2, padx=5, pady=5)

    self.select_listbox4 = tk.Listbox(self, width=18, height=5, selectmode='multiple', exportselection=0)
    self.select_listbox4.grid(row=1, column=3, padx=5, pady=5)

    self.choose_analysis_scale()
