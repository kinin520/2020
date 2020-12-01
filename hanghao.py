lines_maxlenth = 0                                                                  #1
line_numbers = 1                                                                    #2
code_in = open("demo.py","r").readlines()                                           #3
code_out = open("demo_new.py", "w")                                                 #4
for i in code_in:                                                                   #5
        lines_maxlenth = len(i) if lines_maxlenth < len(i) else lines_maxlenth      #6
for i in code_in:                                                                   #7
    i = i.ljust(lines_maxlenth+1).replace('\n','') + "#" + str(line_numbers) + "\n" #8
    line_numbers += 1                                                               #9
    code_out.write(i)                                                                #10
