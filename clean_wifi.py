def clean(filename, output_fname):
    cleaned_lines = []
    with open(filename, "r") as f:
        dupl_str = ""
        last_start_time = ""
        for line in f.readlines()[1:]:
            line = line.strip()
            if last_start_time != line.split(",")[0]:
                last_start_time = line.split(",")[0]
                dupl_str = ""
            line = line.replace(dupl_str, "", 1)
            dupl_str += line
            cleaned_lines.append(line)
    with open(output_fname, "w") as f:
        f.write("\n".join(cleaned_lines))


if __name__ == '__main__':
    for fname in ["X_WIFI_1485241623228.csv", "WIFI_1485241620877.csv", "WIFI_1485241170033.csv"]:
        clean(fname, output_fname="C_" + fname)
