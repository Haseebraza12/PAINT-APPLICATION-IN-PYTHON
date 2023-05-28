import base64
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser,filedialog,messagebox,simpledialog
import PIL.ImageGrab as ImageGrab
from PIL import Image, ImageDraw
import PIL
from PIL import ImageTk, Image
import math
#
icon = """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"""

icondata = base64.b64decode(icon)
#
main=Tk()
main.title("Haseeb Soft Paint")
main.iconbitmap('logo.ico')
theme_image=PhotoImage(file=r'Assets\Theme.png')
green_image=PhotoImage(file=r'Assets\Green.png')
red_image=PhotoImage(file=r'Assets\Red.png')
blue_image=PhotoImage(file=r'Assets\Blue.png')
yellow_image=PhotoImage(file=r'Assets\Yellow.png')
grey_image=PhotoImage(file=r'Assets\Grey.png')
purple_image=PhotoImage(file=r'Assets\Purple.png')
black_image=PhotoImage(file=r'Assets\Black.png')
brown_image=PhotoImage(file=r'Assets\Brown.png')
pink_image=PhotoImage(file=r'Assets\Pink.png')
orange_image=PhotoImage(file=r'Assets\Orange.png')
color_image=PhotoImage(file=r'Assets\color.png')
#
Width=0
Height=0
image = PIL.Image.new("RGB",(Width,Height), (255,255,255))
#global variables
x1=None
y1=None
brush_active = False
pen_width=1
pen_color='black'
eraser_color='white'
Last_x,Last_y=None,None
shape_id=None
bezier_points = []
shapes=None
redo_shapes=[]
selection_start = None
selection_rectangle = None

#function
#####################

def open_file():
    file_name = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png")])
    if file_name:
        # Open the image file
        image = Image.open(file_name)
        # Get the size of the canvas
        canvas_width = canvas.winfo_width()
        canvas_height = canvas.winfo_height()
        # Resize the image to fit the canvas
        image = image.resize((canvas_width, canvas_height))
        # Create a Tkinter-compatible photo image
        photo = ImageTk.PhotoImage(image)
        # Display the image on the canvas
        canvas.create_image(0, 0, image=photo, anchor="nw")
        # Set the photo as an attribute of the canvas to prevent it from being garbage collected
        canvas.image = photo


################################
def saved():
    file_name=filedialog.asksaveasfile(defaultextension=".jpg")
    x=main.winfo_rootx()+canvas.winfo_x()
    y=main.winfo_rooty()+canvas.winfo_y()
    x1=x+canvas.winfo_width()
    y1=y+canvas.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)
    messagebox.showinfo("Paint Notification","Iamge is saved as"+str(file_name))

def on_closing():#on closing
    answer = messagebox.askyesnocancel("QUIT","DO YOU WANT TO SAVE IT?",parent=main) # L mean Lament which means sorrow or grief if you have dirty mind plz google it
    if answer is not None:
        if answer:
            saved()
        main.destroy()

#################################    
def line(e):
    global x1,y1
    line=canvas.create_line(x1,y1,e.x,e.y,fill=pen_color,width=pen_width,smooth=True,capstyle='round')
    x1=e.x
    y1=e.y

def com(e):   #line changing function which helps to start with  the position of the mouse pointer
    global x1,y1
    x1=e.x
    y1=e.y 

 ##################################

def change():
    width=width_spin.get()
    height=height_spin.get()
    canvas.config(width=width,height=height)
    canvas.focus_set()
def size(e):# changing pen width
    global pen_width
    pen_width=e
def pencolor(x):#changing pen color
    global pen_color
    pen_color=x
    indicator.config(bg=x)
    canvas.focus_set()
def theme():
    a=colorchooser.askcolor()
    canvas.config(bg=a[-1])
    canvas.focus_set()
def colour(): # choosing colour for colour pallete
    global pen_color
    a=colorchooser.askcolor()
    pen_color=a[-1]
    indicator.config(bg=a[-1])
    canvas.focus_set()
'''def colour_change(c):# the function used in eraser
    global color
    color=c'''
############################## Brush

def brush_draw( event):
        global Last_x,Last_y
    
        if Last_x == None:
            Last_x , Last_y = event.x, event.y
            return
        
        canvas.create_line(Last_x, Last_y, event.x, event.y, width =pen_width, capstyle=ROUND, fill=pen_color)
        Last_x , Last_y = event.x, event.y
       

