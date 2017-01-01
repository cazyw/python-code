#######################################################
# Python Project 1 - backup script
# Updated: 04/04/2016
# Created in order to assist with backing up files
# Options:
# 1. get list of files from source folder
# 2. compare files between source and destination and
#    flag those new/updated
# 3. copy new/update files from source to destination
# 
# Using Python 3
# 
#######################################################

import os
import string
import re
import shutil
import time
from datetime import date
from tkinter import *
from tkinter import filedialog


# Class for the Global Variables

class GlobalVar():
  def __init__(self):
    self.OLD_FOLDER = r""
    self.NEW_FOLDER = r""
    self.num_files = 0
    self.num_copied = 0
    self.TIME_NOW = time.time()
    self.TIME_NOW_S = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(self.TIME_NOW))
    self.OLD_LOGFILE = ""
    self.NEW_LOGFILE = ""

  # create the log file name based on timestamp

  def create_log(self):
    # logFile of copy program
    if not os.path.exists("copy_logs"):
      os.makedirs("copy_logs")

    self.TIME_NOW = time.time()
    self.TIME_NOW_S = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime(self.TIME_NOW))
    self.OLD_LOGFILE = os.path.join("copy_logs", self.TIME_NOW_S + "-logFile-SRC" + ".txt")
    self.NEW_LOGFILE = os.path.join("copy_logs", self.TIME_NOW_S + "-logFile-DST" + ".txt")

  # get and set the old and new folder path

  def get_old_folder(self):
    return self.OLD_FOLDER

  def get_new_folder(self):
    return self.NEW_FOLDER

  def set_old_folder(self, old_f):
    self.OLD_FOLDER = old_f

  def set_new_folder(self, new_f):
    self.NEW_FOLDER = new_f

  # get the copy log files

  def get_old_log(self):
    return self.OLD_LOGFILE

  def get_new_log(self):
    return self.NEW_LOGFILE

  # get and increment the number of files
  # and the number of files copied
  # and also resets the value to zero

  def get_num_files(self):
    return self.num_files

  def get_num_copied(self):
    return self.num_copied

  def add_num_files(self):
    self.num_files += 1

  def add_num_copied(self):
    self.num_copied += 1

  def reset_num_files(self):
    self.num_files = 0

  def reset_num_copied(self):
    self.num_copied = 0



# Class for the GUI to display the program
# Inputs old and new folder and gives the option to
# 1. list the files in the old folder
# 2. compare files in old and new folder
# 3. copy new files from old to new folder

