from tkinter import *
import hashlib
window = Tk()
window.title('PyEncrypter')

def MD5():
   TEXT['text'] = hashlib.md5(ENTRY.get().encode('utf-8')).hexdigest()

def SHA1():
    TEXT['text'] = hashlib.sha1(ENTRY.get().encode('utf-8')).hexdigest()

def SHA224():
    TEXT['text'] = hashlib.sha224(ENTRY.get().encode('utf-8')).hexdigest()

def SHA256():
    TEXT['text'] = hashlib.sha256(ENTRY.get().encode('utf-8')).hexdigest()

def SHA384():
    TEXT['text'] = hashlib.sha384(ENTRY.get().encode('utf-8')).hexdigest()

def SHA512():
    TEXT['text'] = hashlib.sha512(ENTRY.get().encode('utf-8')).hexdigest()

NEW = Frame()
NEW.pack(side=BOTTOM)

NEW2 = Frame()
NEW2.pack(side=BOTTOM)

ENTRY = Entry()
ENTRY.pack(side=TOP)

TEXT = Label(state='normal')
TEXT.pack()

MD5 = Button(NEW2, text='  MD5  ', command=MD5)
MD5.pack(side=LEFT)

SHA1 = Button(NEW2, text='  SHA1  ', command=SHA1)
SHA1.pack(side=LEFT)

SHA224 = Button(NEW2, text='SHA224', command=SHA224)
SHA224.pack(side=LEFT)

SHA256 = Button(NEW, text='SHA256', command=SHA256)
SHA256.pack(side=LEFT)

SHA384 = Button(NEW, text='SHA384', command=SHA384)
SHA384.pack(side=LEFT)

SHA512 = Button(NEW, text='SHA512', command=SHA512)
SHA512.pack(side=LEFT)


mainloop()
