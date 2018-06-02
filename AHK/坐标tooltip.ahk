#Warn
#NoTrayIcon     ;不显示托盘图标

;以固定的速率运行子程序
SetTimer, UpdateOSD1,10
gosub, UpdateOSD1
;~ return 

UpdateOSD1:
MouseGetPos, MouseX, MouseY    ;获取当前鼠标位置的坐标
PixelGetColor, color, %MouseX%, %MouseY%, RGB    ;获取前一步获得的坐标处的颜色码
WinGetActiveTitle, Title    ;获取当前活动窗口的的标题
winget,pid,PID,%title%    ;获取当前活动窗口的的PID（进程ID）
winget,ahk_exe,ProcessName,%title%   ;获取当前活动窗口的进程名
winget,ahk_path,ProcessPath,%title%   ;获取当前活动窗口的进程路径
SysGet, VirtualWidth, 78
SysGet, VirtualHeight, 79
WinGetPos,,,width,height,%title%
if(title != "")
{
	ToolTip,Title`t`t%Title%`ncoordinate`tX%MouseX%   Y%MouseY%`nRGB`t`t%color%`nPID`t`t%pid%`nprocess`t`t%ahk_exe%`npath`t`t%ahk_path%`nwidth、height`t%width%x%height%    ;已tooptip的方式显示以上获取的内容
return
}
else
{
	ToolTip,coordinate`t`tX%MouseX%   Y%MouseY%`nmonitor resolution`t%VirtualWidth%*%VirtualHeight%    ;title为空只显示坐标
	return
}
;停止
F9::
SetTimer, UpdateOSD1,off
ToolTip
return
;开始
F10::
SetTimer, UpdateOSD1,On
return

Esc::
ExitApp