import csv
import os
import xml.etree.ElementTree as ET
from pathlib import Path


def createCSVFile(rows):
    with open('/Users/adarshsajjan/Desktop/permission.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main():
    adware_location = "/Users/adarshsajjan/Downloads/Adware/APKCode"
    benign_location = "/Users/adarshsajjan/Downloads/benign/APKCode"
    malware_location = "/Users/adarshsajjan/Downloads/malware/APKCode"
    ransomware_location = "/Users/adarshsajjan/Downloads/Ransomware/APKCode"

    headers = ["applicationName", "applicationType", "permission"]
    rows = [headers]
    for apk_name in os.listdir(benign_location):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(benign_location, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                row = ["0"] * 3
                row[0] = apk_name + ".apk"
                for item in root.findall('./permission'):
                    row[2] = "1"

                rows.append(row)

    for apk_name in os.listdir(malware_location):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(malware_location, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                row = ["0"] * 3
                row[1] = "1"
                row[0] = apk_name + ".apk"
                for item in root.findall('./permission'):
                    row[2] = "1"

                rows.append(row)

    for apk_name in os.listdir(adware_location):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(adware_location, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                row = ["0"] * 3
                row[1] = "1"
                row[0] = apk_name + ".apk"
                for item in root.findall('./permission'):
                    row[2] = "1"

                rows.append(row)

    for apk_name in os.listdir(ransomware_location):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(ransomware_location, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                row = ["0"] * 3
                row[1] = "1"
                row[0] = apk_name + ".apk"
                for item in root.findall('./permission'):
                    row[2] = "1"

                rows.append(row)

    print(len(rows))
    createCSVFile(rows)


if __name__ == "__main__":
    main()
