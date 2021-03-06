# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.
import os
import sys
fpath = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                     '../fdint/gfd.pyx'))

with open(fpath, 'w') as f:
    f.write("""# Copyright (c) 2015, Scott J Maddox. All rights reserved.
# Use of this source code is governed by the BSD-3-Clause
# license that can be found in the LICENSE file.

# This file was generated by `scripts/gen_gfd_pyx.py`.
# Do not edit this file directly, or your changes will be lost.
'''
Generalized Fermi-Dirac integrals.
'''
""")
    f.write('from fdint cimport _fdint\n')
    f.write('import numpy\n')
    for i in xrange(-1,6,2):
        a = str(i).replace('-','m')
        f.write('''
def gfd{a}h(phi, beta, out=None):
    cdef int num
    if isinstance(phi, numpy.ndarray):
        num = phi.shape[0]
        assert isinstance(beta, numpy.ndarray) and beta.shape[0] == num
        if out is None:
            out = numpy.empty(num)
        else:
            assert isinstance(out, numpy.ndarray) and out.shape[0] == num
        _fdint.vgfd{a}h(phi, beta, out)
        return out
    else:
        assert not isinstance(beta, numpy.ndarray)
        return _fdint.gfd{a}h(phi, beta)
'''.format(a=a))
