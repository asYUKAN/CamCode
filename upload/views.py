from django.shortcuts import render

from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage

from . models import Images

# Create your views here.



from django.views.generic import TemplateView

import os 

img1_path=""
word_sug1=""
textcod=""
def index(request):

    return render(request, 'upload/index.html')

def uploaded(request):

	s = Images()

	text=''


	

	if request.method == 'POST':
		
		

		os.system("rm -r media/")

		uploaded_file=request.FILES['image']


		fs = FileSystemStorage()

		
		fs.save(uploaded_file.name,uploaded_file)



		pa='media/'+uploaded_file.name
		
		
		s.img_name=uploaded_file.name

		s.img_path='media/'+uploaded_file.name 

		global img1_path

		img1_path=s.img_path



		import cv2

		import pytesseract 

		img=cv2.imread(pa)
		# import numpy as np
		# from PIL import Image
		# im_gray = np.array(Image.open(s.img_path).convert('L'))

		# thresh = 128
		# im_bool = im_gray > thresh
		# maxval = 255
		# im_bin = (im_gray > thresh) * maxval
		# img=Image.fromarray(np.uint8(im_bin))



		text=pytesseract.image_to_string(img)
		global textcod
		textcod=text
      
		s.img_content=text

		text=text.split('\n')

		d=[]

		for j in text:

			dd=j.strip()

			if(dd!=''):
				d.append(j) 

		text=d

		res_list=['main','#include','alignas', 'double', 'reinterpret_cast', 'alignof', 'dynamic_cast', 'requires', 'and', 'else', 'return', 'and_eq', 'enum', 'short', 'asm', 'explicit', 'signed', 'atomic_cancel', 'export', 'sizeof', 'atomic_commit', 'extern', 'static', 'atomic_noexcept', 'false', 'static_assert', 'auto', 'float', 'static_cast', 'bitand', 'for', 'struct', 'bitor', 'friend', 'switch', 'bool', 'goto', 'synchronized', 'break', 'if', 'template', 'case', 'import', 'this', 'catch', 'inline', 'thread_local', 'char', 'int', 'throw', 'char16_t', 'long', 'true', 'char32_t', 'module', 'try', 'class', 'mutable','typedef', 'compl', 'namespace', 'typeid','concept', 'new', 'typename', 'const', 'noexcept','union', 'constexpr', 'not', 'unsigned', 'const_cast', 'not_eq', 'using', 'continue', 'nullptr ', 'virtual', 'co_await ', 'operator', 'void','co_return', 'or', 'volatile', 'co_yield', 'or_eq', 'wchar_t', 'decltype', 'private', 'while', 'default', 'protected', 'xor', 'delete', 'public', 'xor_eq,' 'do', 'register','<iostream>','std','cout','cin' ]
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
		        if(d*2>lw and lw>2):
		            ans.append([d,i])
		    ans.sort(reverse=True)
		    final=[]
		    for j in ans:
		        final.append(j[1])
		    return final
		global word_sug1
		word_sug1=[]
		for i in text:
			g=i.split(' ')
			if(len(g)!=0):
				for j in g:
					word,wordarr=j,find_suggestion(j.lower(),res_list) 
					if(len(wordarr) and word!=wordarr[0]):
						word_sug=[word," , ".join(wordarr[:min(5,len(wordarr))])]
						word_sug1.append(word_sug)





		
	return render(request,'upload/upload.html',{'text':textcod,'img1':img1_path,'suggestion':word_sug1})
		
def Executed(request):
	code=''
	if request.method == 'POST':
		code=request.POST.get("my_textarea")
	# print('Hello Yukan1')
	f = open("/home/yukan/Documents/Sem 5/Summe Project/CamCode/Backend/upload/sample.cpp", "w")
	f.write(code)
	f.close()
	import subprocess
	# print('tgrrthvh')
	# from bs4 import BeautifulSoup
	# # markup = '''<html><body><div id="container">Div Content</div></body></html>'''
	# with open('upload/upload.html', 'r') as f:
	# 	markup = f.read()
	# print(markup)
	# soup = BeautifulSoup(markup, 'html.parser')
	  
	# #finding the div with the id
	# div_bs4 = soup.find('div', id = "content")
	
	# print(div_bs4.string)


	# subprocess.call(["g++","/home/yukan/Documents/Sem 5/Summe Project/CamCode/Backend/upload/sample.cpp"])
	
	e=subprocess.run(["g++","/home/yukan/Documents/Sem 5/Summe Project/CamCode/Backend/upload/sample.cpp"], stderr=subprocess.PIPE)

	p= subprocess.Popen("./a.out",stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)

	(output,err)=p.communicate()
	e=e.stderr.decode('utf-8')
	if(len(e)>1):

		output=e.replace("/home/yukan/Documents/Sem 5/Summe Project/CamCode/Backend/upload/sample.cpp","")

	else:
		output=output.decode()
	
	# # p_status=p.wait()
	# result = subprocess.run(["g++","/home/yukan/Documents/Sem 5/Summe Project/CamCode/Backend/upload/sample.cpp"], stderr=subprocess.PIPE)
	# print("Error :",result.stderr.decode('utf-8'))
	# output=""

	img1_path=""
	for file in os.listdir('/home/yukan/Documents/Sem 5/Summe Project/CamCode/Backend/media'):
		img1_path="/media/"+file
	print(img1_path)
	return render(request,'upload/upload.html',{'text':'','code':code,'output':output,'img1':img1_path})