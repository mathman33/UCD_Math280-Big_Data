from __future__ import division

import matplotlib.pyplot as plt
import numpy as np
import gc as garbage

normally_distributed = [
    0,
    1.4069e-13,
    6.9317e-10,
    3.1246e-10,
    6.204e-10,
    6.5421e-13,
    1.0399e-12,
    1.0523e-12,
    1.2633e-12,
    1.9475e-12,
    1.6035e-12,
    4.1611e-12,
    2.6914e-12,
    3.8275e-09,
    2.7451e-12,
    1.751e-09,
    4.0219e-09,
    3.4676e-12,
    3.4321e-11,
    3.1465e-09,
    5.8438e-09,
    0.20935,
    0.0051273,
    5.6003e-08,
    0.029257,
    0.25248,
    0.22326,
    0.31448,
    0.67176,
    0.73926,
    0.50769,
    0.77005,
    1.6653,
    1.1427,
    1.529,
    1.5499,
    1.8609,
    2.122,
    2.3833,
    3.038,
    3.1217]

normally_distributed_nonnegative = [
    0,
    3.8239e-11,
    6.1125e-11,
    1.9041e-10,
    2.2666e-13,
    2.9219e-13,
    4.8903e-13,
    6.983e-13,
    9.855e-13,
    1.0762e-12,
    1.8476e-12,
    1.8539e-12,
    2.8613e-12,
    4.2962e-10,
    3.4281e-12,
    7.9764e-09,
    5.7421e-09,
    4.8189e-09,
    6.5628e-11,
    3.6516e-09,
    6.4377e-12,
    7.2957e-09,
    2.4122e-08,
    1.9064e-09,
    0.028952,
    0.17898,
    0.2903,
    0.50774,
    0.24714,
    1.0232,
    0.55508,
    0.67906,
    1.1941,
    1.1893,
    1.1397,
    2.0971,
    1.2408,
    2.562,
    2.2939,
    1.7495,
    2.4697]

plt.figure()
plt.semilogy(normally_distributed, "k", linewidth=2)
plt.xlabel(r"$s$-sparse")
plt.ylabel(r"$\ell^2$-Norm Error")
plt.title("Normally Distributed Sparse Vectors")
plt.savefig("normally_distributed.png", dpi=300)
plt.close()

plt.figure()
plt.semilogy(normally_distributed_nonnegative, "k", linewidth=2)
plt.xlabel(r"$s$-sparse")
plt.ylabel(r"$\ell^2$-Norm Error")
plt.title("Absolute Value of Normally Distributed Sparse Vectors")
plt.savefig("normally_distributed_nonnegative.png", dpi=300)
plt.close()


garbage.collect()
