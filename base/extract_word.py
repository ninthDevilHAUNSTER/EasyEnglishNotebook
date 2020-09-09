import re

zhPattern = re.compile(u'[\u4e00-\u9fa5]+')


def extract(line):
    _return = []
    # [(),(),()]
    for item in line.split("|"):
        try:
            _i = item.split(":")
            _return.append(
                (
                    _i[0] if not zhPattern.search(_i[0]) else _i[1]
                    ,
                    _i[0] if zhPattern.search(_i[0]) else _i[1]
                )
            )
        except:
            # print(item," handle ERROR")
            pass
    return _return


def extract_word_from_file(file, output="output/res.csv"):
    res = ""
    with open(file, encoding="utf8") as f:
        x = []
        for i in f.readlines():
            if ":notebook:" in i[0:20] and i.__len__() > 11:
                x.extend(extract(i.replace(":notebook:", "").replace("\n", "")))
        for i in x:
            res += i[0] + "," + i[1] + "\n"
    return open(output, 'w', encoding='utf-8').write(res)
