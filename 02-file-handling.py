with open('example.txt','r') as file :
    # content= file.read()
    # print (content)

    for line in file:
        print(line.strip())


with open("example.txt", 'w') as file: # this overwrite the content 
    file.write("i am soo sad right now") 
    
# to avoid overwrite

with open ('example.txt','a') as file:
    file.write("i am appendsing this line")