# Color algebra definitions (REQUIRED by MG5 even for U(1) models)
import cmath

# Identity color factor (for singlets)
def one(color):
    return 1

# Color matrix class (MG5 expects this)
class Color(object):
    pass

# Color basis definition (crucial for ALOHA)
color_basis = ['1']

# Color matrix definitions (even for trivial case)
color_matrices = {
    'Identity': {
        (0,0): 1
    }
}