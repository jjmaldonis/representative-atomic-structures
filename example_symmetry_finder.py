In [1]: import spglib

In [2]: import ASE
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-2-1c8eac75b72a> in <module>()
----> 1 import ASE

ModuleNotFoundError: No module named 'ASE'

In [3]: import ase

In [4]: import ase.io

In [5]: ase.io.read("ti_hexagonal.xyz")
Out[5]: Atoms(symbols='Ti550', pbc=False)

In [6]: ti_hex = ase.io.read("ti_hexagonal.xyz")

In [7]: ti_hex
Out[7]: Atoms(symbols='Ti550', pbc=False)

In [8]: spglib.get_symmetry(ti_hex)

In [9]: spglib.get_symmetry(ti_hex, symprec=1e-5)

In [10]: cell = ti_hex.cell()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-10-82170897ff2c> in <module>()
----> 1 cell = ti_hex.cell()

TypeError: 'numpy.ndarray' object is not callable

In [11]: cell = ti_hex.cell

In [12]: cell
Out[12]: 
array([[ 0.,  0.,  0.],
       [ 0.,  0.,  0.],
       [ 0.,  0.,  0.]])

In [13]: fe = ase.io.read("Fe_BCC.cif")

In [14]: spglib.get_symmetry(fe, symprec=1e-5)
Out[14]: 
{'equivalent_atoms': array([0, 0], dtype=int32),
 'rotations': array([[[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0,  1]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0, -1]],
 
        [[ 1,  0,  0],
         [ 0,  0, -1],
         [ 0,  1,  0]],
 
        [[-1,  0,  0],
         [ 0,  0,  1],
         [ 0, -1,  0]],
 
        [[ 1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0, -1]],
 
        [[-1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0,  1]],
 
        [[ 1,  0,  0],
         [ 0,  0,  1],
         [ 0, -1,  0]],
 
        [[-1,  0,  0],
         [ 0,  0, -1],
         [ 0,  1,  0]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0,  1]],
 
        [[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0, -1]],
 
        [[-1,  0,  0],
         [ 0,  0,  1],
         [ 0,  1,  0]],
 
        [[ 1,  0,  0],
         [ 0,  0, -1],
         [ 0, -1,  0]],
 
        [[-1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0, -1]],
 
        [[ 1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0,  1]],
 
        [[-1,  0,  0],
         [ 0,  0, -1],
         [ 0, -1,  0]],
 
        [[ 1,  0,  0],
         [ 0,  0,  1],
         [ 0,  1,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0, -1],
         [-1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0,  1],
         [ 1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0, -1,  0],
         [-1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0,  1,  0],
         [ 1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0,  1],
         [-1,  0,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0, -1],
         [ 1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0,  1,  0],
         [-1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0, -1,  0],
         [ 1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0, -1],
         [ 1,  0,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0,  1],
         [-1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0, -1,  0],
         [ 1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0,  1,  0],
         [-1,  0,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0,  1],
         [ 1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0, -1],
         [-1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0,  1,  0],
         [ 1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0, -1,  0],
         [-1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0,  0,  1],
         [-1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0, -1,  0],
         [ 1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0,  1,  0],
         [-1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 0,  0,  1],
         [ 1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0,  0, -1],
         [-1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0,  1,  0],
         [ 1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 0, -1,  0],
         [-1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0,  0, -1],
         [-1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0,  0,  1],
         [ 1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0, -1,  0],
         [-1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 0,  1,  0],
         [ 1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0,  0,  1],
         [-1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0,  0, -1],
         [ 1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0,  1,  0],
         [-1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0, -1,  0],
         [ 1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0,  1]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0, -1]],
 
        [[ 1,  0,  0],
         [ 0,  0, -1],
         [ 0,  1,  0]],
 
        [[-1,  0,  0],
         [ 0,  0,  1],
         [ 0, -1,  0]],
 
        [[ 1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0, -1]],
 
        [[-1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0,  1]],
 
        [[ 1,  0,  0],
         [ 0,  0,  1],
         [ 0, -1,  0]],
 
        [[-1,  0,  0],
         [ 0,  0, -1],
         [ 0,  1,  0]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0,  1]],
 
        [[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0, -1]],
 
        [[-1,  0,  0],
         [ 0,  0,  1],
         [ 0,  1,  0]],
 
        [[ 1,  0,  0],
         [ 0,  0, -1],
         [ 0, -1,  0]],
 
        [[-1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0, -1]],
 
        [[ 1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0,  1]],
 
        [[-1,  0,  0],
         [ 0,  0, -1],
         [ 0, -1,  0]],
 
        [[ 1,  0,  0],
         [ 0,  0,  1],
         [ 0,  1,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0, -1],
         [-1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0,  1],
         [ 1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0, -1,  0],
         [-1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0,  1,  0],
         [ 1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0,  1],
         [-1,  0,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0, -1],
         [ 1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0,  1,  0],
         [-1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0, -1,  0],
         [ 1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0, -1],
         [ 1,  0,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0,  1],
         [-1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0, -1,  0],
         [ 1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0,  1,  0],
         [-1,  0,  0]],
 
        [[ 0,  1,  0],
         [ 0,  0,  1],
         [ 1,  0,  0]],
 
        [[ 0, -1,  0],
         [ 0,  0, -1],
         [-1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 0,  1,  0],
         [ 1,  0,  0]],
 
        [[ 0,  0,  1],
         [ 0, -1,  0],
         [-1,  0,  0]],
 
        [[ 0,  0, -1],
         [ 1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0,  0,  1],
         [-1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0, -1,  0],
         [ 1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0,  1,  0],
         [-1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 0,  0,  1],
         [ 1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0,  0, -1],
         [-1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0,  1,  0],
         [ 1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 0, -1,  0],
         [-1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0,  0, -1],
         [-1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0,  0,  1],
         [ 1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0, -1,  0],
         [-1,  0,  0],
         [ 0,  0, -1]],
 
        [[ 0,  1,  0],
         [ 1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0,  0,  1],
         [-1,  0,  0],
         [ 0, -1,  0]],
 
        [[ 0,  0, -1],
         [ 1,  0,  0],
         [ 0,  1,  0]],
 
        [[ 0,  1,  0],
         [-1,  0,  0],
         [ 0,  0,  1]],
 
        [[ 0, -1,  0],
         [ 1,  0,  0],
         [ 0,  0, -1]]], dtype=int32),
 'translations': array([[ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  0. ],
        [ 1. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  0. ],
        [ 0. ,  1. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  1. ],
        [ 0. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  1. ],
        [ 1. ,  1. ,  0. ],
        [ 1. ,  1. ,  0. ],
        [ 0. ,  0. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  1. ],
        [ 1. ,  0. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  0. ,  1. ],
        [ 1. ,  1. ,  0. ],
        [ 1. ,  1. ,  0. ],
        [ 0. ,  0. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  1. ],
        [ 1. ,  0. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  1. ,  1. ],
        [ 0. ,  0. ,  1. ],
        [ 1. ,  1. ,  0. ],
        [ 1. ,  1. ,  0. ],
        [ 0. ,  0. ,  1. ],
        [ 1. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0. ,  1. ,  1. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 1. ,  0. ,  1. ]])}

