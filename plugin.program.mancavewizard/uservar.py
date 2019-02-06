import os, xbmc, xbmcaddon

#########################################################
### Global Variables ####################################
#########################################################
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')
#########################################################

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'Man Cave Wizard'
BUILDERNAME    = 'Man Cave Entertainment'
EXCLUDES       = [ADDON_ID, 'plugin.program.mancavewizard']
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30
# Text File with build info in it.
BUILDFILE      = 'http://wizard.mancavekodi.com/text/autobuilds.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE        = 'http://wizard.mancavekodi.com/text/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'Media'
YOUTUBEFILE    = 'http://wizard.mancavekodi.com/text/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://wizard.mancavekodi.com/text/Advanced.txt'
#########################################################

#########################################################
### Theming Menu Items ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://wizard.mancavekodi.com/images/builds.png'
ICONMAINT      = 'http://wizard.mancavekodi.com/images/maintenance.png'
ICONSPEED      = 'http://wizard.mancavekodi.com/images/builds.png'
ICONAPK        = 'http://wizard.mancavekodi.com/images/builds.png'
ICONADDONS     = 'http://wizard.mancavekodi.com/images/addoninstallert.png'
ICONYOUTUBE    = 'http://wizard.mancavekodi.com/images/youtube.png'
ICONSAVE       = 'http://wizard.mancavekodi.com/images/savedate.png'
ICONTRAKT      = 'http://wizard.mancavekodi.com/images/trakt.png'
ICONREAL       = 'http://wizard.mancavekodi.com/images/realdebrid.png'
ICONLOGIN      = 'http://wizard.mancavekodi.com/images/mancave.png'
ICONCONTACT    = 'http://wizard.mancavekodi.com/images/contact.png'
ICONSETTINGS   = 'http://wizard.mancavekodi.com/images/settings.png'
# Hide the section seperators 'Yes' or 'No'
HIDESPACERS    = 'Yes'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'lightgoldenrodyellow'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I]([COLOR '+COLOR2+']Man Cave[/COLOR])[/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Current Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Current Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing Man Cave Wizard.\r\n\r\nContact us on facebook at https://www.facebook.com/groups/mancavewizard/'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = os.path.join(ART, 'http://wizard.mancavekodi.com/images/contact.png')
CONTACTFANART  = 'http://wizard.mancavekodi.com/images/wallpaper.jpg'
#########################################################

#########################################################
### Auto Update                   #######################
###        For Those With No Repo #######################
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'http://wizard.mancavekodi.com/text/autobuilds.txt'
#########################################################

#########################################################
### Auto Install                 ########################
###        Repo If Not Installed ########################
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'N0'
# Addon ID for the repository
REPOID         = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = ''
# Url to folder zip is located in
REPOZIPURL     = ''
#########################################################

#########################################################
### Notification Window #################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'Yes'
# Url to notification file
NOTIFICATION   = 'http://wizard.mancavekodi.com/text/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
# Font size of header
FONTHEADER     = 'Font14'
HEADERMESSAGE  = 'Man Cave Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = 'http://'
# Font for Notification Window
FONTSETTINGS   = 'Font13'
# Background for Notification Window
BACKGROUND     = 'http://wizard.mancavekodi.com/images/mancave.png'
#########################################################
