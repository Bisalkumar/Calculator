import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from math import sin, cos, tan, log, exp, radians, degrees

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("")

        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), bd=10, insertwidth=2, width=20, justify='right')
        entry.grid(row=0, column=0, columnspan=5)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('log', 5, 3),
            ('exp', 6, 0), ('rad', 6, 1), ('deg', 6, 2), ('clear', 6, 3),
            ('graph', 1, 4), ('unit conv', 2, 4), ('stats', 3, 4)
        ]

        for (text, row, col) in buttons:
            btn = tk.Button(self.root, text=text, font=('Arial', 15), padx=20, pady=20, command=lambda t=text: self.button_click(t))
            btn.grid(row=row, column=col)

    def button_click(self, char):
        if char == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except:
                self.result_var.set("Error")
        elif char == 'clear':
            self.result_var.set("")
        elif char == 'sin':
            self.result_var.set(str(sin(radians(float(self.result_var.get())))))
        elif char == 'cos':
            self.result_var.set(str(cos(radians(float(self.result_var.get())))))
        elif char == 'tan':
            self.result_var.set(str(tan(radians(float(self.result_var.get())))))
        elif char == 'log':
            self.result_var.set(str(log(float(self.result_var.get()))))
        elif char == 'exp':
            self.result_var.set(str(exp(float(self.result_var.get()))))
        elif char == 'rad':
            self.result_var.set(str(radians(float(self.result_var.get()))))
        elif char == 'deg':
            self.result_var.set(str(degrees(float(self.result_var.get()))))
        elif char == 'graph':
            self.plot_graph()
        elif char == 'unit conv':
            self.unit_conversion()
        elif char == 'stats':
            self.calculate_statistics()
        else:
            self.result_var.set(self.result_var.get() + char)

    def plot_graph(self):
        try:
            x = np.linspace(-10, 10, 400)
            y = eval(self.result_var.get())
            plt.plot(x, y)
            plt.xlabel('x')
            plt.ylabel('y')
            plt.title('Graph')
            plt.grid(True)
            plt.show()
        except:
            self.result_var.set("Invalid Expression")

    def unit_conversion(self):
        self.conv_window = tk.Toplevel(self.root)
        self.conv_window.title("Unit Conversion")

        from_unit_label = tk.Label(self.conv_window, text="From:")
        from_unit_label.grid(row=0, column=0, padx=10, pady=10)
        to_unit_label = tk.Label(self.conv_window, text="To:")
        to_unit_label.grid(row=0, column=2, padx=10, pady=10)

        from_unit_var = tk.StringVar()
        from_unit_combobox = ttk.Combobox(self.conv_window, textvariable=from_unit_var)
        from_unit_combobox['values'] = ("meters", "feet", "inches", "radians", "degrees")
        from_unit_combobox.grid(row=0, column=1, padx=10, pady=10)

        to_unit_var = tk.StringVar()
        to_unit_combobox = ttk.Combobox(self.conv_window, textvariable=to_unit_var)
        to_unit_combobox['values'] = ("meters", "feet", "inches", "radians", "degrees")
        to_unit_combobox.grid(row=0, column=3, padx=10, pady=10)

        value_label = tk.Label(self.conv_window, text="Value:")
        value_label.grid(row=1, column=0, padx=10, pady=10)
        value_var = tk.DoubleVar()
        value_entry = tk.Entry(self.conv_window, textvariable=value_var)
        value_entry.grid(row=1, column=1, padx=10, pady=10)

        converted_label = tk.Label(self.conv_window, text="Converted:")
        converted_label.grid(row=1, column=2, padx=10, pady=10)
        converted_var = tk.StringVar()
        converted_label = tk.Label(self.conv_window, textvariable=converted_var)
        converted_label.grid(row=1, column=3, padx=10, pady=10)

        convert_button = tk.Button(self.conv_window, text="Convert", command=lambda: self.convert_units(from_unit_var.get(), to_unit_var.get(), value_var.get(), converted_var))
        convert_button.grid(row=2, columnspan=4, padx=10, pady=10)

    def convert_units(self, from_unit, to_unit, value, converted_var):
        conversion_factors = {
            ("meters", "feet"): 3.28084,
            ("meters", "inches"): 39.3701,
            ("feet", "meters"): 0.3048,
            ("inches", "meters"): 0.0254,
            ("radians", "degrees"): 180 / np.pi,
            ("degrees", "radians"): np.pi / 180
        }
        if (from_unit, to_unit) in conversion_factors:
            converted_value = value * conversion_factors[(from_unit, to_unit)]
            converted_var.set(f"{converted_value:.4f} {to_unit}")
        else:
            converted_var.set("Invalid Conversion")

    def calculate_statistics(self):
        self.stats_window = tk.Toplevel(self.root)
        self.stats_window.title("Statistics")

        data_label = tk.Label(self.stats_window, text="Data (comma-separated):")
        data_label.grid(row=0, column=0, padx=10, pady=10)
        data_var = tk.StringVar()
        data_entry = tk.Entry(self.stats_window, textvariable=data_var)
        data_entry.grid(row=0, column=1, padx=10, pady=10)

        calculate_button = tk.Button(self.stats_window, text="Calculate", command=lambda: self.calculate_stats(data_var.get()))
        calculate_button.grid(row=1, columnspan=2, padx=10, pady=10)

        results_label = tk.Label(self.stats_window, text="Results:")
        results_label.grid(row=2, column=0, padx=10, pady=10)
        results_var = tk.StringVar()
        results_label = tk.Label(self.stats_window, textvariable=results_var)
        results_label.grid(row=2, column=1, padx=10, pady=10)

    def calculate_stats(self, data_str):
        try:
            data = [float(x.strip()) for x in data_str.split(",")]
            mean = np.mean(data)
            median = np.median(data)
            std_dev = np.std(data)
            results = f"Mean: {mean:.4f}\nMedian: {median:.4f}\nStandard Deviation: {std_dev:.4f}"
            self.results_var.set(results)
        except:
            self.results_var.set("Invalid Data")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
