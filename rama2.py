# lenguajes.py (Rama 2 - Cristian David Rodriguez Ruiz)

# Definición de los lenguajes base
L1 = {"a", "b", "ab", "ba"}
L2 = {"b", "c", "bc", "cb"}
L3 = {"a", "b", "c"}
L4 = {"ab", "ac"}
L5 = {"b", "bc", "ca", "c"}

def interseccion_lenguajes(L, M):

    return L & M

def pertenece(palabra, lenguaje):
 
    return palabra in lenguaje

def ejercicios_interseccion():
    """Resuelve los 10 ejercicios de intersección de lenguajes"""
    print("=== EJERCICIOS DE INTERSECCIÓN ===")
    
    # 1. Intersección L1 ∩ L2
    resultado1 = interseccion_lenguajes(L1, L2)
    print(f"1. L1 ∩ L2 = {resultado1}")
    
    # 2. Intersección L1 ∩ L3
    resultado2 = interseccion_lenguajes(L1, L3)
    print(f"2. L1 ∩ L3 = {resultado2}")
    
    # 3. Intersección L2 ∩ L3
    resultado3 = interseccion_lenguajes(L2, L3)
    print(f"3. L2 ∩ L3 = {resultado3}")
    
    # 4. Intersección L4 ∩ L5
    resultado4 = interseccion_lenguajes(L4, L5)
    print(f"4. L4 ∩ L5 = {resultado4}")
    
    # 5. Intersección L1 ∩ L2 ∩ L3
    interseccion_parcial = interseccion_lenguajes(L1, L2)
    resultado5 = interseccion_lenguajes(interseccion_parcial, L3)
    print(f"5. L1 ∩ L2 ∩ L3 = {resultado5}")
    
    # 6. Lenguajes A = {"01","10","11"} y B = {"10","00","1"}
    A = {"01", "10", "11"}
    B = {"10", "00", "1"}
    resultado6 = interseccion_lenguajes(A, B)
    print(f"6. A ∩ B = {resultado6}")
    
    # 7. Lenguajes A = {"x","y","z"} y B = {"m","n","z"}
    A = {"x", "y", "z"}
    B = {"m", "n", "z"}
    resultado7 = interseccion_lenguajes(A, B)
    print(f"7. A ∩ B = {resultado7}")
    
    # 8. (L1 ∩ L2) y comprobar si "a" pertenece
    interseccion_l1_l2 = interseccion_lenguajes(L1, L2)
    pertenece_a = pertenece("a", interseccion_l1_l2)
    print(f"8. (L1 ∩ L2) = {interseccion_l1_l2}")
    print(f"   ¿Pertenece 'a' a (L1 ∩ L2)? {pertenece_a}")
    
    # 9. (L4 ∩ L5) y comprobar si "b" pertenece
    interseccion_l4_l5 = interseccion_lenguajes(L4, L5)
    pertenece_b = pertenece("b", interseccion_l4_l5)
    print(f"9. (L4 ∩ L5) = {interseccion_l4_l5}")
    print(f"   ¿Pertenece 'b' a (L4 ∩ L5)? {pertenece_b}")
    
    # 10. Ejemplo adicional: Intersección de L2 y L3
    resultado10 = interseccion_lenguajes(L2, L3)
    print(f"10. Intersección adicional: L2 ∩ L3 = {resultado10}")

if __name__ == "__main__":
    ejercicios_interseccion()