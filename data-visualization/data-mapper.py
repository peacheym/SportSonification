import numpy as np
import argparse
import matplotlib.pyplot as plt
import libmapper as mpr

REFRESH_RATE = int(1/104 * 1000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--playback-multiplier",
                        default="1", type=float, help="Playback speed multiplier. Higher number == slower playback")
    # parser.add_argument("--debug",
    #                     default=False, action="store_false", help="Set to true for debug messages to print.")
    
    # TODO: Fix debug above.

    args = parser.parse_args()

    data = np.load('data.npy')

    data = data + 10  # TODO: Import proper dataset

    dev = mpr.Device("data")
    
    # # if args.debug:
    #     print(data.min(), data.max())

    sig_out = dev.add_signal(mpr.Direction.OUTGOING, "data",
                            1, mpr.Type.FLOAT, "a", float(data.min()), float(data.max()))

    curr = 0

    while True:
        dev.poll(int(REFRESH_RATE * args.playback_multiplier))
        sig_out.set_value(float(data[curr]))
        # print(float(data[curr]))
        curr += 1

        if(curr >= len(data)):
            curr = 0
            print("*******************")
