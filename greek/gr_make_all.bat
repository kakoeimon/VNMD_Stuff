python convert_images.py
copy %cd%\novel\foreground\woman3_young.png %cd%\res\foreground\woman3_young.png
python create_image_res.py
python greek_convert.py

copy %cd%\font_greek.png %cd%\res\font_greek.png
python convert_scripts.py

c:\sgdk\bin\make -f c:\sgdk\makefile.gen

c:\RetroArch-Win64\retroarch.exe -L c:\RetroArch-Win64\cores\blastem_libretro.dll %cd%\out\rom.bin