def brush_draw_end(event):
        global Last_x,Last_y
    
        Last_x,Last_y = None, None
def brush_button_pressed():
    #{
        global Last_x,Last_y
        canvas.bind("<B1-Motion>", brush_draw)
        canvas.bind("<ButtonRelease-1>", brush_draw_end)
        Last_x, Last_y = None, None
    # }
 ##################### ERASER
def erase_draw( event):
        global Last_x,Last_y
    
        if Last_x == None:
            Last_x , Last_y = event.x, event.y
            return
        
        canvas.create_line(Last_x, Last_y, event.x, event.y, width =pen_width, capstyle=ROUND, fill="White")
        Last_x , Last_y = event.x, event.y
       

def erase_draw_end(event):
        global Last_x,Last_y
    
        Last_x,Last_y = None, None
def eraser_button_pressed():
    
        global Last_x,Last_y
        canvas.bind("<B1-Motion>", erase_draw)
        canvas.bind("<ButtonRelease-1>", erase_draw_end)
        Last_x, Last_y = None, None  
    
#######################################

def clear():#tool
    canvas.delete("all")

##############################
def undo():
    if shapes:
        # Get the ID of the last drawn shape
        last_shape = shapes.pop()
        # Delete the shape from the canvas
        canvas.delete(last_shape)
        # Store the shape ID in the redo_shapes list
        redo_shapes.append(last_shape)
#####################################
def redo():
    if redo_shapes:
        # Get the ID of the last undone shape
        redo_shape = redo_shapes.pop()
        # Add the shape back to the canvas
        canvas.addtag_withtag(redo_shape, "shape")
####################################
start_x=None
start_y=None
selection=None
nowMove=False
cut_image=None
offset_x = None
offset_y = None
rect_x1=None
rect_x2=None
rect_y1=None
rect_y2=None
selected_item=None
def init( canvas,screen):
        screen=screen
        canvas = canvas

        start_x = None
        start_y = None
        selection = None

        cut_image = None
        selected_item = None
        offset_x = 0
        offset_y = 0
        nowMove=False

def start_selection(event):
       global start_x,start_y
       start_x = event.x
       start_y = event.y

def track_selection( event):
        global start_x,start_y,rect_x1,rect_x2,rect_y1,rect_y2
        canvas.delete(selection)
        selection = canvas.create_rectangle(
            start_x, start_y, event.x, event.y, outline="red",dash=TRUE
        )
        rect_x1=start_x
        rect_x2=event.x
        rect_y1=start_y
        rect_y2=event.y

def end_selection( event):
        canvas.delete(selection)
        selection = canvas.create_rectangle(
           start_x, start_y, event.x, event.y, outline="white",fill="white",tag="remove"
        )
        x1 = min(start_x, event.x)
        y1 = min(start_y, event.y)
        x2 = max(start_x, event.x)
        y2 = max(start_y, event.y)

        cut_image = ImageGrab.grab(bbox=(canvas.winfo_rootx() + x1+1,
                                               canvas.winfo_rooty() + y1+1,
                                               canvas.winfo_rootx() + x2-1,
                                               canvas.winfo_rooty() + y2))

        canvas.delete("pasted_image")
        image = ImageTk.PhotoImage(cut_image)
        selected_item = canvas.create_image(0, 0, anchor=NW, image=image, tags="pasted_image")
        cut_image = None

        if selected_item:
             canvas.unbind("<B1-Motion>")
             canvas.unbind("<ButtonRelease-1>")
             canvas.bind("<B1-Motion>", move_selection)
             canvas.bind("<ButtonRelease-1>", release_selection)

 
def move_selection( event):
        if selected_item:
            if not offset_x and not offset_y:
                offset_x = event.x
                offset_y = event.y
            else:
                canvas.move(selected_item, event.x - offset_x, event.y - offset_y)
                offset_x = event.x
                offset_y = event.y

def release_selection( event):
        global offset_x,offset_y
        offset_x = 0
        offset_y=0
################################## Flood Fill

def pressed_fill():
        canvas["cursor"] = "spraycan"
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")
        canvas.unbind("<Button-1>")
        canvas.bind("<Button-1>", fill)
        canvas.bind("<B1-Motion>", brush_draw)
        canvas.bind("<ButtonRelease-1>", fill_End)
