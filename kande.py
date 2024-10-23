# Data files and below variables can be moodified to met invidual

# Lists representing Kanken levels 7, 6, 5, 4, 3, pre 2, and 2
# A list of lists is used where x represents a given level
# and y repsents the value 
# 10-6 aren't included since it'd be useless data for me based on pretests
# Pre-1 and 1 aren't common taken unless you care about obscure kanji
kanken_lists = [ [], [], [], [], [], [], [] ]


# Lists representing JLPT N5-2
# I'm not taking N1 yet, so I haven't included it in the data yet
# As with the Kanken ones, a list of lists is used
jlpt_lists = [ [], [], [], [] ]


# path = input file path
def read_file(path: str) -> list:
    with open(path, 'r') as file:
        return file.readlines()


# line = line in text file read from above method
def gen_kanji_list(line: str) -> list:
    output = []
    for char in line:
        output.append(char)
    
    return output


# path = input file path
def gen_kanken_lists(path: str):
    global kanken_lists

    kanken_file = read_file(path)

    for i in range(7):
        kanken_lists[i] = gen_kanji_list(kanken_file[i])


# path = input file path
def gen_jlpt_lists(path: str):
    global jlpt_lists

    jlpt_file = read_file(path)

    for i in range(4):
        jlpt_lists[i] = gen_kanji_list(jlpt_file[i])


gen_kanken_lists('data/kanken.txt')
gen_jlpt_lists('data/jlpt.txt')

print(jlpt_lists[0])
print(jlpt_lists[2])
