class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def valid(s, bits):
            if len(s) < bits:
                return None
            if bits == 1:
                if(int(s) < 256 and (s[0] != '0' or len(s)==1)):
                    return [s]
                else:
                    return None
            ret = []
            for l in range(1, min(4, len(s))):
                prefix = s[:l]
                rest = s[l:]
                if int(prefix) < 256 and (l==1 or prefix[0] != '0') and (s1 := valid(rest, bits-1)):
                    for se in s1:
                        ret.append(prefix + '.' + se)
            return ret
        
        return valid(s, 4)
