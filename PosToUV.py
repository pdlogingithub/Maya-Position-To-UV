import maya.cmds as mc

allSelected = mc.ls(sl=True)
for selected in allSelected:
    mc.select(selected)
    if 'PosToUV' in mc.polyUVSet(query=True, allUVSets=True ):
        mc.polyUVSet(delete=True, uvSet='PosToUV')
    mc.polyAutoProjection(createNewMap = True, uvSetName = "PosToUV")
    mc.polyUVSet(currentLastUVSet=True )
   
    uvs = mc.polyListComponentConversion (tuv=True )
    mc.select (uvs)
   
    objPos = mc.xform(str(selected),q=1,ws=1,rp=1)
    mc.polyEditUV(relative=False, uValue=objPos[0], vValue=objPos[2] )
