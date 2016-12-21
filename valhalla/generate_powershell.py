def ps_downloader(raid_type, raid_id):
    if raid_type == '100':
        ps = \
            '$request = "http://localhost:8000/api/run?id='+raid_id+' \n \
$eicar_url = "http://jenda.krynicky.cz/perl/FileType.pm.txt" \n \
Invoke-WebRequest $request | \n \
ConvertFrom-Json | \n \
Select path -OutVariable $folder \n \
$eicar_file = $folder+"eicar.txt" \n \
Invoke-WebRequest -Uri $eicar_url -OutFile $eicar_file'
    else:
        ps = "Type not supported"

    return ps