def fill( event):
           
            x, y = event.x, event.y
            pixel_color = canvas.itemcget(canvas.find_closest(x, y), "fill")
            fillcolor=colorchooser.askcolor(title="Select Fill Color")[1]

            if pixel_color != fillcolor:
                
                item_id = canvas.find_closest(x, y)
                canvas.itemconfigure(item_id, fill=fillcolor)
        
def fill_End(event):
        global Last_x,Last_y,shape_id
        Last_x, Last_y = None, None
        shape_id = None
        canvas.unbind("<Button-1>")
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")
        
        canvas.bind("<B1-Motion>", brush_draw)
        canvas.bind("<ButtonRelease-1>",brush_draw_end)
        canvas["cursor"]="pencil"
########################################################zoom
zoom_scale=1.0
def zoom(event):
        global zoom_scale
        if event.delta > 0:
            zoom_scale *= 1.1
        else:
            zoom_scale /= 1.1

        canvas.scale("all", event.x, event.y, zoom_scale, zoom_scale)
########################################################### Magnifier
magnification_factor=2.5
def magnifier():
        canvas.scale(ALL, 0, 0, magnification_factor-0.7, magnification_factor-0.7)
        canvas.configure(scrollregion=canvas.bbox("all"))

def unmagnifier():
        canvas.scale(ALL, 0, 0, 1.5 / magnification_factor, 1.5 / magnification_factor)
        canvas.configure(scrollregion=canvas.bbox("all"))
############################################## Color Picker
def get_pixel_color( x,y):
        item_id = canvas.find_closest(x,y)[0]
        color = canvas.itemcget(item_id, "fill")
        if color=="":
            print("Pixel color:", "null")
        else:     
            print("Pixel color:", color)

        return color
def clrPickPressed():
        canvas["cursor"] = "hand2"
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")
        canvas.bind("<B1-Motion>", drawClrPick)
        canvas.bind("<ButtonRelease-1>", clrPickEnd)
        
def drawClrPick(event):
        global pen_color
        pen_color=get_pixel_color(event.x,event.y)

def clrPickEnd(event):
        global Last_x,Last_y,shape_id
        Last_x, Last_y = None, None
        shape_id = None
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")
        canvas.bind("<B1-Motion>",brush_draw)
        canvas.bind("<ButtonRelease-1>",brush_draw_end)
        canvas["cursor"] = "pencil"
#############################CIRCLE

def draw_circle(event):
    global Last_x,Last_y,shape_id
    if shape_id is not None:
        canvas.delete(shape_id)
        
    if Last_x is None:
        Last_x,Last_y=event.x,event.y
        return
    radius=abs(Last_x-event.x)+abs(Last_y-event.y)
    x1,y1=(Last_x-radius),(Last_y-radius)
    x2,y2=(Last_x+radius),(Last_y+radius)
    shape_id= canvas.create_oval(x1,y1,x2,y2,outline=pen_color,fill="",width=pen_width) 

def draw_circle_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None


def circle_pressed():#shapes circle
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_circle)
   canvas.bind("<ButtonRelease-1>", draw_circle_end)
#################################### Oval

def draw_oval( event):
        global shape_id,Last_x,Last_y
        if shape_id is not None:
            canvas.delete(shape_id)

        if Last_x is None:
            Last_x = event.x
            Last_y = event.y
            return

        x1, y1 = Last_x, Last_y
        x2, y2 = event.x, event.y

        # Calculate the coordinates for the oval
        if x2 < x1:
            x1, x2 = x2, x1
        if y2 < y1:
            y1, y2 = y2, y1

        center_x = (x1 + x2) / 2
        center_y = (y1 + y2) / 2
        radius_x = abs(x2 - x1) / 2
        radius_y = abs(y2 - y1) / 2

        # Calculate the coordinates of the oval using trigonometry
        points = []
        angle = 0
        step = 2 * math.pi / 360  # Increase the step value for smoother oval shape

        while angle < 2 * math.pi:
            x = center_x + radius_x * math.cos(angle)
            y = center_y + radius_y * math.sin(angle)
            points.append((x, y))
            angle += step

        shape_id = canvas.create_polygon(points, outline=pen_color, fill="", width=pen_width)

def draw_oval_end( event):
        global Last_y,Last_x,shape_id
        Last_x, Last_y = None, None
        shape_id = None

def oval_button_pressed():
      
      canvas.unbind("<B1-Motion>")
      canvas.unbind("<ButtoRelease-1>")
      canvas.bind("<B1-Motion>",draw_oval)
      canvas.bind("<ButtonRelease-1>", draw_oval_end)
       