In [15]: spglib.get_symmetry(fe, symprec=1e-5)["rotations"].shape
Out[15]: (96, 3, 3)

In [16]: spglib.get_symmetry(fe, symprec=1e-5)["translations"].shape
Out[16]: (96, 3)

In [17]: cu_zr = ase.io.read("CuZr2.cif")
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-17-078007976d77> in <module>()
----> 1 cu_zr = ase.io.read("CuZr2.cif")

/Users/jjmaldonis/.local/lib/python3.6/site-packages/ase/io/formats.py in read(filename, index, format, **kwargs)
    299         return list(_iread(filename, index, format, io, **kwargs))
    300     else:
--> 301         return next(_iread(filename, slice(index, None), format, io, **kwargs))
    302 
    303 

StopIteration: 

In [18]: cu_zr = ase.io.read("CuZr2\ copy.cif")
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
<ipython-input-18-da356f9072bf> in <module>()
----> 1 cu_zr = ase.io.read("CuZr2\ copy.cif")

/Users/jjmaldonis/.local/lib/python3.6/site-packages/ase/io/formats.py in read(filename, index, format, **kwargs)
    299         return list(_iread(filename, index, format, io, **kwargs))
    300     else:
--> 301         return next(_iread(filename, slice(index, None), format, io, **kwargs))
    302 
    303 

/Users/jjmaldonis/.local/lib/python3.6/site-packages/ase/io/formats.py in _iread(filename, index, format, io, full_output, **kwargs)
    358                 fd = bz2.BZ2File(filename + '.bz2')
    359             else:
--> 360                 fd = open(filename, 'rU')
    361             must_close_fd = True
    362         else:

FileNotFoundError: [Errno 2] No such file or directory: 'CuZr2\\ copy.cif'

In [19]: cu_zr = ase.io.read("CuZr2 copy.cif")

In [20]: spglib.get_symmetry(cu_zr, symprec=1e-5)["translations"].shape
Out[20]: (8, 3)

In [21]: spglib.get_symmetry(cu_zr, symprec=1e-5)["rotations"].shape
Out[21]: (8, 3, 3)

In [22]: spglib.get_symmetry(cu_zr, symprec=1e-5)
Out[22]: 
{'equivalent_atoms': array([0, 0, 0, 0, 4, 4, 4, 4, 8, 8, 8, 8], dtype=int32),
 'rotations': array([[[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0,  1]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0, -1]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0,  1]],
 
        [[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0, -1]],
 
        [[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0,  1]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0, -1]],
 
        [[-1,  0,  0],
         [ 0, -1,  0],
         [ 0,  0,  1]],
 
        [[ 1,  0,  0],
         [ 0,  1,  0],
         [ 0,  0, -1]]], dtype=int32),
 'translations': array([[ 0. ,  0. ,  0. ],
        [ 0. ,  0. ,  0. ],
        [ 0. ,  0. ,  0. ],
        [ 0. ,  0. ,  0. ],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5],
        [ 0.5,  0.5,  0.5]])}

In [23]: 

