$target = "$PSScriptRoot/../ninja-build"
$dist = "$PSScriptRoot/../pdist"
if (Test-Path $dist) {}else {
    New-Item -ItemType Directory -Path $dist
}

Copy-Item "$target/libapp.dll" "$dist/libapp.dll" -Force

Push-Location $PSScriptRoot/../petool
python copydll.py
Pop-Location
