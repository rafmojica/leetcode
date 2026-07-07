class Solution:
    def simplifyPath(self, path: str) -> str:
        # if char == /: append everything after it until another / 
        # map structure: 1: home, 2: user, 3: Documents, 4: .., 5: Pictures
        # every / marks the beginning of another directory

        # constructing result: 
        # res = ['/', 'home', '/', 'user', '/', 'Pictures']
        # for key in map: if map[key] == '..' pop previous from res. else: append map[key]
        
        directoryMap = {}
        mapIndex = 0
        
        for i in range(len(path)):
            if path[i] != '/':
                directoryMap[mapIndex] = directoryMap.get(mapIndex, '') + path[i]
            else:
                mapIndex += 1
        
        res = ['/']
        for k in directoryMap:
            if directoryMap[k] == '..':
                res.pop()
                if len(res) != 0:
                    res.pop()
            elif directoryMap[k] != '.':
                res.append(directoryMap[k])
                res.append('/')
            
            if len(res) == 0:
                res.append('/')
                
        if len(res) == 1:
            return '/'

        res.pop() # remove trailing '/'
        
        return "".join(res)
        