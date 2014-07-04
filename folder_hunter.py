__author__ = 'Eric'

#SEE LICENSE.txt for this program's licensing

import subprocess
import os
import main_html


#main method of class
#PARAM -- path, which is the current path that will be passed into the html injector,
#      --- along with the path/directory to look for additional subdirectories to inject into
#RETURN -- returns 0 if it works, something else if not
def driver(path):
    print(path)
    main_html.driver(path)
    sub = get_subs(path)
    for i in range(len(sub)):
        new_path = path + '/' + sub[i]
        driver(new_path)
    return 0


#method to get the subdirectories of the current folder (path) that is passed in as a parameter
#PARAM -- path in which to look for subdirectories from
#RETURN -- returns a list containing the subdirectories of the current path
def get_subs(path):
    subs = []
    for x, y, z in os.walk(path):
        subs = y
        break
    return subs


#method to return the path which the current directory is located from the subprocess module
#PARAM -- NONE
#RETURN -- returns a string containing the path of the current directory where this file is located
def get_dir_path():
    loc = subprocess.Popen('pwd', stdout=subprocess.PIPE).communicate()
    loc = loc[0]
    loc = str(loc)
    loc = (loc[2:len(loc)-3])
    return loc


driver(get_dir_path())