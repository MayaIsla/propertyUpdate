$files1 = "C:\Users\filepath\Desktop\t.properties"
$files2 = "C:\Users\filepath\Desktop\s.properties"


compare-object (get-content $files2) (get-content $files1) | select -ExpandProperty InputObject| out-file $files2  -append -Encoding utf8
