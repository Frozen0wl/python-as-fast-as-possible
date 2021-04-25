import time

def same_length(txt):
    if len(txt) == 1:
        return False
    else:    
        txt += 'a'
        i = 0
        count = 1
        count2 = 1
        while txt[i] == txt[i+1]:
            count += 1
            i+=1
            print(count)
            #time.sleep(0.5)

        while txt[i+1] == txt[i+2] and i+2 != 'a':
            count2+=1
            i+=1
            print(count2)
            #time.sleep(0.5)

        return count2 == count
    

print(same_length('11001'))
        