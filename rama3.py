# lenguajes.py (Rama 3 - Jonathan David Lancheros Bello)
# Definición de los lenguajes base
L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}

def concatenacion_lenguajes(L, M):
    resultado = set()
    for palabra1 in L:
        for palabra2 in M:
            resultado.add(palabra1 + palabra2)
    return resultado

def pertenece(palabra, lenguaje):
    return palabra in lenguaje

def ejercicios_concatenacion():
    """Resuelve los 10 ejercicios de concatenación de lenguajes"""
    print("=== EJERCICIOS DE CONCATENACIÓN ===")
    
    # 1. Concatenación L1 · L3
    resultado1 = concatenacion_lenguajes(L1, L3)
    print(f"1. L1 · L3 = {resultado1}")
    
    # 2. Concatenación L3 · L1
    resultado2 = concatenacion_lenguajes(L3, L1)
    print(f"2. L3 · L1 = {resultado2}")
    
    # 3. Concatenación L4 · L5
    resultado3 = concatenacion_lenguajes(L4, L5)
    print(f"3. L4 · L5 = {resultado3}")
    
    # 4. Concatenación L5 · L4
    resultado4 = concatenacion_lenguajes(L5, L4)
    print(f"4. L5 · L4 = {resultado4}")
    
    # 5. Concatenación L1 · L2
    resultado5 = concatenacion_lenguajes(L1, L2)
    print(f"5. L1 · L2 = {resultado5}")
    
    # 6. Lenguajes A = {"a","b"} y B = {"a","c"}
    A = {"a", "b"}
    B = {"a", "c"}
    resultado6 = concatenacion_lenguajes(A, B)
    print(f"6. A · B = {resultado6}")
    
    # 7. Lenguajes A = {"0","1"} y B = {"", "00"} (epsilon es cadena vacía)
    A = {"0", "1"}
    B = {"", "00"}  # epsilon representado como cadena vacía
    resultado7 = concatenacion_lenguajes(A, B)
    print(f"7. A · B = {resultado7}")
    
    # 8. (L1 · L2) y comprobar si "aba" pertenece
    concat_l1_l2 = concatenacion_lenguajes(L1, L2)
    pertenece_aba = pertenece("aba", concat_l1_l2)
    print(f"8. (L1 · L2) = {concat_l1_l2}")
    print(f"   ¿Pertenece 'aba' a (L1 · L2)? {pertenece_aba}")
    
    # 9. (L3 · L4) y comprobar si "cab" pertenece
    concat_l3_l4 = concatenacion_lenguajes(L3, L4)
    pertenece_cab = pertenece("cab", concat_l3_l4)
    print(f"9. (L3 · L4) = {concat_l3_l4}")
    print(f"   ¿Pertenece 'cab' a (L3 · L4)? {pertenece_cab}")
    
    # 10. Ejemplo adicional: Concatenación de L2 y L5
    resultado10 = concatenacion_lenguajes(L2, L5)
    print(f"10. Concatenación adicional: L2 · L5 = {resultado10}")

if __name__ == "__main__":
    ejercicios_concatenacion()