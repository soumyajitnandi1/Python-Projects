import os, shutil as sh

print("\tThese app is made to copy all your 'apk' files present in given path & in all subdirectories  inside the path to Android 'App' folder also present in that path.\n\tIf not present  then will be created if any apk(s) is found & then all the apks will be copied\n\n\t For Whole Phone Memory enter : 'ALL' \n\tOr give any valid path to separate all 'apk(s)' inside the path & all its subdirectories.")

whole_memory_path='/storage/emulated/0'
input_path=input("\tPath : \n\t")
if input_path=='ALL' :
	working_path=whole_memory_path
elif os.path.exists(input_path) :
	working_path=input_path
else :
	print('\tInvalid Input or No Such Directory ! \n\t')
	print('Program is being finished . . . . . .')
	exit()
print('Please wait . . . . . . . .')
all_items=os.walk(working_path)
for paths,folders,files in all_items :
	os.chdir(paths)
	p=working_path
	for file in files :
		if file.endswith('apk') :
			if  not os.path.exists(f'{p}/Android Apps') :
				os.mkdir(f'{p}/Android Apps')
			if not os.path.exists(f'{p}/Android Apps/{file}') :
				sh.copy(f'{file}',f'{p}/Android Apps')
print(f"\t\nAll 'apk' files present in '{p}' path & in all its subdirectories were copied to 'Android Apps' folder present in  '{p}'. ")