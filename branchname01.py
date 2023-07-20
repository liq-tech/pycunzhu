import sys
from datetime import datetime
import subprocess

class AutoBranchName:
    def __init__(self, project_name, project_version, branch_identifier):
        self.project_name = project_name
        self.project_version = project_version
        self.branch_identifier = branch_identifier

    def generate_branch_name(self):
        # now = datetime.now()
        curtime = datetime.now().strftime("%Y%m%d")
        branch_name = f"branch_{curtime}_{self.project_name}_{self.project_version}_{self.branch_identifier}"
        return branch_name

    def output_branch_name(self):
        branch_name = self.generate_branch_name()
        print(branch_name)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("请提供参数：项目名称、项目版本和分支标识")
        sys.exit(1)
    project_name = sys.argv[1]
    project_version = sys.argv[2]
    branch_identifier = sys.argv[3]
    auto_branch_name = AutoBranchName(project_name, project_version, branch_identifier)
    if auto_branch_name.generate_branch_name():
        auto_branch_name.output_branch_name()
    else:
        print("分支名称格式错误，请检查后重新输入")
branch_command = f"git branch {auto_branch_name}"

result = subprocess.run(branch_command, shell=True, text=True).returncode
if result == 0:
   print(f"分支 {auto_branch_name} 创建成功！")
else:
   print(f"分支 {auto_branch_name} 创建失败，返回{result}")