######################################## Rectangle shape
def draw_rectangle(event):
    global Last_x, Last_y, shape_id

    if shape_id is not None:
        canvas.delete(shape_id)

    if Last_x is None:
        Last_x, Last_y = event.x, event.y
        return

    x1, y1 = Last_x, Last_y
    x2, y2 = event.x, event.y

    shape_id = canvas.create_rectangle(x1, y1, x2, y2, outline=pen_color,fill="", width=pen_width)

def draw_rectangle_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None


def Rectangle_pressed():#shapes circle
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_rectangle)
   canvas.bind("<ButtonRelease-1>", draw_rectangle_end)



 ####################################### Triangle Shape
def draw_Triangle( event):
    global shape_id,Last_x,Last_y
    if shape_id is not None:
        canvas.delete(shape_id)

    if Last_x is None:
        Last_x = event.x
        Last_y = event.y
        return

    x1, y1 = Last_x, Last_y
    x2, y2 = event.x, event.y

    # Calculate the coordinates for the points of the triangle
    dx = x2 - x1
    dy = y2 - y1
    radius = min(abs(dx), abs(dy))

    points = []
    angle = -math.pi / 2
    step = 2 * math.pi / 3

    for _ in range(3):
        x = x1 + math.cos(angle) * radius
        y = y1 + math.sin(angle) * radius
        points.append((x, y))
        angle += step

    shape_id = canvas.create_polygon(points, outline=pen_color,fill="",width=pen_width)
#
def draw_triangle_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None


def tri_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_Triangle)
   canvas.bind("<ButtonRelease-1>", draw_triangle_end)

########################################### Square
def draw_square(event):
    global Last_x, Last_y, shape_id

    if shape_id is not None:
        canvas.delete(shape_id)

    if Last_x is None:
        Last_x, Last_y = event.x, event.y
        return

    x1, y1 = Last_x, Last_y
    x2, y2 = event.x, event.y

    # Calculate the side length of the square
    side_length = min(abs(x2 - x1), abs(y2 - y1))

    if x2 < x1:
        x2 = x1 - side_length
    else:
        x2 = x1 + side_length

    if y2 < y1:
        y2 = y1 - side_length
    else:
        y2 = y1 + side_length

    shape_id = canvas.create_rectangle(x1, y1, x2, y2, outline=pen_color,fill="" ,width=pen_width)

def draw_Sqaure_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None

def Square_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_square)
   canvas.bind("<ButtonRelease-1>", draw_Sqaure_end)
########################################### Pentagon
def draw_Pentagon(event):
    global shape_id,Last_x,Last_y
    if shape_id is not None:
        canvas.delete(shape_id)

    if Last_x is None:
        Last_x = event.x
        Last_y = event.y
        return

    x1, y1 = Last_x, Last_y
    x2, y2 = event.x, event.y

    # Calculate the coordinates for the points of the pentagon
    dx = x2 - x1
    dy = y2 - y1
    radius = min(abs(dx), abs(dy))

    points = []
    angle = -math.pi / 2
    step = 2 * math.pi / 5

    for _ in range(5):
        x = x1 + math.cos(angle) * radius
        y = y1 + math.sin(angle) * radius
        points.append((x, y))
        angle += step

    shape_id = canvas.create_polygon(points, outline=pen_color,fill="", width=pen_width)

def draw_Pentagon_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None

def Penta_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_Pentagon)
   canvas.bind("<ButtonRelease-1>", draw_Pentagon_end)
################################################### Star
def draw_star( event):
        global shape_id,Last_x,Last_y
        if shape_id is not None:
            canvas.delete(shape_id)

        if Last_x is None:
            Last_x = event.x
            Last_y = event.y
            return

        x1, y1 = Last_x, Last_y
        x2, y2 = event.x, event.y

        # Calculate the radius of the star
        dx = x2 - x1
        dy = y2 - y1
        radius = min(abs(dx), abs(dy))

        center_x = x1 + dx / 2
        center_y = y1 + dy / 2

        # Define the coordinates for the points of the star
        points = []
        angle = - math.pi / 2
        step = 2 * math.pi / 5

        outer_radius = radius
        inner_radius = radius / 2  # Adjust the inner radius as desired for the hollow effect

        for _ in range(5):
            outer_x = center_x + math.cos(angle) * outer_radius
            outer_y = center_y + math.sin(angle) * outer_radius
            inner_x = center_x + math.cos(angle + step / 2) * inner_radius
            inner_y = center_y + math.sin(angle + step / 2) * inner_radius
            points.extend([(outer_x, outer_y), (inner_x, inner_y)])
            angle += step

        shape_id = canvas.create_polygon(points, outline=pen_color, fill="", width=pen_width)