class Application(Frame):
  def __init__(self, master):
    Frame.__init__(self, master)
    self.pack(fill=BOTH, expand=1)

    self.columnconfigure(0, pad=5, weight=1)
    self.columnconfigure(1, pad=5, weight=3)
    self.columnconfigure(2, pad=5, weight=1)
    self.columnconfigure(3, pad=5, weight=1)
    self.columnconfigure(4, pad=5, weight=1)
    self.rowconfigure(0, pad=5, weight=1)
    self.rowconfigure(1, pad=5, weight=1)
    self.rowconfigure(2, pad=5, weight=1)
    self.rowconfigure(3, pad=5, weight=1)
    self.rowconfigure(4, pad=5, weight=1)
    self.rowconfigure(5, pad=5, weight=1)

    lbl = Label(self, text="Program to list, compare and copy files")
    lbl.grid(row = 0, sticky=W, columnspan=4)

    self.b_exit = self.create_button("exit", 5, 3, "")
    self.b_exit = self.set_button("exit")
    self.create_labels("Enter source folder path:", 1, 0, "W")
    self.create_labels("Should be format C:...\...\...", 2, 0, "W")
    self.src = self.create_entry(50, 1, 1, 3, "W")
    self.src.insert(INSERT, r"C:\Users\Caz\Documents" )
    self.create_labels("Enter destination folder path:", 3, 0, "W")
    self.dst = self.create_entry(50, 3, 1, 3, "W")
    self.dst.insert(INSERT, r"G:\Caz_full_files\Caz\Documents" )

    self.lbl_warn = Label(self, text="")
    self.lbl_warn.grid(row = 4, sticky=W, columnspan=5)

    self.b_list = self.create_button("Print: List", 5, 0, "")
    self.b_list = self.set_button("button_list")
    self.b_compare = self.create_button("Print: Compare", 5, 1, "")
    self.b_compare = self.set_button("button_compare")
    self.b_copy = self.create_button("Print: Copy", 5, 2, "")
    self.b_copy = self.set_button("button_copy")
    self.b_src = self.create_button("..", 1, 4, "")
    self.b_src = self.set_button("src directory")
    self.b_dst = self.create_button("..", 3, 4, "")
    self.b_dst = self.set_button("dst directory")

    # defining options for opening a directory
    self.dir_opt = options = {}
    options['initialdir'] = 'C:\\'
    options['mustexist'] = False
    options['parent'] = root
    options['title'] = 'This is a title'

  def create_button(self, button_text, rowx, coly, stick):
    self.button = Button(self, text = button_text)
    self.button.grid(row = rowx, column = coly, sticky = stick, ipadx=10, padx=10)

  def create_labels(self, display, rowx, coly, stick):
    self.instruction = Label(self, text = display)
    self.instruction.grid(row = rowx, column = coly, sticky = stick)

  def create_entry(self, box_width, rowx, coly, colspan, stick):
    self.input = Entry(self, width = box_width)
    self.input.grid(row = rowx, column = coly, columnspan = colspan, sticky = stick)
    return self.input


  def set_button(self, button_type):
    if button_type == "button_list":
        self.button["command"] = self.button_list
    if button_type == "button_compare":
      self.button["command"] = self.button_compare
    if button_type == "button_copy":
      self.button["command"] = self.button_copy
    if button_type == "exit":
      self.button["command"] = self.quit
    if button_type == "src directory":
      self.button["command"] = self.askdirectory_src
    if button_type == "dst directory":
      self.button["command"] = self.askdirectory_dst

  def button_copy(self):
    copy_files()

  
  def button_print(self):
    print ("hello")

  def button_list(self):
    global global_var
    global_var.set_old_folder(self.src.get())
    global_var.set_new_folder(self.dst.get())
    list_files()

  def button_compare(self):
    global global_var
    global_var.set_old_folder(self.src.get())
    global_var.set_new_folder(self.dst.get())
    compare_files()

  def button_copy(self):
    global global_var
    global_var.set_old_folder(self.src.get())
    global_var.set_new_folder(self.dst.get())
    copy_files()

  def update_label(self, update_text):
    self.lbl_warn["text"] = update_text

  def askdirectory_src(self):
    self.src.delete(0, END)
    self.src.insert(0, filedialog.askdirectory(**self.dir_opt).replace("/","\\"))

  def askdirectory_dst(self):
    self.dst.delete(0, END)
    self.dst.insert(0, filedialog.askdirectory(**self.dir_opt).replace("/","\\"))



# gets the modified time and returns as
# float - time since epoch
# string - formatted time
def get_mod_time(full_path):
  modified_t = os.path.getmtime(full_path)
  modified_t_str = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(modified_t))
  return modified_t, modified_t_str


# print (starting header depending on option selected:
#    1. list files in src
#    2. Copy files from src to dest
def print_header(num_logs):
  global global_var

  global_var.create_log()
  global_var.reset_num_files()
  global_var.reset_num_copied()

  print(50*"=")
  if num_logs == "list":
    print ("PROGRAM: LIST FILES IN SOURCE")

  if num_logs == "comp":
    print ("PROGRAM: COMPARE SOURCE WITH DESTINATION")

  if num_logs == "copy":
    print ("PROGRAM: COPY FILES FROM SOURCE TO DESTINATION")

  print (15*"-")
  print ("source:", os.path.abspath(global_var.get_old_folder()))

  if num_logs == "comp" or num_logs == "copy":
    print ("target:", os.path.abspath(global_var.get_new_folder()))

  print ("source logfile:", global_var.get_old_log())

  if num_logs == "copy":
    print ("target logfile:", global_var.get_new_log())
  print (50*"=")

  sys.stdout.flush()


# print (footer depending on option selected:
#    1. list number of files in src
#    2. ALso list number of files copied
def print_footer(num_logs):
  global global_var

  print (15*"-")
  print ("Files:", global_var.get_num_files())

  if num_logs == "comp":
    print ("Files to copy:", global_var.get_num_copied())

  if num_logs == "copy":
    print ("Files copied:", global_var.get_num_copied())
  print (50*"=")

  sys.stdout.flush()



