import matplotlib.pyplot as plt


def select_analyze_data():
    # subplots 생성
    fig, axs = plt.subplots(3, 3, figsize=(18, 8))
    fig.subplots_adjust(hspace=0.8, wspace=0.5)

    ax1, ax2, ax3, ax4, ax5, ax6, ax7 = axs[1][0], axs[0][0], axs[0][1], axs[0][2], axs[1][1], axs[2][0], axs[1][2]

    #Hide other graph
    for ax in axs.flatten():
        if ax not in [ax1, ax2, ax3, ax4, ax5, ax6, ax7]:
            ax.axis('off')

    return ax1, ax2, ax3, ax4, ax5, ax6, ax7