def draw_star_end( event):
        global shape_id,Last_y,Last_x
        Last_x, Last_y = None, None
        shape_id = None

def star_button_pressed():
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")

        canvas.bind("<B1-Motion>", draw_star)
        canvas.bind("<ButtonRelease-1>", draw_star_end)
################################################## Hexagon
def draw_Hexagon( event):
        global shape_id,Last_x,Last_y
        if shape_id is not None:
            canvas.delete(shape_id)

        if Last_x is None:
            Last_x = event.x
            Last_y = event.y
            return

        x1, y1 = Last_x, Last_y
        x2, y2 = event.x, event.y

        # Calculate the coordinates for the points of the hexagon
        dx = x2 - x1
        dy = y2 - y1
        radius = min(abs(dx), abs(dy))

        points = []
        angle = -math.pi / 2
        step = 2 * math.pi / 6

        for _ in range(6):
            x = x1 + math.cos(angle) * radius
            y = y1 + math.sin(angle) * radius
            points.append((x, y))
            angle += step

        shape_id=canvas.create_polygon(points, outline=pen_color,fill="",width=pen_width)

def draw_Hexagon_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None

    
def hexa_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_Hexagon)
   canvas.bind("<ButtonRelease-1>", draw_Hexagon_end)
################################################ Line
def draw_line(event):
    global Last_x, Last_y, shape_id

    if shape_id is not None:
        canvas.delete(shape_id)

    if Last_x is None:
        Last_x, Last_y = event.x, event.y
        return

    x1, y1 = Last_x, Last_y
    x2, y2 = event.x, event.y

    shape_id = canvas.create_line(x1, y1, x2, y2, fill=pen_color, width=pen_width)

def draw_line_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None

def line_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_line)
   canvas.bind("<ButtonRelease-1>", draw_line_end)

#################################################### Bezier curve


def draw_bezier(event):
    global bezier_points
    bezier_points.append((event.x, event.y))
    
    if len(bezier_points) == 4:
        # Draw the Bezier curve
        x0, y0 = bezier_points[0]
        x1, y1 = bezier_points[1]
        x2, y2 = bezier_points[2]
        x3, y3 = bezier_points[3]
        canvas.create_line(x0, y0, x1, y1, x2, y2, x3, y3, smooth=True, fill=pen_color, width=pen_width)

def draw_bezier_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None

def Bezier_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_bezier)
   canvas.bind("<ButtonRelease-1>", draw_bezier_end)
################################################### Arc
def draw_arc(event):
    global Last_x, Last_y, shape_id

    if shape_id is not None:
        canvas.delete(shape_id)

    if Last_x is None:
        Last_x, Last_y = event.x, event.y
        return

    x1, y1 = Last_x, Last_y
    x2, y2 = event.x, event.y

    shape_id = canvas.create_arc(x1, y1, x2, y2, start=0, extent=180, outline=pen_color, width=pen_width)

def draw_Arc_end(event):
    global Last_x,Last_y,shape_id
    Last_x,Last_y=None,None
    shape_id=None

def Arc_pressed():
   canvas.unbind("<B1-Motion>")
   canvas.unbind("<ButtoRelease-1>")
   canvas.bind("<B1-Motion>",draw_arc)
   canvas.bind("<ButtonRelease-1>", draw_Arc_end)

################################################# N_polygon
#n-polygonn
num_points=None
def pressedPolygon():
        global num_points
        canvas["cursor"] = "cross"
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")
        canvas.bind("<B1-Motion>", drawPolygon)
        canvas.bind("<ButtonRelease-1>", drawPolygonEnd)

        # Create a dialog box that asks for the number of points
        num_points = simpledialog.askinteger("N-Polygon", "Enter the number of points:", parent=shape_frame)

