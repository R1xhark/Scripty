#!/bin/bash

while true; do

    echo -e "Menu:"
    echo "1. Spusti repair boostrap"
    echo "2. Restartuj jednotku pres BMC"
    echo "3. Backup logs"
    echo "4. Pust recovery K2V karty"
    echo "5. Kill unit"
    echo "'k' Ukonci"
    read -p "Zadej vyber:  " choice

    case $choice in
        1)
            echo -e "Running repair boostrap noSFCS"
            cd /folder/test
            while true; do
                echo "Zadej 'k' pro ukonceni"
                read -p "zadej SN: " sn

                if [[ "$sn" == "k" || "$sn" == "K" ]]; then
                    echo "Exiting..."
                    break
                elif [[ -z "$sn" ]]; then
                    echo "SN is an empty string"
                elif [[ "$sn" != *"WAA"* ]]; then
                    echo "Tohle nevypada jako Amber sn :("
                else
                    bash test ${sn} test #input your own tests
                    continue
                fi
            done
            ;;
        2)
            echo "Restarting BMC"
            while true; do
                echo "Zadej 'k' pro ukonceni"
                read -p "zadej BMC IP: " ip

                if [[ "$ip" == "k" || "$ip" == "K" ]]; then
                    echo "ukoncuji..."
                    break
                elif [[ -z "$ip" ]]; then
                    echo "BMC IP is an empty string"
                else
                    echo "restartuji..."
                    ipmitool -U admin -P admin -I lanplus -H ${ip} power cycle
                    continue
                fi
            done
            ;;
        3)
            echo "Backing up logs"
             while true; do
                echo "Zadej 'k' pro odchod"
                read -p "zadej SN: " sn

                if [[ "$sn" == "k" || "$sn" == "K" ]]; then
                    echo "Exiting..."
                    break
                fi

                cd /opt/logs

                if [ -e "$sn" ]; then
                    if [ -e "$sn.bck" ]; then
                        count=1
                        while [ -e "$sn.bck$count" ]; do
                            ((count++))
                        done
                        mv "$sn" "$sn.bck$count"
                        echo "logy zalohovany jako $sn.bck$count"
                    else
                        mv "$sn" "$sn.bck"
                        echo "Logy zalohovany"
                    fi
                else
                    echo "Error: sn:'$sn' neexistuje!"
                    continue
                fi
            done
              ;;
        4)
           echo "K2V recovery"
           while true;do
           echo "Zadej 'k' pro ukonceni"
           read -p "Zadej BMC IP:" bmc

           if [[ "$bmc" == "k" || "$bmc" == "K" ]]; then
                echo "ukoncuji..."
                break
           else
                echo "recovering..."
                ipmitool -U admin -P admin -I lanplus -H ${bmc} raw 0x34 0x75 0x01 0x8C 0x0 0x4e 0x1
                continue
           fi
        done
        ;;
        5)
          echo "Kill process"
          while true;do
          echo "Zadej 'k' pro ukonceni"
          read -p "Zadej IP jednotky:" ip

          if [[ "$ip" == "k" || "$ip" == "K" ]]; then
                echo "ukoncuji..."
                break
          else
                echo "killing process..."
                kill-proces.sh
                continue
          fi
         done
         ;;
         k)
                echo "ukoncuji..."
                exit 0
                ;;

        *)
            echo "Invalid choice. Prosim zadej 1-4"
            ;;
    esac
done




