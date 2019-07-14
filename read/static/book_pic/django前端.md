# Python应用工程师前端

补充知识:  url跳转参数的传递 以及静态页面参数传递

img:    <img src="/static/img/{{ data.user }}.png" alt="" height="30" width="26">

href参数的传递:

​		html:  <a href= {% url 'person' foo.id %}>     <a href= {% url '路由名'   参数 %}>

​		urls:   url(r'^person/(\d+)/', views.person_index, name='person'),

​		views: def person_index(request, user_id):

​							print(user_id)

参考: https://docs.djangoproject.com/es/1.9/ref/templates/builtins/#url

#前端第一部分



### 1 网站建站的流程

1.确定网站主题

网站主题就是你建立的网站所要包含的主要内容，一个网站必须要有一个明确的主题。

2.为网站选择域名  

 一个企业的网站域名被称为“网络商标”，一个与企业名称和形象相符的网站域名，是企业实现网络营销的前提。

3.网站空间服务器的选择

一个网站的建设需要有自己的网站空间，要选择合适的网站空间服务器，空间的大小主要根据网站的规模.网站的内容多少来选择。

4.规划网站 

网站规划包含的内容很多，如网站的结构.栏目的设置.网站的风格.颜色搭配.版面布局.文字图片的运用等。

5.制作网页

按照规划一步步地把自己的想法变成现实了，这是一个复杂而细致的过程。

6.上传测试 

网页制作完毕，最后要发布到Web服务器上，才能够让全世界的朋友观看。

7.维护更新

网站要注意经常维护更新内容，保持内容的新鲜。

 

### 2 网页的组成部分

HTML----相当于我们的毛坯房

CSS----网页的装修队

javascript----智能家居

 

### 3 html基础

#### 3.1 什么是网页？

​	一个HTML文件，就是一个网页。一个程序网页是无数的，每一个打开的页面都是算一个网页！

#### 3.2 什么是网站？

​	把所有的网站资源文件（HTML,CSS,JS,图片,视频等）整合到一起(的一个文件夹)。网站是包含了域名、主机、程序（无论京东、阿里、亚马逊等网站我们所看见的都是程序）。

#### 3.3 什么是html?

​	HTML 指的是超文本标记语言 (Hyper Text Markup Language) 。HTML 不是一种编程语言，而是一种标记语言 (markup language)，是网页制作所必备的。
​	“超文本”就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。
​	超文本标记语言的结构包括“头”部分（英语：Head）、和“主体”部分（英语：Body），其中“头”部提供关于网页的信息，“主体”部分提供网页的具体内容。



初期的网络诞生后，已经出现了许多HTML版本:

| 版本      | 发布时间 |
| --------- | -------- |
| HTML      | 1991     |
| HTML+     | 1993     |
| HTML 2.0  | 1995     |
| HTML 3.2  | 1997     |
| HTML 4.01 | 1999     |
| XHTML 1.0 | 2000     |
| HTML5     | 2012     |
| XHTML5    | 2013     |

#### 3.4 什么是xhtml

​	XHTML指可扩展超文本标记语言（标识语言）（EXtensible HyperText Markup Language）是一种置标语言，表现方式与超文本标记语言（HTML）类似，不过语法上更加严格。

#### 3.5 HBuilder开发工具

​	HBuilder是DCloud（数字天堂）推出的一款支持HTML5的Web开发IDE。HBuilder本身是一款功能丰富、集成开发环境、多平台开发的一款易学易用的开发工具，它可以实现emmet、sass、less自动编译，完整的代码提示、自动补全，极大地提高了开发效率。

**如何安装 HBuilder？**

​	HBuilder下载地址：在HBuilder官网http://www.dcloud.io/点击免费下载，下载最新版的HBuilder。

HBuilder目前有两个版本，一个是windows版，一个是mac版。下载的时候根据自己的电脑选择适合自己的版本。

**常用的快捷键：**

ctrl+D: 删除当前行     

ctrl+r: 运行

ctrl+a ：全选

ctrl+shift+F:整理代码

ctrl+/：注释

Alt+/：激活代码助手

ps:以上快捷键可能与输入法快捷键有冲突（工具->选项->常规->快捷键中可以自定义快捷键）。

#### 3.6建立站点

文件名规范

名称全部用小写英文字母.数字.下划线的组合， 其中不得包含汉字.空格和特殊字符； 必须以英文字母开头。

目的：规划网站的所有内容和代码，整合资源。

#### 3.7 html文档的基本结构

![1557143211(C:/Users/Administrator/Desktop/python%E5%BA%94%E7%94%A8%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%89%8D%E7%AB%AF%E9%83%A8%E5%88%86/python%E5%BA%94%E7%94%A8%E5%B7%A5%E7%A8%8B%E5%B8%88%E5%89%8D%E7%AB%AF%E9%83%A8%E5%88%86/assets/1557143318(1).jpg)](assets/1557143318(1).jpg)

```html
<!DOCTYPE html>命名文档类型
<html>说明我们写的是标记语言
	<head>文件头部(描述区)
	<meta charset=”utf-8”/>编码格式(gb2312/gbk中文编码)
	<title>html5</title>文件标题（显示在状态栏上的内容） </head>
	<body> 
        文件主体(所有要写的内容)
	</body>
</html>
```



#### 3.8 网页的调试工具

（1）PC端调试工具的使用 -浏览器          测试浏览器(Chrome,IE,Firefox)

（2）移动端调试工具Chrome可以测试移动端页面（有很多模拟器）

### 第一个网页

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8" />
		<title>第一个网页</title>
		<!--
			快捷键: ctrl + / 快速注释
			快捷键: ctrl + R 快速运行
			修改后需要保存: ctrl + S
			
			head通常用来放置页面加载信息
			     比如编码
			     比如适配信息
			通常还用来引入外部资源
			  比如css文件
			  比如js文件
			
			title是页面的标题
		-->
	</head>
	<body>
	   第一个网页
	 hello world
	</body>
