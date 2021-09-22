# 西暦を和暦に変更する
import datetime
print('西暦を和暦に変更します。')
nengou =int(input('西暦を入力してください。(1900年以降でお願いします。)'))
now =datetime.datetime.now()

for i in range(1900,now):
    if nengou <= 1899:
        print('1900年以降でお願いします。')
    elif nengou >=1900 and nengou <=1912:
        print('明治{}です。'.format(nengou-1867))
    elif　