# with open("../data/supplierApply.txt","r",encoding="utf-8") as f:
    # 一次读取全部内容
    # data = f.read()
    # print(data)
    # 读取第一行内容
    # data = f.readline()
    # print(data)
    # 读取数据列表展示
    # data = f.readlines()
    # print(data)
    #
    # for line in f.readlines():
    #     line = line.strip('\n')  #去掉列表中每一个元素的换行符
    #     print(line)
from os.path import split


class ReadTxt:
    def get_txt(self):
        with open("../data/supplierApply.txt", "r", encoding="utf-8") as f:
            all_cases = []
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                all_cases.append(line)
                # print(line)
            return all_cases
# ['"甲供","甲供应商：评级很高","很好很好"', '"乙供","乙供应商：评级较好","较好较好"', '"丙供","丙供应商：评级一般","一般一般"', '"丁供","丁供应商：评级很差","很差很差"']

if __name__ == '__main__':
    all_cases = ReadTxt().get_txt()
    print(all_cases)