</html>
```



### 01文本操作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>01文本操作</title>
	</head>
	<body>
		<!--快捷键: Tab快速补全健,  快速的生成标签以及结束标签 
			快捷键: shift + enter 快速生成  <br />
		转意字符 :  &lt; 表示<    &gt; 表示 > 
			在html中如果使用 空格字符,无论连着写多少个,只有一个有效
			&nbsp; 表示空格字符, 可以写多个
		-->
		今天早上有些人&nbsp;迟到   了,明天不允许迟到
		<h1>HBuilder-飞速编码的极客工具，超强的提示功能</h1>
		<h6>边改边看：一边写代码，一边看效果</h6>
		
		<!--p标签是用来标识段落的 -->
		<p>星道教育科学技术研究院&lt;是一家&gt;以互联网+、人工智能、云计算为载体，以践行三好 (好习惯、好成绩、好素养)综合培养优质成长为基础，是一家覆盖从青少年编程基础教育到人工智能高等教育课程设计研发，以及构建三好成长评价，岗位胜任力评价及信用建设体系，组织教育科技高层论坛，学生创新教育大赛，科技创新教育培训，教育科技课题申报与推广等研究单位，是中国七家允许从事科学技术教育的研究院之一，副省级特区资质研究院。</p>

		<p>为学生热爱<b>人工智能</b>编程，<i>探索</i>人工智能<u>科技</u>，综合<b><i>优质成长</i></b>和发展，构建学业，择业和创业更强大的竞争力提供信心与能力的保证！
		<hr />
		
		好好学习,<br />天天向上
	</body>
</html>
```



### 02列表

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>02列表</title>
	</head>
	<body>
		<!--
			我最佩服的姓马的?
			. 马蓉
			. 马化腾
			. 马冬梅
			. 马云

			无序列表: unorder list    ul
			有序列表 :  order list   ol
			列表项: list item    li
			
			自定义列表:dl  
			        dt  dd			
		-->
		<h2>我最佩服的姓马的?</h2>
		<ul>
			<li>马蓉</li>
			<li>马化腾</li>
			<li>马冬梅</li>
			<li>马云</li>
		</ul>
		<hr />
		
		<!--有序列表-->
		<h2>国家领导人</h2>
		<ol type="a" start="1">
			<li>习大大</li>
			<li>马克龙</li>
			<li>奥巴马</li>
			<li>安倍</li>
		</ol>		
		<hr />
		<!--自定义列表-->
		<dl>
			<dt>广东省</dt>
			<dd>深圳</dd>
			<dd>广州</dd>
			<dd>中山</dd>
			<dd>东莞</dd>
			
			<dt>江西省</dt>
			<dd>赣州市</dd>
			<dd>南昌</dd>
			<dd>九江</dd>
		</dl>
	</body>
</html>
```



### 03超链接和图片

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>超链接与图片</title>
	</head>
	<body>
		<a href="http://news.baidu.com/" target="_blank">百度新闻</a><br />

		<!--target常用属性说明：
			_blank：在新的窗口之中打开链接页面；
			_self：在自身窗口打开链接页面，默认；
			_parent：现在的页面如果没有父框架，一般使用这个与_self基本上是一样的。
			
		图片
			本地路径: 相对路径     . 同级目录,  .. 表示父级目录 
			绝对路径  完整的路径  windows: c:\xx.jpg   linux: /root/...
			 html中不需要转意          
			                网址
			       		       
		 	长度单位: px 像素 , 一个点的长度,  分辨率:如: 1920*1080 表示屏幕高度上有1920个点,宽度上有1080个点 
		-->
		<img border="2px" width="500px" height="380px" src="img/01.jpg" alt="加载失败" title="图面描述" /><br />
		<!--img也具有一些比较常用的其他元素：
		title： 这个属性是鼠标悬停在图片上，显示的提示信息；
		alt : 这个属性是当图片出现意外情况，图片没有正确显示的文本替换。-->

		<!--	<img src="img/00.jpg" alt="加载错误"/>-->
		
		<!--这样链接图片是不行的-->
		<img src="https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=python&step_word=&hs=0&pn=10&spn=0&di=192200&pi=0&rn=1" />
	</body>
</html>
```



### 04块标签

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>块标签</title>
		<style type="text/css">
			span{
				color: red;
			}
		</style>
		
	</head>
	<body>
		<!--
			span 块元素, 本身没有作用
			  使用span包裹的内容,可以很容易的提取出来进行操作
			  
			  div 块元素 ,容器元素,用来方便的划分区域,div是自上而下排列的
		-->
		
		今天大家来的一点都不早<br />
		今天大家来的<span>一点</span>都不早
		
		<div></div>
		
	</body>
</html>

```



### 05div划分区域

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>div划分区域</title>
	</head>
	<body>
		<div>导航条</div>
		<div>广告,轮播图</div>
		<div>产品划分</div>
		<div>合作伙伴</div>
		<div>网页版权信息等</div>
	</body>
</html>
```



### 06表格

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>07表格</title>
	</head>

	<body>
		<!--
		    ctrl+enter 表示快速换行
			
			表格
			tr表示一行
			td 表示行中的一个内容
			border 边框宽度
			cellspacing 外边距
			cellpadding  内边距
			
			编程语言中颜色的表现形式: 
			 1.直接使用系统提供的 颜色名词
			 2.使用颜色的具体值来表示
			   颜色是由 3 原色组成    RGB(红red,绿green,蓝blue)
			   R -   0 - 255   会用两个十六进制的数表示    00 - ff
			   G -   0 - 255
			   B -   0 - 255
			 颜色的表现形式: 是以 # 开头,每2位数表示一个颜色值     如: #000000 黑   #ffffff白  
			
		-->
		<!--<table border="1px" cellspacing="2px" cellpadding="20px">-->
		<table align="center" border="1px" bordercolor="#ffcccc" width="300px" height="300px">
			<tr align="center">
				<td align="center">姓名</td>
				<td>年龄</td>
				<td>地址</td>
			</tr>
			<tr align="center">
				<td>马云</td>
				<td>48</td>
				<td>杭州</td>
			</tr>
			<tr align="center">
				<td>王健林</td>
				<td>60</td>
				<td>大连</td>
			</tr>
			<tr align="center">
				<td>马化腾</td>
				<td>50</td>
				<td>深圳</td>
			</tr>
		</table>

	</body>

</html>
```



### 07表格的合并

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>表格的合并</title>
	</head>

	<body>
		<!--
			ctrl + D 快速删除一行
			colspan 代表占据 几列 
			rowspan 代表占据 几行
		-->
		<table border="2px" width="250px" height="250px">
			<tr align="center">
				<td colspan="2" rowspan="2"><img src="img/06.gif" width="150px" height="150px" /></td>
				<td>2</td>
			</tr>
			<tr align="center">
				<td>4</td>
			</tr>
			<tr align="center">
				<td>7</td>
				<td>8</td>
				<td>9</td>

			</tr>
		</table>
	</body>
</html>

```



### 08表单

表单的作用：用来收集用户的信息的;

1、表单框

<form name=“表单名称” method=“post/get”  action=“路径"> </form>

2、表单控件
​      <input type="" />

