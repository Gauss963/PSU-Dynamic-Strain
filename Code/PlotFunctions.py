import matplotlib
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

def do_waveform_plot(DATAS: list[np.ndarray], fs: float = 100000) -> str:

    font1 = {'family':'serif', 'color':'black', 'size':20}
    font2 = {'family':'serif', 'color':'black', 'size':14}
    plt.ioff()

    filename = f'../Plot/do_waveform_plot.pdf'

    fig = plt.figure(figsize = (16, 12))
    gs = gridspec.GridSpec(len(DATAS), 1, height_ratios=[1] * len(DATAS))


    for i in range(len(DATAS)):
        WAVEFORM_DATA = DATAS[i]

        TIME = np.linspace(0, len(WAVEFORM_DATA), len(WAVEFORM_DATA))
        TIME = TIME / fs

        ax = plt.subplot(gs[i, 0])
        
        max_index = np.argmax(WAVEFORM_DATA)
        
        ax.plot(TIME, WAVEFORM_DATA, color = 'C0', label = f'Max Index: {max_index}')
        ax.axvline(x = TIME[max_index], color = 'red')
        ax.set_yticklabels([])
        ax.set_yticks([])
        ax.legend(loc = 'upper right')

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.0, hspace=0.0)
    plt.savefig(filename, dpi=900, bbox_inches = 'tight')
    plt.show()
    plt.close()

    return filename