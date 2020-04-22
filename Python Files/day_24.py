def intensive_properties(properties: tuple, units :tuple) -> tuple:
    """
    A function named intensive_properties which converts temperature and pressure to a desired unit.

    Parameter: --------
                properties: tuple
                            first element is the pressure in N/m2
                            second element is temperature  in Kelvin  
                units: tuple
                            first element is the unit we want to convert the pressure to, available pressure units are Pa,  atm,  mmHg and Bar 
                            second element is the unit we want to convert the temperature to, available temperature units are  oC, oF and oR.
    Returns ----------
            (converter_pres, converted_temp)
            converted_temp: the temperature in the desired unit
            converted_pres: the pressure in the desired unit.
    """    
    try:
        pres, temp = [float(i) for i in properties]
        if pres < 0 or temp < 0:
            raise TypeError
        p_unit, t_unit = units

        #Pressure conversion
        if p_unit == "Pa":
            converted_pres = pres
        elif p_unit == "atm":
            converted_pres = pres / 101325
        elif p_unit == "mmHg":
            converted_pres = (pres * 760) / 101325
        elif p_unit == "Bar":
            converted_pres = pres / (10 ** 5)
        else:
            return "Enter valid units for pressure; [Pa, atm, mmHg, Bar]"
                                                
        #Temperature conversion
        if t_unit == "°C":
            converted_temp = temp - 273
        elif t_unit == "°F":
            converted_temp = ((temp - 273) * (9 / 5)) + 32
        elif t_unit == "°R":
            converted_temp = (((temp - 273) * (9 / 5)) + 32) + 460
        else:
            return "Enter valid units for temperature; [°C, °F, °R]"
                    
        return converted_pres,converted_temp    
    except ValueError:
        return "pressure and temperature values must be integers or/and floats"
    except TypeError:
        return "pressure and temperature can not be less than zero\n(Absolute pressure can not be negative)\n(0K is the lowest possible temperature)"

properties = tuple(i for i in input("Enter the pressure and temperature separated by a single space: ").split())
units = tuple(i for i in input("Enter the units, for pressure and temperature respectively, separated by a single space: ").split())
print(intensive_properties(properties, units))    
