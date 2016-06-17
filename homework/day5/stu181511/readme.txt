运行环境：python 3.5
博客地址：http://www.cnblogs.com/nigel-woo/p/5559676.html


文件说明：
	本次作业是在DAY3作业的购物车基础上增加用户登录、注册、删除、修改密码的功能。
	作业中的ShoppingMall.py文件与DAY3中一样，是原有的购物车功能的实现的一些类。本次新增添的功能主要在LoginUser.py文件中。

	LoginUser.py中主要实现了LoginUserAbs，LoginUserContxt，LoginUserConf，LoginUserJson四个类。

	LoginUserAbs是基类，实现了用户登录、注册、删除、修改密码等方法的业务逻辑。我将用户分为两类，普通用户和管理员。用户登录以后只能新注册普通用户，并且普通用户没有权限删除其他用户。用户只能更新自己的密码，并且在更改密码后需要重新登录。管理员可以删除自己的账号，删除后需要用其他账号重新登录。

	LoginUserContxt类是将用户信息存储在txt文件中的实现。普通用户存储在/cfg1/userConfig.txt中，管理员存储在adminUserConfig.txt中。存储形式为每行都是如“444&555”的形式，&前为用户名，&后为密码。
	
	LoginUserConf类是将用户信息存储在conf文件中，通过python的configparser库来实现的。所有用户信息都存储在userInfo.conf中。conf中的每个sections名字（[]中的字符）即为用户名，admin_flag值为0的是普通用户而值为1的是管理员。
	
	LoginUserJson类是将用户信息存储在json文件中，通过python的json库来实现的。所有用户信息存储在userInfo.json中，字典的键为用户名，值里的列表第一个元素是密码，第二个元素值为0的是普通用户，值为1的是管理员。

	由于其他的业务逻辑完全相同，搜易四个类都只重写了基类里从文件读取信息和将增删改的信息存储回文件的方法。
	
	
使用方法：
	运行入口在exercise1.py中，通过ArgumentParser库实现了根据命令行调用时选择不同存储实现的方法。入参为"-t"，可选值分别为"txt", "conf", "json"，分别对应上述三个子类。
	选择一个开始运行以后，控制台会输出如下：
	Initalize over
	id   command   
	1    Login     
	2    register  
	3    show commands
	4    leave     
	Please input command:
	这里根据命令id输入命令，分别是登陆，注册，显示所有命令，离开。修改密码和删除用户的功能都是必须在登陆后才能使用。
	登陆的用户名和密码必须正确，具体可以到上面提到的配置文件中查看。
	新注册用户必须重复两次密码且必须相同，新的用户名不能和老的已有的重复。用户登录以后只能新注册普通用户。
	每个实例里的属性user_dic是一个存储用户信息的字典，键为用户id，之为列表，第一个值为密码，第二个值标识是否管理员。普通用户值为0，管理员为1。（其实这个字典的形式，和userInfo.json完全一样，第三种实现就是直接把该json读出以后直接load成字典。）
	
	在成功登陆以后，控制台会输出如下：
	id   command   
	1    recharge  
	2    show property
	3    show all products
	4    add product to cart
	5    show your shopping cart
	6    remove product from cart
	7    buy! buy! buy!
	8    Change password
	9    delete user
	10   show commands
	11   leave     
	Please input command:
	其中命令8与9是这次新实现的功能，即改变密码与删除用户。用户只能改变自己的密码，在改变密码前会需要重新输入正确一次原始密码，并且在更改密码后需要重新登录。
	普通用户无法删除其他用户，管理员可以删除自己的账号，删除后需要用其他账号重新登录。
	leave离开命令可以主动回到上级登陆的选择单。
	 