语法：
<input  type=""  name=""  value="" size=""  maxlength=" "    />

说明：
input：标记可以创建按钮、文本输入框、选择框等各种类型的输入字段。
name：属性标识表单域的名称；
type：属性标识表单控件的类型，大概有十几种；
Value：属性定义表单域的默认值，其他属性根据type的不同而有所变化。
maxlength：控制最多输入的字符数，
Size：控制框的宽度（以字符为单位）



1）文本框 <input type="text" value="默认值"/>

2)密码框 <input type="password" />

3)提交按钮 <input type="submit" value="按钮内容" />

4)重置按钮 <input type="reset" value="按钮内容" />

5)空按钮 <input type="button" value="按钮内容" />

6）单选按钮组 <input type="radio" name="ral" />男 <input type="radio" name="ral" checked="checked"/>(默认选中)女

7）复选框组 <input type="checkbox" name="" /> <input type="checkbox" name="" disabled="disabled" />

*disabled="disabled" (禁用) *  checked="checked"   (默认选中)

表单域下拉列表（菜单）
语法：

<select >  
     <option>下拉选项1</option>
     <option>下拉选项2</option>     …………
</select>
表单域多行文本定义：
语法：

<textarea  name=""  cols=""  rows="" > </textarea>

说明：
多行文本。rows属性和cols属性用来设置文本输入窗口的高度和宽度，单位是字符。 

 

**代码示例：**

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>表单</title>
	</head>

	<body>
		<!--
			alt + / 提示
			form 是表单
			action 用来指定用来提交的服务器地址
			method 用来指定请求方式
			 html中最常用的是 get和post, 总共约13种
			 get  获取数据,  直接将请求参数放在url的后面,快,不安全,携带数据量小(2k)
			 post 发送,上传数据  ,将请求数据封装在数据包里, 相对安全,携带数据量大
		-->
		<form action="http://www.baidu.com/" method="get">
			<!--登陆-->
			账号:&nbsp;&nbsp;<input type="text" name="username" value="xingdao@163.com" /><br /> 密码:&nbsp;&nbsp;
			<input type="password" name="passwd" value="123456" /><br />
			<input type="reset" value="重来" />
			<input type="submit" />
			
			<!--多选框-->
			<h3>爱好</h3>
			<input type="checkbox" name="likes" value="eat" /> 吃饭
			<input type="checkbox" checked="checked" name="likes" value="sleep" /> 睡觉
			<input type="checkbox" name="likes" value="playCode" /> 打代码
			
			<!--单选-->
			<hr />
			<h3>性别:</h3>
			<input type="radio" name="sex" value="man" /> 男
			<input type="radio" checked="checked" name="sex" value="women" />女
		</form>
	</body>
</html>

```



### 09选择器基本格式

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>选择器基本格式</title>
		<!--
			选择器的格式:
			 选择器{属性名:属性值;属性名:属性值;...}
		-->
		<style type="text/css">
			div {
				width: 100%;
				height: 300px;
				background-color: red;
			}
		</style>

	</head>
	<body>
		<div></div>
	</body>
</html>

```



### 10选择器的位置

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>选择器的位置</title>

		<style type="text/css">
			div {
				width: 100%;
				height: 300px;
				background-color: #FF0000 !important;
			}
		</style>

		<!--关联外部的css文件-->
		<link rel="stylesheet" type="text/css" href="css/选择器位置.css" />

	</head>

	<body>
		<!--style 最好不要写在标签里-->
		<div style="width: 100%;height: 300px;background-color: #ccffcc;"></div>
	</body>

</html>

```

#前端第二部分

### 01选择器

id选择器  使用#  最优先

类选择器  使用 .  次级优先

元素选择器  最后

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>01选择器</title>
		<style type="text/css">
			/*
			 在css中的注释   ctrl + / 
			 元素选择器格式 :  元素名{属性;}
			 如果该元素没有使用自定义的选择器或者自身设置的属性则使用标记的元素选择器
			 * */
			div{ 
				width: 200px;
				height: 200px;
				background-color: red;
			}
			
			/*
			 * id选择器格式:   #id名{属性},  注意需要以 "#" 开始, 使用的标签需要需要指定 id 属性 
			 * */
			#head{
				width: 300px;
				height: 300px;
				background-color: green;
			}
			
			/*
			 *id一般用来标识选择器的唯一性, 但是多数浏览器可以将使用了同一个id的标签渲染出来
			 * 
			 * 一般使用类选择器,来给一类标签设置属性
			 * 
			 * 类选择器格式: .class名{属性}   注意需要以"."开始, 使用标签的时候需要指定  class 属性
			 * */
			.one{
				width: 400px;
				height: 400px;
				background-color: blue;
			}
		</style>
	</head>
	<body>
		<div></div>
		<div id="head"></div>
		<!-- 快捷方式: #id名 按tab健 可以快速生成以 id名为id的div -->
		<!--<div id="head"></div>-->
		
		<div class="one">		</div>
		
		
	</body>
</html>

```



### 02使用多个选择器

**示例1：**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>使用多个选择器</title>
		<style type="text/css">
			
			/*
			 style 可以写多个选择器,  
			 * */
			.one{
				width: 100px;
			    
			}
			.two{
				height: 100px;
			}
			#three{
				background-color: red;
				
			}			
			
		</style>
		
	</head>
	<body>
		<!--可以同时使用多个类选择器, 多个类选择器之间用空格隔开
			可以使用多种选择器
			同时使用多个类选择器 会按照style内的顺序执行
		-->
		<div class="one two" id="three"></div>
        
	</body>
</html>
```

**示例2：**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			div{width: 300px;
				height: 300px;
			}
			.one{
				background: red;
			}
			.two{
				background: green;
				
			}
			.three{
				background: blue;
			}
			
			
		</style>
		
	</head>
	<body>
			<div class="one"></div>
			<div class="two"></div>
			<div class="three"></div>
		
	</body>
</html>
```



### 03伪类选择器

```
a:link {color: #FF0000}		/* 未访问的链接 */
a:visited {color: #00FF00}	/* 已访问的链接 */
a:hover {color: #FF00FF}	/* 鼠标移动到链接上 */
a:active {color: #0000FF}	/* 选定的链接 */
```

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>伪类选择器</title>
		<style type="text/css">
			/*
			  颜色的状态: 1.系统提供的颜色名
			          2.十六进制的颜色值  #ffffff
			          3.rgb(红,绿,蓝)  0-255
			            alpha
			          4.rgba(红,绿,蓝,透明度)  透明度的范围是 0-1    0.5半透明  
			 * 
			 * */
			
			a:link {
				color: red;
			}
			
			a:visited {
				color: green
			}
			
			a:hover {
				color: blue;
			}
			
			a:active {
				color: #ffcccc
			}
		</style>
	</head>

	<body>
		<a href="https://www.baidu.com/" target="_blank">超链百度搜索首页</a>
	</body>

