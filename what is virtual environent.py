#Virtual environment is a bit difficult topic in python, what it basically does is that, lets say i have a package pandas and i have the version 1 of it installed on my computer, however my friend has pandas 2 installed on his computer. I want to make a project for him using pandas, and if i use pandas 1 then he will have to install it. This is true if my code is uses the pandas installed on my computer. But what if I create a sort of virtual environment where when i write the code and give it to my friend pandas 1 would already be installed on it so he doesnt have to worry. Similarly he can create a virtual environment and send the code in it to me where he could have already installed pandas 2 or heck even pandas 4, and when i access the code because i am in that virtual environment i dont have to install pandas 4. 

'''
To create a virtual environment, we should first make an empty folder, then run powershell on it, then we have to write,

python -m venv <name of your virtual environment>
(enter)
cd <name of your virtual environment>
(enter)
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
(enter)
Scripts\activate       

E.g.
python -m venv hudor
cd hudor
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
Scripts\activate


'''


#Now you have successfully created a virtual environemt and this will make a new folder inside your empty (not necessarily) folder, the folder's name will be the same as your environment's.

#This folder e.g. hudor or myenv are basically virtual environments that we have created and we can create hundreds or thousands of them, each containing different packages and independent of the packages on the computer itself.

#What i really mean by independent is that if for e.g. you have pandas 1 installed on your computer and now you want to create a virtual environmnet which should also have pandas 1, you have to download it separately.


#And Wollah! you are inside of your virtual environment.


#We wrot this statement Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass because it allows the system to create a virtual environment. Many computers like mine dont allow to create virtual environments and the running of scirpts to create them, so we write this statement, which basically tells the comp to chill tf out and let me run this virtual environment. However, this is a temporary statement and we have to write it manually again and again when we create new virtual environments or access an existing one.



#For deactivating, write;

'''
deactivate
'''



#One more thing that we use in virtual environments and even our normal python programs (the one that depend upon the versions and things our computer installs) is pip freeze. By using it we can find out what versions are our packages of. Like, in my virtual env named lolzzz, i have 2 packages installed, there can be hundreds or thousands, and if we want to see what version of packages are installed, we can use pip freeze.


'''
if we want these versions in a txt file, we can simple write;

pip freeze > requirements.txt

But this is how i create a txt file, but if i share this virtual envrionment with my friend and he wants the txt file he can just write;

pip install -r requirements.txt

'''