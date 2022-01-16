import pytesseract
import cv2
def lcs(s1 , s2):
   m, n = len(s1), len(s2)
   prev, cur = [0]*(n+1), [0]*(n+1)
   for i in range(1, m+1):
       for j in range(1, n+1):
           if s1[i-1] == s2[j-1]:
               cur[j] = 1 + prev[j-1]
           else:
               if cur[j-1] > prev[j]:
                   cur[j] = cur[j-1]
               else:
                   cur[j] = prev[j]
       cur, prev = prev, cur
   return prev[n]
def find_suggestion(word,res_list):
    ans=[]
    lw=len(word)
    for i in res_list:
        d=lcs(word,i)
        if(d*2>lw):
            ans.append([d,i])
    ans.sort(reverse=True)
    final=[]
    for j in ans:
        final.append(j[1]) 
    return final
res_list=[ 'alignas', 'double', 'reinterpret_cast', 'alignof', 'dynamic_cast', 'requires', 'and', 'else', 'return', 'and_eq', 'enum', 'short', 'asm', 'explicit', 'signed', 'atomic_cancel', 'export', 'sizeof', 'atomic_commit', 'extern', 'static', 'atomic_noexcept', 'false', 'static_assert', 'auto', 'float', 'static_cast', 'bitand', 'for', 'struct', 'bitor', 'friend', 'switch', 'bool', 'goto', 'synchronized', 'break', 'if', 'template', 'case', 'import', 'this', 'catch', 'inline', 'thread_local', 'char', 'int', 'throw', 'char16_t', 'long', 'true', 'char32_t', 'module', 'try', 'class', 'mutable',
'typedef', 'compl', 'namespace', 'typeid','concept', 'new', 'typename', 'const', 'noexcept','union', 'constexpr', 'not', 'unsigned', 'const_cast', 'not_eq', 'using', 'continue', 'nullptr ', 'virtual', 'co_await ', 'operator', 'void','co_return', 'or', 'volatile', 'co_yield', 'or_eq', 'wchar_t', 'decltype', 'private', 'while', 'default', 'protected', 'xor', 'delete', 'public', 'xor_eq,' 'do', 'register','iostream','std','cout','cin' ]
import cv2

import pytesseract 

img=cv2.imread(pa)



text=pytesseract.image_to_string(img)

text=text.split('\n')

d=[]

for j in text:

    dd=j.strip()

    if(dd!=''):
        d.append(j) 

for i in text:
    print(i,find_suggestion(i,res_list))