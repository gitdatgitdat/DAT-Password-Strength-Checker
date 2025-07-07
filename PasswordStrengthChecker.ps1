#Password Strength Checker
#v0.1

#Loop for repeat checks
while ($true) {
    #Header
    Write-Host "============================="
    Write-Host " Password Strength Checker "
    Write-Host "============================="
    
    #Prompt for password
    $password = Read-Host "Enter password to check or type 'exit' to quit"

    if($password -eq "exit") {
        break
    }

    #Initialize score
    $score = 0

    #Length checker
    if ($password.Length -ge 8) {
        $score += 1
        Write-Host "Length check passed"
    } else {
        Write-Host "Password is too short (Minimum 8 characters)"
    }

    #Uppercase check
    if ($password -cmatch "[A-Z]") {
        $score += 1
        Write-Host "Uppercase letter check passed"
    } else {
        Write-Host "No uppercase letters found"
    }

    #Lowercase check
    if ($password -cmatch "[a-z]") {
        $score += 1
        Write-Host "Lowercase letter check passed"
    } else {
        Write-Host "No lowercase letters found"
    }

    #Number check
    if ($password -match "[0-9]") {
        $score += 1
        Write-Host "Number check passed"
    } else {
        Write-Host "No numbers found"
    }

    #Special character check
    if ($password -match "[^a-zA-Z0-9]") {
        $score += 1
        Write-Host "Special character check passed"
    } else {
        Write-Host "No special characters found"
    }

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

    Write-Host ""  # single blank line to separate rounds

}


