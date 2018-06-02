#NoEnv
#Warn
#SingleInstance Force
SetWorkingDir %A_ScriptDir%

gui, font, s10, mononoki
;~ gui, font, s10, 楷体


IniRead,u,%A_ScriptDir%\coordinate.ini,register,username
IniRead,p,%A_ScriptDir%\coordinate.ini,register,Password
IniRead,x1,%A_ScriptDir%\coordinate.ini,test,a
IniRead,y1,%A_ScriptDir%\coordinate.ini,test,b
IniRead,x2,%A_ScriptDir%\coordinate.ini,test,c
IniRead,y2,%A_ScriptDir%\coordinate.ini,test,d


Gui Add, GroupBox, x10 y10 w380 h100, 登录信息
Gui,add,text,x90 y30,用户名：
gui,add,edit,x150 y30 w150 h20 Limit5 vusername,%u%
Gui,add,text,x90 y60,密码：
gui,add,edit,x150 y60  w150 h20 Password* vpassword,%p%
Gui,add,checkbox,vcheck,是否保留用户信息
Gui Add, GroupBox, x10 y115 w380 h80, 坐标信息
Gui,add,text,x60 y135,添加按钮：
Gui Add, Edit, x150 y130 w54 h21 vtxt1,%x1%
Gui Add, Text, x210 y130 w24 h23 +0x200,  —
Gui Add, Edit, x230 y130 w54 h21 vtxt2,%y1%
Gui,add,button,x320 y130 h21,1
Gui,add,text,x60 y165,确定按钮：
Gui Add, Edit, x150 y160 w54 h21 vtxt3,%x2%
Gui Add, Text, x210 y160 w24 h23 +0x200,  —
Gui Add, Edit, x230 y160 w54 h21 vtxt4,%y2%
Gui,add,button,x320 y160 h21,2
Gui Add, GroupBox, x10 y200 w380 h310, 公告内容
Gui,add,text,x30 y235,公告条数：
Gui add,edit,x100 y230 w50 h23 vnumber
Gui,add,text,x155 y235,公告标题：
Gui add,edit,x220 y230 w150 h23 vtitle
Gui add,edit,x30 y260 w280 h23 vfilepath
Gui add,edit,x30 y290 w340 r14 Limit200 vfile,不超过200个字
Gui Add, Button, x320 y260 w50 h23, 浏览
Gui Add, Button, x30 y520 w70 h23, 确定
Gui Add, Button, x300 y520 w70 h23, 取消
Gui Show,w400 h550, 写公告1.0
Return

button1:
SetTimer, UpdateOSD1, 200
gosub, UpdateOSD1
return

button2:
SetTimer, UpdateOSD2, 200
gosub, UpdateOSD2
return

button浏览:
Gui,submit,nohide
    FileSelectFile,filename,3,,请选择文件,file(*.txt;*.ahk;*.ini;*.*)
    guicontrol,,filepath,%Filename%
    FileRead, FileContents, %Filename%
    GuiControl,, file, %FileContents%
    return
button确定:
gui,submit,NoHide
IniWrite,%txt1%,%A_ScriptDir%\coordinate.ini,test,a
IniWrite,%txt2%,%A_ScriptDir%\coordinate.ini,test,b
IniWrite,%txt3%,%A_ScriptDir%\coordinate.ini,test,c
IniWrite,%txt4%,%A_ScriptDir%\coordinate.ini,test,d
if(check==1){
    IniWrite,%username%,%A_ScriptDir%\coordinate.ini,register,username
    IniWrite,%Password%,%A_ScriptDir%\coordinate.ini,register,Password
}
    return
;~ FileDelete, %Filepath%
;~ FileAppend,%FileContents%,%Filepath%



UpdateOSD1:
  MouseGetPos, MouseX, MouseY
  ToolTip,X%MouseX%   Y%MouseY%
	GuiControl,, txt1, %MouseX%
    GuiControl,, txt2, %MouseY%
  GetKeyState, state, RButton
  If state = D
{
	GuiControl,, txt1, %MouseX%
    GuiControl,, txt2, %MouseY%
	SetTimer,UpdateOSD1,off
}
return

UpdateOSD2:
  MouseGetPos, MouseX, MouseY
  ToolTip,X%MouseX%   Y%MouseY%
	GuiControl,, txt3, %MouseX%
    GuiControl,, txt4, %MouseY%
  GetKeyState, state, RButton
  If state = D
{
	GuiControl,, txt3, %MouseX%
    GuiControl,, txt4, %MouseY%
	SetTimer,UpdateOSD2,off
}
return

GuiEscape:
GuiClose:
Button取消:
    ExitApp

; End of the GUI section