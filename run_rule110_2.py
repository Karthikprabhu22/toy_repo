import three_state_ca
import matplotlib.pyplot as plt
initial_conditions = three_state_ca.random_string(10)
field = three_state_ca.spacetime_field(110, initial_conditions, 10)
three_state_ca.spacetime_diagram(field)
plt.savefig('rule110_2.pdf')
