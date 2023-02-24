files=($(find ./docs -type f -name '*.rst'))
for item in ${files[*]}
do
  printf "   %s\n" $item
  install -d ${DIR}/build/$item
  pandoc $item -f rst -t markdown -o ${DIR}/build/$item.md;
  rm -Rf ${DIR}/build/$item
done