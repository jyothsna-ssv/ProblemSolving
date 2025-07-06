class Solution(object):
    def generateTag(self, caption):
        w = caption.split()

        if not w:
            return "#"

        # else
        tag = "#" + w[0].lower()

        for x in w[1:]:
            tag = tag + x.capitalize()

        fresh = [tag[0]]
        for ch in tag[1:]:
            if ch.isalpha():
                fresh.append(ch)
        result = ''.join(fresh)[:100]

        return result
        
        
        