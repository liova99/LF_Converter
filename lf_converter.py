import subprocess 
import fileinput

def file_name():
	global file_name
	file_name = input("""Enter the markdown file name
	 without the extension (e.x. 'my_code_file') >>>  """)
	return  file_name

def to_rst():
	cmd_to_rst = ("pandoc " + file_name + ".md -f markdown_strict -s -o " + file_name +".rst")
	print (cmd_to_rst)
	# to rst
	subprocess.call(cmd_to_rst , shell = True)
	print("File ready")


def update_rst():
	file = file_name + ".rst"
	# the "r" before the path is for the \ escape character, or unicode
	f1 = open(file, 'r+')

	for line in fileinput.FileInput(file):
	    line = line.replace('::', '.. code:: java' )

	    f1.write(line,)
	f1.close()    

	print ("rst file updated")


def update_css():
	ask = input ("Do you want to create a html file??  ")

	cmd_to_html = ("pandoc " + file_name + ".rst  -s -o " + file_name +".html")
	print (cmd_to_html)
	# to rst
	subprocess.call(cmd_to_html , shell = True)
	print("html File ready")
	print(" Updating CSS for text hight lighting")



	file = file_name + ".html"
	# the "r" before the path is for the \ escape character, or unicode
	f1 = open(file, 'r+')

	for line in fileinput.FileInput(file):
	    line = line.replace('div.sourceCode { overflow-x: auto; }', '''div.sourceCode { overflow-x: auto; display: inline-block; 
						     background-color: #efefef; 
						     padding:0.2em 2em;
						     border-radius: 5px;
						     margin-left:3em;}''' )

	    f1.write(line,)
	f1.close()    

	print ("CSS Updated")





if __name__ == "__main__":
	file_name()
	to_rst()
	update_rst()
	update_css()
	