</html>
```



### 04群组选择器

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>群组选择器</title>
		<style type="text/css">
			/*h2{
				color: red;
			}
			
			.one{
				color: red;
			}
			
			#two{
				color: red;
			}
			*/
			/*
			 群组选择器,将多个选择器放在一块, 每个选择器之间用  , 号隔开
			 * */
			
			h2,
			.one,
			#two {
				color: red;
			}
		</style>

	</head>

	<body>
		<h2>今天晚上要下雨了</h2>
		<p class="one">今天晚上吃鸡</p>
		<h5 id="two">不吃鸡了,学习才是硬道理</h5>
	</body>

</html>
```



### 05包含选择器

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>包含选择器</title>
		<style type="text/css">
			div {
				color: red;
			}
			/*
			 包含选择器
			 父标签名 子标签名   可以设置某个父标签下的子标签的样式, 是以 空格 连接的
			 * */
			
			div div {
				color: green;
			}
		</style>

	</head>

	<body>
		<div>
			父亲的财产
			<div>
				儿子的财产
			</div>
		</div>

	</body>

</html>
```



### 06通配符选择器

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>通配符选择器</title>
		<style type="text/css">
			/*
			    * 号 表示通配符选择器,可以匹配任何一个标签, 一般不使用
			 * */
			*{color: red;}
		</style>
	</head>
	<body>
		<h1 >今天晚上吃什么</h1>
		<p>大吉大利,晚上吃鸡</p>
		<div>不吃了，好好学习</div>
		
	</body>
</html>
```



### 07选择器权重

id                       100
class/属性/伪类  10
标签/伪元素         1
通配符                 0

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>选择符的权重(优先级)</title>
		<style type="text/css">
			/*
			 元素选择器权重为 :   0001
			 * */
			
			p {
				color: red;
			}
			/*
			 id选择器权重为 :   0100
			 * */
			
			#one {
				color: green;
			}
			/*
			 类选择器权重为: 0010
			 * */
			
			.two {
				color: blue;
			}
		</style>

	</head>

	<body>
		<p id="one" class="two">日照香炉生紫烟，遥看瀑布挂前川。<br/>飞流直下三千尺，疑是银河落九天。</p>
	</body>

</html>
```



### 08字体属性

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>08字体属性</title>
		<style type="text/css">
			.one{
				font-size: 24px;
			}
			
			/* 
			 em 相对长度 ,   1em = 16px
			 * */
			.two{
				font-size: 1.5em;
			}
			
			.color{
				color: red;
			}
			
			/*加粗*/
			.three{
				font-weight: bold;
			}
			/*
			 倾斜
			 italic
			 oblique 重一点的倾斜
			 normal正常字体
			 * */
			.four{
				/*font-style: italic;*/ 
				font-style: oblique;
			}
			
			/*
			 * 将文本转换成 大小写
			 * lowercase小写
			 * uppercase 大写
			 */
			.five{
				/*text-transform: lowercase;*/
				text-transform: uppercase;
			}
			.six{
				width: 600px;
				height: 300px;
				background-color: violet;
				
				/*位置*/
				text-align: center;
				
				/*vertical-align: middle; 没有效果,不好用*/
				line-height: 300px;
			}
			
			/*
			 添加下划线
			 underline 下滑钱
			 line-through 删除线
			 none 没有
			 * */
			#seven{
				text-decoration: none;
			}
			
			a{
				text-decoration: none;
			}
			
		</style>
	
	</head>
	<body>
		<p class="one">人生自古谁无死,留取丹心照汗青</p>
		<p class="two">人生自古谁无死,留取丹心照汗青</p>
		<p class="color">天苍苍，野茫茫，风吹草低见牛羊</p>
		<p >天苍苍，野茫茫，风吹<span class="three">草低</span>见牛羊</p>
		<p class="four">我要做一个安安静静敲代码的美男子</p>
		<p class="five">li 李  is a  GOOD  man</p>
		<div class="six">
			星小智很爱学习,小花花很喜欢
		</div>
		<p>小俊俊真的是<span id="seven">帅气</span></p>
		<!--
			超链接的下划线属性是默认设置在 text-decoration属性上的
		-->
		<a href="https://www.baidu.com/">星小智</a>
		
	</body>
</html>

```



### 09列表属性

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>列表属性</title>
		<style type="text/css">
			.one {
				/*
				 *图片格式:
				 * png 开发常用 ,androd,ios 常用
				 *   可以拉伸,拉伸后失真低
				 * jpg 压缩效率高 
				 * */
				/*列表符合属性*/
				/*list-style-type: circle;*/
				/*列表图片属性*/
				list-style-image: url(img/pay-dot.png);
				/*列表位置属性*/
				list-style-position: outside;
			}
			
			li {
				background-color: #ffcccc;
			}
			
			.two {
				/*综合使用: 每个属性之间用空格隔开, 可以颠倒顺序*/
				list-style: inside url(img/pay-dot.png);
			}
		</style>

	</head>

	<body>
		<h2>对女友要求</h2>
		<ul class="one">
			<li>女的</li>
			<li>身高167以上</li>
			<li>性格温婉</li>
		</ul>
		<hr />
		<h2>有什么好吃的</h2>
		<ul class="two">
			<li>火锅</li>
			<li>羊肉</li>
			<li>小笼包</li>
		</ul>

	</body>

</html>

```



### 10边框属性

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>边框属性</title>
		<style type="text/css">
			.one {
				width: 300px;
				height: 300px;
				/*综合使用*/
				/*border: 2px solid green;*/
				border-width: 2px 8px 16px 32px;
				border-style: dashed solid;
				border-color: red green blue yellow;
				/*
				 * 边框有四条边,给每个属性设置值时,可以设置1到4个参数
				 * 时钟原则
				 * 1个参数 --- 4个边都使用该参数
				 * 2个参数 --- 第一个参数表示上下的值, 第二个参数表示左右的值
				 * 3个参数  --- 第一个参数表示上的值, 第二个参数表示左右的值,第三个参数表示下边的值
				 * 4个参数  --- 遵循:  1上   2右  3下  4左
				 * */
			}
			
			.two {
				width: 300px;
				height: 300px;
				/*border-bottom: blue solid 10px;*/
				border-bottom-color: red;
				border-bottom-style: solid;
				border-bottom-width: 15px;
			}
		</style>

	</head>

	<body>
		<div class="one"></div>
		<div class="two"></div>
	</body>
</html>

```



