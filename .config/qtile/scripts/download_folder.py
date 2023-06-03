import os
import shutil
# from rich.progress import Progress

home_dir = os.path.expanduser("~")


def file_list(path):
    file_list = []
    for file in os.listdir(path):
        file_name, file_ext = os.path.splitext(file)
        if file_ext == "" or file_ext == ".crdownload":
            continue
        temp = [file_name, file_ext]
        file_list.append(temp)
    return file_list


# path = home_dir + "/Downloads"
path = "/home/mahesh/Downloads/"
# path = input("Enter the file path: ")


def create_folder(ext):
    for i in ext:
        if i[1][1:] in os.listdir(path):
            continue
        else:
            os.mkdir(path + "/" + i[1][1:])


def move(files):
    try:
        for file in files:
            source_file = path + "/" + file[0]+file[1]
            desti_file = path + "/" + file[1][1:]
            if file[1] == ".crdownload":
                continue
            shutil.move(source_file, desti_file)
        # with Progress() as progress:
        #     task = progress.add_task(
        #         f"[cyan]Copying {file[0]+file[1]}...", total=shutil.os.path.getsize(source_file))
        #     shutil.copy2(source_file, desti_file, follow_symlinks=True)
        #     while not progress.finished:
        #         progress.update(
        #             task, completed=shutil.os.path.getsize(desti_file))
    except:
        os.popen("notify-send \"There is some errors\"")


os.popen("notify-send \"Download folder is organized\"")

File_name_list = file_list(path)

create_folder(File_name_list)
move(File_name_list)
