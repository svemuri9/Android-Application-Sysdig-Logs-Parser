import os
import xml.etree.ElementTree as ET
import csv
from collections import defaultdict
from pathlib import Path


def create_csv_file(rows):
    with open('/Users/adarshsajjan/Downloads/final_data.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main():
    benign_base = "/Users/adarshsajjan/Downloads/benign/APKCode"
    malware_base = "/Users/adarshsajjan/Downloads/malware/APKCode"

    total_permissions = set()
    benign_permissions_count = defaultdict(int)
    malware_permissions_count = defaultdict(int)
    columns = []
    columns.append("App_Name")
    columns.append("App_Type")
    column_index = 2
    permission_index = defaultdict(int)

    # Calculating Benign Permissions Count Along with Total Permissions
    for apk_name in os.listdir(benign_base):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(benign_base, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                temp = set()
                for entry in root.findall('./uses-permission'):
                    permission = entry.attrib["{http://schemas.android.com/apk/res/android}name"]
                    total_permissions.add(permission)
                    temp.add(permission)
                for i in temp:
                    benign_permissions_count[i] += 1

    # Calculating Malware Permissions Count Along with Total Permissions
    for apk_name in os.listdir(malware_base):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(malware_base, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                temp = set()
                for entry in root.findall('./uses-permission'):
                    permission = entry.attrib["{http://schemas.android.com/apk/res/android}name"]
                    total_permissions.add(permission)
                    temp.add(permission)
                for i in temp:
                    malware_permissions_count[i] += 1

    # Tracking the Column Indexes
    for permission in total_permissions:
        if benign_permissions_count[permission] > 0 and 0 < malware_permissions_count[permission] and \
                malware_permissions_count[permission] < benign_permissions_count[permission]:
            columns.append(permission)
            permission_index[permission] = column_index
            column_index += 1
        elif 0 < benign_permissions_count[permission] and benign_permissions_count[permission] < malware_permissions_count[
            permission] and malware_permissions_count[permission] > 0:
            columns.append(permission)
            permission_index[permission] = column_index
            column_index += 1

    length = len(columns)
    rows = []
    rows.append(columns)

    # Setting Values for Benign Columns
    for apk_name in os.listdir(benign_base):
        if apk_name[0] != '.':
            row = ["0"] * length
            row[0] = apk_name + ".apk"
            manifest_file_location = os.path.join(benign_base, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                for entry in root.findall('./uses-permission'):
                    permission = entry.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if benign_permissions_count[permission] > 0 and 0 < malware_permissions_count[permission] and \
                            malware_permissions_count[permission] < benign_permissions_count[permission]:
                        row[permission_index[permission]] = "1"
                    elif 0 < benign_permissions_count[permission] and benign_permissions_count[permission] < \
                            malware_permissions_count[permission] and malware_permissions_count[permission] > 0:
                        row[permission_index[permission]] = "1"

                rows.append(row)

    # Setting Values for Malware Columns
    for apk_name in os.listdir(malware_base):
        if apk_name[0] != '.':
            row = ["0"] * length
            row[1] = "1"
            row[0] = apk_name + ".apk"
            manifest_file_location = os.path.join(malware_base, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            if Path(manifest_file_location).exists():
                tree = ET.parse(manifest_file_location)
                root = tree.getroot()
                for entry in root.findall('./uses-permission'):
                    permission = entry.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if benign_permissions_count[permission] > 0 and 0 < malware_permissions_count[permission] and \
                            malware_permissions_count[permission] < benign_permissions_count[permission]:
                        row[permission_index[permission]] = "1"
                    elif 0 < benign_permissions_count[permission] and benign_permissions_count[permission] < \
                            malware_permissions_count[permission] and malware_permissions_count[permission] > 0:
                        row[permission_index[permission]] = "1"

                rows.append(row)

    # Calling the "create_csv_file" to generate the CSV File output
    create_csv_file(rows)


if __name__ == "__main__":
    main()