### 11背景属性

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>背景属性</title>
		<style type="text/css">
			.one {
				border: 2px red solid;
				width: 400px;
				height: 400px;
				/*设置背景色*/
				/*background-color: #ffcccc;*/
				/*background: #ccccff;*/
			}
			
			.two {
				border: 2px green solid;
				width: 800px;
				height: 800px;
				background-image: url(img/02.jpg);
				background-repeat: no-repeat;
				/*背景图片的大小*/
				background-size: 100%;
				background-position: center;
			}
		</style>
	</head>

	<body>
		<div class="one"></div>
		<div class="two"></div>
	</body>

</html>

```



### 12浮动

**示例1 ：**

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>浮动</title>
		<style type="text/css">
			/*
			  浮动的块只能设置 左右方向
			 非浮动的块决定 上下方向
			 相当于2层
			 * 
			 * */
			
			.one {
				width: 50%;
				height: 300px;
				background: red;
				float: left;
			}
			
			.two {
				width: 50%;
				height: 300px;
				background: green;
				float: left;
			}
			
			.three {
				width: 100%;
				height: 300px;
				background: blue;
				float: left;
			}
		</style>

	</head>

	<body>
		<div>
			<div class="one"></div>
			<div class="two"></div>
			<div class="three"></div>
		</div>
	</body>

</html>

```

**示例2 ：**

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			/*
			   注意: 当修改浏览器的宽度时,
			    当浮动块的宽度超出浏览器的宽度时,文档流会重新对浮动块进行排序 
			 * 在浏览器范围外的浮动块,会依次去找高度最小的块, 浮动块会放在高度最小的块的下面
			 * 但是美中不足的是该快的位置会受到上一个块的高度影响
			 * */
			
			.one {
				width: 300px;
				height: 300px;
				background: red;
				float: left;
			}
			
			.two {
				width: 300px;
				height: 80px;
				background: green;
				float: left;
			}
			
			.three {
				width: 300px;
				height: 300px;
				background: blue;
				float: left;
			}
			
			.four {
				width: 300px;
				height: 200px;
				background: yellow;
				float: left;
			}
		</style>

	</head>

	<body>
		<div>
			<div class="one"></div>
			<div class="two"></div>
			<div class="three"></div>
			<div class="four"></div>
		</div>
	</body>

</html>

```

**示例3(错误示范) ：**

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>浮动bug</title>
		<style type="text/css">
			.one {
				width: 300px;
				height: 300px;
				background: red;
				float: left;
			}
			
			.two {
				width: 300px;
				height: 300px;
				background: green;
				float: left;
			}
			
			.three {
				width: 300px;
				height: 300px;
				background: blue;
				float: left;
			}
			/*
			 在浮动的末端加上一个空的块,
			 执行  clear: both; 清除浮动
			 * */
			
			.six {
				clear: both;
			}
			
			.five {
				width: 300px;
				height: 300px;
				background: blue;
			}
			
			.four {
				border: 2px yellow solid;
				/*在父级元素中添加*/
				/*overflow: hidden;*/
			}
		</style>

	</head>

	<body>
		<div class="four">
			<div class="one"></div>
			<div class="two"></div>
			<div class="three"></div>
			<div class="six"></div>
		</div>
		<div class="five"></div>
	</body>

</html>

```

#前端第三部分

### 01**标准盒子模型**

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>01标准盒子模型</title>
		<style type="text/css">
			.one {
				width: 300px;
				height: 300px;
				border: 2px solid green;
				padding: 10px 20px 30px 40px;
				margin: 10px 20px;
				/*border-width: {1,4};
				 padding,margin 可以设置 1到4个值, 遵守时钟原则 上 右 下 左
				 
				 padding-left: ; margin-left: ; 也可以分别去指定上下左右的大小
				 * */
			}
			/*
			 *标准的盒子模型:
			 *   组成:  content内容区域
			 *         padding内边剧
			 *         border 边框区域
			 *         margin 外边距
			 * 
			 * 注意: 
			 * 给一个区域设置的宽度高度,实际是作用在内容上的宽度和高度
			 * 实际的宽度/高度    是 content加上 padding*2 + border*2 
			 * margin算区域范围外的
			 * 
			 *  */
		</style>
	</head>

	<body>
		<div>
			<div class="one">深圳是个好地方</div>
		</div>
	</body>
</html>
```

### 02盒子模型外边距问题



```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>盒子模型外边距问题</title>
		<style type="text/css">
			#one {
				width: 800px;
				height: 800px;
				border: solid blue 2px;
			}
			
			.box {
				width: 200px;
				height: 200px;
				border: solid red 2px;
				margin: 10px;
				float: left;
			}
			
			.box2 {
				width: 200px;
				height: 200px;
				border: solid green 2px;
				margin: 20px;
				float: left;
			}
			/*
			 * 在每个块纵向排列时, 相邻外边距会重叠, 会取外边距大的值 ,相等时取一个
			 * 注意:在横向排列时, 相邻的外边距会相加,
			 * 需要注意标准盒子模型的边距计算
			 * */
		</style>
	</head>

	<body>
		<div id="one">
			<div class="box"></div>
			<div class="box2"></div>
		</div>
	</body>
</html>
```

### 03怪异盒子模型

注意: 怪异盒子不算内边距

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			#one {
				width: 800px;
				height: 800px;
				border: solid blue 2px;
			}
			
			.box {
				width: 200px;
				height: 200px;
				border: solid red 2px;
				padding: 3px;
				margin: 5px;
			}
			
			.box2 {
				width: 200px;
				height: 200px;
				border: solid green 2px;
				padding: 6px;
				margin: 5px;
				/*
				 使用怪异盒子模型
				 实际宽度width   是 content加上 padding*2 + border*2 
				 
				 * */
				box-sizing: border-box;
			}
		</style>
	</head>

	<body>
		<div id="one">
			<div class="box">现在认真学习，努力奋斗</div>
			<div class="box2">大吉大利,晚上学习</div>
		</div>
	</body>
</html>
```



