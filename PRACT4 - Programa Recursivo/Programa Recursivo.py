import time

# ── RECURSIVO ──────────────────────────────────────────
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# ── ITERATIVO ──────────────────────────────────────────
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# ── MENÚ ───────────────────────────────────────────────
def main():
    print("=== FIBONACCI: Recursivo vs Iterativo ===\n")

    n = int(input("Ingresa n: "))

    # Recursivo
    inicio = time.perf_counter()
    resultado = fibonacci_recursivo(n)
    tiempo = time.perf_counter() - inicio
    print(f"\nRecursivo  → F({n}) = {resultado}  |  Tiempo: {tiempo:.6f}s")

    # Iterativo
    inicio = time.perf_counter()
    resultado = fibonacci_iterativo(n)
    tiempo = time.perf_counter() - inicio
    print(f"Iterativo  → F({n}) = {resultado}  |  Tiempo: {tiempo:.6f}s")

main()
