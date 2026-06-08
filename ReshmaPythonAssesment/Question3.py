import re

try:
    file = open("server_log.txt", "r")
    data = file.read()
    lines = file.readlines()
    total_lines = len(lines)
    total_words = len(data.split())
    total_chars = len(data)
    vowels = "aeiouAEIOU"
    total_vowels = 0
    for ch in data:
        if ch in vowels:
            total_vowels += 1
    info = len(re.findall(r"\[INFO\]", data))
    warning = len(re.findall(r"\[WARNING\]", data))
    error = len(re.findall(r"\[ERROR\]", data))
    critical = len(re.findall(r"\[CRITICAL\]", data))
    report = open("log_report.txt", "w")
    report.write("Total Lines : " + str(total_lines) + "\n")
    report.write("Total Words : " + str(total_words) + "\n")
    report.write("Total Chars : " + str(total_chars) + "\n")
    report.write("Total Vowels : " + str(total_vowels) + "\n\n")
    report.write("INFO : " + str(info) + "\n")
    report.write("WARNING : " + str(warning) + "\n")
    report.write("ERROR : " + str(error) + "\n")
    report.write("CRITICAL : " + str(critical) + "\n\n")
except FileNotFoundError:
    print("File not found")