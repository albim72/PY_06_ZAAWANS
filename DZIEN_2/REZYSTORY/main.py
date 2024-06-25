from oldresistor import OldResistor
from resistor import Resistor
from voltage import VoltageResistance

print("_______ klasa OldResistor _______")
r0=OldResistor(10.2E3)
print(r0)
print(r0.get_ohms())
r0.set_ohms(2.88E3)
print(r0.get_ohms())

print("_______ klasa Resistor _______")
r1 = Resistor(50E3)
r1.ohms = 18.3
print(f'układ elektryczny \n'
      f'oporność: {r1.ohms} omów\n'
      f'napięcie eleketryczne: {r1.voltage} V\n'
      f'natężenie elektryczne: {r1.current} A\n')

print("_______ klasa VoltageResistance _______")
r2 = VoltageResistance(1E3)
print(f'początkowe natężenie prądu: {r2.current} A')
r2.voltage = 45
print(f'napięcie prądu : {r2.voltage} V')
print(f'natężenie prądu: {r2.current} A')
