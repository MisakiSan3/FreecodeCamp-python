import re
def preprocess(s,display):
    operand=re.findall(r'\d+',s)
    operator=re.findall(r'[^\d ]',s)
    if len(operand)>2 or len(operator)>1:
        return "Error: Numbers must only contain digits."
    if len(operand[0])>4 or len(operand[1])>4:
        return "Error: Numbers cannot be more than four digits."
    if not (operator[0] in ('-','+') ):
        return "Error: Operator must be '+' or '-'."
    maxlen=max(len(operand[0]),len(operand[1]))
    block=[operand[0].rjust(maxlen+2),operator[0]+' '+operand[1].rjust(maxlen),'-'*(maxlen+2)]
    if display:
        if operator[0]=='-':
            block.append(str(int(operand[0])-int(operand[1])).rjust(maxlen+2))
        if operator[0]=='+':
            block.append(str(int(operand[0])+int(operand[1])).rjust(maxlen+2))
    return block

def arithmetic_arranger(problems,display=False):
    if len(problems)>5 :
        return "Error: Too many problems."
    seperator=' '*4

    blocks=[]
    for s in problems:
        blocks.append(preprocess(s,display))
        if type(blocks[-1])==str:
            return blocks[-1]

    arranged_problems=''
    if display==True:
        count=4
    else:
        count=3
    for i in range(count):
        for j in blocks:
            arranged_problems+=j[i]+seperator
            if j==blocks[-1]:
                arranged_problems=arranged_problems[0:-4]
        arranged_problems+='\n'
    return arranged_problems[0:-1]


if __name__ == "__main__":
    print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]))  
