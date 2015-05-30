# _*_ coding = utf-8 _*_

names = ['javascript','php','python','html5','css3']

print names[0]

#len() get list'length number

print len(names)

#insert(index,data) insert data to the list

names.insert(1,'asp.net') 

print names #['javascript', 'asp.net', 'php', 'python', 'html5', 'css3']

#pop(index)  delete element  when index is null which delete the last element for list , but not delete the index of element

names.pop()

print names

