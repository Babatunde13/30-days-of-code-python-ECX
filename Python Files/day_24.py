def intensive_properties(properties, units):
    """
    This function takes in a tuple of pressure  and  temperature  values  in SI  units 
    (N/m^2 and  K)  and  a tuple  containing  the  desired  output  unit  as parameters 
    then  returns  a  tuple  of the pressure  and temperature  in  the  desired  units. 
    e.g   intensive_properties((101325, 298),(atm,  oC))  returns  (1, 25) 
    (Valid  output
    pressure  units:[Pa,  atm,  mmHg,  Bar]
    output  temperature  units:[ oC, oF, oR]).
    """    
    try:
        pressure, temperature = [float(i) for i in properties]
        if pressure < 0 or temperature < 0:
            raise TypeError
        p_unit, t_unit = units
        #p_unit is the desired pressure unit
        #t_unit is the desired temperature unit     
        
        #Pressure conversion
        if p_unit == "Pa":
            converted_pressure = pressure
        elif p_unit == "atm":
            converted_pressure = (pressure / 101325)
        elif p_unit == "mmHg":
            converted_pressure = ((pressure * 760) / 101325)
        elif p_unit == "Bar":
            converted_pressure = (pressure / (10 ** 5))
        else:
            return "Enter valid units for pressure; [Pa, atm, mmHg, Bar]"
                                                
        #Temperature conversion
        if t_unit == "°C":
            converted_temperature = (temperature - 273)
        elif t_unit == "°F":
            converted_temperature = (((temperature - 273) * (9 / 5)) + 32)
        elif t_unit == "°R":
            converted_temperature = ((((temperature - 273) * (9 / 5)) + 32) + 460)
        else:
            return "Enter valid units for temperature; [°C, °F, °R]"
                    
        return (converted_pressure,converted_temperature)    
    except ValueError:
        return "pressure and temperature values must be integers or/and floats"
    except TypeError:
        return "pressure and temperature can not be less than zero\n(Absolute pressure can not be negative)\n(0K is the lowest possible temperature)"

properties = tuple(i for i in input("Enter the pressure and temperature separated by a single space: ").split())
units = tuple(i for i in input("Enter the units, for pressure and temperature respectively, separated by a single space: ").split())
print(intensive_properties(properties, units))    
