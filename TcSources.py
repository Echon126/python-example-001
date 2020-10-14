import binascii
# import struct
import pandas as pd

# data = pd.read_excel(r'C:\Users\ZKTT\Desktop\wkl\tc-parse.xls', sheet_name='整星动中-数传天线固定站')
# f = open(r'C:\Users\ZKTT\Desktop\wkl\指令文件20201014\totianta\遥控\码字核对\BJBFDZ_2020-09-24-20_10_57', 'rb')
# for row in data.values:
#     print('{}{}{}'.format(row[0], "  ", binascii.b2a_hex(f.read(row[2]))))
#
# f.close()


# data = pd.read_excel(r'C:\Users\ZKTT\Desktop\wkl\tc-parse.xls', sheet_name='整星动中-成像参数设置-记录模式')
# f = open(r'C:\Users\ZKTT\Desktop\wkl\指令文件20201014\totianta\遥控\码字核对\CXJLDZ\CXJLDZ_2020-09-29-03_56_37', 'rb')
# for row in data.values:
#     print('{}{}{}'.format(row[0], "  ", binascii.b2a_hex(f.read(row[2]))))
#
# f.close()


data = pd.read_excel(r'C:\Users\ZKTT\Desktop\wkl\tc-parse.xls', sheet_name='整星动中-成像参数设置-记录模式')
f = open(r'C:\Users\ZKTT\Desktop\wkl\指令文件20201014\totianta\遥控\码字核对\CXJLDZ\CXJLDZ_2020-09-29-03_56_37', 'rb')
for row in data.values:
    print('{}{}{}'.format(row[0], "  ", binascii.b2a_hex(f.read(row[2]))))

f.close()
