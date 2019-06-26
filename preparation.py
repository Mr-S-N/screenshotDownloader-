import os
def exe():
  cDirectory = os.getcwd()
  if not os.path.exists(os.path.join(cDirectory,"downloaded")):
    os.makedirs(os.path.join(cDirectory,"downloaded"))
  if not os.path.exists(os.path.join(cDirectory,"selected")):
    os.makedirs(os.path.join(cDirectory,"selected"))
  if not os.path.exists(os.path.join(cDirectory,"unselected")):
    os.makedirs(os.path.join(cDirectory,"unselected"))
