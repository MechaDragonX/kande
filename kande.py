# Data files and below variables can be moodified to met invidual

# Lists representing Kanken levels 7, 6, 5, 4, 3, pre 2, and 2
# 10-6 aren't included since it'd be useless data for me based on pretests
# Pre-1 and 1 aren't common taken unless you care about obscure kanji
kanken7 = []
kanken6 = []
kanken5 = []
kanken4 = []
kanken3 = []
kankenp2 = []
kanken2 = []

# Lists representing JLPT N5-2
# I'm not taking N1 yet, so I haven't included it in the data yet
n5 = []
n4 = []
n3 = []
n2 = []


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
    global kanken7
    global kanken6
    global kanken5
    global kanken4
    global kanken3
    global kankenp2
    global kanken2

    kanken = read_file(path)
    # The following lines expect a specific number of lines in the same position as the var list
    kanken7 = gen_kanji_list(kanken[0])
    kanken6 = gen_kanji_list(kanken[1])
    kanken5 = gen_kanji_list(kanken[2])
    kanken4 = gen_kanji_list(kanken[3])
    kanken3 = gen_kanji_list(kanken[4])
    kankenp2 = gen_kanji_list(kanken[5])
    kanken2 = gen_kanji_list(kanken[6])


# path = input file path
def gen_jlpt_lists(path: str):
    global n5
    global n4
    global n3
    global n2

    jlpt = read_file(path)
    # The following lines expect a specific number of lines in the same position as the var list
    n5 = gen_kanji_list(jlpt[0])
    n4 = gen_kanji_list(jlpt[1])
    n3 = gen_kanji_list(jlpt[2])
    n2 = gen_kanji_list(jlpt[3])


gen_kanken_lists('data/kanken.txt')
gen_jlpt_lists('data/jlpt.txt')
