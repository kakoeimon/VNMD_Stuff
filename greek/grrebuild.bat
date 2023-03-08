del %cd%\out\rom.bin

copy %cd%\font_greek.png %cd%\res\font_greek.png

python greek_convert.py


python convert_scripts.py
c:\sgdk\bin\make -f c:\sgdk\makefile.gen

c:\RetroArch-Win64\retroarch.exe -L c:\RetroArch-Win64\cores\blastem_libretro.dll %cd%\out\rom.bin