import cv2
from tkinter import *
from tkinter import messagebox

f = open('camera.cfg', 'r')
c1 = f.readline()
f.close()


def addItem():
    if len(entry1.get()) == 0:
        messagebox.showinfo("Внимание", "Вы не ввели строку подключения")
        return

    cap = cv2.VideoCapture(entry1.get())

    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:

            frame = maintain_aspect_ratio_resize(frame, width=int(entry2.get()))
            cv2.imshow('frame', frame)
            # cv2.moveWindow('frame', 1, 1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyWindow('frame')
                file = open('camera.cfg', 'w')
                file.write(entry1.get())
                file.close()
                break

        else:
            break


# cap = cv2.VideoCapture('rtsp://admin:Admin2018@192.168.0.64/2')


def maintain_aspect_ratio_resize(image, width=None, height=None, inter=cv2.INTER_AREA):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]

    # Return original image if no need to resize
    if width is None and height is None:
        return image

    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the 0idth and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # Return the resized image
    return cv2.resize(image, dim, interpolation=inter)


# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')
# out = cv2.VideoWriter('output.avi', fourcc, 25.0, (1920, 1080))


def setwindow(root):
    root.title("Окно программы")
    root.resizable(False, False)

    w = 400
    h = 250
    ws = root.winfo_screenwidth()
    wh = root.winfo_screenheight()

    x = int(ws / 2 - w / 2)
    y = int(wh / 2 - h / 2)

    # root.geometry("800x600+700+400")
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, x, y))


root = Tk()
setwindow(root)
root.title("Воспроизведение RTSP потока")

label1 = Label(text="Поле ввода", font="Tahoma 12")
label1.pack()
entry1 = Entry(font="Tahoma 12", width=40)
entry1.insert(END, c1)
entry1.pack(anchor=CENTER)
label5 = Label(text="Ширина окна", font="Tahoma 12")
label5.pack()
entry2 = Entry(font="Tahoma 12", width=10, text="1024")
entry2.insert(END, "1024")
entry2.pack(anchor=CENTER)
badd = Button(font="Tahoma 14", text="Открыть поток", command=addItem)
badd.pack()
label4 = Label(text=" ", font="Tahoma 10")
label2 = Label(text="В поле ввода вводится строка подключения к камере, ", font="Tahoma 9")
label3 = Label(text="например - rtsp://Имя пользователя:пароль@IP адрес камеры/2", font="Tahoma 9")
label4.pack()
label2.pack()
label3.pack()

root.mainloop()
