__author__ = 'Eric'

#This is a method to implement a navigation bar, which is required on every visible
#page. To be implemented in the html_injector directory and called upon from the
# main_html file



def insert_nav_bar(folder_name):
    temp = []
    main_div='    <div class="nav_bar">\n'
    div = '     <div class="'
    div += str(determine_link(folder_name))
    div += '">\n'
    li1= '<li><a href="index.html" class="homeLink">Home</a></li>\n'
    li2= '<li><a href="about.html" class="aboutLink">About Us</a></li>\n'
    li3 = '<li><a href="projects.html" class="projectLink">Projects</a></li>\n'
    li4 = '<li><a href="/eric/blog.html" class="blogLink">Blog</a></li>\n'
    li5 = '<li><a href="/ops/comment.html" class="commentLink">Feedback</a></li>\n'
    li6 = '<li><a href="/ops/links.html" class="linksLink">Links</a></li>\n'
    cl_div = '</div>\n'
    temp=[main_div, div, li1,li2,li3,li4,li5,li6,cl_div,cl_div]
    return temp
# This doesn't have the underline in it like it should, stupid firefox screws it up

#this method needs revised as to where it takes in the parameter of a list which contains
#the links that are put into the nav_bar, but I want to be lazy right now and just copypaste

#this method determines the link that will be used on the navigation bar from the folder name
#THIS METHOD MUST BE UPDATED WHEN THE NAV BAR IS!!
#RETURN: a string which is the link
def determine_link(folder):
    if folder == 'eric':
        return 'blogLink'
    if folder =='about':
        return 'aboutLink'
    if folder == 'ops':
        return 'commentLink'
    if folder =='links':
        return 'linksLink'
    if folder == 'www':
        return 'homeLink'
    if folder =='projects':
        return 'projectLink'

#DEBUG CODE
#x=insert_nav_bar('test')
#print(x)