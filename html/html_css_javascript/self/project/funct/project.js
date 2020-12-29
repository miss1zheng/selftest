function textFunction()//改变文本或文本样式
{
	x=document.getElementById("textdemo");	// 找到元素
	x.innerHTML="Hello JavaScript!";	// 改变内容
	x.style.color="#ff0000";		  // 改变样式（这里时改变颜色）
}
function changeImage()//下面两张图片来回切换
{
	element=document.getElementById('imagedemo')
	if (element.src.match("blue")) //获取的图像名称由blue字样则执行此语句，否则执行else
	{
		element.src="./funct/white.png";
	}
	else
	{
		element.src="./funct/blue.png";
	}
}
function valueFunction()//若不是数字则有弹窗
{
	var x=document.getElementById("valuedemo").value;
	if(isNaN(x)||x.replace(/(^\s*)|(\s*$)/g,"")=="")//正则表达式，有些判断不出来的可做转换
	{
		alert("不是数字");//这里是实现弹窗功能
	}
}
function sumfunction()
{
	var x=0.0,y=0.0,z=0.0;

	x=document.getElementById("value_a").value;
	y=document.getElementById("value_b").value;
	var s=document.getElementById("suboradd").value;
	if(isNaN(x)||x.replace(/(^\s*)|(\s*$)/g,"")=="")
	{
		alert("a不是数字");
	}
	if(isNaN(y)||y.replace(/(^\s*)|(\s*$)/g,"")=="")
	{
		alert("b不是数字");
	}
	if(s=='+')
		z=parseInt(x)+parseInt(y);//parseInt：将字符串转换成十进制数字
	if(s=='-')
		z=parseInt(x)-parseInt(y);
	if(s=='*')
		z=parseInt(x)*parseInt(y);
	if(s=='/')
		z=parseInt(x)/parseInt(y);
	document.getElementById("value_sum").innerHTML = z;
}

