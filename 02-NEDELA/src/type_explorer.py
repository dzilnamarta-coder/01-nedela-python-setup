# --- 1. PAMATA TIPI UN TYPE() ---
vards = "Marta"         # str (virkne)
vecums = 21             # int (vesels skaitlis)
augstums = 1.68         # float (daļskaitlis)
ir_students = True      # bool (loģiskais tips)
dati = None             # NoneType (tukša vērtība)

print(f"Vērtība: {vards}, Tips: {type(vards)}")
print(f"Vērtība: {vecums}, Tips: {type(vecums)}")
print(f"Vērtība: {augstums}, Tips: {type(augstums)}")
print(f"Vērtība: {ir_students}, Tips: {type(ir_students)}")

# --- 2. TRUTHY / FALSY EKSPERIMENTI ---
print("\n--- Truthy / Falsy ---")
print(f"Tukša virkne: {bool('')}")    # False
print(f"Atstarpe: {bool(' ')}")       # True (simbols eksistē!)
print(f"Skaitlis 0: {bool(0)}")        # False
print(f"Virkne '0': {bool('0')}")     # True (tā ir netukša virkne)

# --- 3. KONVERSIJA UN ROBEŽGADĪJUMI ---
print("\n--- Konversijas ---")
print(int("5") + 3)          # 8 (no str uz int)
print(int(3.86))             # 3 (norauj decimāldaļu)

# Robežgadījums: nevar pārvērst tekstu ar punktu pa taisno par int
# print(int("3.14"))       # Šis izmests ValueError
print(int(float("3.14")))    # Šis strādā: str -> float -> int

# --- 4. INTERESANTIE GADĪJUMI ---
print("\n--- Interesantie gadījumi ---")
print(f"True + True: {True + True}")       # 2 (True ir 1)
print(f"0.1 + 0.2 == 0.3: {0.1 + 0.2 == 0.3}") # False (precizitātes dēļ)
print(f"round(2.5): {round(2.5)}")         # 2
print(f"round(3.5): {round(3.5)}")         # 4