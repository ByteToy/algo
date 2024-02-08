def per(s):
    lens=len(s)
    if lens<=1:
        return s
    else:
        result=[]
        for i in range(lens):
            ch=s[i]
            rest=s[0:i]+s[i+1:lens]
            for j in per(rest):
                result.append(ch+j)
        return result

if __name__=="__main__":
    print(per('abcde'))