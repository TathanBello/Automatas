# lenguajes.py (Rama 1 - Yury Andrea Dorado Lucas)

# Definición de los lenguajes base
L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}

def union_lenguajes(L, M):
    return L | M

def pertenece(palabra, lenguaje):

    return palabra in lenguaje

def ejercicios_union():
    """Resuelve los 10 ejercicios de unión de lenguajes"""
    print("=== EJERCICIOS DE UNIÓN ===")
    
    # 1. Unión L1 ∪ L2
    resultado1 = union_lenguajes(L1, L2)
    print(f"1. L1 ∪ L2 = {resultado1}")
    
    # 2. Unión L1 ∪ L3
    resultado2 = union_lenguajes(L1, L3)
    print(f"2. L1 ∪ L3 = {resultado2}")
    
    # 3. Unión L2 ∪ L3
    resultado3 = union_lenguajes(L2, L3)
    print(f"3. L2 ∪ L3 = {resultado3}")
    
    # 4. Unión L4 ∪ L5
    resultado4 = union_lenguajes(L4, L5)
    print(f"4. L4 ∪ L5 = {resultado4}")
    
    # 5. Unión L1 ∪ L2 ∪ L3
    union_parcial = union_lenguajes(L1, L2)
    resultado5 = union_lenguajes(union_parcial, L3)
    print(f"5. L1 ∪ L2 ∪ L3 = {resultado5}")
    
    # 6. Lenguajes A = {"cad","aca","ad"} y B = {"a","d","c"}
    A = {"cad", "aca", "ad"}
    B = {"a", "d", "c"}
    resultado6 = union_lenguajes(A, B)
    print(f"6. A ∪ B = {resultado6}")
    
    # 7. Lenguajes A = {"10","01","11"}, B = {"0","1"} y C = {"00","10"}
    A = {"10", "01", "11"}
    B = {"0", "1"}
    C = {"00", "10"}
    union_ab = union_lenguajes(A, B)
    resultado7 = union_lenguajes(union_ab, C)
    print(f"7. A ∪ B ∪ C = {resultado7}")
    
    # 8. (L1 ∪ L2) y comprobar si "abc" pertenece
    union_l1_l2 = union_lenguajes(L1, L2)
    pertenece_abc = pertenece("abc", union_l1_l2)
    print(f"8. (L1 ∪ L2) = {union_l1_l2}")
    print(f"   ¿Pertenece 'abc' a (L1 ∪ L2)? {pertenece_abc}")
    
    # 9. (L4 ∪ L5) y comprobar si "a" pertenece
    union_l4_l5 = union_lenguajes(L4, L5)
    pertenece_a = pertenece("a", union_l4_l5)
    print(f"9. (L4 ∪ L5) = {union_l4_l5}")
    print(f"   ¿Pertenece 'a' a (L4 ∪ L5)? {pertenece_a}")
    
    # 10. Ejemplo adicional: Unión de L1 y L4
    resultado10 = union_lenguajes(L1, L4)
    print(f"10. Unión adicional: L1 ∪ L4 = {resultado10}")

if __name__ == "__main__":
    ejercicios_union()