# open logs
def open_logs(num_logs):
  global global_var, source_log, target_log

  source_log = open(global_var.get_old_log(),'w+')
  source_log.write(50*"=" + "\n")

  if num_logs == "list":
    source_log.write("PROGRAM: LIST FILES IN SOURCE FOLDER\n")

  if num_logs == "comp":
    source_log.write("PROGRAM: LIST FILES IN SOURCE FOLDER (* denotes new file to copy)\n")
  
  if num_logs == "copy":
    source_log.write("PROGRAM: LIST FILES IN SOURCE FOLDER (* denotes new file to copy)\n")
    
    target_log = open(global_var.get_new_log(),'w+')
    target_log.write(50*"=" + "\n")
    target_log.write("PROGRAM: FILES COPIED FROM SOURCE (* denotes new file to copy)\n")
    target_log.write("Source: " + os.path.abspath(global_var.get_old_folder())+"\n")
    target_log.write("Target: " + os.path.abspath(global_var.get_new_folder())+"\n")
    target_log.write(50*"=" + "\n")

  source_log.write("Source: " + os.path.abspath(global_var.get_old_folder())+"\n")

  if num_logs == "comp" or num_logs == "copy":
    source_log.write("Target: " + os.path.abspath(global_var.get_new_folder())+"\n")
  source_log.write(50*"=" + "\n")


# close logs
def close_logs(num_logs):
  global global_var, source_log, target_log
  source_log.write(50*"=" + "\n")
  source_log.write("Files: " + str(global_var.get_num_files()) + "\n")

  if num_logs == "comp":
    source_log.write("New Files: " + str(global_var.get_num_copied()) + "\n")

  if num_logs == "copy":
    source_log.write("Files Copied: " + str(global_var.get_num_copied()) + "\n")

  source_log.write(50*"=" + "\n")
  source_log.close()

  if num_logs == "copy":
    target_log.write(50*"=" + "\n")
    target_log.write("Files Copied: " + str(global_var.get_num_copied()) + "\n")
    target_log.write(50*"=" + "\n")
    target_log.close()


# checks for errors in the source and target directories
def dir_has_error():
  global app, global_var
  # checks that the source folder exists
  if not os.path.exists(global_var.get_old_folder()):
    print ("Source folder '" + global_var.get_old_folder() + "' doesn't exist")
    sys.stdout.flush()
    app.update_label("WARNING: Source folder '" + global_var.get_old_folder() + "' doesn't exist")
    return 1

  if not os.path.exists(global_var.get_new_folder()):
    print ("Destination folder '" + global_var.get_new_folder() + "' doesn't exist")
    sys.stdout.flush()
    app.update_label("WARNING: Destination folder '" + global_var.get_new_folder() + "' doesn't exist")
    return 1

  if global_var.get_new_folder() == "":
    print ("Destination folder has not been completed")
    sys.stdout.flush()
    app.update_label("WARNING: Destination folder has not been completed")
    return 1

  if global_var.get_old_folder() == global_var.get_new_folder():
    print ("The source and destination folders are the same")
    sys.stdout.flush()
    app.update_label("WARNING: Source and destination folders are the same")
    return 1

  return 0


# lists the files in the source directory
def list_files():
  global source_log, app, global_var

  # checks for errors in source and target directory chosen
  if dir_has_error():
    return

  print_header("list")
  open_logs("list")
  app.update_label("")

  # for files in source directory, cycles through the tree
  # and prints and writes a list of the files

  log_text = ""

  for root, dirs, files in os.walk(global_var.get_old_folder()):
    for fname in files:
      
      # old file path
      old_full_path = os.path.join(root, fname)

      # skips files with '$' in the name
      matchObj = re.match( r'.*\$.*', old_full_path, re.I)
      if matchObj:
        break

      global_var.add_num_files()
      m_t, m_t_s = get_mod_time(old_full_path)
      log_text += m_t_s + "\t" + old_full_path +"\n"
      print ("- " + old_full_path)

  sys.stdout.flush()
  source_log.write(log_text)
  close_logs("list")
  print_footer("list")



