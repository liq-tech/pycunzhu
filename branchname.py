import subprocess
import datetime

class BranchNameGenerator:
   def __init__(self, project_name,version,identifier):
       self.project_name = project_name
       self.version = version
       self.identifier = identifier
   def generate_branch_name(self):
       project_time = datetime.datetime.now().strftime("%Y%m%d")

       branch_name = f"branch_{project_time}_{self.project_name}_{self.version}_{self.identifier}"
       return branch_name

generator = BranchNameGenerator("y","1.0.0","snopshot")
branch_name = generator.generate_branch_name()
# print(branch_name)
# 创建分支命
branch_command = f"git branch {branch_name}"

result = subprocess.run(branch_command, shell=True, text=True).returncode
if result == 0:
   print(f"分支 {branch_name} 创建成功！")
else:
   print(f"分支 {branch_name} 创建失败，返回{result}")


















