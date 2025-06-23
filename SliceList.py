original_list=[1,2,3,4,5,6,7,8,9,10]

extracted_list=original_list[:5]

reversed_extracted_list=[]

for item in extracted_list:
    reversed_extracted_list.insert(0,item)

print("original list")
print(original_list)
print("extracted list")
print(extracted_list)
print("reversed list")
print(reversed_extracted_list)
