# For this application to run it is necessary the the below information is filled as described.
# The names of the students appearing for the exam should be put in a txt file which should be chosen
# in the file dialog box once the script is run. The txt file with test takers' usernames can be placed anywhere.

import os

# Do not modify this parameter
curr_dir = os.getcwd()

# web_url: Specify the root url where the student folders are placed
# For e.g.: web_url = "http://users.fs.cvut.cz/~"
web_url = "http://users.fs.cvut.cz/~"

# answer_folder: The directory where downloaded files are stored
# For e.g.: answer_folder = os.path.join(curr_dir, "Answers")
answer_folder = os.path.join(curr_dir, "Answers")

# tasks_folders: Specify the folders on the web file-system
# where the answer files should be downloaded from.
# For e.g.: tasks_folders = ["Task1", "Task2", "Task3"]
tasks_folders = ["Task1", "Task2", "Task3"]

# rep_dir: The directory where the reports generated regarding
# downloading of the files should be stored.
rep_dir = os.path.join(curr_dir, "Reports")
