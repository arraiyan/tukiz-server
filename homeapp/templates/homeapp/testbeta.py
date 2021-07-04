from typing import final


string = "hi there how are you IMAGE(0xffffff)there it goes IMAGE(0xffffff)inthere it goes IMAGE(0xffffff)asdfasd"

j = 0
final_str = list()

while j>=0:
    j = string.find('IMAGE',j)
    img_id = string[j+6:j+14]
    print(img_id)
    if j<0:
        break
    j=j+15
    txt ="txt_"+ string[j:string.find('IMAGE',j)]
    

    final_str.append(txt)
    i = "img_"+ str(int(img_id,16))
    final_str.append(i)
j=0   
d=dict()
for i in final_str:
    d[j]=i
    j+=1
print(d)
