import subprocess
import fileinput
from time import sleep
from tkinter import *
from tkinter.filedialog import askopenfilename

def menu():
    menu_item = input('''

    MENU [1]
    MENU [2]
    MENU [3]

    ''')



def file_name():
    global file_name
    root = Tk()
    # file_name = input("""
    # Copy your file at the same location as the LF_converter.exe
    # Enter the markdown file name
    # without the extension (e.x. 'my_code_file')
    # >>> """)
    the_label = Label(root, text = "This is Label")

    file_name = askopenfilename(title = "Choose a file")

    Button(text = 'File Open', command = file_name).pack(fill = X)


    the_label.pack()
    file_name.pack()
    root.mainloop()

    return file_name



def to_rst():
    make_dir = "mkdir rst"
    cmd_to_rst = ("pandoc %s.md -f markdown_strict  -s -o rst\%s.rst" %(file_name, file_name))
    cmds = [make_dir, cmd_to_rst]

    for cmd in cmds:
        subprocess.call(cmd , shell = True)
    print("rst file ready")
    print("Adding text highlighting...")
    sleep(1)


def update_rst():
    file_rst = "rst\%s.rst" % file_name
    f1 = open(file_rst, 'r+')

    for line in fileinput.FileInput(file_rst):
        line = line.replace('::', '.. code:: java')

        f1.write(line, )
    f1.close()

    print("rst file updated")


def update_css():
    while True:
        ask = input("Do you want to create a html file?? Y/N ")
        if ask == 'Y':
            break
        elif ask == 'N':
            input('Pres Enter to exit... ')
            exit(1)
        else:
            "please answer with 'Y' or 'N' (Yes or No) "
            continue

    make_dir = ("mkdir html")
    cmd_to_html = ("pandoc rst\%s.rst  -s -o html\%s.html" %(file_name, file_name))

    cmds = [make_dir, cmd_to_html]
    for cmd in cmds:
        subprocess.call(cmd, shell = True)
    print("html File ready")
    print("Updating CSS...")
    sleep(2)
    file = "html\%s.html" %file_name
    # the "r" before the path is for the \ escape character, or unicode
    f1 = open(file, 'r+')

    for line in fileinput.FileInput(file):
        line = line.replace('div.sourceCode { overflow-x: auto; }', '''div.sourceCode { overflow-x: auto; display: inline-block;
                             background-color: #efefef;
                             padding:0.2em 2em;
                             border-radius: 5px;
                             margin-left:3em;}''')

        f1.write(line, )
    f1.close()

    print("CSS Updated")
    input("press Enter to exit... ")


if __name__ == "__main__":
    file_name()
#    mainloop()
    # to_rst()
    # update_rst()
    # update_css()
