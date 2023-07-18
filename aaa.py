from time import strftime
import random
import re


class Get_git_Path():
    def project_name(self):
        list1 = ['a','b','c']
        value = random.choice(list1)
        return value

    def git_path(self):
        list2 = ["snopshot", "hoxfix"]
        value = random.choice(list2)
        return value

    def get_name(self,version,time=strftime("%Y%m%d")):
        str1 = "branch"
        return str1+"_"+time+"_"+self.project_name()+"_"+str(version)+"_"+self.git_path()

if __name__ == '__main__':
    a = Get_git_Path()
    name = a.get_name("1.0.0")
    print(name)





















