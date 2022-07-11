import re

f = open("input.srt", 'r')
lines = f.readlines()

new_lines = []

for line in lines:
    m = re.match(r"\d\d:\d\d:\d\d,\d\d\d --> \d\d:\d\d:\d\d,\d\d\d\n", line)
        if m:
            l = list(m.group(0))
            min1=int(m.group(0)[3:5])
            sec1=int(m.group(0)[6:8])
            min2=int(m.group(0)[20:22])
            sec2=int(m.group(0)[23:25])
            new_sec1 = (sec1 + 37) % 60
            new_min1 = min1 + (sec1 + 37) // 60
            new_sec2 = (sec2+37)%60
            new_min2 = min2 + (sec2 + 37) // 60
            l[3] = str(new_min1 // 10)
            l[4] = str(new_min1 % 10)
            l[6] = str(new_sec1 // 10)
            l[7] = str(new_sec1 % 10)
            l[20] = str(new_min2 // 10)
            l[21] = str(new_min2 % 10)
            l[23] = str(new_sec2 // 10)
            l[24] = str(new_sec2 % 10)
            new_lines.append("".join(l))
        else:
            new_lines.append(line)

f = open("output.srt", 'w')
f.writelines(new_lines)
f.close()
