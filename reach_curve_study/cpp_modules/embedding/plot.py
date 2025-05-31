with open("counts.txt","r") as file:
    for line in file:
        line_vars=line.strip().split()
        if not line_vars:
            continue
        if "Processing" in line_vars[0]:
            continue
        if not ("e906" in line_vars[0]):
            continue
        nfile=float(line_vars[0][line_vars[0].find("e906/")+5:line_vars[0].find("/embedding")])
        average=float(line_vars[1])
        stdev=float(line_vars[2])
        print(f"{nfile} {average} {stdev}")
