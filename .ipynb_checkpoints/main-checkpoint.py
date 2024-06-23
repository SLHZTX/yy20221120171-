"""
场景设置:
有是一家电子商务公司，希望分析客户的购买行为，以便更好地理解不同类别产品的销售情况以及客户的购买习惯。
可以使用 Seaborn 的 swarmplot 和 histplot 函数来进行数据可视化和分析。
"""
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

"""
用户可以选择不同的图表类型，然后点击按钮来显示相应的图表。图表会嵌入到Tkinter窗口中进行显示。
"""

# 数据
information = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'purchase_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01', '2024-01-02', '2024-01-03',
                      '2024-01-01', '2024-01-02', '2024-01-03', '2024-01-01'],
    'product_category': ['Electronics', 'Books', 'Clothing', 'Electronics', 'Books', 'Clothing', 'Electronics',
                         'Books', 'Clothing', 'Electronics'],
    'purchase_amount': [200, 15, 50, 220, 20, 55, 250, 18, 60, 230],
    'purchase_time': [10, 15, 12, 11, 14, 16, 13, 15, 10, 9]
}
information = pd.DataFrame(information)

# 创建主窗口
root = tk.Tk()
root.title("分析图表选择")

# 创建图表选择下拉菜单
chart_options = ['购买数量分布', '购买时间分布']
selected_chart = tk.StringVar()
selected_chart.set(chart_options[0])


# 绘制图表的函数
def plot_chart():
    chart_type = selected_chart.get()

    # 清除当前图表
    for widget in chart_frame.winfo_children():
        widget.destroy()

    fig, ax = plt.subplots(figsize=(10, 6))

    if chart_type == '购买数量分布':
        sb.swarmplot(x='product_category', y='purchase_amount', hue='purchase_date', data=information, size=10, ax=ax)
        ax.set_title('purchase_amount_distribution')
        ax.set_xlabel('product_category')
        ax.set_ylabel('purchase_amount')
    elif chart_type == '购买时间分布':
        sb.histplot(data=information, x='purchase_time', hue='product_category', bins=10, kde=True, ax=ax)
        ax.set_title('purchase_time_distribution')
        ax.set_xlabel('purchase_time')
        ax.set_ylabel('frequency')

    # 将绘制的图表绘制到到Tkinter窗口
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# 退出
def exit_func():
    exit()


# 创建选择框
chart_menu = ttk.Combobox(root, textvariable=selected_chart, values=chart_options)
chart_menu.pack(pady=10)

# 创建绘图按钮
plot_button = tk.Button(root, text="绘图", command=plot_chart)
plot_button.pack(pady=5)

# 创建退出按钮
exit_button = tk.Button(root, text="退出", command=root.quit)
exit_button.pack(pady=5)

# 创建用于显示图表的框架
chart_frame = tk.Frame(root)
chart_frame.pack(pady=20)

root.mainloop()
