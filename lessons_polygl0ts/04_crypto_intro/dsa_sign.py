import hashlib, secrets
def dsa_sign(q, p, g, x, message: bytes) -> tuple[int, int]:
    m = int.from_bytes(hashlib.sha1(message).digest(), "big")
    r = s = 0
    while r == 0 or s == 0:
        k = 2 + secrets.randbelow(q - 2)
        r = pow(g, k, p) % q
        s = pow(k, -1, q) * (m + x * r) % q
    return r, s
