import numpy as np
import matplotlib.pyplot as plt

data = np.load('/Users/hueyke/Downloads/p5993e.npz', allow_pickle=True)
data = data["experiment"][()]

# run 1 is the second run named shs1
# event 2 is the thrid event
event = data['runs'][1]['events'][2]


# this is the raw strain in voltage
# gage factor is 2
# I forgot the excitation voltage... Let me get back to you. It's definitely <= 15V.
# you need to convert the raw voltage strain data in Voltage to strain.
# gage 6 is the 7th strain gage
# gages 0--12 are exy
# gages 13--15 are eyy of gage 0, 6, and 12
# using gage 6 gives you both exy and eyy to fit simultaneously 
# locations of each gage can be found at event['strain']['locations']
exy6 = event['strain']['raw'][6]
eyy6 = event['strain']['raw'][12]
plt.plot(event['strain']['time'], exy6 - exy6[0], label=r'$\epsilon_{xy}$')
plt.plot(event['strain']['time'], eyy6 - eyy6[0], label=r'$\epsilon_{yy}$')
plt.show()


# info about the strain gage
# KFGS-5-350-D17-16 Strain Gage Package of 10
# Series: KFGS
# Gage length: 5 mm
# Gage resistance: 350 ohm
# Gage pattern: Triaxial
# Applicable Linear Expansion Coefficient (x10–6/°C ): 16
# Lead wire: 25mm long silver coated copper wire
# 10 pcs / package