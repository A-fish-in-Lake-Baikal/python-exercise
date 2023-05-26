#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn All, StdOut  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

xmldata = clipboard
(join`r`n
<?xml version="1.0"?>
<root>
<itemLookup>
 <version>1.0</version>
 <typeID>37</typeID>
 <typeName>Isogen</typeName>
</itemLookup>
<itemLookup>
 <version>2.0</version>
 <typeID>33</typeID>
 <typeName>Isogen</typeName>
</itemLookup>
</root>
)
doc := ComObjCreate("MSXML2.DOMDocument.6.0")
doc.async := false
doc.loadXML(xmldata)
;取第一个itemLookup的typeID
DocNode := doc.selectSingleNode("//itemLookup/typeID")
DocText := DocNode.text
MsgBox %DocText%

;取符合某个条件的itemLookup的typeID
DocNode := doc.selectSingleNode("//itemLookup[version=""2.0""]/typeID")
DocText := DocNode.text
MsgBox %DocText%

;遍历itemLookup
nodes:=doc.selectSingleNode("/root").childNodes

for node in nodes
{
	DocText := node.text
	MsgBox %DocText%
}