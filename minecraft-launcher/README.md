RPM for the "Official Minecraft Launcher"
Repack installation from https://www.minecraft.net/en-us/download
to rpm usable on Fedora.

This package builds the lates version of the "bootstrap" launcher.
Boostrap launcher is the minimal version needed to update and download the current
launcher from the mojang.com, which will be stored in the user's home directory
in ~/.minecraft folder .

For current versions check
```
curl https://launchermeta.mojang.com/v1/products/launcher/6f083b80d5e6fabbc4236f81d0d8f8a350c665a9/linux.json |\
jq '."launcher-bootstrap"'
```

For checking checksum try downloading the manifes from the current launcher-bootstrap and compare
```
culr https://piston-meta.mojang.com/v1/packages/d72c08ef9605e645fd81f705d66b8ebd9620d7a1/manifest.json |\
|jq '.files."minecraft-launcher".downloads.raw'
```

Instructions re-building the Fedora RPM:
0) Get current Fedora system
https://fedoraproject.org/workstation/download
... live DVD boot-up in virtual machine would be enough

1) Install rpm building tools
```
sudo dnf -y install rpm-build rpmdevtools
```

2) deploy the spec + other files to right place for rebuild (as normal user)
one of 2a) or 2b)
2a) install this nosrc.rpm
```
rpm -Uhv minecraft-launcher-1.0.1221-1.fc40.nosrc.rpm
```

2b) or copy the files manually
```
mkdir -p ~/rpmbuild/{SPECS,SOURCES}
cp -p minecraft-launcher.spec ~/rpmbuild/SPECS/
cp -p minecraft-launcher.desktop ~/rpmbuild/SOURCES/
cp -p minecraft-launcher.metanfo.xml ~/rpmbuild/SOURCES/
```

3) download sources from official site
```
# create secondary file without the "Nosource" stanzas
cd ~/rpmbuild/SPECS/
grep -v Nosource minecraft-launcher.spec > minecraft-launcher.src.spec

# download the sources (tar.gz and svg) from the upstream
cd ~/rpmbuild/SOURCES/
spectool -g ~/rpmbuild/SPECS/minecraft-launcher.src.spec
```

4) build the package
```
rpmbuild -ba ~/rpmbuild/SPECS/minecraft-launcher.spec
```

or
```
rpmbuild --rebuild minecraft-launcher-1.0.1221-1.nosrc.rpm
```

5) install the rpm
```
sudo dnf install ~/rpmbuild/RPMS/x86_64/minecraft-launcher-1.0.1221-1.fc*.x86_64.rpm
```

At this point minecraft can be started in the Application menu by "Minecraft Launcher"
or by running "minecraft-launcher" from commandline.

