#given a sentence, break it into words, note down its emision probabilities
def make_input(input_sentence):
    val=[]
    input_sentence=input_sentence.strip()
    input_words=input_sentence.split()
    for i in input_words:
        i=i.lower()
        if i=='cojelo':
            val.append([0.1,0.3])
        if i=='con':
            val.append([0.2,0.3])
        if i=='take':
            val.append([0.3,0.15])
        if i=='it':
            val.append([0.2,0.15])
        if i=='easy':
            val.append([0.2,0.1])
    return len(input_words),val
#generate all possible transition strings given sentence length
def generate_possibilities(i,size,temp):
    if i==size:
        options.append(temp)
        return
    generate_possibilities(i+1, size, temp + ['S'])
    generate_possibilities(i+1, size, temp + ['E'])
#find max answer by checking all 2**n options for possible transition strings
def get_max_probability(n,options,val):
    for i in range(2**n):
        for j in range(n):
            if j==0:
                if options[i][j]=='E':
                    ans= 0.6*val[j][0]
                else:
                    ans=0.4*val[j][1]
                    
            elif options[i][j]=='E' and options[i][j-1]=='E':
                ans*= 0.3*val[j][0]
            elif options[i][j]=='E' and options[i][j-1]=='S':
                ans*= 0.6*val[j][0]
            elif options[i][j]=='S' and options[i][j-1]=='S':
                ans*= 0.4*val[j][1]
            else:
                ans*=0.7*val[j][1]
        temp.append(ans)
    maxm = -float('inf')
    final_ans = []
    for i in range(len(temp)):
        if temp[i]>maxm:
            maxm = temp[i]
            final_ans = [options[i]]
        elif temp[i]==maxm:
            final_ans.append(options[i])
    for i in range(len(final_ans)):
        print('"'+" ".join(final_ans[i]) + '":'+str(round(maxm,5)))

#the main function outputting all answers   
if __name__ =='__main__':
    n,val=make_input('cojelo con take it easy')
    options=[]
    temp=[]
    generate_possibilities(0,n,temp)
    get_max_probability(n,options,val)
    n,val=make_input('con take it easy')
    options=[]
    temp=[]
    generate_possibilities(0,n,temp)
    get_max_probability(n,options,val)
    n,val=make_input('easy con')
    options=[]
    temp=[]
    generate_possibilities(0,n,temp)
    get_max_probability(n,options,val)
    n,val=make_input('cojelo easy take it')
    options=[]
    temp=[]
    generate_possibilities(0,n,temp)
    get_max_probability(n,options,val)

