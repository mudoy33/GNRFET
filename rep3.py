# Read in the old configuration
device_configuration = nlread("zaz66_gate_pos1_25.hdf5",DeviceConfiguration)[0]
calculator = device_configuration.calculator()
# Output filename
filename = 'ivscan-6-6_1_0_gate_pos1_25.hdf5'
# Define bias voltages
voltage_list=numpy.linspace(-2,2.0,50)*Volt
for voltage in voltage_list:
    # Set new calculator with modified electrode voltages on the configuration
    # use the self consistent state of the old calculation as starting input.
    device_configuration.setCalculator(
    calculator(electrode_voltages=(1*voltage,0*voltage)),
               initial_state=device_configuration)
    #Analysis
    
    
    transmission_spectrum = TransmissionSpectrum(
        configuration=device_configuration,
        energies=numpy.linspace(-2,2,200)*eV)
    nlsave(filename, transmission_spectrum, object_id='trans'+str(voltage))
    nlprint(transmission_spectrum)
