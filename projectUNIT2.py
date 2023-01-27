Avogadro_num = float (6.022140876 * 10**23)
weight_1 = float (input())
atomic_mass_of_element = float (input())
amount_of_moles = weight_1/atomic_mass_of_element
final_amount_of_moles = round(amount_of_moles,3)
final_amount_of_atoms = final_amount_of_moles * Avogadro_num
print (final_amount_of_atoms)
