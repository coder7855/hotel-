
import tkinter as tk
from tkinter import ttk, messagebox
import re

class ModernCafeBillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("☕ Cafe Coffee Billing System")
        self.root.geometry("750x850")
        self.root.configure(bg="#F8EDEB")  # soft cafe-themed background

        self.name = tk.StringVar()
        self.phone_number = tk.StringVar()
        self.orders = {}
        self.total_bill = tk.IntVar(value=0)

        self.menu = {
            
    "🍕 Pizza": 100,
    "🍔 Burger": 50,
    "🥟 Momos": 20,
    "🍵 Tea": 10
}

        

        self.first_page()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def first_page(self):
        self.clear_frame()

        tk.Label(self.root, text="☕ Welcome to CAFE COMIX ☕", font=("Segoe UI", 28, "bold"),
                 fg="#6D4C41", bg="#F8EDEB").pack(pady=40)

        tk.Label(self.root, text="Enter Your Details", font=("Segoe UI", 18), bg="#F8EDEB", fg="#3E2723").pack(pady=10)

        form_frame = tk.Frame(self.root, bg="#F8EDEB")
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Name:", font=("Segoe UI", 14), bg="#F8EDEB").grid(row=0, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.name, font=("Segoe UI", 14), width=30, bd=2, relief="groove").grid(row=0, column=1, pady=5)

        tk.Label(form_frame, text="Phone Number:", font=("Segoe UI", 14), bg="#F8EDEB").grid(row=1, column=0, sticky="w", pady=5)
        tk.Entry(form_frame, textvariable=self.phone_number, font=("Segoe UI", 14), width=30, bd=2, relief="groove").grid(row=1, column=1, pady=5)

        tk.Button(self.root, text="Next ➡", font=("Segoe UI", 16), bg="#8E7DBE", fg="white",
                  command=self.validate_user, relief="flat", padx=20, pady=10).pack(pady=40)

    def validate_user(self):
        name = self.name.get().strip()
        phone = self.phone_number.get().strip()

        if not name or not phone:
            messagebox.showerror("Missing Info", "Please enter both Name and Phone Number.")
        elif not re.match(r'^\d{10}$', phone):
            messagebox.showwarning("Invalid", "Phone number must be 10 digits.")
        else:
            self.menu_page()

    def menu_page(self):
        self.clear_frame()
        self.total_bill.set(0)
        self.orders = {}

        tk.Label(self.root, text="📋 CAFE COMIX Menu", font=("Segoe UI", 26, "bold"), bg="#F8EDEB", fg="#4E342E").pack(pady=30)
        tk.Label(self.root, text="Select items and quantity", font=("Segoe UI", 16), bg="#F8EDEB").pack(pady=5)

        for item, price in self.menu.items():
            item_frame = tk.Frame(self.root, bg="#F8EDEB")
            item_frame.pack(padx=80, anchor="w", pady=10)

            tk.Label(item_frame, text=f"{item} - ₹{price}", font=("Segoe UI", 14), bg="#F8EDEB").pack(side="left")

            qty_var = tk.IntVar()
            spin = ttk.Spinbox(item_frame, from_=0, to=10, width=5, textvariable=qty_var, font=("Segoe UI", 14))
            spin.pack(side="right", padx=10)

            qty_var.trace_add("write", lambda *args: self.update_total())
            self.orders[item] = (price, qty_var)

        tk.Label(self.root, text="Total Bill:", font=("Segoe UI", 16, "bold"), bg="#F8EDEB").pack(pady=20)
        self.total_label = tk.Label(self.root, text="₹0", font=("Segoe UI", 16, "bold"), bg="#F8EDEB", fg="green")
        self.total_label.pack()

        tk.Button(self.root, text="💳 View Final Bill", font=("Segoe UI", 16), bg="#FF6F61", fg="white",
                  command=self.bill_page, relief="flat", padx=20, pady=10).pack(pady=30)

    def update_total(self):
        total = 0
        for price, qty_var in self.orders.values():
            try:
                quantity = int(qty_var.get())
                total += quantity * price
            except ValueError:
                continue
        self.total_bill.set(total)
        self.total_label.config(text=f"₹{total}")

    def bill_page(self):
        self.clear_frame()

        tk.Label(self.root, text="🧾 Final Bill", font=("Segoe UI", 26, "bold"), bg="#F8EDEB", fg="#3E2723").pack(pady=20)
        tk.Label(self.root, text=f"Name: {self.name.get()}", font=("Segoe UI", 16), bg="#F8EDEB").pack()
        tk.Label(self.root, text=f"Phone: {self.phone_number.get()}", font=("Segoe UI", 16), bg="#F8EDEB").pack()

        bill_frame = tk.Frame(self.root, bg="#F8EDEB")
        bill_frame.pack(pady=20)

        tk.Label(bill_frame, text=f"{'Item':<20}{'Qty':<10}{'Price'}", font=("Segoe UI", 16, "bold"), bg="#F8EDEB").pack(anchor="w")

        for item, (price, qty_var) in self.orders.items():
            qty = qty_var.get()
            if qty > 0:
                line = f"{item:<20}     {qty:<10}    ₹{qty * price}"
                tk.Label(bill_frame, text=line, font=("Segoe UI", 14), bg="#F8EDEB").pack(anchor="w")

        tk.Label(self.root, text=f"Total: ₹{self.total_bill.get()}", font=("Segoe UI", 18, "bold"), bg="#F8EDEB", fg="green").pack(pady=15)
        tk.Label(self.root, text="☕ Thank you for visiting CAFE COMIX ", font=("Segoe UI", 16), bg="#F8EDEB", fg="#4E342E").pack(pady=20)

        tk.Button(self.root, text="🔁 New Order", command=self.first_page, font=("Segoe UI", 14), bg="#8BC34A", fg="white", relief="flat", padx=15, pady=5).pack(pady=5)
        tk.Button(self.root, text="❌ Exit", command=self.root.destroy, font=("Segoe UI", 14), bg="#E57373", fg="white", relief="flat", padx=15, pady=5).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCafeBillingApp(root)
    root.mainloop()
