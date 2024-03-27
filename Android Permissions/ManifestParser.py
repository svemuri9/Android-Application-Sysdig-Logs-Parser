import os
import xml.etree.ElementTree as ET
from collections import defaultdict
import matplotlib.pyplot as plt


def plot_graph(x, y):
    plt.plot(x, y, c='xkcd:darkgreen')

    plt.xlabel('No of Permissions', labelpad=6, fontweight='bold')
    plt.ylabel('No of Applications', labelpad=6, fontweight='bold')
    plt.title('APK Permissions Stats', fontweight='bold')
    plt.show()


def main():
    base = "/Users/adarshsajjan/Downloads/selectedAPKs/"
    base_location = "/Users/adarshsajjan/Downloads/selectedAPKs/APKCode"
    apk_permissions_count = defaultdict(int)
    permission_count = defaultdict(int)
    for apk_name in os.listdir(base_location):
        if apk_name[0] != '.':
            manifest_file_location = os.path.join(base_location, apk_name)
            manifest_file_location = os.path.join(manifest_file_location, "AndroidManifest.xml")
            tree = ET.parse(manifest_file_location)
            root = tree.getroot()
            for item in root.findall('./uses-permission'):
                permission = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                apk_permissions_count[apk_name + ".apk"] += 1
                permission_count[permission] += 1

    apk_permissions_count = sorted(apk_permissions_count.items(), key=lambda x: x[1], reverse=True)
    permission_count = sorted(permission_count.items(), key=lambda x: x[1], reverse=True)

    permissions_file = open(base + "PermissionsCount.txt", "w")
    apk_permissions_count_file = open(base + "ApkPermissionsCount.txt", "w")

    for entry in apk_permissions_count[0:10]:
        apk_permissions_count_file.write(str(entry[0]) + "  -  " + str(entry[1]))
        apk_permissions_count_file.write('\n')
    apk_permissions_count_file.close()

    for entry in permission_count[0:10]:
        permissions_file.write(str(entry[0]) + "  -  " + str(entry[1]))
        permissions_file.write('\n')

    permissions_file.close()
    values_count = defaultdict(int)
    for entry in apk_permissions_count:
        values_count[entry[1]] += 1

    values_count = sorted(values_count.items(), key=lambda x: x[0])

    x_values = []
    y_values = []
    for entry in values_count:
        x_values.append(entry[0])
        y_values.append(entry[1])

    plot_graph(x_values, y_values)


if __name__ == "__main__":
    main()
