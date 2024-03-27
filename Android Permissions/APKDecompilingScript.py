import os


def main():
    password = input("Enter the Password: ")
    folder_path = "/Users/adarshsajjan/Downloads/selectedAPKs"
    for (root, dirs, files) in os.walk(folder_path):
        for file in files:
            apk_file_location = os.path.join(root, file)
            apk_dir = file[:-4]
            output_location = os.path.join(root, "APKCode")
            output_location = os.path.join(output_location, apk_dir)
            command = "echo {} | sudo -S apktool d -o {} {}".format(password, output_location,
                                                                                   apk_file_location)
            print(command)
            os.system(command)


if __name__ == "__main__":
    main()