### 04文本溢出

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>文本溢出</title>
		<style type="text/css">
			.one {
				width: 100px;
				height: 100px;
				border: solid 2px green;
				/*文本过长会超出文本区域
				 visible 默认的,默认会全部显示,超出部分显示在边框外
				 hidden 隐藏,内容会被裁剪,超出部分不可见
				 scroll 以滚动条的形式显示全部内容,可拖动滚动条
				 * */
				overflow: scroll;
			}
			
			.two {
				width: 300px;
				height: 500px;
				border: solid 2px green;
				text-overflow: ellipsis; 
				white-space: nowrap;
				overflow: hidden;
                /*文本过长会超出文本区域
				 text-overflow 超出部分以省略号代替
				white-space: nowrap 不换行   normal 换行
                overflow: hidden;  超出部分隐藏
				 * */
			}
		</style>
	</head>

	<body>
		<div class="one">
			在学习阶段把自己所学的知识点归档整理，方便复习，以后工作中对档案实体和档案信息进行管理，能够利用档案开展各项业务工作，是职业管理最基本的组成部分。
		</div>
		<p class="two">星道研究院教师和高级专家团队充分结合人工智能全球化的快速发展趋势，针对每一个岗位如何能具备出色胜任力而制定出分为（三好）好习惯、好成绩、好素养三大方面的18个岗位胜任力的测评要素点。</p>

	</body>
</html>
```



### 05标签类型

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>标签类型</title>
		<style type="text/css">
			.one {
				width: 200px;
				height: 200px;
				border: solid 2px green;
			}
			
			.two {
				width: 300px;
				height: 200px;
				border: solid 2px red;
			}
			
			.three {
				width: 200px;
				height: 200px;
				border: solid 2px blue;
			}
			
			span {
				width: 500px;
				height: 500px;
				/*display: block;
				 将行内元素转换成块级元素, 支持宽高,占据一行
				 * */
				border: solid 2px blue;
			}
			
			img {
				width: 200px;
				height: 200px;
				border: 2px red solid;
			}
			/*
			  元素的划分:
			   块级元素: block, 默认会占据一行,支持宽高属性
			  行内元素 : in line, 不会占据一行,默认会横向排列,当超出当前行的范围后,自动换行,  不支持宽高属性 
			  特殊元素: 不会单独占据一行,同时支持宽高属性, 比如img,
			 
			 注意:标签之间使用了换行时,可能出现空格间距问题
			 * * 
			 * */
		</style>
	</head>

	<body>
		<div class="one"></div>
		<div class="two"></div>
		<div class="three"></div>

		<input type="text" />
		<input type="password" />
		<span>文本</span>
		<img src="img/03.jpg" />
		<img src="img/06.gif" />

	</body>

</html>
```



### 06abssolute位置

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" lang="en">

	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<title>absolute定位</title>
		<style type="text/css">
			.box {
				width: 1000px;
				height: 1000px;
				position: relative;
			}
			
			.one {
				width: 200px;
				height: 200px;
				background: red;
				position: absolute;
				/*理解成以左上角为参考点*/
				left: 200px;
				top: 0px
				/*absolute位置是以当前浏览器的宽高来计算的*/
				/*理解成以右下角为参考点*/
				/*right: 0px;
				bottom: 0px;*/
				;
				/*
				   postsion:absolute 
				   绝对位置: 
				 * 默认相对于html左上角为坐标系原点
				 * 支持 left,top,bottom,right属性来设置位置
				 * 脱离文档流
				 * *absolute位置是以当前浏览器的宽高来计算的*
				 * 
				 * absolute参考的坐标原点是可以改变的
				 * 可以相对于父容器为坐标原点, 
				 * 会自动向上一级父容器中去寻找是否有 position属性,并且属性置为 relative或者absolute(一般不用),
				 * 如果找到了则会以找到父容器的左上角为坐标原地, 没找到会继续向上一级父容器中去找,如果没有找到,则以html为坐标原点
				 * 
				 * */
			}
			
			.two {
				width: 200px;
				height: 200px;
				background: green;
			}
			
			.three {
				width: 200px;
				height: 200px;
				background: blue;
			}
		</style>

	</head>

	<body>
		<div class="box">
			<div class="one"></div>
			<div class="two"></div>
			<div class="three"></div>
		</div>

	</body>

</html>
```



### 07relative位置

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>relative</title>
		<style type="text/css">
			.one {
				width: 200px;
				height: 200px;
				background: red;
			}
			
			.two {
				width: 200px;
				height: 200px;
				background: green;
				/*
				 * 不会影响原文档流,即不会影响原来的效果
				 * relative 是相对于自己原来位置的左上角为坐标原点
				 * */
				position: relative;
				left: 20px;
				top: 20px
			}
			
			.three {
				width: 200px;
				height: 200px;
				background: blue;
			}
		</style>

	</head>

	<body>
		<div class="one"></div>
		<div class="two"></div>
		<div class="three"></div>
	</body>

</html>
```



### 08fixed定位

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>08fixed定位</title>
		<style type="text/css">
			
			.one{
				width: 200px;
				height: 2000px;
				background: red;
				
			}
			
			.two{
				width: 200px;
				height: 200px;
				background: green;
				/*脱离文档流 类似于绝对定位
				 * 相对浏览器当前可视区域的绝对定位
				 */
				position: fixed;
				bottom: 0px;
				left: 0px;
				/*position:
				 * staic: 默认的, 不会脱离文档流, 不支持top,left,bottom,rigth属性
				 * absolute,relative,fixed 都支持top,left,bottom,rigth属性
				 * absolute,fixed 绝对位置,会脱离文档流
				 * relative 不会影响原文档流
				 * */
			}
			
			.three{
				width: 200px;
				height: 200px;
				background: blue;
				
			}
			
			
		</style>
	</head>
	<body>
		    <div class="one"></div>
			<div class="two"></div>
			<div class="three"></div>
	</body>
</html>
```



### 09z-index属性

z-link: 谁的数字大谁在表层 

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			.one {
				width: 200px;
				height: 200px;
				background: red;
			}
			
			.two {
				width: 200px;
				height: 200px;
				background: green;
				position: relative;
				left: 20px;
				top: 20px;
				z-index: 2;
			}
			
			.three {
				width: 200px;
				height: 200px;
				background: blue;
				position: relative;
			}
		</style>

	</head>

	<body>
		<div class="one"></div>
		<div class="two"></div>
		<div class="three"></div>
	</body>

</html>

```



### 10始终居中

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>始终居中</title>
		<style type="text/css">
			.one{
				height: 2000px;
				width: 100%;
			}
			/*.content{
				width: 200px;
				height: 200px;
				background: #ffcccc;
				position: fixed;
				right: 0px;
				bottom: 50%;
				margin-bottom: -100px;
			}*/
			.content{
				width: 200px;
				height: 200px;
				background: #ffcccc;
				position: fixed;
				right: 0px;
				/*
				 calc 是css3中,可以用来计算一些值  
				  -  两边要有 空格
				 * */
				
				bottom: calc(50% - 100px);
			}
			
		</style>
	</head>
	<body>
		<div class="one"></div>
		<div class="content">星道-人工智能，决胜未来</div>
	</body>