def drawPolygon(event):
        global shape_id,Last_x,Last_y
        if shape_id is not None:
            canvas.delete(shape_id)

        if Last_x is None:
            Last_x = event.x
            Last_y = event.y
            return

        x1, y1 = Last_x, Last_y
        x2, y2 = event.x, event.y

        # Calculate the coordinates for the points of the polygon
        dx = x2 - x1
        dy = y2 - y1
        radius = min(abs(dx), abs(dy))

        # Use the number of points from the dialog box
        points = []
        angle = -math.pi / 2
        step = 2 * math.pi / num_points

        for _ in range(num_points):
            x = x1 + math.cos(angle) * radius
            y = y1 + math.sin(angle) * radius
            points.append((x, y))
            angle += step

        shape_id = canvas.create_polygon(points, outline=pen_color,fill="",width=pen_width)

def drawPolygonEnd( event):
        global Last_x,Last_y,shape_id
        Last_x, Last_y = None, None
        shape_id = None
        canvas.unbind("<B1-Motion>")
        canvas.unbind("<ButtonRelease-1>")
        canvas.bind("<B1-Motion>", brush_draw)
        canvas.bind("<ButtonRelease-1>", brush_draw_end)
        canvas["cursor"] = "pencil"
############################################
main.wm_iconphoto(True,PhotoImage(data=icondata))
main.protocol("WM_DELETE_WINDOW",on_closing)
#
frame1=Frame(main,height=100)
frame1.pack(side=TOP,fill=X)
#tool frame
tool_frame=LabelFrame(main,text='Tools',relief=RIDGE,bg="White",font="arial")
tool_frame.place(x=700,y=5,width=420,height=150)
# Shapes frame
shape_frame=LabelFrame(main,text='Shapes',relief=RIDGE,bg="white",font="arial")
shape_frame.place(x=1150,y=5,width=350,height=150)
# 
#x button
width_label=Label(frame1,text='x= ')
width_label.place(x=5,y=2)
width_spin=ttk.Spinbox(frame1,from_=2,to=1000,width=7,command=change)
width_spin.set(600)
width_spin.bind('<Return>',lambda e:change())
width_spin.place(x=25,y=2)
#y button
height_label=Label(frame1,text='y= ')
height_label.place(x=5,y=30)
height_spin=ttk.Spinbox(frame1,from_=2,to=1000,width=7,command=change)
height_spin.set(600)
height_spin.bind('<Return>',lambda e:change())
height_spin.place(x=25,y=30)
#button for theme 
theme=ttk.Button(frame1,image=theme_image,command=theme)
theme.place(x=100,y=3)
#
scaling=Scale(frame1,from_=1,to=100,orient=HORIZONTAL,command=size)
scaling.place(x=165,y=5)
# indicator
indicator=Label(frame1,bg='black',width=8,height=4)
indicator.place(x=300,y=5)
# button
btn=[ttk.Button()]*10
k=0
x=400
y=5
for i in range(2):
    for j in range(5):
        btn[k]=ttk.Button(frame1)
        btn[k].place(x=x,y=y)
        x+=50
        k+=1
    x=400
    y+=50
btn[0].config(image=red_image,command=lambda :pencolor('red'))
btn[1].config(image=green_image,command=lambda :pencolor('green'))
btn[2].config(image=blue_image,command=lambda :pencolor('blue'))
btn[3].config(image=orange_image,command=lambda :pencolor('orange'))
btn[4].config(image=yellow_image,command=lambda :pencolor('yellow'))
btn[5].config(image=pink_image,command=lambda :pencolor('pink'))
btn[6].config(image=black_image,command=lambda :pencolor('black'))
btn[7].config(image=grey_image,command=lambda :pencolor('grey'))
btn[8].config(image=brown_image,command=lambda :pencolor('brown'))
btn[9].config(image=purple_image,command=lambda :pencolor('purple'))

#color pallete
color=ttk.Button(frame1,image=color_image,command=colour)
color.place(x=650,y=5)
#TOOLS BUTTON
save_b1=Button(tool_frame,text='Save',bd=4,bg='grey',command=saved,relief=RIDGE)
save_b1.grid(row=0,column=0,padx=2)

eraser_b2=Button(tool_frame,text='Eraser',bd=4,bg='grey',command=eraser_button_pressed,relief=RIDGE)
eraser_b2.grid(row=0,column=1,padx=2)

clear_b3=Button(tool_frame,text='Clear',bd=4,bg='grey',command=clear,relief=RIDGE)
clear_b3.grid(row=0,column=2,padx=2)

open_b4=Button(tool_frame,text='Open',bd=4,bg='grey',command=open_file,relief=RIDGE)
open_b4.grid(row=0,column=3,padx=2)

