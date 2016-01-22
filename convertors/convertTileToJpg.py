# -*- coding: UTF-8 -*-
from os import listdir, rename
from os.path import isfile, isdir
from os.path import join as joinpath

mypath = "."

def convertTileToJpg(path):
  for i in listdir(path):
    # Если файл
    if isfile(joinpath(path,i)):
      # файл нужного формата - переименовываем
      if (joinpath(path,i).endswith('.tile')):
	oldNameWithOutTile = joinpath(path,i)[0:-4]
	rename(joinpath(path,i), oldNameWithOutTile + 'jpg')
    # если папка
    if isdir(joinpath(path,i)):
      newPath = path + "/"+ i
      convertTileToJpg(newPath)

convertTileToJpg(mypath)

