博客地址：    http://www.cnblogs.com/cp-miao/p/5567115.html

计算器  :
	  一，def chen()  定义一个计算没有括号的值的结果
		 一.1，第一个判断，如果包含【*/】号，匹配进入，用re.search匹配到，并把值分开。
			1.2， 计算完把结果递归返回给 def chen.直到，计算完没有[*/]号为止。
			2， 如果是负数做加减，进入第二匹配，计算结果返回。
			3. 如果是加减法，用第三匹配计算总结果返回。
			4.return 总结果
	  
      二,while True  1.如果传过来的值包含括号，取出最括号里面的值，并传给 def chen()处理。
					 2.如果没有括号，直接传过去给 def chen()处理。接收结果打印
