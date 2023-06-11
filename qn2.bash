#!/bin/bash

cd ../Modified


for file in * ; do
  filename=$(basename -- "$file")
  extension="${filename##*.}"
  filename="${filename%.*}"
  date_string=$(date +"%Y-%m-%d_%H-%M-%S")
  mv "$file" "$filename-$date_string.$extension"
done

