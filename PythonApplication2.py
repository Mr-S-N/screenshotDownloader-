from scan import *
from preparation import *
from parsImg import *
import os

#hldYClL.png
text = textFromImg(os.path.join(os.getcwd(),"downloaded","hldYClL.png"))
print(text)

#for filename in os.listdir(os.path.join(os.getcwd(),"downloaded")):
#    text = textFromImg(os.path.join(os.getcwd(),"downloaded",filename))
#    print(text)
#    print("----------")