#!/usr/bin/env python

#-------------------------------------------------------------------------------
# MIT License
# 
# Copyright (c) 2017  -  Harold Coenen ( a.k.a. OldskoolOrion )
#
# E-mail :
#     OldskoolOrion@gmail.com
#
# First shared at GitHub (2017.05.16) - v0.1.0 :
#     https://github.com/OldskoolOrion/Deluge.SR.nzbToMedia.Launcher.git
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
# Name      : executor.py
# Version   : 0.1.5
# Last mod. : 2017.05.27
# Created   : 2017.05.16
# License   : MIT
# Copyright : (c) 2017  -  Harold Coenen ( a.k.a. OldskoolOrion )
# E-mail    : OldskoolOrion@gmail.com
# Location  : https://github.com/OldskoolOrion/Deluge.SR.nzbToMedia.Launcher.git
#-------------------------------------------------------------------------------


##  TESTDATA -> invoke on cli :
##  D:\_Development_\PortableGit\home\OldskoolOrion\Deluge.SR.nzbToMedia.Launcher\executor.py "d2d6a72b60cdb2cc5e80d3277d89d5df18c3ecbc" "Logan.2017.1080p.WEB-DL.DD5.1.H264-FGT" "D:\Feed.Me.Bytes\u.movie"
##
##  Commandline command      : pyw D:\Feed.Me.Bytes\d.downloading\config\TorrentToMedia.py "193593c6678281cc3fd2b4e23232747c4855820f" "Last.Week.Tonight.with.John.Oliver.S04E12.720p.WEBRip.AAC2.0.H264-doosh[rarbg]" "D:\Feed.Me.Bytes\u.series"
##  Directory to clean       : D:\Feed.Me.Bytes\u.series\Last.Week.Tonight.with.John.Oliver.S04E12.720p.WEBRip.AAC2.0.H264-doosh[rarbg]
##  Filemasks to delete      : links nfo exe chm nzb par sfv srr pics txt numbered OSX RARBG.* Goedkoop*.rar
##  Former simplyfied delete : FOR %%g IN ( *.nzb *.par2 *.par *.sfv *.srr *.jpg *.5 *.4 *.3 *.2 *.1 *.gif *.png *.txt *.nfo *.url Q-for-You.* *.exe *.chm *._Contents *.plist *.wflow *.workflow RARBG.* Goedkoop*.rar ) DO ( DEL "%%g" )
##  ==============================================================================================================================================================================================================================================
##  NOTE : sometimes the directory is passed as argument in the following format :  \\?\D:\etc
##       : when this is the case, transform it to standard notation              :  D:\etc
##  CODE : SET resultdir=%~3\%~2
##       : SET resultdir=%resultdir:\\?\=%


# import modules
import sys, os
from datetime import date

# constants
executeScript = "TorrentToMedia.py"
executionPath = "D:\\Feed.Me.Bytes\\d.downloading\\config\\"

preProcessed  = 0
exitCode      = 4 - len(sys.argv)

if not exitCode == 0:
    print("** ERROR - Expecting 3 arguments. Check below for an example how to call this script:")
    print("\n            cli>> path.to/executor.py \"< torrent-id >\"  \"< release-name >\"  \"< destination-path >\" ")
    print("\n\n** NOTE  : <releaseName> can be a either a video-file, or the directory-name containing the content to process.")
    print("\nErrorcode: "+str(exitCode))
    exit(exitCode)
else:
    argumentList    = str(sys.argv)
    torrentID       = sys.argv[1]
    releaseName     = sys.argv[2]
    destinationPath = sys.argv[3]
    combinedPath    = os.path.join(destinationPath, releaseName)
    
    if os.path.isdir(combinedPath):
        print("\nEntering directory : "+str(combinedPath))
        #change into directory and clean unwanted files
        preProcessed = 1
    else:
        if path.os.isfile(combinedPath):
            print("\nRelease passed was not a directory but an existing single video-file! : "+str(combinedPath))
            # create directory & move file
            preProcessed = 1
        #else:
            exitCode = 0xFF

if not exitCode == 0
    print("** ERROR detected")
    print("\nErrorcode: "+str(exitCode))
else:
    print("No Errors message + steps taken (preProcessed) (maybe executed script in case of series)")
    print("\nExiting with code : "+str(exitCode))

exit(exitCode)
