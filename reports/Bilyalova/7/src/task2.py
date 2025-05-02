import tkinter as tk
from tkinter import ttk, colorchooser, filedialog, messagebox
from PIL import Image, ImageDraw, ImageTk
import math

class SierpinskiTriangleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Треугольная салфетка Серпинского")
        
        # Параметры фрактала
        self.depth = 3
        self.width = 600
        self.height = 600
        self.bg_color = "white"
        self.triangle_color = "blue"
        self.padding = 20
        
        # Создаем холст для отрисовки
        self.canvas = tk.Canvas(root, width=self.width, height=self.height, bg=self.bg_color)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)
        
        # Создаем панель управления
        self.control_frame = ttk.Frame(root)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)
        
        # Элементы управления
        ttk.Label(self.control_frame, text="Глубина рекурсии:").pack(pady=5)
        self.depth_slider = ttk.Scale(self.control_frame, from_=0, to=8, 
                                     command=self.update_depth)
        self.depth_slider.set(self.depth)
        self.depth_slider.pack(pady=5)
        
        self.depth_label = ttk.Label(self.control_frame, text=f"Текущая глубина: {self.depth}")
        self.depth_label.pack(pady=5)
        
        ttk.Label(self.control_frame, text="Цвет треугольника:").pack(pady=5)
        self.color_btn = ttk.Button(self.control_frame, text="Выбрать", 
                                  command=self.choose_color)
        self.color_btn.pack(pady=5)
        
        ttk.Label(self.control_frame, text="Цвет фона:").pack(pady=5)
        self.bg_color_btn = ttk.Button(self.control_frame, text="Выбрать", 
                                     command=self.choose_bg_color)
        self.bg_color_btn.pack(pady=5)
        
        self.draw_btn = ttk.Button(self.control_frame, text="Нарисовать", 
                                 command=self.draw_fractal)
        self.draw_btn.pack(pady=10)
        
        self.save_btn = ttk.Button(self.control_frame, text="Сохранить изображение", 
                                 command=self.save_image)
        self.save_btn.pack(pady=10)
        
        self.draw_fractal()
    
    def draw_fractal(self):
        self.canvas.delete("all")
        self.canvas.config(bg=self.bg_color)
        
        # Размеры треугольника с учетом отступов
        size = min(self.width, self.height) - 2 * self.padding
        height = size * math.sqrt(3) / 2
        
        # Координаты вершин равностороннего треугольника
        x1, y1 = self.width // 2, self.padding
        x2, y2 = self.padding, self.padding + height
        x3, y3 = self.padding + size, self.padding + height
        
        # Рисуем фрактал
        self.draw_sierpinski(x1, y1, x2, y2, x3, y3, self.depth)
    
    def draw_sierpinski(self, x1, y1, x2, y2, x3, y3, depth):
        if depth == 0:
            self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, 
                                     fill=self.triangle_color, 
                                     outline="black")
        else:
            x12 = (x1 + x2) / 2
            y12 = (y1 + y2) / 2
            x13 = (x1 + x3) / 2
            y13 = (y1 + y3) / 2
            x23 = (x2 + x3) / 2
            y23 = (y2 + y3) / 2
            
            self.draw_sierpinski(x1, y1, x12, y12, x13, y13, depth-1)
            self.draw_sierpinski(x12, y12, x2, y2, x23, y23, depth-1)
            self.draw_sierpinski(x13, y13, x23, y23, x3, y3, depth-1)
    
    def update_depth(self, value):
        self.depth = int(float(value))
        self.depth_label.config(text=f"Текущая глубина: {self.depth}")
    
    def choose_color(self):
        color = colorchooser.askcolor(title="Выберите цвет треугольника")[1]
        if color:
            self.triangle_color = color
    
    def choose_bg_color(self):
        color = colorchooser.askcolor(title="Выберите цвет фона")[1]
        if color:
            self.bg_color = color
            self.canvas.config(bg=self.bg_color)
    
    def save_image(self):
        image = Image.new("RGB", (self.width, self.height), self.bg_color)
        draw = ImageDraw.Draw(image)
        
        # Рисуем фрактал на изображении
        self.draw_sierpinski_on_image(draw, self.depth)
        
        filetypes = [("PNG файлы", "*.png"), ("JPEG файлы", "*.jpg"), ("Все файлы", "*.*")]
        filename = filedialog.asksaveasfilename(defaultextension=".png", 
                                              filetypes=filetypes)
        if filename:
            try:
                image.save(filename)
                messagebox.showinfo("Успешно", "Изображение сохранено")
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")
    
    def draw_sierpinski_on_image(self, draw, depth):
        size = min(self.width, self.height) - 2 * self.padding
        height = size * math.sqrt(3) / 2
        
        x1, y1 = self.width // 2, self.padding
        x2, y2 = self.padding, self.padding + height
        x3, y3 = self.padding + size, self.padding + height
        
        self._draw_sierpinski_recursive(draw, x1, y1, x2, y2, x3, y3, depth)
    
    def _draw_sierpinski_recursive(self, draw, x1, y1, x2, y2, x3, y3, depth):
        if depth == 0:
            draw.polygon([(x1, y1), (x2, y2), (x3, y3)], 
                        fill=self.triangle_color, 
                        outline="black")
        else:
            x12 = (x1 + x2) / 2
            y12 = (y1 + y2) / 2
            x13 = (x1 + x3) / 2
            y13 = (y1 + y3) / 2
            x23 = (x2 + x3) / 2
            y23 = (y2 + y3) / 2
            
            self._draw_sierpinski_recursive(draw, x1, y1, x12, y12, x13, y13, depth-1)
            self._draw_sierpinski_recursive(draw, x12, y12, x2, y2, x23, y23, depth-1)
            self._draw_sierpinski_recursive(draw, x13, y13, x23, y23, x3, y3, depth-1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SierpinskiTriangleApp(root)
    root.mainloop()