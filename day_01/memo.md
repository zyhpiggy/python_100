## Day 1 Python零基础教程快速上手_全程干货+实用技巧小白必看
https://www.bilibili.com/video/BV1FT4y1R7sz?p=10&spm_id_from=pageDriver&vd_source=9a3365fff774e958354d6f2880eb6833

- 1、VS code 添加注释模板，Ctrl+Shift+p 进入命令面板，输入snippets,点击输入新建全局代码片段文件，输入代码片段名字，然后插入下述代码  
		 { 
			  // Place your 全局 snippets here. Each snippet is defined under a snippet name and has a scope, prefix, body and  
	          // description. Add comma separated ids of the languages where the snippet is applicable in the scope field. If scope  
	          // is left empty or omitted, the snippet gets applied to all languages. The prefix is what is  
	          // used to trigger the snippet and the body will be expanded and inserted. Possible variables are:  
	          // $1, $2 for tab stops, $0 for the final cursor position, and ${1:label}, ${2:another} for placeholders.  
	          // Placeholders with the same ids are connected.  
	          // Example:  
	             "Print to console": {  
	 	           "scope": "python",  
	 	           "prefix": "jude",  
	 	           "body":   
			         "\"\"\"",  
	 		         " * @Author:Jude",  
	             " * @Description:${1://TODO}",  
	             " * @Date:$CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE",  
			         "\"\"\"",  
	 	           ],  
	           }  
	          // 	"description": "Log output to console"  
	          // }  
            }  
- 2、使用了一些VS code的快捷键

   1）行增加缩进：ctrl + [
   
   2）行减少缩进：ctrl + ]
   
   3）向上复制一行：shift + alt + up
   
   4）向下复制一行：shift + alt + down
   
   5）删除行：Shift + Space
   
   6）代码格式化：shift + alt + f
- 3、关于浮点数的坑：
 0.1+0.2 输出结果是0.30000000000000004，这是编程语言浮点数显示的问题，所以尽量不要用浮点数进行直接运算
