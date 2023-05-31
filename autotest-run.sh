

#!/bin/bash
cd /richard/test
while true; do
echo "zadej k pro ukonceni"
read -p "Zadej sn:" sn


if [[ "$sn" == "k" ]]; then
        echo "ukoncuji"
        exit 0
elif [[ -z "$sn" ]]; then
        echo "sn is an empty string"
elif [[ "$sn" != *"..."* ]]; then
        echo "Tohle nevypada jako valid sn :( "
else
        bash test-test ${sn} list
        continue
fi

done
