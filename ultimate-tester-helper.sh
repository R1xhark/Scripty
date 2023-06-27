#!/bin/bash

while true; do  

    echo -e "Menu:"
    echo "1. Spusti repair boostrap"
    echo "2. Restartuj jednotku pres BMC"
    echo "3. Backup logs"
    echo "4. Pust recovery K2V karty"
    echo "5. Kill unit"
    echo "6. Fan control"
    echo "7. Sel print/clear"
    echo "8. SSH Connect"
    echo "'k' Ukonci"
    read -p "Zadej vyber:  " choice

    case $choice in
        1)
            echo -e "Running repair boostrap noSFCS"
            cd /opt/TE/Amber/mfg
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
                    bash FS-Autotest.sh ${sn} BOOTSTRAP_REPAIR_NOSFCS.list
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
		kill-tty1.sh ${ip}
                continue
          fi
         done
         ;;
	6)    
        echo "Fan Control"
        while true; do
        echo "Zadej 'k' pro ukonceni"
        read -p "Zadej BMC IP: " ip

        if [[ "$ip" == "k" ]]; then
        echo "Ukoncuji..."
        break
    	else
          read -p "Zadej procentualni vykon fanu: " vykon

          if [[ "$vykon" == "2" ]]; then
            ipmitool -I lanplus -U admin -P admin -H ${ip} raw 0x30 0x91 2
            echo "Fans set to default mode"
            break
          elif [[ "$vykon" -gt 100 ]]; then
            echo "Vykon fanu nemuze byt vyssi nez 100"
            continue
          else
            ipmitool -I lanplus -U admin -P admin -H ${ip} raw 0x30 0x91 1 0 ${vykon}
            echo "Fan mode set to $vykon"
            break
          fi
    	 fi
        done
		;;
	7)
	 echo "SEL Tool"
	echo "Pro odchod stiskni 'k'"
	while true; do
    	 read -p "Zadej BMC IP: " ip
    	 read -p "Zadej Grep request: " request
    	 read -p "1.List, 2.Clear: " vyber

    	if [[ "$ip" == "k" || "$ip" == "K" || "$request" == "k" || "$request" == "K" || "$vyber" == "k" || "$vyber" == "K" ]]; then
         echo "Ukoncuji..."
         break
     	elif [[ -z "$request" && "$vyber" == 1 ]]; then
         echo "Listing SEL without grep"
         ipmitool -U admin -P admin -H $ip sel list
         continue
      	elif [[ -z "$request" && "$vyber" == 2 ]]; then
         echo "Clearing SEL..."
         ipmitool -U admin -P admin -H $ip sel clear
         continue
     	elif [[ "$vyber" == 2 ]]; then
      	 echo "Can't clear SEL with request"
      	 echo "Ignoring request"
      	 echo "Clearing SEL..."
      	 ipmitool -U admin -P admin -H $ip sel clear
       	continue
      	else
      	 ipmitool -U admin -P admin -H $ip sel list | grep "$request"
       	 echo "SEL printed with grep: $request"
      	 continue
      fi
	done
 	;;
	8)
	 echo "SSH Connect"
	 while true;do
		echo "Type 'Exit' to exit"
		read -p "Enter etherIP:" ip
		
		if [[ "$ip" == "Exit" || "$ip" == "exit" || "$ip" == "EXIT" ]];then
			echo "ukoncuji"
			break
		elif [[ -z "$ip" ]]; then
		   xterm -hold ssh ${ip}
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
