@echo off
start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"

docker build -t a1docker - < FSADA1Docker
docker run --rm -v "%cd%/Test:/marking" a1docker

echo Press any key to exit...
pause>nul
exit
