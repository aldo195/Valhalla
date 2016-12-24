def ps_downloader(raid_type, raid_id, trophy):
    if raid_type in ['100', '101', '102']:
        ps = \
            '$request = "http://localhost:8000/api/run?raidid='+raid_id+'" \n \
$eicar_url = "http://jenda.krynicky.cz/perl/FileType.pm.txt" \n \
Invoke-WebRequest $request | \n \
ConvertFrom-Json | \n \
Select trophy -ExpandProperty trophy -OutVariable trophyValue > $null \n \
$eicar_file = $env:temp+"\\"+$trophyValue+".txt" \n \
Invoke-WebRequest -Uri $eicar_url -OutFile $eicar_file \n \
Get-Date -Format g \n \
Write-Host "Raid launch completed." '
    else:
        ps = "Type not supported"

    return ps
