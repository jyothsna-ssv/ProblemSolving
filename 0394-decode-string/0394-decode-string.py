class Solution:
    def decodeString(self, s: str) -> str:
        stack = []           
        current_text = ""    
        current_number = 0    
        for ch in s:
            if ch.isdigit():
                current_number = current_number * 10 + int(ch)
            elif ch == "[":
                stack.append((current_text, current_number))
                current_text, current_number = "", 0
            elif ch == "]":
                prev_text, repeat_count = stack.pop()
                current_text = prev_text + current_text * repeat_count
            else:
                current_text += ch
        return current_text
