import tkinter

len_words = 0

def read_file():
    global len_words
    with open('read.txt','r+',encoding = 'utf-8') as fp:
        file_text = fp.read()
    len_words = len(file_text)
    number.set(len_words)
    address.set('read.txt')
    text_t.insert('insert',file_text)

#write file function
def write_file():
    global len_words

    file_txt = write_entry.get()
    len_words = len(file_txt)
    number.set(len_words)
    address.set('write.txt')

    with open('write.txt','w+',encoding = 'utf-8') as fp:
        fp.write(file_txt)

#create the main window
main_window = tkinter.Tk()

#create frames
text_frame = tkinter.Frame(main_window)
top_frame = tkinter.Frame(main_window)
middle_frame = tkinter.Frame(main_window)
address_frame = tkinter.Frame(main_window)
bottom_frame = tkinter.Frame(main_window)

#create and write read widgets
text_t = tkinter.Text(top_frame,width=45, height=5)
text_t.pack()

#create and pack write widgets
write_label = tkinter.Label(top_frame,text = '写入文本：')
write_entry = tkinter.Entry(top_frame,width = 35)

write_label.pack(side = 'left')
write_entry.pack(side = 'left')

#create count and pack widgets
words_label = tkinter.Label(middle_frame,text = '文本字数：')

number = tkinter.StringVar()    #To update number
number_label = tkinter.Label(middle_frame,textvariable = number)

words_label.pack(side = 'left')
number_label.pack(side = 'left')

#create and pack address widgets
address_label = tkinter.Label(address_frame,text = '文本地址：')

address = tkinter.StringVar()    #To update address
add_label = tkinter.Label(address_frame,textvariable = address)

address_label.pack(side = 'left')
add_label.pack(side = 'left')

#create buttons
read_button = tkinter.Button(bottom_frame,text = '读文件',width=15, height=2, command = read_file)
write_button = tkinter.Button(bottom_frame,text = '写文件', width=15, height=2, command = write_file)

read_button.pack(side = 'left')
write_button.pack(side = 'left')

#pack the frames
text_frame.pack()
top_frame.pack()
middle_frame.pack()
address_frame.pack()
bottom_frame.pack()

#start the main loop
tkinter.mainloop()

