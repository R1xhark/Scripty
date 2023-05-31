#!/usr/bin/env python3

import os
import urllib.request
import zipfile

# Download the Minecraft server jar
url = "https://cdn.getbukkit.org/craftbukkit/craftbukkit-1.17.jar"
urllib.request.urlretrieve(url, "minecraft_server.jar")

# Create the server configuration files
eula_file = open("eula.txt", "w")
eula_file.write("eula=true")
eula_file.close()

server_properties_file = open("server.properties", "w")
server_properties_file.write("generator-settings=\n")
server_properties_file.write("op-permission-level=4\n")
server_properties_file.write("allow-nether=true\n")
server_properties_file.write("level-name=world\n")
server_properties_file.write("enable-query=false\n")
server_properties_file.write("allow-flight=false\n")
server_properties_file.write("announce-player-achievements=true\n")
server_properties_file.write("server-port=25565\n")
server_properties_file.write("max-world-size=29999984\n")
server_properties_file.write("level-type=default\n")
server_properties_file.write("enable-rcon=false\n")
server_properties_file.write("level-seed=\n")
server_properties_file.write("force-gamemode=false\n")
server_properties_file.write("server-ip=\n")
server_properties_file.write("network-compression-threshold=256\n")
server_properties_file.write("max-build-height=256\n")
server_properties_file.write("spawn-npcs=true\n")
server_properties_file.write("white-list=false\n")
server_properties_file.write("spawn-animals=true\n")
server_properties_file.write("snooper-enabled=true\n")
server_properties_file.write("hardcore=false\n")
server_properties_file.write("texture-pack=\n")
server_properties_file.write("online-mode=true\n")
server_properties_file.write("pvp=true\n")
server_properties_file.write("difficulty=1\n")
server_properties_file.write("gamemode=0\n")
server_properties_file.write("max-players=20\n")
server_properties_file.write("spawn-monsters=true\n")
server_properties_file.write("generate-structures=true\n")
server_properties_file.write("view-distance=10\n")
server_properties_file.write("motd=A Minecraft Server\n")
server_properties_file.close()

# Start the server
os.system("java -Xmx1024M -Xms1024M -jar minecraft_server.jar nogui")
