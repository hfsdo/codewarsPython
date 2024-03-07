def tribonacci(signature, n):
    if (n<=3):
        return signature[0:n]
    i = len(signature)
    signature.append(signature[i-3]+signature[i-2]+signature[i-1])
    if (n>4):
        tribonacci(signature, n-1)
    return signature