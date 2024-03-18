import tkinter as tk
from tkinter import ttk
import subprocess
import re
import threading

class MasscanGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Masscan HTTP GET Scanner")
        self.geometry("600x400")

        # Create UI elements
        self.subnet_label = tk.Label(self, text="Subnet (e.g. 192.168.1.0/24):")
        self.subnet_label.pack()
        self.subnet_entry = tk.Entry(self)
        self.subnet_entry.pack()

        self.scan_button = tk.Button(self, text="Scan", command=self.run_scan)
        self.scan_button.pack(pady=10)

        self.results_label = tk.Label(self, text="Results:")
        self.results_label.pack()
        self.results_text = tk.Text(self, height=15, width=70)
        self.results_text.pack()

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def run_scan(self):
        subnet = self.subnet_entry.get()
        if not subnet:
            self.status_label.config(text="Please enter a subnet", fg="red")
            return

        self.results_text.delete("1.0", tk.END)
        self.status_label.config(text="Scanning in progress...", fg="green")

        # Run masscan in a separate thread to prevent UI freezing
        thread = threading.Thread(target=self.scan_subnet, args=(subnet,))
        thread.start()

    def scan_subnet(self, subnet):
        try:
            masscan_output = subprocess.check_output(
                f"masscan {subnet} --ports 0-9000 --rate 10000 --banners --http-method-GET",
                shell=True,
                universal_newlines=True,
            )
        except subprocess.CalledProcessError as e:
            self.status_label.config(text="Error: " + str(e), fg="red")
            return

        self.results_text.insert(tk.END, masscan_output)
        self.status_label.config(text="Scan completed", fg="green")

if __name__ == "__main__":
    app = MasscanGUI()
    app.mainloop()