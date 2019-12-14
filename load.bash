FILE=save.txt
if [ -f "$FILE" ]; then
    rm save.txt
    touch save.txt
else
    touch save.txt
fi
