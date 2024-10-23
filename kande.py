import regex

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

# Dictionaries containing lists representing overlaps between Kanken lists
# Overlap lists and methods were not made for N5 and 4 since I studied those in school
# Key: Kanken level. Index levels used for simplicity in code
# Value: List containing Kanken kanji at that level found in the given JLPT level
n3_overlaps = { 0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [] }
n2_overlaps = { 0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [] }



# path = input file path
def read_file(path: str) -> list:
    with open(path, 'r') as file:
        return file.readlines()


# path = output file path
# content = content of file as list
def write_file_lines(path: str, content: list):
    with open(path, 'w') as file:
        for line in content:
            file.write(f'{line}\n')


# path = output file path
# content = content of file as str
def write_file_str(path: str, content: str):
    with open(path, 'w') as file:
        file.write(f'{content}\n')



# line = line in text file read from above method
def gen_kanji_list(line: str) -> list:
    output = []
    for char in line:
        output.append(char)
    
    # Remove trailing newline
    output.pop()

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


# A generic method could be used for this, but the variables aren't as generic 
def gen_n3_overlaps():
    global n3_overlaps
    global kanken_lists
    global jlpt_lists
    
    for i in range(7):
        for kanken_char in kanken_lists[i]:
            if kanken_char in jlpt_lists[2]:
                n3_overlaps[i].append(kanken_char)


def gen_n2_overlaps():
    global n2_overlaps
    global kanken_lists
    global jlpt_lists
    
    for i in range(7):
        for kanken_char in kanken_lists[i]:
            if kanken_char in jlpt_lists[3]:
                n2_overlaps[i].append(kanken_char)


def gen_n3_missing():
    covered = n3_overlaps[0] + n3_overlaps[1] + n3_overlaps[2] + n3_overlaps[3] + n3_overlaps[4] + n3_overlaps[5] + n3_overlaps[6]

    missing = []
    for char in jlpt_lists[2]:
        if char not in covered:
            missing.append(char)
    
    return missing


def gen_n2_missing():
    covered = n2_overlaps[0] + n2_overlaps[1] + n2_overlaps[2] + n2_overlaps[3] + n2_overlaps[4] + n2_overlaps[5] + n2_overlaps[6]

    missing = []
    for char in jlpt_lists[3]:
        if char not in covered:
            missing.append(char)
    
    return missing



gen_kanken_lists('data/kanken.txt')
gen_jlpt_lists('data/jlpt.txt')

gen_n3_overlaps()
n3_overlap_file_content = [
    ''.join(n3_overlaps[0]),
    ''.join(n3_overlaps[2]),
    ''.join(n3_overlaps[3]),
    ''.join(n3_overlaps[4]),
    ''.join(n3_overlaps[5]),
    ''.join(n3_overlaps[6]),
]
write_file_lines('data/n3_overlaps.txt', n3_overlap_file_content)

gen_n2_overlaps()
n2_overlap_file_content = [
    ''.join(n2_overlaps[0]),
    ''.join(n2_overlaps[2]),
    ''.join(n2_overlaps[3]),
    ''.join(n2_overlaps[4]),
    ''.join(n2_overlaps[5]),
    ''.join(n2_overlaps[6]),
]
write_file_lines('data/n2_overlaps.txt', n2_overlap_file_content)

print(''.join(gen_n2_missing()))
write_file_str('data/n3_missing.txt', ''.join(gen_n3_missing()))
write_file_str('data/n2_missing.txt', ''.join(gen_n2_missing()))


