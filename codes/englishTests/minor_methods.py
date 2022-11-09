vowels=['a','e','i','o','u']
mistakes={}
similar_vowels={
    'a':'e',
    'e':'i',
    'i':'e',
    'o':'u',
    'u':'o',
}
similar={
    "quran":["kuran"],
    "q":["k"],

}

def generate_erronious_vowel_text(string):
    string_lit=[]
    string_lit.append(string)
    num_vol=0
    for i in string:
        if i in vowels:
            num_vol=num_vol+1
    
    for i in range(len(string)):
        for k in range(len(vowels)):
            # print("ith = ",i,k,vowels[k])
            try:
                vol_idx=string.index(vowels[k])
                # print("vol idx",vol_idx,vowels[k])
                
            except ValueError:
                # print("substring not found")
                pass
            else:
                # print("printing all iters")
                for j in range(len(vowels)):
                    if(vol_idx>(len(string)/2)):
                        temp = string[:vol_idx] + vowels[j] + string[vol_idx + 1:]
                        # print("text = ",vowels[j]," = ",temp)
                        string_lit.append(temp)
                # print("printing similar vowels")
                for j in similar_vowels:
                    if(vowels[k]==j and vol_idx<(len(string)/2)):
                        temp = string[:vol_idx] + similar_vowels[j] + string[vol_idx + 1:]
                        # print("text = ",similar_vowels[j]," = ",temp)
                        string_lit.append(temp)
    return string_lit
import itertools





def without_vowel_words(string):
    string_lit=[]
    string_lit.append(string[0])
    num_vol=0
    perm = []

    for i in string:
        if i in vowels:
            num_vol=num_vol+1
    
    if num_vol==0:
        return string_lit
    else:
        list1=[]
        for i in range(num_vol):
            for k in range(len(vowels)):
                # print("ith = ",i,k,vowels[k])
                try:
                    vol_idx=string.index(vowels[k])
                    list1.append(vol_idx)
                    # print("vol idx",vol_idx,vowels[k])
                except:
                    pass
        list1=list(set(list1))
        # print(list1)
        perm = []
        for i in range(1,len(list1)+1):
            perm.extend(list(itertools.permutations(list1, r=i)))
        # print(perm)
        lit=list(string)
        lit2=[]
        # print(lit)
        # print(len(perm))
        for k in range(len(perm)):
            for l in perm[k]:
                # print(k,l)
                if l>0 and l<len(string)-1:
                    
                    lit[l]=0
                    # str1=str1.join(lit)
                    
                    # print(str1)
            for i in range(len(lit)):
                for j in lit:
                    if j==0:
                        lit.remove(j)
           
            
            str1=""
            str1=str1.join(lit)
            lit2.append(str1)
            lit2=list(set(lit2))
            lit2.insert(0, string)
            # print(lit2)
            
            lit=list(string)
    lit2.append(string)
    return lit2
            

        # for i in range(num_vol):
        #     for k in range(len(vowels)):
        #         # print("ith = ",i,k,vowels[k])
        #         try:
        #             vol_idx=string.index(vowels[k])
        #             print("vol idx",vol_idx,vowels[k])
                    
        #         except ValueError:
        #             # print("substring not found")
        #             pass
        #         else:
        #             for j in range(len(vowels)):
        #                 if vol_idx>0 and vol_idx<len(string)-1 :
        #                     temp = string[:vol_idx] + string[vol_idx + 1:]
        #                     # print("text = ",vowels[j]," = ",temp)
        #                     string_lit.append(temp)
        # string_lit=list(set(string_lit))
    





# def without_vowel_words(word):
#   string = ''
#   ans=[]
#   vowel = ['a','e','i','o','u']
#   while len(word) > 0:
#     for index,i in enumerate(word):
#       if i in vowel:
#         occurence = index
#         break
#     string = word[:occurence] + word[occurence+1:]
#     ans.append(string)
#     word = string
#     flag = 0
#     for j in word:
#       if j in vowel:
#         flag = 1
#     if flag == 0:
#       break
#     string=''
#   return ans

# def without_vowel_words(word):
#   string = ''
#   ans=[]
#   vowel = ['a','e','i','o','u']
#   while len(word) > 0:
#     for i in word:
#       if i in vowel:
#         continue
#       string+=i
#     ans.append(string)
#     word = string 
#     return ans

def create_dictionary(data):
    dictionary={}
    for i in data:
        returned_list=generate_erronious_vowel_text(i)
        returned_list2=without_vowel_words(i)
        returned_list.extend(returned_list2)
        dictionary[returned_list[0]]=list(set(returned_list[:]))
    return dictionary

test=create_dictionary(["actually"])
print(test)