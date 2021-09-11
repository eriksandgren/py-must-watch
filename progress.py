#!python
import re
import datetime

def duration_from_line(line):
    h = int(line[1:3])
    m = int(line[4:6])
    s = int(line[7:9])
    return h * (60**2) + m * 60 + s

with open("Readme.md", "r") as f:
    readme = f.read()
durations = re.findall("\[\d{2}:\d{2}:\d{2}\]", readme)
seconds_tot = sum((duration_from_line(l) for l in durations))

print("~~~~ Watched videos ~~~~")
completed_vids = [x.replace("~~", "") for x in re.findall("~~.*~~", readme)]
for vid in completed_vids:
    print(vid, "\n")

seconds_done = sum((duration_from_line(l) for l in durations[:len(completed_vids)]))

print(f"Total videos:   {len(durations)}, total duration:   {datetime.timedelta(seconds=seconds_tot)}")
print(f"Watched videos: {len(completed_vids)}, watched duration: {datetime.timedelta(seconds=seconds_done)}")

print(f"Completion rate (viewing time): {round( 100 * seconds_done / seconds_tot)}%")
print(f"Completion rate (video count):  {round( 100  * len(completed_vids) / len(durations))}%")




