__author__ = 'Eric'

#SEE LICENSE.txt for this program's licensing

#This class hunts through the folder whos path is passed in, looking for
# .html files that don't contain opening html tags, indicating that
# it is an html file, but is not formatted properly

import subprocess


#main method that gets the list of files that need html formatting done to them
#PARAM -- path of the file
#RETURN -- returns a list of files which need html formatting written in them
def driver(path):
    f_list = get_files(path)
    return f_list


#get file method, method which gets a list of files and then calls a method to
#parse them and find the appropriate ones to inject HTML into
#PARAM -- path which to look in (via subprocess)
#RETURN -- returns the list of files that need parsed
def get_files(path):
    #find the files that are in a folder
    x = (subprocess.Popen(['ls', path], stdout=subprocess.PIPE)).communicate()
    files = str(x[0])
    files = files[2:len(files)-1]
    #parse out the file names from the ridiculously large string
    raw_file_list = files.split('\\n')
    file_list = parse_list(raw_file_list, path)
    return file_list


#method that parses a list of files, looking for the html's, called by get_files()
#PARAM -- list that contains all of the files from get_files()
#RETURN -- returns a list of html files that need formatted with html
def parse_list(listy, path):
    files = []
    for i in range(len(listy)):
        file=path + '/' + listy[i]
        file_ext = file[len(file)-5:len(file)]
        if file_ext == '.html':
            cmd = ['head', '-n', '1', file]    # This will pull the first line out of the file to html check
            x = (subprocess.Popen(cmd, stdout=subprocess.PIPE)).communicate()
            text = str(x[0])
            if text == '<':
                files.append(file)
                continue
            text = text[2:len(files)-1]
            # this may need refined, right now it only checks if '<' exists indicating html
            if len(text)==0:
                files.append(file)
                continue
            if text[0] != '<':
                files.append(file)
    return files


#method to get the folder name of the current directory that this file is
#located in
#PARAM -- None
#RETURN -- string indicating current path
def get_folder_name():
    x = (subprocess.Popen('pwd', stdout=subprocess.PIPE)).communicate()
    path = str(x[0])
    path = path.split('/')
    path = (path[-1])
    path = path[0:len(path)-3]
    return path
