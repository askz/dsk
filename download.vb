Download "http://trashtube.it/~askz/dsk/data/insee_postal.csv",  "insee_postal.csv"
Download "http://trashtube.it/~askz/dsk/data/accidents.csv", "accidents.csv"

Const strFolder = "C:\MyFolder\", strFile1 = "insee_postal.csv", strFile2 = "accidents.csv"

Const Overwrite = True
Dim oFSO

Set oFSO = CreateObject("Scripting.FileSystemObject")

If Not oFSO.FolderExists(strFolder) Then
  oFSO.CreateFolder strFolder
End If

oFSO.CopyFile strFile1, strFolder, Overwrite
oFSO.CopyFile strFile2, strFolder, Overwrite

Sub Download( myFileURL, myDestFile )
' This function uses X-standards.com's X-HTTP component to download a file
'
' Arguments:
' myFileURL  [string] the URL of the file to be downloaded
' myDestFile [string] the fully qualified path of the downloaded "target" file
'
' Written by Rob van der Woude
' http://www.robvanderwoude.com
'
' The X-HTTP component is available at:
' http://www.xstandard.com/page.asp?p=C8AACBA3-702F-4BF0-894A-B6679AA949E6
' For more information on available functionality read:
' http://www.xstandard.com/printer-friendly.asp?id=32ADACB9-6093-452A-9464-9269867AB16E
    Dim objHTTP
    Set objHTTP = CreateObject("XStandard.HTTP")
    objHTTP.Get myFileURL
    objHTTP.SaveResponseToFile myDestFile
    Set objHTTP = Nothing
End Sub