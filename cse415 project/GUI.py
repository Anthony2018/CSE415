''' HMM GUI 1.4
HMM GUI support. It will output graphic showing of HMM calculation.
Programmed by Yuhan Gao
UW NetID: yuhang4@uw.edu
CSE 415 Project Option 4
'''
import tkinter as tk
import math
from tkinter import Canvas, Scrollbar

# define circle function for creating a circle conviently
def circle(canvas, x, y, r, f):
    id = canvas.create_oval(x-r, y-r, x+r, y+r, fill=f)
    return id

def guiGenerate(operation, probability, viterbi=[]):

    # handle mousewheel event for scrolling canvas by mousewheel or touchpad
    def mousewheel(event):
        gui_canvas.xview_scroll(-1*(event.delta), "units")

    # GUI initializing
    gui = tk.Tk()
    gui.title("HMM GUI 1.4")
    weather = ['Rainy','Sunny','Cloudy','Partly\nCloudy','Smoke']
    weather2 = ['Rainy','Sunny','Cloudy','Partly Cloudy','Smoke']
    color = ["#87CEEB", "#00FFFF", "#FFFFE0", "#FFE4E1", "#B22222"]
    circle_dic = {}
    # [SkyBlue 天蓝色, Aqua 浅绿色/水色, LightYellow 浅黄色, MistyRose 浅玫瑰色, FireBrick 火砖色]

    # GUI parameter difining
    start_ovel_center = 35
    gap = 250
    op_gap = 60
    weather_gap = 120
    circle_rad = 30
    canvas_width = (len(operation)+1)*gap+100
    canvas_height = 700
    half_height = canvas_height/2
    end_ovel_center = start_ovel_center+(len(operation)+1)*gap

    # Canvas initializing, if size too large, then use scrollbar
    if canvas_width > 1350:
        xbar = tk.Scrollbar(gui, orient=tk.HORIZONTAL)
        xbar.pack(fill=tk.X, side=tk.BOTTOM)
        gui_canvas = tk.Canvas(gui, width=1350, height=700, scrollregion=(0,0,canvas_width,canvas_height), xscrollcommand=xbar.set)
        gui_canvas.bind_all("<MouseWheel>", mousewheel) # bind all point to mousewheel event for scrolling canvas
        gui_canvas.pack(fill=tk.BOTH)
        xbar.config(command=gui_canvas.xview)
    else:
        gui_canvas = Canvas(gui, width=canvas_width, height=canvas_height)
        gui_canvas.pack()

    # Create start circle
    circle(gui_canvas, start_ovel_center, half_height, circle_rad, "#800080")
    gui_canvas.create_text(start_ovel_center, half_height, text="<S>", fill="#FFFFFF")

    # Create main loop of operation 
    for i in range(len(operation)):
        # Draw operation text on the top
        gui_canvas.create_text(start_ovel_center+gap*(i+1), half_height-2*weather_gap-op_gap, text=operation[i])
        circle_dic[i] = []
        
        # Draw each weather condition circle
        for j in range(len(weather)):
            circle(gui_canvas, start_ovel_center+gap*(i+1), half_height-2*weather_gap+j*weather_gap, circle_rad, color[j]) 
            gui_canvas.create_text(start_ovel_center+gap*(i+1), half_height-2*weather_gap+j*weather_gap, text=weather[j])
            gui_canvas.create_text(start_ovel_center+gap*(i+1), half_height-2*weather_gap+j*weather_gap+40, text=probability[i][j])
            circle_dic[i].append((start_ovel_center+gap*(i+1), half_height-2*weather_gap+j*weather_gap))

    # Create end circle
    circle(gui_canvas, end_ovel_center, half_height, circle_rad, "#800080")
    gui_canvas.create_text(end_ovel_center, half_height, text="<E>", fill="#FFFFFF")

    # Create arrow for start circle
    for i in range(len(weather)):
        theta = math.atan2(circle_dic[0][i][1]-half_height, circle_dic[0][i][0]-start_ovel_center)
        start_x = start_ovel_center + circle_rad * math.cos(theta)
        start_y = half_height + circle_rad * math.sin(theta)
        end_x = circle_dic[0][i][0] - circle_rad * math.cos(theta)
        end_y = circle_dic[0][i][1] - circle_rad * math.sin(theta)
        gui_canvas.create_line(start_x, start_y, end_x, end_y, arrow='last')

    # Create arrow for any other circle but last
    for i in range(len(circle_dic)):
        if i != len(circle_dic)-1:
            c_list = circle_dic[i]
            c_list_next = circle_dic[i+1]
            for start_point in c_list:
                ori_start_x = start_point[0]
                ori_start_y = start_point[1]
                for end_point in c_list_next:
                    ori_end_x = end_point[0]
                    ori_end_y = end_point[1]
                    theta = math.atan2(ori_end_y - ori_start_y, ori_end_x - ori_start_x)
                    start_x = ori_start_x + circle_rad * math.cos(theta)
                    start_y = ori_start_y + circle_rad * math.sin(theta)
                    end_x = ori_end_x - circle_rad * math.cos(theta)
                    end_y = ori_end_y - circle_rad * math.sin(theta)
                    gui_canvas.create_line(start_x, start_y, end_x, end_y, arrow='last')
        else:
            c_list = circle_dic[i]
            for start_point in c_list:
                ori_start_x = start_point[0]
                ori_start_y = start_point[1]
                ori_end_x = end_ovel_center
                ori_end_y = half_height
                theta = math.atan2(ori_end_y - ori_start_y, ori_end_x - ori_start_x)
                start_x = ori_start_x + circle_rad * math.cos(theta)
                start_y = ori_start_y + circle_rad * math.sin(theta)
                end_x = ori_end_x - circle_rad * math.cos(theta)
                end_y = ori_end_y - circle_rad * math.sin(theta)
                gui_canvas.create_line(start_x, start_y, end_x, end_y, arrow='last')
    
    if viterbi!=[]:
        ori_start_x = start_ovel_center
        ori_start_y = half_height
        for i in range(len(viterbi)):
            weather_index = weather2.index(viterbi[i])
            ori_end_x = circle_dic[i][weather_index][0]
            ori_end_y = circle_dic[i][weather_index][1]

            theta = math.atan2(ori_end_y - ori_start_y, ori_end_x - ori_start_x)
            start_x = ori_start_x + circle_rad * math.cos(theta)
            start_y = ori_start_y + circle_rad * math.sin(theta)
            end_x = ori_end_x - circle_rad * math.cos(theta)
            end_y = ori_end_y - circle_rad * math.sin(theta)
            gui_canvas.create_line(start_x, start_y, end_x, end_y, arrow='last', fill="#FF0000", width=4)

            ori_start_x = ori_end_x
            ori_start_y = ori_end_y
        
        new_end_x = end_ovel_center
        new_end_y = half_height

        theta = math.atan2(new_end_y - ori_start_y, new_end_x - ori_start_x)
        start_x = ori_start_x + circle_rad * math.cos(theta)
        start_y = ori_start_y + circle_rad * math.sin(theta)
        end_x = new_end_x - circle_rad * math.cos(theta)
        end_y = new_end_y - circle_rad * math.sin(theta)
        gui_canvas.create_line(start_x, start_y, end_x, end_y, arrow='last', fill="#FF0000", width=4)

    gui.mainloop()




