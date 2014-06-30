__author__ = 'albmin'
import subprocess
import os
import main_html
import time
#method which controls the recursion and filewriting
def driver(path):
   # path = get_dir_path()
    print('CURR PATH')
    print(path)
    #call the main_html driver method to inject html into current folder
    main_html.driver()
    sub = get_subs(path)
    #print(sub)
    #step through the subdirectories, moving the files and changing the folder_hunter copies name to the original
    for i in range(len(sub)):
        new_path = path
        new_path += '/'
        new_path += sub[i]
        new_path += '/folder_hunter.py'
        print('Loop:')
        print(sub[i])
        print(new_path)
        #passed in param may be a little sketchy
        move_pys(sub[i])
        #call folder_hunter.py in order to write html and further recursion
        args = ['python3', new_path]
        print('RECURSE')
        print('BORK')
        print(args)
        subprocess.call(args)
        # print('TEST')
        # print(subprocess.Popen(['python3', new_path+= '.get_dir_path()']))
        #may want to add an error checker for stderr or stdout to make sure the method works properly
        #time.sleep(10)
        del_pys(sub[i])
    return 0


def move_pys(sub):
    #probably need to add error checks here too
    #im using move because it should cut down on rewrite/write resources
    #could probably loop this later, but also i should probably multithread this whole thing too
    #print(subprocess.Popen('pwd', stdout=subprocess.PIPE).communicate())
    print('MOVE PYS')
    print(sub)
    args = ['cp', 'get_text_filev1.py', sub]
    subprocess.Popen(args)
    args[1] = 'main_html.py'
    subprocess.Popen(args)
    args[1] = 'nav_bar.py'
    subprocess.Popen(args)
    args[1] = '__init__.py'
    subprocess.Popen(args)
    #this one does need copied though
    temp = sub
    temp += '/folder_hunter.py'
    args = ['cp', 'folder_hunter_cp.py', temp]
    subprocess.Popen(args)
    cp_temp = sub
    cp_temp += '/folder_hunter_cp.py'
    args = ['cp', 'folder_hunter_cp.py', cp_temp]
    subprocess.Popen(args)
    #print('FILES')
    #print(sub)
    #print(subprocess.Popen(['ls', sub]).communicate())
    return 0


def del_pys(sub):
    print('GAHHH')
    file = sub
    file += '/get_text_filev1.py'
    args = ['rm', file ]
    subprocess.Popen(args)
    file = sub
    file += '/main_html.py'
    args[1] = file
    print(args)
    subprocess.Popen(args)
    file = sub
    file += '/nav_bar.py'
    args[1]= file
    #args[1] = 'nav_bar.py'
    subprocess.Popen(args)
    file = sub
    file += '/folder_hunter.py'
    args = ['rm', file]
    subprocess.Popen(args)
    file = sub
    file += '/folder_hunter_cp.py'
    args = ['rm', file]
    subprocess.Popen(args)
    file = sub
    file += '/__init__.py'
    args = ['rm', file]
    subprocess.Popen(args)
    #this one does need copied though
    # file = sub
    # file += '/folder_hunter.py'
    # args[1] = file
    # subprocess.Popen(args)
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

#print('FACHK')
#print(get_subs(get_dir_path()))
driver(get_dir_path())