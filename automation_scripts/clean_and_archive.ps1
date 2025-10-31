param([string]$TargetDir = ".\sample_folder")
$ArchiveDir = "$TargetDir\archive_$(Get-Date -Format yyyyMMdd)"
New-Item -ItemType Directory -Force -Path $ArchiveDir | Out-Null
Get-ChildItem -Path $TargetDir -Recurse -File | Where-Object { $_.Length -eq 0 } | Remove-Item
$Threshold = (Get-Date).AddDays(-30)
Get-ChildItem -Path $TargetDir -Recurse -File | Where-Object { $_.LastWriteTime -lt $Threshold } | ForEach-Object {
    Move-Item $_.FullName -Destination $ArchiveDir -Force
}
Get-ChildItem -Path $TargetDir -Recurse -File | ForEach-Object {
    $newName = $_.Name -replace " ", "_"
    if ($_.Name -ne $newName) { Rename-Item $_.FullName $newName }
}
Write-Host "✅ Cleanup complete. Archived files moved to $ArchiveDir"
