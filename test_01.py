#
# -*-coding:UTF-8 -*-


import re
import datetime
import os
#1、发布版本：应用名称_预计发布时间_项目名称_版本号_release
#例如：Dataex_20230622_shdx_1.0.0_release.tar.gz；
#2、测试版本：应用名称_预计发布时间_项目名称_版本号_snopshot
#例如：Dataex_20230622_shdx_1.0.0_snopshot.tar.gz；
#分支命名规范:自动化生成分支名和分支冲突拦截检测;


# 在非py脚本路径下执行时使用
dirname = os.path.dirname(__file__)
basedir = os.path.abspath(dirname)
os.chdir(basedir)

dircode="D:\pycha\pycunzhu"
os.chdir(dircode)
git_url="git clone ssh://srd19302890819@code.srdcloud.cn:29418/dataProject/dataProject && scp -p -P 29418 srd19302890819@code.srdcloud.cn:hooks/commit-msg dataProject/.git/hooks/"
#specifications="branch_"+"项目启动时间"+"_"+"项目名称"+"_"+"版本号"+"_"+"分支标识"

#分支命名
curtime = datetime.datetime.now().strftime("%Y%m%d")
def auto_branch(project_name,version,identifi):
    if project_name and version and identifi:
       if identifi == 'snopshot' or identifi == 'hoxfix':
         branch_name = f'branch_{curtime}_{project_name}_{version}_{identifi}'
    else:
         branch_name = 'master'
    return branch_name

if __name__ == '__main__':
    branch_name = auto_branch(project_name='w',version='1.0.0',identifi='hoxfix')
    print(branch_name)

#标签命名

def auto_tag(versions,project_names):
    if versions and project_names:
        tag_name = f'{versions}-tag-{curtime}-{project_names}'
    else:
        tag_name = 'master'
    return tag_name

if __name__ == '__main__':
    tag_name = auto_tag(versions='1.0.0',project_names='ctsc')
    print(tag_name)


#打包命名
def auto_starlink(git_name,project_name2, versioni, identify):

    if git_name and project_name2 and versioni and identify:
        starlink_name = f'starlink-{git_name}_{curtime}_{project_name2}_{versioni}_{identify}'
    else:
        starlink_name = 'master'
    return starlink_name


if __name__ == '__main__':
    starlink_name = auto_starlink(git_name='s',project_name2='ctsh', versioni='1.0.0', identify='snopshot.tar.gz')
    print(starlink_name)

