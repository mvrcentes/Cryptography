from Utility import Utility

# https://andrea.corbellini.name/2015/05/30/elliptic-curve-cryptography-ecdh-and-ecdsa/
class ECCKeyGenerator:
    def __init__(self):
        self.utility = Utility()
        self.curve = {
            'name': 'secp256k1',
            'p': 0xfffffffffffffffffffffffffffffffffffffffffffffffffffffffefffffc2f,
            'a': 0,
            'b': 7,
            'g': (0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798,
                  0x483ada7726a3c4655da4fbfc0e1108a8fd17b448a68554199c47d08ffb10d4b8),
            'n': 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141,
            'h': 1
        }

    def inverse_mod(self, k, p):
        """Calcula el inverso modular de k mod p."""
        if k == 0:
            raise ZeroDivisionError('division by zero')
        if k < 0:
            return p - self.inverse_mod(-k, p)

        s, old_s = 0, 1
        t, old_t = 1, 0
        r, old_r = p, k

        while r != 0:
            quotient = old_r // r
            old_r, r = r, old_r - quotient * r
            old_s, s = s, old_s - quotient * s
            old_t, t = t, old_t - quotient * t

        return old_s % p

    def is_on_curve(self, point):
        """Verifica si un punto está en la curva elíptica."""
        if point is None:
            return True

        x, y = point
        return (y * y - x * x * x - self.curve['a'] * x - self.curve['b']) % self.curve['p'] == 0

    def point_add(self, point1, point2):
        """Suma dos puntos en la curva."""
        if point1 is None:
            return point2
        if point2 is None:
            return point1

        x1, y1 = point1
        x2, y2 = point2

        if x1 == x2 and y1 != y2:
            return None

        if x1 == x2:
            m = (3 * x1 * x1 + self.curve['a']) * self.inverse_mod(2 * y1, self.curve['p'])
        else:
            m = (y1 - y2) * self.inverse_mod(x1 - x2, self.curve['p'])

        x3 = m * m - x1 - x2
        y3 = y1 + m * (x3 - x1)
        result = (x3 % self.curve['p'], -y3 % self.curve['p'])

        return result

    def scalar_mult(self, k, point):
        """Multiplica un punto por un escalar."""
        if k % self.curve['n'] == 0 or point is None:
            return None

        if k < 0:
            return self.scalar_mult(-k, self.point_neg(point))

        result = None
        addend = point

        while k:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1

        return result

    def ascii_to_private_key(self, ascii_text):
        """Convierte texto ASCII en una clave privada numérica usando las funciones de Utility."""
        binary_representation = ''.join(self.utility.ascii_to_binary(ascii_text))
        private_key = int(binary_representation, 2) % self.curve['n']  # Ajuste para el rango de la curva
        return private_key

    def generate_key_pair(self, ascii_text):
        """Genera un par de claves a partir de un texto ASCII."""
        private_key = self.ascii_to_private_key(ascii_text)
        public_key = self.scalar_mult(private_key, self.curve['g'])
        return private_key, public_key