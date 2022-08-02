#init var property files on desktop

$files1 = "C:\Users\mislambo\OneDrive - Western Alliance Bank\Desktop\t.properties" #requested property file
$files2 = "C:\Users\mislambo\OneDrive - Western Alliance Bank\Desktop\s.properties" #original file
$files3 = "C:\Users\mislambo\OneDrive - Western Alliance Bank\Desktop\u.properties" #Your new property file

Add-Content -Path "C:\Users\mislambo\OneDrive - Western Alliance Bank\Desktop\sb.properties" -Value (Get-Content -Path $files2)
Get-Content -Path $files2 #create a backup of s.properties (your main property original file)

compare-object (get-content $files1) (get-content $files2) | select -ExpandProperty InputObject | out-file $files2  -append -Encoding utf8 #compares and pastes vars that do not exist into new original file


Get-Content $files2 | Group-Object {$_.Split(' = ')[0] } | ForEach-Object {$_.Group[-1] } | Where {$_ -notmatch '^#.*'} | Out-File $files3 -encoding utf8
