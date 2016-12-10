def ps_downloader(id, url):
    ps = '$url = "'+url+'" \n \
$output = "eicar.txt"\n \
$start_time = Get-Date\n \
Invoke-WebRequest -Uri $url -OutFile $output\n \
Write-Output "Time taken: $((Get-Date).Subtract($start_time).Seconds) second(s)"'

    return ps
