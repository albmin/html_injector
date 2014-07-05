__author__ = 'Eric'

#SEE LICENSE.txt for this program's licensing

import get_text_file
import nav_bar


#main method that iterates through the list of unformatted .html files and formats them
#PARAM -- path of the folder to look for unformatted .html files
#RETURN -- 0 if operates correctly, something else if not
def driver(path):
    files = get_text_file.driver(path)
    for i in range(len(files)):
        inject_html(path, files[i])
    return 0


#method to write the html into the file, this method opens the passed in file and then writes
#the necessary html to format the file
#PARAM --path: path of the folder in which the parameter, file_name, can be located
#      --file_name: name of the html file in which this method formats
#RETURN --None, this method writes in the file, no return necessary
def inject_html(path,file_name):
    raw = []  #GLOBAL variable for storing the data of the text file
    raw.append(insert_header(file_name))  #method call for header text, takes in the file_name
    #read in the file and store each line as a list (nested list prolly not necessary)
    file =  file_name
    with open(file)as f:
        for line in f:
            raw.append([line])  #lines will be read in one at a time
            raw.append('<br>\n')
    # raw[0] is where the header information is from the insert_header tags are
    # the rest of the list holds the text
    insert_body(raw)
    f = open(file, 'w')
    #Code to write back into the file
    for i in range(len(raw)):
        for j in range(len(raw[i])):
            f.write(raw[i][j])


#method for inserting the doctype, meta tags, opening html, title, and head
#PARAM -- file name to attach as the title
#RETURN -- list containing all of the opening html to write into the file
def insert_header(fname):
    doc_type = '<!doctype.html>\n'
    meta_1 = '<meta http-equiv="X-UA-Compatible" content = "IE-edge"/>\n'
    meta_2 = '<meta charset="utf-8">\n'
    html = '<html>\n'
    head = ' <head>\n'
    title = '  <title>\n'
    f_name = fname + '\n'
    cl_title = '  </title>\n'
    css = '<link href = "styles.css" rel="stylesheet" type="text/css">\n'  #css link !!MAY NEED REVISED!!
    cl_head = ' </head>\n'
    #now append all the elements to the list, and return it
    return [doc_type, meta_1, meta_2, html, head, title, f_name, cl_title, css, cl_head]


#Method in order to insert the body tags and the following closing html tag
#PARAM --list containing all of the file's text and html from the insert_header method
#      ---this method will append to this list
#RETURN -- None, apparently this method appends to a global variable that is passed in
#       -- not really my best implementation I guess, but supposedly it works...
def insert_body(text):
    body = ' <body>\n'
    nav = nav_bar.insert_nav_bar(get_text_file.get_folder_name())
    for i in range(2):
        nav.append('<br>')
    paragraph =  '  <p>\n'
    cl_paragraph = '  </p>\n'
    cl_body = ' </body>\n'
    cl_html = '</html>'
    header = [' <header> <h1> Telescopium Conscientia </h1>  </header>\n']
    cl_bod = [cl_paragraph, cl_body, cl_html]
    #because the html has to be inserted in particular places, they are appended at certain positions
    #on the list, !! may be able to do this in the previous method? !!
    text.insert(1, body)
    text.insert(2, header)
    text.insert(3, nav)
    text.insert(4, paragraph)
    text.insert(len(text), cl_bod)
