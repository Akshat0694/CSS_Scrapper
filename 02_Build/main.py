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

        # creating required directories
        if not os.path.exists(config_file.rep_dir):
            os.mkdir(config_file.rep_dir)

        if not os.path.exists(config_file.answer_folder):
            os.mkdir(config_file.answer_folder)

        ans_folder_name = os.path.join(config_file.answer_folder,  "Answers_" + str(datetime.datetime.now()))
        if not os.path.exists(ans_folder_name):
            os.mkdir(ans_folder_name)

        # downloading answers and working on success report file
        with open(os.path.join(config_file.rep_dir, "report " + str(datetime.datetime.now()) + ".txt"),
                  "w") as report_file:
            report_file.write("_" * 75 + "\n")
            report_file.write(" Test Taker " + "| Tasks " + "  |                 Status                |" + "  File Name  " + "\n")
            report_file.write("-" * 75 + "\n")

            for test_taker in test_takers_list:
                for tasks_folder in config_file.tasks_folders:
                    # fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/" + tasks_folder + "/test.docx"
                    # fileurl = "http://users.fs.cvut.cz/~" + test_taker + "/test.docx"
                    usr_folder = config_file.web_url + test_taker
                    folder_url = config_file.web_url + test_taker + "/" + tasks_folder
                    if file_fldr_exists(usr_folder):
                        folder_name = file_download(folder_url)

                        if folder_name != 0:
                            os.rename(tasks_folder, tasks_folder + ".html")
                            existing_files = filenames_from_html(os.path.join(os.getcwd(), tasks_folder + ".html"))
                            os.remove(os.path.join(os.getcwd(), tasks_folder + ".html"))
                            if len(existing_files) > 0:
                                for file_name in existing_files:
                                    file_url = folder_url + "/" + file_name
                                    file_name = file_download(file_url)

                                    dest_usr = os.path.join(ans_folder_name, test_taker)
                                    if not os.path.exists(dest_usr):
                                        os.mkdir(dest_usr)

                                    dest_task = os.path.join(ans_folder_name, test_taker, tasks_folder)
                                    if not os.path.exists(dest_task):
                                        os.mkdir(dest_task)

                                    move_file(file_name, test_taker, tasks_folder, ans_folder_name)

                                    # Report specific data
                                    success_text_report = "  " + test_taker + "  | " + tasks_folder + " |      Files successfully downloaded      | " + file_name + "\n"
                                    report_file.write(success_text_report)

                            else:
                                # Report specific data
                                no_files_found = "  " + test_taker + "  | " + tasks_folder + " |No files found in the folder to download |" + "\n"
                                report_file.write(no_files_found)

                        else:
                            # Report specific data
                            folder_not_found = "  " + test_taker + "  | " + tasks_folder + " |      Folder named " + tasks_folder + " not found       |" + "\n"
                            report_file.write(folder_not_found)

                    else:
                        # Report specific data
                        error_dwnld_file = "  " + test_taker + "  | " + tasks_folder + " |Can't access url or user folder not found|" + "\n"
                        report_file.write(error_dwnld_file)

                report_file.write(" " + "." * 75 + "\n")
            report_file.write(" " + "-" * 75 + "\n")
            report_file.close()

            dialog_box("Success!", "Run Result")

    except Exception as err:
        dialog_box("Error!" + "\n" + err.message, "Run Result")
        raise SystemExit(err.message)


if __name__ == "__main__":
    main()
    # pass
