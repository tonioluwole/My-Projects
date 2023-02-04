import sys
import PIL.Image
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
img1 = PIL.Image.open(root.filename) #returns file path
print (img1)

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
img2 = PIL.Image.open(root.filename) #returns file path
print (img2)

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
img3 = PIL.Image.open(root.filename) #returns file path
print (img3)

def horizontal_join():
    img = PIL.Image.new('RGB', (img1.width + img2.width, img1.height))
    img.paste(img1, (0, 0))
    img.paste(img2, (img1.width, 0))
    return img

def vertical_join():
    img = PIL.Image.new('RGB', (img1.width + img1.width, img2.height))
    img.paste(img1, (0, 0))
    img.paste(img2, (0,img1.height))
    return img
    

choice = input("Horizontal join - 1\n"+
               "Vertical join - 2\n\n") 
choice = int(choice)

if choice == 1:
    horizontal_join().save('test2.jpg')

if choice == 2:
    vertical_join().save('test3jpg')