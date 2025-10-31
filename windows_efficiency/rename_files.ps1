param([string]$TargetDir = ".\Documents\Test")
Get-ChildItem -Path $TargetDir -Recurse -File | ForEach-Object {
    $newName = $_.Name -replace " ", "_"
    if ($_.Name -ne $newName) { Rename-Item $_.FullName $newName }
}
Write-Host "✅ Files renamed successfully"
