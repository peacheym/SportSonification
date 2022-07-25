from tkinter import X
import numpy as np
import argparse
import matplotlib.pyplot as plt
import libmapper as mpr

REFRESH_RATE = int(1/104 * 1000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--playback-multiplier",
                        default="1", type=float, help="Playback speed multiplier. Higher number == slower playback")
    parser.add_argument("--filename",
                        default="./ergdata.txt", help="file name associated with acceleration data.")
    # parser.add_argument("--debug",
    #                     default=False, action="store_false", help="Set to true for debug messages to print.")

    # TODO: Fix debug above.

    args = parser.parse_args()

    def smooth(y, box_pts):
        box = np.ones(box_pts)/box_pts
        y_smooth = np.convolve(y, box, mode='same')
        return y_smooth - 10

    f = open(args.filename)

    x_axis = []
    y_axis = []
    z_axis = []
    avg = []
    vel = []

    last_vel = 0

    for i in f:
        line = i.split(",")
        x_axis.append(float(line[0]))
        y_axis.append(float(line[1]))
        # Z Axis seems to hover around 1 rather than 0 like X & Y.
        z_axis.append(1-float(line[2]))

        # Average of three axis
        avg_a = (float(line[0]) + float(line[1]) + float(line[0]))/3 - 5
        avg.append(avg_a)

    window = 10
    avg_smooth = smooth(z_axis, window)

    avg_smooth[:window] = -10
    avg_smooth[-window:] = -10

    dev = mpr.Device("data")

    # # if args.debug:
    #     print(data.min(), data.max())

    sig_out_x = dev.add_signal(mpr.Direction.OUTGOING, "acc_x",
                               1, mpr.Type.FLOAT, "m/s^2", float(np.asarray(x_axis).min()), float(np.asarray(x_axis).max()))

    sig_out_y = dev.add_signal(mpr.Direction.OUTGOING, "acc_y",
                               1, mpr.Type.FLOAT, "m/s^2", float(np.asarray(y_axis).min()), float(np.asarray(y_axis).max()))

    sig_out_z = dev.add_signal(mpr.Direction.OUTGOING, "acc_z",
                               1, mpr.Type.FLOAT, "m/s^2", float(np.asarray(z_axis).min()), float(np.asarray(z_axis).max()))


    """
    " Initialize main libmapper loop below.
    """
    curr = 0
    print("Starting datamapper device...")
    while True:
        dev.poll(int(REFRESH_RATE * args.playback_multiplier))
        sig_out_x.set_value(float(x_axis[curr]))
        sig_out_y.set_value(float(y_axis[curr]))
        sig_out_z.set_value(float(z_axis[curr]))

        # print(float(z_axis[curr]))
        curr += 1

        if(curr >= len(x_axis)):
            curr = 0
            print("*******************")