</html>

```



### 11锚点连接

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title></title>
		<style type="text/css">
			.head{
				width: 100%;
				height: 100px;
				background: #ffcccc;
			}
			.bannar{
				width: 100%;
				height: 250px;
				background: #ccffcc;
			}
			.content{
				width: 100%;
				height: 800px;
				background: #ffff00;
			}
			.foot{
				width: 100%;
				height: 100px;
				background: gray;
			}
		</style>
		
	</head>
	<body>
		<div>
		    <div class="head"  id="head"></div>
		    <div class="bannar"></div>	
		    <div class="content" id="content"></div>
		    <div class="foot">
		    	<a href="#head">返回顶部</a>
		    	<a href="#content">返回内容</a>
		    </div>
		</div>
	</body>
</html>

```



### 12js基础（hello world）

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>JavaScriptHelloWorld</title>
		<script type="text/javascript">
			// 单行注释   alert是一个函数, 用来弹出一个警告窗口
			
			/*多行注释       ctrl + shift + /
			 * js 在加载页面时会执行
			 * */
			alert("细思极恐: 怎么又学hello world")
			//在浏览器的控制台打印信息
			console.log("Hello world")
			
			document.write("<h1>细思极恐:感觉很难，但是我用心学就能学会</h1>")
			
		</script>
	</head>
	<body>
	</body>
</html>

```



### 13js的引入方式&变量创建

django数据传递给json  <https://code.ziqiangxuetang.com/django/django-json-templates.html>

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>js的引入方式和变量的创建方式</title>
		<!--引入外部的js文件  
			<src  可以快速的引入外部js文档
			-->
		<script type="text/javascript" src="js/content.js" >
		</script>
		
		<script type="text/javascript">
			var name;
			
			//js是弱类型语言
			name = "团团";
			name = 1;
			
			var age = 12,address="成都";
			console.log(name);
			console.log(age);
			console.log(address);
		</script>
		
	</head>
	<body>
	</body>
</html>


```



#前端第四部分

js 的基本了解 : <http://www.w3school.com.cn/js/js_syntax.asp>

### 01数据类型

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>数据类型</title>
		<script type="text/javascript">
			var name = "小汤圆";
			var age = 23;
			var isHaveGirlFirend = false;
			var address = "杭州";
			//ctrl + shift + R 快速复制一行
			var address = null;
			console.log(name)
			console.log(age)
			console.log(isHaveGirlFirend)
			//查看数据类型
			console.log(typeof name)
			console.log(typeof age)
			console.log(typeof isHaveGirlFirend)
			//特殊的数据类型
			
			//变量最好先定义再使用
			console.log(address)
			//变量没有定义时,是特殊的类型 是 undefined
			//特殊的数据 null,null的类型是object类型
			console.log(typeof address)
			
			//判读
			//注意: null的值与 undefinded的值一样,类型不一样
			console.log(null == undefined)
			console.log(typeof null ==  typeof undefined)
			
			//浮点数
			var heigth = 12.3
			var heigth = .3
			//浮点类型占据空间比整型大,会自动将12.0后的0舍弃,转换成整型
			var heigth = 12.0
			console.log(heigth)
			
			//注意: 
//			var number = 10/3

			//			特殊: Infinity 无穷大
//			var number =  10/0
			//NaN    not a number 不是一个数
			var number = 0/0
			//NaN
			var number = 10/0*0
			console.log(number)
			
		    console.log(NaN == number)
		    //判断是否是一个 NaN
		    console.log(isNaN(number))
			
			
			//数据类型转换
			//转换成字符串 
			var weigth = 12.11
			var strW = String(weigth)
			//可以转换成字符串,  数字可以和字符串拼接
			var strW = weigth + ""
			console.log(typeof strW)
			console.log(strW)
			
			//转换成数字: 转换成float用parseFloat, 转换成int 用parseInt()
			var phoneNumber = "a123.92a"
//			var number = parseInt(phoneNumber)
			var number = parseFloat(phoneNumber)
			
			console.log(typeof number)
			console.log(number)
			
			/*boolean
			 * 非0即为真, 非空即为真
			 * null, undefined
			 * NaN
			 * */
			console.log(Boolean(NaN))
		</script>
	</head>
	<body>
	</body>
</html>
```



### 02 运算符

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>运算符</title>
		<script type="text/javascript">
			/*
			 * ==  表示判断值是否相等
			 * === 当 两者 值相等,且类型也一样时,返回true
			 * !==
			 * !=
			 * */
			var age = "12";
			var number = "12";
			console.log(age == number)
			console.log(age === number)
			
			/*
			 *   &&  逻辑与 相当于python中的  and
			     ||   逻辑或  相当于 python中的  or 
			          遵循短路原则
			 * */
			
			
			/*
			    a++ a先拿出用,再加, ++a 先加,再用 , --a,a--
			   表示: a =a+1, a=a+1,a=a-1,a=a-1
			   
			 * */
			var a = 10;
			console.log(a++)//10
			console.log(a)//11
			console.log(++a)//12
			console.log(a)//12
		</script>
	</head>
	<body>
	</body>
</html>
```



### 03分支语句

```html
<!DOCTYPE html>
<html>

	<head>
		<meta charset="UTF-8">
		<title>03分支语句</title>
		<script type="text/javascript">
			/*
			 * */
			/*if(判断表达式){
				判断语句
			}*/
			isLike = false;
			if(isLike) {
				console.log("喜欢大熊猫")
			} else {
				console.log("不喜欢小灰灰")
			}
			//			console.log("跳出来的")

			/*if(){
			 * 	
			 * }
			 * else if(){}
			 * else if(){}
			 * else()
			 * */
			var age = 25;
			if(age < 20 && age > 0) {
				console.log("青少年")
			} else if(age < 30 && age >= 20) {
				console.log("中年")
			} else if(age < 40 && age >= 30) {
				console.log("老年")
			} else {

			}

			/*
			 switch语法
			 * */
			classNumber = 9

			switch(classNumber) {
				case 1:
					console.log("1班");
					break;
				case 2:
					console.log("2班")
					break;
				case 3:
					console.log("3班")
					break;
				case 4:
					console.log("4班")
					break;
				default:
					console.log("你不属于xx班")
					break;
			}

			//三目运算符
			//  判断表达式 ? res1:res2   如果判断表达式成立, 则返回结果1,如果不成立返回结果2
			className = "2"
			res = className == "1" ? "python1" : "python2"
			console.log(res)
		</script>
	</head>

	<body>
	</body>

</html>
```



