@echo off
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"

docker build -f "pgdocker\Dockerfile" -t pgdocker - < pgdocker.tar.gz
docker run --rm -v "%cd%/Test:/data" pgdocker

echo Press any key to exit...
pause>nul
exit
