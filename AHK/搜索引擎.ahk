#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#NoEnv
#Warn
SetWorkingDir %A_ScriptDir%

;读取配置文件
IniRead,s,%A_ScriptDir%\zuobiao.ini,test,a
IniRead,t,%A_ScriptDir%\zuobiao.ini,test,b

Menu Tray, Icon, C:\Users\Administrator\Desktop\vendetta.ico
gui, font, s8, mononoki
Gui,add,tab2,,search|zuobiao ;创建tab菜单
Gui Show,AutoSize, test

Gui,tab,1
Gui Add, Text, x20 y40 w120 h23 +0x200, 请选择要访问的搜索引擎
Gui Add, DropDownList,  w150 vchoose, 百度|必应|维基|搜狗
Gui Add, CheckBox,x190 y70 vcheck, whether?
Gui Add, Text, x20 y90 w120 h23 +0x200, 请选择文件:
Gui Add, Edit, w150 vMyEdit
Gui Add, Button, x20 y190 w75 h23, 确定
Gui Add, Button, x190 y190 w75 h23, 取消
Gui Add, Button, x190 y120 w75 h23, 浏览
Gui,tab,2
Gui Add, Text, x30 y80 w47 h23 +0x200, 坐标点：
Gui Add, Edit, x90 y80 w54 h23 vtxt1,%s%
Gui Add, Text, x170 y80 w24 h23 +0x200,  —
Gui Add, Edit, x210 y80 w57 h21 vtxt2,%t%
Gui add, button,x160 y120,刷新
return

Button浏览:
    gui,submit,NoHide
    FileSelectFile,filename,3,,请选择文件,file(*.txt;*.ahk;*.ini)
    guicontrol,,MyEdit,%Filename%
    return
button确定:
    gui,submit,NoHide
    FileAppend,`n%choose%`t%MyEdit%`t%Check%`t%txt1%`t%txt2%,%A_ScriptDir%\运行结果.config
    if(check==1){
		Run,%filename%
	}
	else
		msgbox ,您选择了不打开文件
    if(choose =="百度"){
    Run,www.baidu.com
    return
    }
    else if(choose == "必应"){
    Run,www.bing.com
    return
    }
    else if(choose == "维基"){
    Run,www.wiki.com
    return
    }
    else if(choose == "搜狗"){
    Run,www.sougou.com
    return
    }
	else if(choose==""){
		MsgBox,您没有选择搜索引擎
	}
    return

button刷新:
gui,submit,nohide
IniWrite,%txt1%,%A_ScriptDir%\zuobiao.ini,test,a
IniWrite,%txt2%,%A_ScriptDir%\zuobiao.ini,test,b
click,%txt1%,%txt2% Right
send,{E}
return
GuiEscape:
button取消:
GuiClose:
    ExitApp
    
    
;~ result()
;~ {
    ;~ FileAppend,`n%chose%`t%MyEdit%`t%txt1%`t%txt2%,%A_ScriptDir%\运行结果.txt
    ;~ return
;~ }