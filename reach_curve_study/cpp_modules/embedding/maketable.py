with open("counttable.csv","w") as table:
    table.write("file_number,average,stdev\n")
    with open("counts.txt","r") as file:
        for line in file:
            line_vars=line.strip().split()
            if not line_vars:
                continue
            if "Processing" in line_vars[0]:
                continue
            if not ("e906" in line_vars[0]):
                continue
            nfile=int(line_vars[0][line_vars[0].find("e906/")+5:line_vars[0].find("/embedding")])
            average=float(line_vars[1])
            stdev=float(line_vars[2])
            print(f"{nfile} {average} {stdev}")
            table.write(f"{nfile},{average},{stdev}\n")
