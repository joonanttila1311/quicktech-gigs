param([string]$TargetDir = ".\Documents\Test")
$ArchiveDir = "$TargetDir\archive_$(Get-Date -Format yyyyMMdd)"
New-Item -ItemType Directory -Force -Path $ArchiveDir | Out-Null
$Threshold = (Get-Date).AddDays(-30)
Get-ChildItem -Path $TargetDir -Recurse -File | Where-Object { $_.LastWriteTime -lt $Threshold } | Move-Item -Destination $ArchiveDir
Write-Host "✅ Archived files moved to $ArchiveDir"
