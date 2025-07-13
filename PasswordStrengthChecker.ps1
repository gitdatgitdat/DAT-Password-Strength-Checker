#Password Strength Checker
#v0.1

#Dynamically set script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
#Grabbing txt file for list of commonly used passwords
$commonPWs = Get-Content -Path (Join-Path $scriptDir "common-passwords.txt")

#Loop for repeat checks
while ($true) {
    #Header
    Write-Host "============================="
    Write-Host " Password Strength Checker "
    Write-Host "============================="
    
    #Prompt for password
    $password = Read-Host "Enter password to check or type 'exit' to quit"

    if ($password -eq "exit") {
        break
    }

    #Normalization input for common password comparison
    $normalizedPW = ($password.Trim() -replace '\s', '').ToLower()

    #Checking for common passwords before running checks
    if ($commonPWs -contains $normalizedPW) {
        Write-Host "This password is commonly used and considered unsafe."
        Write-Host "Please try a more unique password."
        Write-Host ""
        continue
    }

    #Initialize score
    $score = 0

    #Store rule results as flags
    $hasLength = $password.Length -ge 8
    $hasUpper = $password -cmatch "[A-Z]"
    $hasLower = $password -cmatch "[a-z]"
    $hasNumber = $password -match "[0-9]"
    $hasSpecial = $password -match "[^a-zA-Z0-9]"

    #Rule evaluation based on flags
    if ($hasLength) { $score += 1; Write-Host "Length check passes" } else { Write-Host "Password is too short (Minimum 8 characters)" }
    if ($hasUpper) { $score += 1; Write-Host "Uppercase letter check passed" } else { Write-Host "No uppercase letters found" }
    if ($hasLower) { $score += 1; Write-Host "Lowercase letter check passed" } else { Write-Host "No lowercase letters found" }
    if ($hasNumber) { $score += 1; Write-Host "Number check passed" } else { Write-Host "No numbers found" }
    if ($hasSpecial) { $score += 1; Write-Host "Special character check passed" } else { Write-Host "No special characters found" }

    Write-Host ""

    #Summary
    Write-Host "Password score: $score out of 5"

    if ($score -eq 5) {
        Write-Host "This is a strong password"
    } elseif ($score -ge 3) {
        Write-Host "This is a decent password"
    } else {
        Write-Host "This is a weak password"
    }

    # Suggestions based on failed checks
    Write-Host ""

    if (-not $hasLength) { Write-Host "Tip: Make your password at least 8 characters long." }
    if (-not $hasUpper) { Write-Host "Tip: Include at least one uppercase letter." }
    if (-not $hasLower) { Write-Host "Tip: Include at least one lowercase letter." }
    if (-not $hasNumber) { Write-Host "Tip: Add at least one number." }
    if (-not $hasSpecial) { Write-Host "Tip: Add at least one special character (e.g., !, @, #)." }

    Write-Host ""  # single blank line to separate rounds
}


