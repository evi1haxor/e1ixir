---
title: "$Termux$"
date: 2018-08-26T00:46:53+05:30
draft: false
---

Termux is Linux terminal emulator on Android which supports Linux packages and uses APT package manager. It's a free app and can be downloaded either from [Play store](https://play.google.com/store/apps/details?id=com.termux) or from [F-droid](https://f-droid.org/en/packages/com.termux/). It comes very handy when you are out of good machine. Although I discourage using termux if you already have a laptop or desktop. However, no strings on you! You can use it anyway.<br><br>
One more thing you should know as a prerequisite is that while downloading, you should not mix the downloads from F-droid and playstore. They ain't mutually compatible. This is because each download website uses a specific key for keysigning Termux and Addons.<br><br>
Here I'm going to give a concise idea about Termux and how to set it up.<br><br><br>
## Installation
Apart from Termux app, there are several add-on apps which should be downloaded. Not all add-ons are necessary, but I recommend you to download [Termux API](https://play.google.com/store/apps/details?id=com.termux.api). Not particularly because it helps in accessing device API:s through CLI, but because it is the only free add-ons available on play store. Though you always have option to go on F-droid.<br><br><br>
## Setting up the terminal
I recommend you to check for updates and upgrades for termux based systems, for example for setting up termux storage, and some more. For this, run the following command on the CLI.<br>

```$ apt update && upgrade``` 


After this, it is suggested to install `coreutils` before moving on. Most of them (like `ls` and `mv` etc.) come pre-installed, but just to stand on the safe side, it is good to refresh them by running <br>

```$ apt install coreutils``` 


Next step is to set up storage. Just to brief you about the termux storage, there are three types of storage in Termux.

1. **App-private storage:** It's the `$HOME` directory, approachable from outside or within the app.
2. **Shared Storage:** Like every other app, Termux also have shared storage which can be stimulated by allowing permission to the app by running ```$ termux-setup-storage``` command and tapping on _Allow_ button on the appeared dialogue box. It'll make _storage_ directory inside ```$HOME``` which consists of symlinks to different storage folders like ```~storage/shared```, ```~storage/dcim```, ```~storage/downloads```, ```~storage/movies```, ```~storage/external```, ```~storage/music```,```~storage/pictures```
3. **External Storage:** Termux API for this is not yet available.


Now you may like to make a seperate directory in ```$HOME``` for storing your projects and codes that you might mount on GitHub or other similar platform. Use <br>
```$ mkdir DIRECTORY_NAME```<br>
for making a directory. <br><br><br>
If you're new to Linux, you can install and work on ```fish``` for few days, till you make yourself comfortable with Linux environment. For installing ```fish``` execute command- <br>
```$ apt install fish``` <br>
then type and enter <br>
```$ fish``` <br>
on the terminal to enter the fish mode.<br><br>
## A few must have packages 
```$ apt install git```

```$ apt install vim```

```$ apt install clang```

```$ apt install g++```

```$ apt install cowsay```

```$ apt install fortune```

```$ apt install sl```

```$ apt install toilet```


There are many more, I'll add them, with their functions and specs, as I get. 
<br>
I generally use APT repository, however, ```pkg``` package manager can also be used on Termux. Infact, ```pkg``` is rather more efficient than ```apt``` due to extra update commands which are needed to be executed while working with ```apt```, which are automatic with ```pkg```. 


### Signing off
It's okay to mess up and get terribly perplexed during initial days, take it as the general process of mastery. This isn't the final post on Termux, I'm gonna make one or two more of such on Termux, so stay tuned. If you have any suggestions or queries regarding this, you know how to contact me online. Or you can just perch upon my Haveli. Attached address for your reference.<br><br>

Haveli No. 318<br>
Lift ke samne wali gali<br>
G5<br>
IIT JODHPUR
