import subprocess

subprocess.call(["g++","sample.cpp"])
p= subprocess.Popen("./a.out",stdout=subprocess.PIPE,shell=True)
(output,err)=p.communicate()
p_status=p.wait()
print(output.decode())
print(p_status)