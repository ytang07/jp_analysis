from get_filenames import get_filenames

def avg(_list):
    return sum(_list)/len(_list)

# get average polarities
def avg_polarities():
    filenames = get_filenames()
    for filename in filenames:
        with open(f"./polarities/{filename}.txt", "r") as f:
            entries = f.read()
        polarities = [float(entry) for entry in entries.split('\n') if len(entry) > 1]
        with open(f"./polarities/{filename}_avg.txt", "w") as f:
            f.write(str(avg(polarities)))

avg_polarities()
