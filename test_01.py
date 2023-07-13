#!/usr/bin/env python
# -*-coding:UTF-8 -*-
# date: 20230710



import os
import time

#1、发布版本：应用名称_预计发布时间_项目名称_版本号_release
#例如：Dataex_20230622_shdx_1.0.0_release.tar.gz；
#2、测试版本：应用名称_预计发布时间_项目名称_版本号_snopshot
#例如：Dataex_20230622_shdx_1.0.0_snopshot.tar.gz；
#分支命名规范:自动化生成分支名和分支冲突拦截检测;


# 在非py脚本路径下执行时使用
dirname = os.path.dirname(__file__)
basedir = os.path.abspath(dirname)
os.chdir(basedir)

now_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
branch_time = time.strftime("%Y%m%d", time.localtime())
tag_time = time.strftime("%Y%m%d", time.localtime())

#定义分支信息
dircode="D:\pycha\pycunzhu"
os.chdir(dircode)

git_url="git clone ssh://srd19302890819@code.srdcloud.cn:29418/dataProject/dataProject && scp -p -P 29418 srd19302890819@code.srdcloud.cn:hooks/commit-msg dataProject/.git/hooks/"
git_project="zy"
git_project1="ctzb"
product_version="1.0.0"
product_test="_snopshot"
product_hotfix="_hotfix"
git_specifications="branch_"+"项目启动时间"+"_"+"项目名称"+"_"+"版本号"+"_"+"分支标识"
git_branch_zy_snopshot="branch_"+branch_time+"_"+git_project+"_"+product_version+product_test + "(自研项目分支)"
git_branch_ctzb_snopshot="branch_"+branch_time+"_"+git_project1+"_"+product_version+product_test + "(集团总部项目分支）"
git_branch_ctzb_hotfix="branch_"+branch_time+"_"+git_project1+"_"+product_version+product_hotfix + "(总部紧急分支)"
git_branch_zy_hotfix="branch_"+branch_time+"_"+git_project+"_"+product_version+product_hotfix + "(自研紧急分支)"

#分支命名规范
print(git_specifications)
print(git_branch_zy_snopshot)
print(git_branch_ctzb_snopshot)
print(git_branch_ctzb_hotfix)
print(git_branch_zy_hotfix)

#标签命名规范
git_specifications1="版本号-"+"tag-"+"发布时间"+"-"+"项目名称"
git_project2="zy"
git_project3="ctsc"
product_version1="1.0.0"
git_tag_zy=product_version1+"-"+"tag-"+tag_time+"-"+git_project2
git_tag_ctsc=product_version1+"-"+"tag-"+tag_time+"-"+git_project3
print(git_specifications1)
print(git_tag_zy)
print(git_tag_ctsc)
#打包命名规范
git_specifications2="应用名称_"+"预计发布时间"+"_"+"项目名称"+"_"+"版本号_release"
git_project4="ctsh"
product_version2="1.0.0"
product_web="_release.tar.gz"
product_dafaflow="_snopshot.tar.gz"
git_pack_ctsh_relese="starlink-web_"+branch_time+"_"+git_project4+"_"+product_version2+product_web
git_pack_ctsh_snopshot="starlink-dafaflow_"+branch_time+"_"+git_project4+"_"+product_version2+product_dafaflow
print(git_specifications2)
print(git_pack_ctsh_relese)
print(git_pack_ctsh_snopshot)