brush_b5=Button(tool_frame,text='Brush',bd=4,bg='grey',command=brush_button_pressed,relief=RIDGE)
brush_b5.grid(row=1,column=0,padx=2)

magni_b6=Button(tool_frame,text='Magnifier',bd=4,bg='grey',command=magnifier,relief=RIDGE)
magni_b6.grid(row=1,column=1,padx=2)

undo_b7=Button(tool_frame,text='Demagnifier',bd=4,bg='grey',command=unmagnifier,relief=RIDGE)
undo_b7.grid(row=1,column=2,padx=2)

redo_b8=Button(tool_frame,text='CP',bd=4,bg='grey',command=clrPickPressed,relief=RIDGE)
redo_b8.grid(row=1,column=3,padx=2)

select_b9=Button(tool_frame,text='Selection',bd=4,bg='grey',command=start_selection,relief=RIDGE)
select_b9.grid(row=0,column=4,padx=2)

move_b10=Button(tool_frame,text='Move',bd=4,bg='grey',command=move_selection,relief=RIDGE)
move_b10.grid(row=0,column=5,padx=2)

cut_b11=Button(tool_frame,text='Cut',bd=4,bg='grey',command=None,relief=RIDGE)
cut_b11.grid(row=1,column=4,padx=2)

copy_b12=Button(tool_frame,text='Copy',bd=4,bg='grey',command=None,relief=RIDGE)
copy_b12.grid(row=1,column=5,padx=2)

flood_b13=Button(tool_frame,text='Flood',bd=4,bg='grey',command=pressed_fill,relief=RIDGE)
flood_b13.grid(row=0,column=6,padx=2)
#Shapes Button
circle_b1=Button(shape_frame,text='Circle',bd=4,bg='grey',command=circle_pressed,relief=RIDGE)
circle_b1.grid(row=0,column=1,padx=2)

triangle_b2=Button(shape_frame,text='Triangle',bd=4,bg='grey',command=tri_pressed,relief=RIDGE)
triangle_b2.grid(row=0,column=2,padx=2)

rectangle_b3=Button(shape_frame,text='Rectangle',bd=4,bg='grey',command=Rectangle_pressed,relief=RIDGE)
rectangle_b3.grid(row=0,column=3,padx=2)

square_b4=Button(shape_frame,text='Square',bd=4,bg='grey',command=Square_pressed,relief=RIDGE)
square_b4.grid(row=1,column=1,padx=2)

pentagon_b6=Button(shape_frame,text='Pentagon',bd=4,bg='grey',command=Penta_pressed,relief=RIDGE)
pentagon_b6.grid(row=1,column=2,padx=2)

hexagon_b6=Button(shape_frame,text='Hexagon',bd=4,bg='grey',command=hexa_pressed,relief=RIDGE)
hexagon_b6.grid(row=1,column=3,padx=2)

line_b7=Button(shape_frame,text='Line',bd=4,bg='grey',command=line_pressed,relief=RIDGE,height=1,width=3)
line_b7.grid(row=0,column=4,padx=2)

bezier_b8=Button(shape_frame,text='Bezier',bd=4,bg='grey',command=Bezier_pressed,relief=RIDGE,height=1,width=3)
bezier_b8.grid(row=1,column=4,padx=2)

Arc_b9=Button(shape_frame,text='Semi',bd=4,bg='grey',command=Arc_pressed,relief=RIDGE)
Arc_b9.grid(row=0,column=5,padx=2)

star_b10=Button(shape_frame,text='Star',bd=4,bg='grey',command=star_button_pressed,relief=RIDGE)
star_b10.grid(row=1,column=5,padx=2)

oval_b11=Button(shape_frame,text='Oval',bd=4,bg='grey',command=oval_button_pressed,relief=RIDGE)
oval_b11.grid(row=0,column=6,padx=2)

npoly_b12=Button(shape_frame,text='N-poly',bd=4,bg='grey',command=pressedPolygon,relief=RIDGE)
npoly_b12.grid(row=1,column=6,padx=2)

#
#canvas
frame2=Frame(main)
frame2.pack(expand=True,fill=BOTH)
canvas=Canvas(frame2,width=600,height=600,bg='white')
canvas.place(x=5,y=5)
canvas.bind('<B1-Motion>',line)
canvas.bind('<Button-1>',com)
canvas.bind("<MouseWheel>",zoom)
main.mainloop()