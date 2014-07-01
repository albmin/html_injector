__author__ = 'Eric'
import subprocess
import os
import main_html
#main method
def driver(path):

    main_html.driver(path)
    sub = get_subs(path)
    for i in range(len(sub)):
        new_path = path + '/' + sub[i]
        driver(new_path)
    return 0

#method which takes in the path of a folder and will then look through the subfolders
#and recursively step through, inserting the html_injector files and running them
def get_subs(path):
    subs = []
    for x,y,z in os.walk(path):
        subs = y
        break
    print("SUBS")
    print(subs)
    return subs

#method to return the path which the current directory is located from the subprocess module
def get_dir_path():
    loc = subprocess.Popen('pwd', stdout=subprocess.PIPE).communicate()
    loc = loc[0]
    # print(loc)
    loc = str(loc)
    loc = (loc[2:len(loc)-3])
    print('MOD')
    print(loc)
    return loc

driver(get_dir_path())