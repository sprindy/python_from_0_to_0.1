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

# 计数变量
cnt = 0
with open(text_file, 'r') as f:
    lines = f.readlines()
    # print(lines)
    for line in lines:
        # 两个都可以，都是把字符串里的标点符号去掉，只剩下字母
        # line_new = re.sub(r' |, |\. ', "", line)
        line_new = re.sub('[^a-zA-Z]', "", line)
        # print(line)
        # print(line_new)
        # print(len(books_list))
        # 遍历这个列表，挨个查找是否匹配
        for i in range(len(books_list)):
            # 要在替换后的字符串里搜索
            m = re.search(books_list[i], line_new, re.I)
            if m is not None:
                # 计数器加1
                cnt = cnt + 1
                # 打印计数值，和书名表里的第几个匹配，匹配的内容，书名
                print(cnt, i, m.group(), books_list[i])
