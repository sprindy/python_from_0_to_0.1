import re

text_file = 'a.txt'
books_list = [
'Genesis', 'Exodus', 'Leviticus', 'Numbers', 'Deuteronomy',
'Joshua', 'Judges', 'Ruth', 'Samuel', 'Kings',
'Chronicles', 'Ezra', 'Nehemiah', 'Tobit',
'Judith', 'Esther', 'Maccabees', 'Job',
'Psalms', 'Proverbs', 'Ecclesiastes', 'Song of Songs',
'Wisdom', 'Sirach', 'Isaiah', 'Jeremiah',
'Lamentations', 'Baruch', 'Ezekiel', 'Daniel',
'Hosea', 'Joel', 'Amos', 'Obadiah',
'Jonah', 'Micah', 'Nahum', 'Habakkuk',
'Zephaniah', 'Haggai', 'Zechariah', 'Malachi',
'Matthew', 'Mark', 'Luke', 'John',
'Acts', 'Romans', 'orinthians', 'Galatians',
'Ephesians', 'Philippians', 'Colossians', 'Thessalonians',
'Timothy', 'Titus', 'Philemon', 'Hebrews',
'James', 'Peter', 'John', 'Jude',
'Revelation']

cnt = 0
with open(text_file, 'r') as f:
    lines = f.readlines()
    # print(lines)
    for line in lines:
        # line_new = re.sub(r' |, |\. ', "", line)
        line_new = re.sub('[^a-zA-Z]', "", line)
        # print(line)
        # print(line_new)
        # print(len(books_list))
        for i in range(len(books_list)):
            m = re.search(books_list[i], line_new, re.I)
            if m is not None:
                cnt = cnt + 1
                print(cnt, i, m.group(), books_list[i])
