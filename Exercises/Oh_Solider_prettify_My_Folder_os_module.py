
import os


def solider(path,filename,format):
	
	all=os.listdir(path)
	
	all_files=[i for i in all if os.path.isfile(f"{path}{i}")]
	
	
	file_data=open(f"{os.path.join(path,filename)}")
	
	file_list=file_data.readlines()
	
	
	no=1
	
	for every_file in all_files:
		
		try:
		
			format_of_file=every_file.split(".")[1]
			
			name_of_file=every_file.split(".")[0]
			
			file_path=f"{os.path.join(path,every_file)}"
			
		except:#Error Handling If file format is incorrect or file is corrupted or many more reasons
			
			continue

		
		
		if name_of_file in file_list:
		
			continue
			
		elif f"{name_of_file}.{format_of_file}"==filename:

			continue
			
		elif format_of_file==format:
				
			no_format= f"{no}.{format_of_file}"
			
			new_name=f"{os.path.join(path,no_format)}"
		
			os.rename(file_path,new_name)
			
			no+=1
			
		else:
			
			new_name_of_file= f"{name_of_file.capitalize()}.{format_of_file}"
			
			
			new_name=f"{os.path.join(path,new_name_of_file)}"
			

			os.rename(file_path,new_name)


if __name__=="__main__":
			
	print("Welcome to 'Oh soldier Prettify My Folder'\n")
	
	path_input=input("\n Enter Folder path note:- There should be '/' at last\n\n")
	
	filename_input=input(f"\n Enter Filename (Only enter file name and it's extension not path) Be sure file should be in same directory or folder '{path_input}'\n\n")
	
	format_input=input("\n Enter format or extension to which you want to give special name like 1.mp3 to 100.mp3 'extensions should be [txt,mp3,py,jpg,pmg,pdf,etc..]'\n\n")
	
			
			
	solider(path_input,filename_input,format_input)
	
	print("Solider Prettified the Folder \n")
	
