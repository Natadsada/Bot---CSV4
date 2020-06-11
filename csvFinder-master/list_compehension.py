list = [1,2,3,4]

new_list = []
# for i in list:  ###แบบ ธรรมดา
#     new_list.append(i+2)

# print(new_list)

###########################################################

new_list = [i+2 for i in list]  ##List Compehension
print(new_list)