import os

# rename files based on the actual file name, excluding the additional kobocat 
# directories from name

files = len(os.listdir('.'))
i = 1

print('This directory has '+str(files)+' files.')
for filename_old in os.listdir('.'):
	filename, file_extension = os.path.splitext(filename_old)
	if file_extension == '.txt':
		parts = filename.split('%2F')
		# extract file name and remove trailing . added by kobocat
		nameonly = parts[len(parts)-1].split('.')[0]
		os.rename(filename_old, nameonly+'.txt')
		print(str(i)+'/'+str(files)+' done. renamed '+filename_old+' > '+nameonly+'.txt')
		i+=1
