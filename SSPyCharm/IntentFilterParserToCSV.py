import csv
import os
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


def createCSVFile(rows):
    with open('/Users/adarshsajjan/Desktop/intent_filter.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerows(rows)


def main():
    benign_location = "/Users/adarshsajjan/Downloads/benign/APKCode"
    malware_location = "/Users/adarshsajjan/Downloads/malware/APKCode"
    adware_location = "/Users/adarshsajjan/Downloads/Adware/APKCode"
    ransomware_location = "/Users/adarshsajjan/Downloads/Ransomware/APKCode"

    intents_set = set()
    benign_intent_count = defaultdict(int)
    malware_intent_count = defaultdict(int)
    headers = ["applicationName", "applicationType"]

    for apk_name in os.listdir(benign_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(benign_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                cur_intents = set()
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for intent in cur_intents:
                    benign_intent_count[intent] += 1

    for apk_name in os.listdir(malware_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(malware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                cur_intents = set()
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for intent in cur_intents:
                    malware_intent_count[intent] += 1

    for apk_name in os.listdir(adware_location):
        if apk_name[0] != '.':
            manifest_location = os.path.join(adware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                cur_intents = set()
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        intents_set.add(intent)
                        cur_intents.add(intent)

                for intent in cur_intents:
                    malware_intent_count[intent] += 1

    index = 2
    intent_index = defaultdict(int)
    for intent in intents_set:
        headers.append(intent)
        intent_index[intent] = index
        index += 1

    sz = len(headers)
    print(sz)
    rows = []
    rows.append(headers)

    for apk_name in os.listdir(benign_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            manifest_location = os.path.join(benign_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

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
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                rows.append(row)

    for apk_name in os.listdir(adware_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            row[1] = "1"
            manifest_location = os.path.join(adware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")
            if Path(manifest_location).exists():
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                rows.append(row)

    for apk_name in os.listdir(ransomware_location):
        if apk_name[0] != '.':
            row = ["0"] * sz
            row[0] = apk_name + ".apk"
            row[1] = "1"
            manifest_location = os.path.join(ransomware_location, apk_name)
            manifest_location = os.path.join(manifest_location, "AndroidManifest.xml")

            if Path(manifest_location).exists():
                print(manifest_location)
                tree = ET.parse(manifest_location)
                root = tree.getroot()
                for item in root.findall('./application/activity/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/activity-alias/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/service/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/receiver/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                for item in root.findall('./application/provider/intent-filter/action'):
                    intent = item.attrib["{http://schemas.android.com/apk/res/android}name"]
                    if "android.intent" in intent:
                        row[intent_index[intent]] = "1"

                rows.append(row)

    print(headers)
    createCSVFile(rows)


if __name__ == "__main__":
    main()
