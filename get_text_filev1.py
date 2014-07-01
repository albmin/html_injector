# IM PRETTY SURE THIS IS THE GOOD METHOD
#This class hunts through the folder that it's placed in, looking for
# .html files that don't contain opening html tags, indicating that
# it is an html file, but is not formatted properly
__author__ = 'Eric'
import subprocess

#driver method that gets the list of files that need html formatting done to them
def driver(path):
    f_list = get_files(path)
    #folder = get_folder_name()
   # print(f_list)
    #print(folder)
    return f_list
def get_folder_name():
    x = (subprocess.Popen('pwd', stdout=subprocess.PIPE)).communicate()
    path = str(x[0])
    path = path.split('/')
    path = (path[-1])
    path = path[0:len(path)-3]
    return path
#get file method, i really don't think there are any other methods that i need

def get_files(path):
    #find the files that are in a folder
    x = (subprocess.Popen(['ls', path], stdout=subprocess.PIPE)).communicate()
    #print(x)
    files = str(x[0])
    files = files[2:len(files)-1]  #THIS LINE IS SCREWING UP THE FIRST LINE OF OUTPUT
    #parse out the file names from the ridiculously large string
    raw_file_list = files.split('\\n')
    file_list = parse_list(raw_file_list)
    #print(file_list)
    return file_list

#method that parses a list of files, looking for the html's
#from here, something happens...
def parse_list(listy):
    files = []
    for i in range(len(listy)):
        file=listy[i]
        file_ext = file[len(file)-5:len(file)]
        if file_ext == '.html':
            cmd = ['head', '-n', '1', file]    # This will pull the first line out of the file to html check
              #THIS IS WHERE THE INDEX OUT OF BOUNDS ERROR IS OCCURRING FROM
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

#driver()
