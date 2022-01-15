from get_filenames import get_filenames

# build dictionary of NERs
# extract most common NERs
# expects list strings
def build_dict(ners: list):
    outer_dict = {}
    for ner in ners:
        splitup = ner.split(" ", 1)
        entity_type = splitup[0]
        entity_name = splitup[1]
        if entity_type in outer_dict:
            if entity_name in outer_dict[entity_type]:
                outer_dict[entity_type][entity_name] += 1
            else:
                outer_dict[entity_type][entity_name] = 1
        else:
            outer_dict[entity_type] = {
                entity_name: 1
            }
    return outer_dict

# return most common entities after building the NERS out
def most_common(ners: list):
    _dict = build_dict(ners)
    mosts = {}
    for ner_type in _dict:
        sorted_types = sorted(_dict[ner_type], key=lambda x: _dict[ner_type][x], reverse=True)
        mosts[ner_type] = sorted_types[0]
    return mosts

def ner_processing():
    filenames = get_filenames()
    for filename in filenames:
        with open(f"./ners/{filename}.txt", "r") as f:
            entries = f.read()
        entries = entries.split('\n')
        while '' in entries:
            entries.remove('')
        print(filename)
        mce = most_common(entries)
        with open(f"./ners/{filename}_most_common.txt", "w") as f:
            for ner in mce.items():
                f.write(ner[0] + " " + ner[1] + '\n')
                
ner_processing()
    