def compare_files():
  global source_log, global_var

  # checks for errors in source and target directory chosen
  if dir_has_error():
    return

  print_header("comp")
  open_logs("comp")
  app.update_label("")

  # for files in source directory, cycles through the tree
  # and checks to see if it exists in the new directory and if
  # the source file is newer than the destination file
  # if newer or doesn't exist, adds asterisk to file list

  log_text = ""
  log_new_files = ""

  for root, dirs, files in os.walk(global_var.get_old_folder()):
    for fname in files:
      
      #old and new file path
      old_full_path = os.path.join(root, fname)
      new_full_path = os.path.join(str.replace(root,global_var.get_old_folder(),global_var.get_new_folder(), 1), fname)

      # skips files with '$' in the name
      matchObj = re.match( r'.*\$.*', old_full_path, re.I)
      if matchObj:
        break

      global_var.add_num_files()
      m_t, m_t_s = get_mod_time(old_full_path)

      # checks if the file exists in the
      # target location
      if not os.path.exists(new_full_path):
        global_var.add_num_copied()
        log_text += "* " + m_t_s + "\t" + old_full_path +"\n"
        log_new_files += "* " + m_t_s + "\t" + old_full_path +"\n"
        print ("* " + old_full_path)
      
            # if the file already exists, checks
            # if the source file is newer than the
            # target file 
      else:
        new_m_t, new_m_t_s = get_mod_time(new_full_path)
        if (m_t - new_m_t) >  1:
          global_var.add_num_copied()
          log_text += "* " + new_m_t_s + "\t" + old_full_path +"\n"
          log_new_files += "* " + new_m_t_s + "\t" + old_full_path +"\n"
          print ("* " + old_full_path)
        else:
          log_text += "- " + m_t_s + "\t" + old_full_path +"\n"
          print ("- " + old_full_path)

  sys.stdout.flush()
  source_log.write(log_text)
  source_log.write(50*"=" + "\n")
  source_log.write("New Files to Copy\n" + 20*"=" + "\n")
  source_log.write(log_new_files)        
  close_logs("comp")
  print_footer("comp")



# main program to cycle through the source folder (OLD)
# and for each file check in the target folder (NEW): 
# doesn't exist --> copy it
# older than source --> copy it
# writes the old and new files to separate logs
# new: if copied prefix with *
def copy_files():
  global global_var, source_log, target_log

  # checks for errors in source and target directory chosen
  if dir_has_error():
    return

  print_header("copy")
  open_logs("copy")
  app.update_label("")

  src_log_text = ""
  dst_log_text = ""

  for root, dirs, files in os.walk(global_var.get_old_folder()):
    for fname in files:
      
      #old and new file path
      old_full_path = os.path.join(root, fname)
      new_full_path = os.path.join(str.replace(root,global_var.get_old_folder(),global_var.get_new_folder(), 1), fname)

      # skips files with '$' or '.ini' in the name
      matchObj = re.match( r'.*(\$|\.ini).*', old_full_path, re.I)
      if matchObj:
        break

      global_var.add_num_files()

      m_t, m_t_s = get_mod_time(old_full_path)

      # checks if the file exists in the
      # target location
      # > no? --> checks if directories exist
      #     > no? --> creates directories
      #   then copies the file

      if not os.path.exists(new_full_path):
        global_var.add_num_copied()
        if not os.path.exists(os.path.dirname(new_full_path)):
          os.makedirs(os.path.dirname(new_full_path))
          
        shutil.copy2(old_full_path,new_full_path) # copy file and stats
        src_log_text += "* " + m_t_s + "\t" + old_full_path +"\n"
        dst_log_text += "* " + m_t_s + "\t" + new_full_path +"\n"
        print ("* " + old_full_path)
        sys.stdout.flush()
      
      # if the file already exists, checks
      # if the source file is newer than the
      # target file and if so, copies the file
      else:
        new_m_t, new_m_t_s = get_mod_time(new_full_path)
        if (m_t - new_m_t) >  1:
          global_var.add_num_copied()
          shutil.copy2(old_full_path,new_full_path) # copy file and stats
          src_log_text += "* " + m_t_s + "\t" + old_full_path +"\n"
          dst_log_text += "* " + new_m_t_s + "\t" + new_full_path +"\n"
          print ("* " + old_full_path)
          sys.stdout.flush()
        else:
          src_log_text += "- " + m_t_s + "\t" + old_full_path +"\n"
          print ("- " + old_full_path)
          sys.stdout.flush()

  sys.stdout.flush()
  source_log.write(src_log_text)
  source_log.write("New Files to Copy\n" + 20*"=" + "\n")
  source_log.write(dst_log_text)
  target_log.write(dst_log_text)
  close_logs("copy")
  print_footer("copy")

##################################################
# Begin

# Set up the root frame
root = Tk()
root.title("Class Buttons")
root.geometry("500x200")
# # Initialise global variables
global_var = GlobalVar()

# # Initialise GUI
app = Application(root)
root.mainloop()

