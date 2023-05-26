#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn All, StdOut  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
; 格式化XML文本
; 监听快捷键 Ctrl + Alt + F
^!f::
  ClipSaved := ClipboardAll ; 保存剪贴板内容
  clipboard = ; 清空剪贴板
  Send ^c ; 复制选中的文本
  ClipWait ; 等待剪贴板有内容
  clipboard  XML := Clipboard ; 将剪贴板中的内容赋值给变量
  FileDelete, %A_Temp%\temp.xml ; 删除临时文件
  FileAppend, %XML%, %A_Temp%\temp.xml ; 将XML写入文件
  oXML := ComObjCreate("MSXML2.DOMDocument.6.0") ; 创建XML DOM对象
  oXML.async := false ; 同步模式
  oXML.validateOnParse := false ; 不验证XML有效性
  oXML.resolveExternals := false ; 不解析外部引用
  oXML.load(A_Temp . "\temp.xml") ; 加载XML文件
  oXML.setProperty("SelectionLanguage", "XPath") ; 设置查询语言
;  oXML.setProperty("SelectionNamespaces", '') ; 设置命名空间
  formattedXML := oXML.xml ; 格式化后的XML文本
  Clipboard := formattedXML ; 将格式化后的XML赋值给剪贴板
  Send ^v ; 粘贴剪贴板内容
  Clipboard := ClipSaved ; 恢复剪贴板内容
return
