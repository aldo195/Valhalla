def ps_downloader(id, url):
    ps = \
        '$request = "http://localhost:8000/api/run" \n \
$eicar_url = "http://jenda.krynicky.cz/perl/FileType.pm.txt" \n \
Invoke-WebRequest $request | \n \
ConvertFrom-Json | \n \
Select path -OutVariable $folder \n \
$eicar_file = $folder+"eicar.txt" \n \
Invoke-WebRequest -Uri $eicar_url -OutFile $eicar_file'

    return ps
