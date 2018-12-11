sum = 0
dict_result = {}
with open('RATING.txt', 'r') as result:
    for line1 in result.readlines():
        line1 = line1.replace("\'", "")
        line1 = line1.replace("\n","")
        str_array1 = line1.split('\t')
        dict_key1 = (int(str_array1[0]), int(str_array1[1]))
        dict_value1 = float(str_array1[2])
        dict_result[dict_key1] = dict_value1

dict_truth = {}
with open('rating_truth.txt', 'r') as truth:
    for line2 in truth.readlines():
        line2 = line2.replace("\n","")
        str_array2 = line2.split('\t')
        dict_key2 = (int(str_array2[0]), int(str_array2[1]))
        dict_value2 = float(str_array2[2])
        dict_truth[dict_key2] = dict_value2

for key in dict_result:
    value_result = dict_result[key]
    value_truth = dict_truth[key]
    sum = sum + pow((value_result - value_truth),2)

result = sum / len(dict_result)
print(result)