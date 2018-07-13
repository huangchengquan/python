
		
#循环
while True: #死循环
	
	#交互---》输入
    story = input("输出你的故事：" )

	#要求：故事不能超过6个字；len:长度
	if len(story) <= 6:

		#输出
		print("人生苦段，我用python!!",story)
		#终止循环
		break
	else:
		print("您输入的内容有误!重新说！")
print("很好！你的故事很精彩...")



