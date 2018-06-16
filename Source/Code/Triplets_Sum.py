import sys

def Sum_Zero(list):
    sorted_list = sorted(list)
    if(len(list) < 3):
        sys.exit(0)
    elif(len(list) >= 3):
        for f_element in range(len(sorted_list)):
            s_element = f_element + 1
            for r_element in range(s_element + 1, len(sorted_list)):
                if((sorted_list[f_element] + sorted_list[s_element] + sorted_list[r_element]) == 0):
                    print(sorted_list[f_element],sorted_list[s_element],sorted_list[r_element])

if __name__ == '__main__':
    list = [1,3,6,2,-1,2,8,-2,9]
    Sum_Zero(list)




