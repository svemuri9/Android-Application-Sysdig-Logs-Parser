import csv
import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


def createCSVFile(rows):
    with open('/Users/adarshsajjan/Desktop/uses-permissions.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main():
    benign_location = "/Users/adarshsajjan/Downloads/benign/APKCode"
    malware_location = "/Users/adarshsajjan/Downloads/malware/APKCode"
    adware_location = "/Users/adarshsajjan/Downloads/Adware/APKCode"
    ransomware_location = "/Users/adarshsajjan/Downloads/Ransomware/APKCode"

    permissions_set = set()
    benign_permission_count = defaultdict(int)
    malware_permission_count = defaultdict(int)
    headers = []
    headers.append("applicationName")
    headers.append("applicationType")

    for apk_name in os.listdir(benign_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(benign_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                cur_permissions = set()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    permissions_set.add(permission)
                    cur_permissions.add(permission)
                for permission in cur_permissions:
                    benign_permission_count[permission] += 1

    for apk_name in os.listdir(malware_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(malware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                cur_permissions = set()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    permissions_set.add(permission)
                    cur_permissions.add(permission)
                for permission in cur_permissions:
                    malware_permission_count[permission] += 1

    for apk_name in os.listdir(adware_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(adware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    permissions_set.add(permission)

    for apk_name in os.listdir(ransomware_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(ransomware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    permissions_set.add(permission)

    index = 2
    permission_index = defaultdict(int)
    for permission in permissions_set:
        headers.append(permission)
        permission_index[permission] = index
        index += 1

    sz = len(headers)
    print(sz)
    rows = [headers]

    for apk_name in os.listdir(benign_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            manifest_location = os.path.join(benign_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    row[permission_index[permission]] = "1"
                rows.append(row)

    for apk_name in os.listdir(malware_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            row[1] = "1"
            manifest_location = os.path.join(malware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    row[permission_index[permission]] = "1"
                rows.append(row)

    for apk_name in os.listdir(adware_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            row[1] = "1"
            manifest_location = os.path.join(adware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            print(manifest_location)
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    row[permission_index[permission]] = "1"
                rows.append(row)

    for apk_name in os.listdir(ransomware_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            row[1] = "1"
            manifest_location = os.path.join(ransomware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            print(manifest_location)
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./uses-permission'):
                    permission = item.attrib["{http://schemas.android.com/apk/res/android}name"].split('.')[-1]
                    row[permission_index[permission]] = "1"
                rows.append(row)

    print(headers)
    createCSVFile(rows)


if __name__ == "__main__":
    main()
