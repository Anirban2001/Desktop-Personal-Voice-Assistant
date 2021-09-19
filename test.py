import ast

dict_file = open("x.txt", "r")
dict_string = dict_file.readline().strip()
dict_file.close()

d = ast.literal_eval(dict_string) 

#change your dictionary e.g:
d["me"]= "8927902898"
f = open("x.txt", "w")
f.write(str(d))
f.close()