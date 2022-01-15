import os
from get_filenames import get_filenames

# collect all the separate mcps, ners, polarities, and summaries
filenames = get_filenames()
    
part_filenames = []
for filename in filenames:
    parts = []
    for part_name in os.listdir("./ners"):
        if part_name.startswith(filename+"_"):
            parts.append(part_name)
    parts = sorted(parts, key=len)
    part_filenames.append(parts)

for i, filename in enumerate(filenames):
    # ners
    ners = []
    for part_filename in part_filenames[i]:
        with open(f"./ners/{part_filename}", "r") as f:
            entries = f.read()
            ners.append(entries)
    with open(f"./ners/{filename}.txt", "w") as f:
        for entry in ners:
            f.write(entry)
    
    # mcps
    mcps = []
    for part_filename in part_filenames[i]:
        with open(f"./mcps/{part_filename}", "r") as f:
            entries = f.read()
            mcps.append(entries)
    with open(f"./mcps/{filename}.txt", "w") as f:
        for entry in mcps:
            f.write(entry)
    
    # polarities
    polarities = []
    for part_filename in part_filenames[i]:
        with open(f"./polarities/{part_filename}", "r") as f:
            entries = f.read()
            polarities.append(entries)
    with open(f"./polarities/{filename}.txt", "w") as f:
        for entry in polarities:
            f.write(entry + '\n')
            
    # summaries
    summaries = []
    for part_filename in part_filenames[i]:
        with open(f"./summaries/{part_filename}", "r") as f:
            entries = f.read()
            summaries.append(entries)
    with open(f"./summaries/{filename}.txt", "w") as f:
        for entry in summaries:
            f.write(entry + '\n')