# Copyright 2021 The FACEGOOD Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import maya.cmds as cmds
import numpy as np
selectList = cmds.ls(selection=True)
attri = cmds.listConnections(selectList[0])

shapeSetName = 'blendShape1' #shapesBS
bs_nameSet = cmds.listConnections(shapeSetName,type='animCurveTU')


DataMap =[[]]

timeStart = 0
timeEnd = 2

for i in range(timeStart,timeEnd):
    cmds.currentTime(i)
    rowData_temp=[]
    for nameStr in bs_nameSet:
        nameStr = nameStr.replace('_','.',1)
        a = cmds.getAttr(nameStr)
        rowData_temp.append(a)
    print(len(rowData_temp))
    DataMap.append(rowData_temp)

np.save(r'BS_name.npy',bs_nameSet)
np.save(r'BS_value.npy',DataMap)
