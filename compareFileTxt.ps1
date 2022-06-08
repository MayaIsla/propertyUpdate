$files1 = "C:\Users\mislambo\OneDrive - Western Alliance Bank\Desktop\t.properties"
$files2 = "C:\Users\mislambo\OneDrive - Western Alliance Bank\Desktop\s.properties"


compare-object (get-content $files2) (get-content $files1) | select -ExpandProperty InputObject| out-file $files2  -append -Encoding utf8
