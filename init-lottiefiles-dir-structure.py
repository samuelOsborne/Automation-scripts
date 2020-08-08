import os
import sys
import shutil
from os import path

walk_dir = sys.argv[1]

copy_jsons = sys.argv[2]

copy_aep = sys.argv[3]

delete_original_dossier = sys.argv[4]

aep_path = None

subdir_paths = []

if path.isdir(os.path.abspath(walk_dir)) is False:
	print(os.path.abspath(walk_dir) + " does not exist.", file=sys.stderr)

for root, subdirs, files in os.walk(walk_dir):
	print('--\nroot = ' + root)
	for subdir in subdirs:
		print('\t- subdirectory ' + os.path.join(root, subdir))
		subdir_paths.append(os.path.join(root, subdir))

	for filename in files:
		file_path = os.path.join(root, filename)
		print('\n\t- file %s (full path: %s)' % (filename, file_path))
		if filename.endswith('.aep'):
			aep_path = os.path.join(walk_dir + '\\' + filename)
			print('\t\t\t- aep filepath : ' + aep_path)
		if filename.endswith('.json'):
			new_dir = os.path.join(walk_dir + '\\' + os.path.splitext(filename)[0])
			print('\n\t- Creating : ' + new_dir)
			os.mkdir(new_dir)
			if (copy_jsons == 'true') or (copy_jsons == 'True') is True:
				json_path = os.path.join(root + '\\' + filename)
				print('\n\t- Copying ' + json_path + ' to ' + new_dir)
				shutil.copy2(json_path, new_dir)
			if (copy_aep == 'true') or (copy_aep == 'True') is True:
				if aep_path is not None:
					print('\n\t- Copying aep file ' + aep_path + ' to ' + new_dir)
					shutil.copy2(aep_path, new_dir)
				else:
					print("\n\t- No AEP found!", file=sys.stderr)

# Error because the subdirs are saved to the arrays ex: '/vault/fill/'

if (delete_original_dossier == 'True') or (delete_original_dossier == 'true') is True:
	for subdir in subdir_paths:
		print("\n\t- Deleting subdir : " + subdir)
		shutil.rmtree(subdir)
