一、博客按照如下文档结构编排。

	（一）微机原理

	（二）操作系统
 
	（三）数据结构
 
	（四）python之c语言源码
 
	（五）python知识点结构
		
		博客地址：1）http://www.cnblogs.com/lx63blog/articles/5538317.html
 
	（六）网络通讯原理
 
	（七）python各个版本差异（持续更新中）
 
	（八）常用小技巧

		博客地址：1）http://www.cnblogs.com/lx63blog/articles/5538317.html 
				增加了一些优化代码的思路，和某些特殊常见问题的代码实现方法。总结了一些经典的问题。
 
	（九）疑问总结

		博客地址：1）http://www.cnblogs.com/lx63blog/articles/5494947.html

二、代码

        ***highlights：

	1）练习题3-7都是要求输入一个string，list或tuple，而用raw_input输入接收到的都是一个字符串，所以无法满足输入list等类型的需求。

	   由于调试有一定的工作量和重复操作，所以只对习题3,4做了优化。即测试者可以输入您想输入的所有序列，string，list，tuple都可以，然后正常返回3,4题目功能结果。

	2）第八题要求实现递归，作业从某些实际场景出发，考虑到可能会出现不允许修改原功能代码的情况，所以使用到装饰器。这样就能对现有的功能进行任意的耦合与扩展。


	2.1、代码功能
	
	共7个py文件，分别对应以下功能。
	
	1）写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数                                    //文件名 t2.py

        2）写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。                                             //文件名 t3.py

	3）写函数，检查用户传入的对象（字符串、列表、元组）的每一个元素是否含有空内容。                                //文件名 t4.py

	4）写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。                 //文件名 t5.py

	5）写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。                //文件名 t6.py

	6）写函数，检查传入字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。     //文件名 t7.py
	
	7）写函数，利用递归获取斐波那契数列中的第 10 个数，并将该值返回给调用者。                                      //文件名 t8.py
	
	2.2、运行代码

	每个程序都提供了可以循环测试该函数代码的功能，即运行代码后，会提示输入，输入‘q’退出测试。其余任意键都会循环测试该功能代码。

三、作业题

	第一题，在博客中呈现。博客地址：http://www.cnblogs.com/lx63blog/articles/5494700.html
	