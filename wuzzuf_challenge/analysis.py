___author__ = 'Ahmed Hani Ibrahim'
import matplotlib.pyplot as plt
import collections


class Analyzer(object):
    def __init__(self, data):
        self.__data = data

    def trending_category(self):
        category1 = list(map(lambda v: v.get_job_category_1(), self.__data))
        category2 = list(map(lambda v: v.get_job_category_2(), self.__data))
        category3 = list(map(lambda v: v.get_job_category_3(), self.__data))

        all_categories = []

        for i in range(0, len(category1)):
            if category1[i] == category2[i] == category3[i]:
                all_categories.append(category1[i])
            elif category1[i] == category2[i]:
                all_categories.append(category1[i])
                all_categories.append(category3[i])
            elif category1[i] == category3[i]:
                all_categories.append(category1[i])
                all_categories.append(category2[i])
            elif category2[i] == category3[i]:
                all_categories.append(category2[i])
                all_categories.append(category1[i])
            else:
                all_categories.append(category1[i])
                all_categories.append(category2[i])
                all_categories.append(category3[i])

        freq = collections.Counter(all_categories)

        plt.subplots_adjust(bottom=0.35)
        plt.bar(range(len(freq)), freq.values(), align="center")
        plt.xticks(range(len(freq)), list(freq.keys()), rotation='vertical')
        plt.show()



