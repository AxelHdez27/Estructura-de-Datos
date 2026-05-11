"""
LIBRERÍA DE ORDENAMIENTO INTERNO
Métodos implementados:
1. Burbuja (Bubble Sort)
2. Inserción (Insertion Sort)
3. Selección (Selection Sort)
4. Radix Sort
5. Heap Sort
6. Quick Sort
7. Shell Sort
"""

from random import randrange
from typing import List, Union

Number = Union[int, float]


# =============================================================
# MÉTODOS BÁSICOS O(n²)
# =============================================================

def bubble_sort(arr: List[Number]) -> List[Number]:
    """
    Método Burbuja
    Complejidad: O(n²)
    Compara elementos adyacentes y los intercambia si están en orden incorrecto
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(arr: List[Number]) -> List[Number]:
    """
    Método por Inserción
    Complejidad: O(n²)
    Construye la lista ordenada insertando cada elemento en su posición correcta
    """
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr: List[Number]) -> List[Number]:
    """
    Método por Selección
    Complejidad: O(n²)
    Encuentra el mínimo elemento y lo coloca al inicio
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# =============================================================
# MÉTODOS AVANZADOS O(n log n)
# =============================================================

RADIX = 10

def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort
    Complejidad: O(n * d) donde d es número de dígitos
    Solo para números enteros no negativos
    """
    if not arr:
        return []
    arr = arr[:]
    placement = 1
    max_digit = max(arr)
    while placement <= max_digit:
        buckets = [[] for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            for i in buckets[b]:
                arr[a] = i
                a += 1
        placement *= RADIX
    return arr


def heapify(arr: List[int], index: int, heap_size: int) -> None:
    """Función auxiliar para Heap Sort"""
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort
    Complejidad: O(n log n)
    Utiliza una estructura de montículo (heap)
    """
    arr = arr[:]
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


def quick_sort(arr: List) -> List:
    """
    Quick Sort
    Complejidad: O(n log n) promedio, O(n²) peor caso
    Usa pivote para dividir y conquistar
    """
    if len(arr) < 2:
        return arr[:]
    arr = arr[:]
    pivot_index = randrange(len(arr))
    pivot = arr.pop(pivot_index)
    lesser = [item for item in arr if item <= pivot]
    greater = [item for item in arr if item > pivot]
    return [*quick_sort(lesser), pivot, *quick_sort(greater)]


def shell_sort(arr: List[int]) -> List[int]:
    """
    Shell Sort
    Complejidad: O(n log² n)
    Versión mejorada del ordenamiento por inserción
    """
    arr = arr[:]
    gaps = [701, 301, 132, 57, 23, 10, 4, 1]
    for gap in gaps:
        for i in range(gap, len(arr)):
            insert_value = arr[i]
            j = i
            while j >= gap and arr[j - gap] > insert_value:
                arr[j] = arr[j - gap]
                j -= gap
            if j != i:
                arr[j] = insert_value
    return arr


# =============================================================
# DICCIONARIO DE MÉTODOS DISPONIBLES
# =============================================================

METODOS_INTERNOS = {
    "1": ("Burbuja (Bubble Sort)", bubble_sort, "O(n²) - Compara elementos adyacentes"),
    "2": ("Inserción (Insertion Sort)", insertion_sort, "O(n²) - Inserta cada elemento en su posición"),
    "3": ("Selección (Selection Sort)", selection_sort, "O(n²) - Selecciona el mínimo repetidamente"),
    "4": ("Radix Sort", radix_sort, "O(n*d) - Ordena por dígitos (solo enteros)"),
    "5": ("Heap Sort", heap_sort, "O(n log n) - Usa estructura de montículo"),
    "6": ("Quick Sort", quick_sort, "O(n log n) - Divide y conquista con pivote"),
    "7": ("Shell Sort", shell_sort, "O(n log² n) - Inserción mejorada"),
}
