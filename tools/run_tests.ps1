# Start a simple server and open the browser to the tests page
$pwd = Get-Location
Write-Host "Serving $pwd on http://localhost:8000/tests/index.html"
Start-Process -FilePath python -ArgumentList '-m','http.server','8000'
Start 'http://localhost:8000/tests/index.html'
