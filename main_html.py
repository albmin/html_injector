__author__ = 'Eric'
import os
#this appends the head and body tags to a file
#MAIN METHOD


def inject_html(file_name, pure_text):
    raw = []  #GLOBAL variable for storing the data of the text file
    raw.append(insert_header(file_name))  #method call for header text, takes in the file_name
    #read in the file and store each line as a list (nested list prolly not necessary)
    with open(file_name)as f:
        for line in f:
            raw.append([line])  #lines will be read in one at a time
            raw.append('<br>\n')
    # raw[0] is where the header information is from the insert_header tags are
    # the rest of the list holds the text
    insert_body(raw)
    print(raw)  #visual debugging
    print(raw[1:len(raw)])

#if pure text, insert the <p> tags around it


    file = open('test.html', 'w')
##Code to write back into the file
    for i in range(len(raw)):
        for j in range(len(raw[i])):
            file.write(raw[i][j])

#method for inserting the doctype, meta tags, opening html, title, and head
# takes in the file_name to attach as the title
def insert_header(fname):
    temp = []  #holder to insert the header information into, appended then to raw
    doc_type = '<!doctype.html>\n'
    meta_1 = '<meta http-equiv="X-UA-Compatible" content = "IE-edge"/>\n'
    meta_2 = '<meta charset="utf-8">\n'
    html = '<html>\n'
    head = ' <head>\n'
    title = '  <title>\n'
    f_name = fname + '\n'
    cl_title = '  </title>\n'
    css = '<link href = "/styles.css" rel="stylesheet" type="text/css">\n'  #css link !!MAY NEED REVISED!!
    cl_head = ' </head>\n'
    #now append all the elements to the list, and return it
    temp = [doc_type, meta_1, meta_2, html, head, title, f_name, cl_title, css, cl_head]
    return temp

#Method in order to insert the body tags and the following closing html tag
def insert_body(text):
    body = ' <body>\n'
    nav = nav_bar()
    paragraph =  '  <p>\n'
    cl_paragraph = '  </p>\n'
    cl_body = ' </body>\n'
    cl_html = '</html>'
    bod = [body, paragraph]
    cl_bod = [cl_paragraph, cl_body, cl_html]
    text.insert(1, body)
    text.insert(2, nav)
    text.insert(3, paragraph)
    text.insert(len(text), cl_bod)
    #text.append('</html>\n')
inject_html('blog_4.html', None)

#NEED TO DO SOMETHING ABOUT TITLE TEXT, POSSIBLE PROMPT, BUT FOR NOW PARSE OUT THE .HTML PART