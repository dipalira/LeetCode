class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        elif n == 2:
            return '11'
        current  = '11'
        current_l = list(current)
        print(current_l)
        for i in range(3,n+1):
            #Check for numbers n-1 in the string
            #Convert string to list
            #current
            str_map = {}
            key,value = 0,0
            updated = []
            for i in range(0, len(current_l)):
                try:
                    if current_l[i] == current_l[i+1]:
                        key = current_l[i]
                        value +=1
                    else:
                        key = current_l[i]
                        value += 1 
                        updated += [str(value)] 
                        updated += [str(key)]
                        key,value = 0,0
                except:
                    key = current_l[i]
                    value += 1 
                    updated += [str(value)] 
                    updated += [str(key)]
                    key,value = 0,0
            current_l = updated
        print(current_l)
        return ''.join(current_l)
