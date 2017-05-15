from __future__ import print_function
from scrapper import *
import os
import config_file


def main():
    """Entry point to the script

    This function does the following:
    a. calls the file_download function to download the files from a web location
    b. Checks for plagiarism
    c. generates success report
    """
    import datetime

    try:
        test_takers_list = test_takers()
        print(test_takers_list)

        if not os.path.exists(config_file.rep_dir):
            os.mkdir(config_file.rep_dir)

        ans_folder_name = config_file.answer_folder + "_" + str(datetime.datetime.now())
        if not os.path.exists(ans_folder_name):
            os.mkdir(ans_folder_name)

        with open(os.path.join(config_file.rep_dir, "report " + str(datetime.datetime.now()) + ".txt"), "w") as report_file:
            report_file.write(" " + "_" * 64 + "\n")
            report_file.write("| Test Taker " + "| Tasks " + "  |                  Status                 |" + "\n")
            report_file.write(" " + "-" * 64 + "\n")
            for test_taker in test_takers_list:
                count = 0
                for tasks_folder in config_file.tasks_folders:
                    count += 1
                    # fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/" + tasks_folder + "/test.docx"
                    # fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/test.docx"
                    fileurl = config_file.web_url + test_taker
                    if file_exists(fileurl):
                        file = file_download(fileurl)
                        if len(file) > 0:

                            dest_usr = os.path.join(ans_folder_name, test_taker)
                            if not os.path.exists(dest_usr):
                                os.mkdir(dest_usr)

                            dest_task = os.path.join(ans_folder_name, test_taker, tasks_folder)
                            if not os.path.exists(dest_task):
                                os.mkdir(dest_task)

                            move_file(file, test_taker, tasks_folder, ans_folder_name)

                            if count == 1:
                                report_file.write(
                                    "|  " + test_taker + "  | " + tasks_folder + "   |      Files successfully downloaded      |" + "\n")
                            else:
                                report_file.write(
                                    "|            | " + tasks_folder + "   |      Files successfully downloaded      |" + "\n")
                    else:
                        if count == 1:
                            report_file.write(
                                "|  " + test_taker + "  | " + tasks_folder + "   |Error while downloading files from server|" + "\n")
                        else:
                            report_file.write(
                                "|            | " + tasks_folder + "   |Error while downloading files from server|" + "\n")
            report_file.write(" " + "-" * 64 + "\n")
            report_file.close()

            dialog_box("Success!", "Run Result")

    except Exception as err:
        dialog_box(err.message)
        raise SystemExit(err.message)

if __name__ == "__main__":
    main()
    # pass
