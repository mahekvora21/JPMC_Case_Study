input_sentence=[]
#make all possible sentences of size n
def generate_input_sentences(i,size,temp):
    if i==size:
        input_sentence.append(temp)
        return
    generate_input_sentences(i+1, size, temp + 'cojelo ')
    generate_input_sentences(i+1, size, temp + 'con ')
    generate_input_sentences(i+1, size, temp + 'take ')
    generate_input_sentences(i+1, size, temp + 'it ')
    generate_input_sentences(i+1, size, temp + 'easy ')
#store their emission probabilities
def make_input(size):
    val=[]
    input_words=[]
    generate_input_sentences(0,size,'')
    for i in input_sentence:
         i=i.strip()
         l=(i.split())
         input_words.append(l)

    res=[]
    #print(input_words)
    for j in range(len(input_sentence)):
        for i in input_words[j]:
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
       #print(val)
        res.append(val)
        val=[]
    return len(input_words[0]),res
#all possible transition strings given a strings length
def generate_possibilities(i,size,temp):
    if i==size:
        options.append(temp)
        return
    generate_possibilities(i+1, size, temp + ['S'])
    generate_possibilities(i+1, size, temp + ['E'])

def solve(n,options,res,x):
    temp=[]
    for i in range(2**n):
        #print(options[i])
        for j in range(n):
            if j==0:
                if options[i][j]=='E':
                    ans= 0.6*res[x][j][0]
                else:
                    ans=0.4*res[x][j][1]
                    
            elif options[i][j]=='E' and options[i][j-1]=='E':
                ans*= 0.3*res[x][j][0]
            elif options[i][j]=='E' and options[i][j-1]=='S':
                ans*= 0.6*res[x][j][0]
            elif options[i][j]=='S' and options[i][j-1]=='S':
                ans*= 0.4*res[x][j][1]
            else:
                ans*=0.7*res[x][j][1]
            #print(ans)
        temp.append(ans)
    a=0
    for i in range(len(temp)):
        a=a+temp[i]
        #print(temp[i])
    return a

#main function, shows output
if __name__ =='__main__':
    n,res=make_input(2)
    options=[]
    temp=[]
    generate_possibilities(0,n,temp)
    ans=0
    for i in range(len(input_sentence)):
        ans=ans+solve(n,options,res,i)
    print('The sum of the probabilities for all possible strings and their possible transition strings of a fixed length is :'+str(ans))
    
    

