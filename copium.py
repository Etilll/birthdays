# tmp = {'cattie':{'brattie':'11'}, 'John Gattsby':'22'}

# for k,v in tmp.items():
#     print(str(k))
from datetime import datetime, timedelta
tmp_o = datetime(2023, 12, 26).date()
tmp_t = datetime(2024, 1, 1).date()
tmp_delta = timedelta(days=(7))

if (tmp_t >= tmp_o) and ((tmp_t - tmp_o) <= tmp_delta):
    print("YES " + str(tmp_t.weekday()))



# tmp = "sgefg/sgdfgesd/oiooioi/eleven_pieces"
# tmp = tmp[tmp.rfind("/") + 1:]
# print(tmp)
# from pathlib import Path
# import sys
# tmp_l = []
# tmp_l.append(Path('123/suppie/No_ext'))

# print(str(tmp_l[0]))
# print(str(tmp_l[0]).rfind("\\"))
#[str(tmp_l[0]).rfind("/"):]

# tmp = 'wsqr'.encode()
# tmq = '12sdfa'.encode()

# list = []
# list.append(tmp)
# list.append(tmq)
# print(list)


# fh = open('123.txt', 'w+')
# fh.writelines(['Kovalchuk Oleksiy,301,175,180,155\n', 'Ivanchuk Boryslav,101,135,150,165\n', 'Karpenko Dmitro,201,155,175,185'])
# #fh.seek(0)
# fh.close()

# fh = open('123.txt', 'r')
# text = fh.read()
# print(text)


# fh.close()


# import re


# def find_all_emails(text):
#     pattern = '[a-zA-Z].{1,100}@[a-zA-Z]{2,100}\.[a-zA-Z]{2,100}'
#     result = re.findall(pattern, text)
#     #print(result)
#     return result

# print(find_all_emails('Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net'))



# for num in range(12):
#     print('{:^10} {:^10} {:^10}'.format(str(num) + "|", num ** 2, num ** 3))


# a = ("John", "Charles", "Mike")
# b = ("Jenny", "Christy", "Monica")

# x = zip(a.upper(), b)

# #use the tuple() function to display a readable version of the result:

# print(dict(x))



# str = "DCSB"

# map = {ord('D'): '11', ord('C'): '90', ord('S'): '23', ord('b'): '00'}

# print(str.translate(map))

# str = "\n123"
# map = {ord('\n'): 'www'}
# print(str.translate(map))

# if str.find("x") != -1:
#     print("suckass")
# else:
#     print("TRUE")


# elist = {"F":22, "C":41}

# if elist["A"]:
#     print(len(elist))
# else:
#     print("Dick")



# busted = False
# str = "holiday"
# if str.find("hole"):
#     print('really?')
# else:
#     print('reading')

# if busted:
#     print('Busted')
# elif not busted:
#     print('Lua')