# -*- coding: UTF-8 -*-
from os import listdir, rename
from os.path import isfile, isdir
from os.path import join as joinpath

mypath = "."
      
def convertJpgToTile(path):
  for i in listdir(path):
    # Если файл
    if isfile(joinpath(path,i)):
      # файл нужного формата - переименовываем
      if (joinpath(path,i).endswith('.jpg')):
	oldNameWithOutTile = joinpath(path,i)[0:-3]
	rename(joinpath(path,i), oldNameWithOutTile + 'tile')
    # если папка
    if isdir(joinpath(path,i)):
      newPath = path + "/"+ i
      convertJpgToTile(newPath)

convertJpgToTile(mypath)

