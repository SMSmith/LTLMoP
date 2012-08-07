# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
foldArms, 1

CompileOptions:
convexify: False
fastslow: False

CurrentConfigName:
Untitled configuration

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
willowExample.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
wait, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
Office = p16
lab2 = p15
Lab1 = p17
others = p1

Spec: # Specification in structured English
robot starts in Office with false
infinitely often not wait

visit lab2
visit Office

if you were in Office then do foldArms

if you are sensing wait then stay there

