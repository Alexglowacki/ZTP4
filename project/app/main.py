from ui.view import ProductView
import tkinter as tk
from viewModel import Products

app = tk.Tk()

view_model = Products()
view = ProductView(app, view_model)

app.mainloop()
