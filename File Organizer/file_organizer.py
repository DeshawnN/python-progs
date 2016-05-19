import os, glob, shutil, unicodedata

# Change to directory 
print 'Please Enter the path to the directory you want to organize (or Press enter to organize current directory): '
directory = raw_input()
if directory == '':
	directory = os.getcwd()
os.chdir(directory)

# Images
image_dir = './Images'
image_types = (u'*.jpg', u'*.jpeg', u'*.gif', u'*.png')

# Videos
video_dir = './Videos'
video_types = (u'*.mp4', u'*.avi', u'*.webm', u'*.flv', u'*.mkv', u'*.mpg')

# Music
music_dir = './Music'
music_types = (u'*.mp3', u'*.flac', u'*.wav')

# Documents
doc_dir = './Documents'
doc_types = (u'*.docx', u'*.txt', u'*.pdf', u'*.csv')

# Programs
prog_dir = './Programs'
prog_types = (u'*.exe', u'*.iso', u'*.msi')

# Zipped files
comp_dir = './Compressed'
comp_types = (u'*.zip', u'*.rar', u'*.gz', u'*.7z')

# Adobe files
adobe_dir = './Adobe'
adobe_types = (u'*.psd', u'*.psb', u'*.ai')

# Misc files
misc_dir = './Miscellaneous'
misc_types = (u'*.torrent', u'*.log')

# Directories to create tuple
directories_to_create = (image_dir, video_dir, music_dir, doc_dir, prog_dir, comp_dir, adobe_dir, misc_dir)

# If Directory doesn't exist, make directory.
for dirs in directories_to_create:
	if not os.path.exists(dirs):
		os.makedirs(dirs)
	# Do nothing
	else:
		pass

# Grab files
images, videos, music, documents, programs, compressed, adobe, misc = [], [], [], [], [], [], [], []

for files in image_types:
	images.extend(glob.glob(files))
	for image in images:
		# If aleady in a folder with Images in the name, skip moving files.
		if image_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(image, image_dir)
		except:
			continue

for files in video_types:
	videos.extend(glob.glob(files))
	for video in videos:
		# If aleady in a folder with Video in the name, skip moving files.
		if video_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(video, video_dir)
		except:
			continue

for files in music_types:
	music.extend(glob.glob(files))
	for music_file in music:
		# If aleady in a folder with Music in the name, skip moving files.
		if music_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(music_file, music_dir)
		except:
			continue

for files in doc_types:
	documents.extend(glob.glob(files))
	for document in documents:
		# If aleady in a folder with Documents in the name, skip moving files.
		if doc_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(document, doc_dir)
		except:
			continue

for files in prog_types:
	programs.extend(glob.glob(files))
	for program in programs:
		# If aleady in a folder with Programs in the name, skip moving files.
		if prog_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(program, prog_dir)
		except:
			continue

for files in comp_types:
	compressed.extend(glob.glob(files))
	for zipped in compressed:
		# If aleady in a folder with Compressed in the name, skip moving files.
		if comp_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(zipped, comp_dir)
		except:
			continue

for files in adobe_types:
	adobe.extend(glob.glob(files))
	for ado_file in adobe:
		# If aleady in a folder with Adobe in the name, skip moving files.
		if adobe_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(ado_file, adobe_dir)
		except:
			continue

for files in misc_types:
	misc.extend(glob.glob(files))
	for misc_file in misc:
		# If aleady in a folder with Miscellaneous in the name, skip moving files.
		if misc_dir[2::] in os.getcwd():
			break
		try:
			shutil.move(misc_file, misc_dir)
		except:
			continue

# If at the end of the scripts execution a created folder remains empty, delete that folder.
for dirs in directories_to_create:
	if os.listdir(dirs) == []:
		os.rmdir(dirs)