### 04循环语句

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>循环语句</title>
		<script type="text/javascript">
			/*while,do wile, for 
			 * */
			/*1+......+100*/
			/*var number = 1;
			var sum = 0
			while(number <= 100){
				sum += number
				number++;
			}
			console.log(sum)
			*/
			
			//先执行在判断,第一次没有判断
		/*	var number = 101;
			var sum = 0
			do{
				sum += number
				number++;
			}while (number <= 100);
			console.log(sum)*/
		
		/*
		 	格式: for(申明变量并设置初始值;判断表达式;计数表达式){
		 		循环体
		 	}
		 * */
		var sum = 0;
		
		for(var i = 1;i <= 100;i++){
			sum += i 
		}
		console.log(sum)
		</script>
	</head>
	<body>
	</body>
</html>
```



### 05值的位置交换

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>值的位置交换</title>
		<script type="text/javascript">
			var a = 1;
			var b = 2;
			/* 想让a 和 b的值进行交换 */
//			python的写法: a,b = b,a;
			
			//使用的中间变量
//			var tem = a
//			a = b;
//			b = tem;
			
			//在不引入新的变量的情况下交换值
			a = a + b;
			b = a - b;
			a = a - b;

			console.log(a);
			console.log(b)
			
			
		</script>
		
	</head>
	<body>
	</body>
</html>
```



### 06数组的操作

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>数组的操作</title>
		<script type="text/javascript">
			//创建或者定义一个数组
			var arr = new Array()
			//创建一个空的数组
			var arr = Array()
			//如果有一个参数,表示创建 该数值长度的数组
			var arr = Array(5)
			
			//如果有多个参数,则这多个参数会当作数组的元素
			var arr = Array(5,6,7)
			//可以以  [元素1,元素2,... ]的形式创建 
			var arr = [1,2,3,4,5,6,7]
			
			//索引从0开始
			
			console.log(arr)
			console.log(typeof arr)
//			arr.length 表示获取数组的长度
			console.log(arr.length)
			
			//增
			//在数组的末尾加,可以添加一个值,也可以多个,
			arr.push(10)
			arr.push(10,11,12)
			
			//在数组的前端加数据,可以加多个, 
			//加入数据后,原数据会向后移
			arr.unshift(20,20)
			
			//在数组的某个位置插入数据
			arr.splice(3,0,33)
			//第一个参数表示要插入的位置, 第二个值表示插入的位置删除几个元素,第三个参数表示用来替换的值
			//从第3个往后,表示的是要插入的值
			arr.splice(3,1,33,44)
			
			//删 -- 数据结构: 队列,栈
			//从数组的末尾删除数据,并返回删除的值
			var data = arr.pop()
			//从数组的前端删除数据, 并返回删除的值, 后方的数据会向前移动
			var data = arr.shift()
			//从指定位置删除数据, 并返回删除(可以删除多个)的值的列表
			var data = arr.splice(3,1)
			
			console.log(data)
			//改 
			arr[1] = 222;
			//角标超出范围后,相当于在对应的位置,插入了数据, 数组的长度也会随之改变
			arr[10] = 10000
			
			//查
			var data = arr[2];
			//越界后,取出的值是 undefined, 不会报错
			var data = arr[12];
			
			//截取  
			//参数1是起始位置, 参数2是结束位置  , 包前不包后
			var data = arr.slice(1,3)
			
			console.log(data)
			
			console.log(arr)
			console.log(typeof arr)
			console.log(arr.length)
			
			//数组拼接
			var arr1 = [0,1,2];
			var arr2 = [3,4,5];
			var arr3 = arr1.concat(arr2)
			console.log(arr3)
			
		</script>
	</head>
	<body>
	</body>
</html>
```



### 07数组的排序

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>数组的排序</title>
		<script type="text/javascript">
			var arr = [9,2,1,12,4,7,45,2,8,88,6]
			
			//定义一个函数来申明那个数在前,那个数在后
			function compare(value1,value2){
				
				if(value1 < value2){ //从小到大-- 不换位置 --返回 -1,0表示不交换位置
					return -1;
				}else{
					return 1;  //返回1表示交换位置
				}
				
				
			}
			
			//排序 sort()是从小到大排序,默认是按照字符编码依次排序, 
//			var arr2 = arr.sort()
			var arr2 = arr.sort(compare) 
			//reverse反转
//			var arr2 = arr.sort().reverse()
			console.log(arr2)
			
			
		</script>
	</head>
	<body>
	</body>
</html>
```



### 08函数的定义

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>函数的定义</title>
		<script type="text/javascript">
			//定义函数以function 关键字开始, 后面跟的是函数名, 函数名是自己定义的,遵守标识符命名规则
			function add(a,b){
				console.log("a:"+a)
				console.log("b:"+b)
				return a+b;
			}
			
			//调用,调用时可以传与函数定义不一样个数的参数, 传递的参数会按照顺序依次传递给定义的函数的参数中
//		    add(100,200)
		    var res = add(100,200)
			console.log(res)
			
			
			
		</script>
	</head>
	<body>
	</body>
</html>
```



### 09 dom的简单使用

```html
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>dom的简单使用</title>
		<script type="text/javascript">
			window.onload = function(){
//				var data = document.getElementById("one")
//				console.log(data)
				//结果是obejct 类型
//				console.log(typeof data)
				//获取到元素中的内容
//				content = data.innerHTML
//				console.log(content)
				//设置元素中的内容
//				data.innerHTML = "细思极恐: 貌似考不过30分"
				
//				console.log(data.tagName)
//				console.log(data.id)
//				console.log(data.innerHTML)
//				data.className = "h2style"
//				console.log(data.className)
//				
				//结果是数组
				elements = document.getElementsByTagName("h4");
//			    length = elements.length()

				for(var i = 0;i<elements.length;i++){
					elements[i].className = "h4xxx";
				}
//				document.getElementsByClassName()
				
				
			}
		</script>
		<style type="text/css">
			.h2style{
				color: red;
			}
			
			.h4xxx{
				color:blue;
			}
		</style>
		
	</head>
	<body>
		<h2 id="one">杭州西湖</h2>
		<div>
			<h4>水光潋滟晴方好</h4>
			<h4>山色空蒙雨亦奇</h4>
			<h4>欲把西湖比西子</h4>
			<h4>淡妆浓抹总相宜</h4>
		</div>
	</body>
</html>



```



