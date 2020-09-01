from periphery import I2C

name = "Name Undefined"
module = "Module Undefined"

# Flag Definitions
FLAGS_DOUBLE_V = 0x0001 # Double the V for one rail (ZCU111)
FLAGS_TPS53681 = 0x0002 # TPS53681 instead of INA226
FLAGS_CHANNEL  = 0x0004 # PMIC channel
FLAGS_6X_I     = 0x0008 # 6x the current for one rail (VCK190)

class poweradvantage:
    def __init__(self, name0, module0):
        ''' Constructor for this class '''
        name = name0
        module = module0


        # Create some members
        if name == "ZCU111":

            self.bus = [
                3,3,3,3,
                3,3,3,3,
                3,3,3,3,
                3,3]

            self.address = [
                0x40,0x45,0x46,0x49,
                0x4a,0x4b,0x4c,0x4d,
                0x4e,0x43,0x47,0x48,
                0x41,0x42]

            self.name = [
                "VCCINT","VADJ_FMC","MGTAVCC","VCCINT_AMS",
                "DAC_AVTT","DAC_AVCCAUX","ADC_AVCC","ADC_AVCCAUX",
                "DAC_AVCC","VCC1V2","MGT1V2","MGT1V8",
                "VCCPSINT","VCC1V8"]

            self.description = [
                "PL Core Rail",
                "Main FMC Rail",
                "Receiver and Transmitter Internal",
                "ADC and DAC Digital Logic",
                "DAC Termination",
                "Analog for the custom DAC block",
                "Digital for the custom ADC block",
                "Analog for the custom ADC block",
                "Digital for the custom DAC block",
                "DDR Termination",
                "GTH Termination Power",
                "GTH Power",
                "PS Core Rail",
                "Auxiliary Circuits"]

            self.domain = [
                "PL Domain","PL Domain","PL Domain","PL Domain",
                "PL Domain","PL Domain","PL Domain","PL Domain",
                "PL Domain","FPD","FPD","FPD",
                "LPD","LPD"]

            self.mOhm = [
                2,5,5,5,
                5,5,5,5,
                5,5,5,5,
                5,5]

            self.flags = [
                0x00,0x00,0x00,0x00,
                FLAGS_DOUBLE_V,0x00,0x00,0x00,
                0x00,0x00,0x00,0x00,
                0x00,0x00]

        elif name == "Tenzing":

            self.bus = [
#                8,
                8,8,8,
                5,8,8,8,8,
                6,8,5,
                6,
                6,8,
                6,8,8,8,8,
                8]

            self.address = [
#                0x4a,
                0x4b,0x4c,0x4d,
                0x60,0x46,0x47,0x48,0x49,
                0x43,0x40,0x60,
                0x45,
                0x44,0x44,
                0x42,0x42,0x43,0x45,0x41,
                0x4e]

            self.name = [
#                "VADJ_FMC",
                "MGTYAVCC","MGTYAVTT","MGTYVCCAUX",
                "VCCINT","VCC1V8","VCC3V3","VCC1V2","VCC1V1",
                "VCC_RAM","VCCAUX","VCC_IO_SOC",
                "VCC_PSFP",
                "VCC_PSLP","VCCO_502",
                "VCC_PMC","VCCO_500","VCCO_501","VCCO_503","VCCAUX_PMC",
                "VCC_BATT"]

            self.description = [
#                "FMC primary power supply",
                "GTY transceiver primary analog power supply",
                "GTY transceiver termination power supply",
                "GTY transceiver auxiliary analog (PLL) power supply",
                "PL and AIE primary power supply",
                "1.8V GPIO, UART, Sysctlr power supply",
                "3.3V PCIE, HDMI, HDIO power supply",
                "1.2V DDR4 termination supply",
                "1.1V LPDDR4 termination supply",
                "RAM and clocking network power supply",
                "Auxiliary power supply",
                "NOC and DDR controller primary power supply",
                "PS Full-power domain power supply",
                "PS Low-power domain power supply",
                "PS Low-power domain IO power supply",
                "PMC primary power supply",
                "PMC IO power supply",
                "PMC POR, Error, JTAG, Mode power supply",
                "PMC Sysmon, IO power supply",
                "PMC auxiliary power supply",
                "Battery-backed power domain supply"]

            self.domain = [
#                "FMC Domain",
                "Transceiver Domain","Transceiver Domain","Transceiver Domain",
                "PL Domain","PL Domain","PL Domain","PL Domain","PL Domain",
                "PL Domain","PL Domain","System Domain",
                "FPD",
                "LPD","LPD",
                "PMC Domain","PMC Domain","PMC Domain","PMC Domain","PMC Domain",
                "Battery Domain"]

            self.mOhm = [
#                5,
                1,1,5,
                1,5,5,1,5,
                5,5,1,
                5,
                5,5,
                5,5,5,5,5,
                10000]

            self.flags = [
#                0x00,
                0x00,0x00,0x00,
                FLAGS_TPS53681,0x00,0x00,0x00,0x00,
                0x00,0x00,FLAGS_TPS53681+FLAGS_CHANNEL,
                0x00,
                0x00,0x00,
                0x00,0x00,0x00,0x00,0x00,
                0x00]

        elif (name == "VCK190") or (name == "VMK180"):

            if module == "SC":

                self.bus = [
                    6,
                    6,6,6,
                    4,6,6,6,6,
                    4,6,4,
                    4,
                    4,
                    4,6,6]

            else:
                
                self.bus = [
                    5,
                    5,5,5,
                    3,5,5,5,5,
                    3,5,3,
                    3,
                    3,
                    3,5,5]

            self.address = [
                0x4a,
                0x4b,0x4c,0x4d,
                0x40,0x46,0x47,0x48,0x49,
                0x43,0x40,0x41,
                0x45,
                0x44,
                0x42,0x45,0x41]

            self.name = [
                "VADJ_FMC",
                "MGTYAVCC","MGTYAVTT","MGTYVCCAUX",
                "VCCINT","VCC1V8","VCC3V3","VCC1V2","VCC1V1",
                "VCC_RAM","VCCAUX","VCC_SOC",
                "VCC_PSFP",
                "VCC_PSLP",
                "VCC_PMC","VCCO_MIO","VCCAUX_PMC"]

            self.description = [
                "FMC primary power supply",
                "GTY transceiver primary analog power supply",
                "GTY transceiver termination power supply",
                "GTY transceiver auxiliary analog Quad PLL (QPLL) power supply",
                "PL and AIE primary power supply",
                "1.8V GPIO, UART, Sysctlr power supply",
                "3.3V PCIE, HDMI, HDIO power supply",
                "1.2V DDR4 termination supply",
                "1.1V LPDDR4 termination supply",
                "RAM and clocking network power supply",
                "Auxiliary power supply",
                "NOC and DDR controller primary power supply",
                "PS Full-power domain power supply",
                "PS Low-power domain power supply",
                "PMC primary power supply",
                "PMC and Low-power domain IO power supply",
                "PMC auxiliary power supply"]

            self.domain = [
                "FMC Domain",
                "Transceiver Domain","Transceiver Domain","Transceiver Domain",
                "PL Domain","PL Domain","PL Domain","PL Domain","PL Domain",
                "PL Domain","PL Domain","System Domain",
                "FPD",
                "LPD",
                "PMC Domain","PMC Domain","PMC Domain"]

            self.mOhm = [
                2,
                2,2,5,
                0.5,5,5,5,5,
                5,5,0.5,
                5,
                5,
                5,5,5]

            self.flags = [
                0x00,
                0x00,0x00,0x00,
                FLAGS_6X_I,0x00,0x00,0x00,0x00,
                0x00,0x00,0x00,
                0x00,
                0x00,
                0x00,0x00,0x00]

            
    def help(self):
        print()
        print("poweradvantage rev 0.02")
        print("-------------- --- ----")
        print("pa          = poweradvantage(<name>, <module>) # Initialization")
        print("                                               # Board Names: VCK190, VMK180")
        print("                                               # Modules: \"\" Main Module, SC System Controller")
        print("pa          = poweradvantage(\"VCK190\", \"\")     # Configure to be run on VCK190 Versal")
        print("pa          = poweradvantage(\"VCK190\", \"SC\")   # Configure to be run on VCK190 System Controller")
        print("name        = pa.getname()                     # Get power rail names")
        print("description = pa.getdescription()              # Get power rail descriptions")
        print("domain      = pa.getdomain()                   # Get power rail domains")
        print("power       = pa.getpower()                    # Get power rail Volts, Amps, Watts")
        print("              pa.printpower()                  # Print the power")
        print("power       = pa.printpower()                  # Print the power and get the power")
        print("              pa.help()                        # Print these instructions")
        print()

    def getname(self):
        return self.name

    def getdescription(self):
        return self.description

    def getdomain(self):
        return self.domain

    def linear11_to_float(self, data):
#        print("%04x" % data)
        exponent = (data & 0xf800) >> 11
        mantissa = data & 0x07ff
#        print("exponent=%04x mantissa=%04x" % (exponent, mantissa))
        if (exponent & 0x0010):
            exponent = 0x0020 - exponent
        if (mantissa & 0x0400):
            mantissa = 0x0800 - mantissa
        f = mantissa / 0x0400 * (2 ** exponent)
#        print("exponent=%04x mantissa=%04x float=%f" % (exponent, mantissa, f))
        return f

    def ina226x(self, bus, address, mOhms, flags):
        print(bus, address, mOhms, flags)

        INA226_SHUNT_VOLTAGE_ADDR = 0x01
        INA226_BUS_VOLTAGE_ADDR = 0x02

        # Open I2C mux to bus for INA226
        i2c = I2C(bus)

        # Read byte at address INA226_BUS_VOLTAGE_ADDR of INA226
        msgs = [I2C.Message([INA226_BUS_VOLTAGE_ADDR]), I2C.Message([0x00, 0x00], read=True)]
        i2c.transfer(address, msgs)
        vAdc = msgs[1].data[0] * 0x100 + msgs[1].data[1];
        print("%04x %02x %02x" % (vAdc, msgs[1].data[0], msgs[1].data[1]))
        
    def ina226(self, bus, address, mOhms, flags):

        INA226_SHUNT_VOLTAGE_ADDR = 0x01
        INA226_BUS_VOLTAGE_ADDR = 0x02

        # Open I2C mux to bus for INA226
        i2c = I2C(bus)

        # Read byte at address INA226_BUS_VOLTAGE_ADDR of INA226
        msgs = [I2C.Message([INA226_BUS_VOLTAGE_ADDR]), I2C.Message([0x00, 0x00], read=True)]
        i2c.transfer(address, msgs)
        vAdc = msgs[1].data[0] * 0x100 + msgs[1].data[1];
#        print("%04x %02x %02x" % (vAdc, msgs[1].data[0], msgs[1].data[1]))
        if flags & FLAGS_DOUBLE_V:
            vAdc = vAdc * 2
        
        # Read byte at address INA226_SHUNT_VOLTAGE_ADDR of INA226
        msgs = [I2C.Message([INA226_SHUNT_VOLTAGE_ADDR]), I2C.Message([0x00, 0x00], read=True)]
        i2c.transfer(address, msgs)
        vShuntAdc = msgs[1].data[0] * 0x100 + msgs[1].data[1];
#        print("%04x %02x %02x" % (vShuntAdc, msgs[1].data[0], msgs[1].data[1]))
        if vShuntAdc >= 0x8000:
            vShuntAdc = 0
    
        # Calculate v, i, p    
        v = vAdc * 5 / 4 / 1000
        i = vShuntAdc * 2500 / mOhms / 1000 / 1000
        if flags & FLAGS_6X_I:
            i = i * 6
        p = i / 200 * vAdc / 4

        i2c.close()

        return v, i, p

    def tps53681(self, bus, address, mOhms, flags):

        TPS53681_PAGE_ADDR = 0x00
        TPS53681_PHASE_ADDR = 0x04
        TPS53681_READ_VOUT_ADDR = 0x8b
        TPS53681_READ_IOUT_ADDR = 0x8c
        TPS53681_READ_TEMPERATURE_1_ADDR = 0x8d
        TPS53681_READ_POUT_ADDR = 0x96
        TPS53681_MFR_SPECIFIC_04_ADDR = 0xd4 # VOUT in linear format (mantissa and exponent) 
        
        # Open I2C mux to bus for INA226
        i2c = I2C(bus)

        # Save the original channel and sum of current on TPS53681
        msgs = [I2C.Message([TPS53681_PAGE_ADDR]), I2C.Message([0x00], read=True)]
        i2c.transfer(address, msgs)
        page0 = msgs[1].data[0]
        msgs = [I2C.Message([TPS53681_PHASE_ADDR]), I2C.Message([0x00], read=True)]
        i2c.transfer(address, msgs)
        phase0 = msgs[1].data[0]

        # Select the channel and sum of current on TPS53681
        if flags & FLAGS_CHANNEL:
            msgs = [I2C.Message([TPS53681_PAGE_ADDR]), I2C.Message([0x01])]
        else:
            msgs = [I2C.Message([TPS53681_PAGE_ADDR]), I2C.Message([0x00])]
        i2c.transfer(address, msgs)
        msgs = [I2C.Message([TPS53681_PHASE_ADDR]), I2C.Message([0x80])]
        i2c.transfer(address, msgs)
        
        # Read byte at address TPS53681_MFR_SPECIFIC_04_ADDR of TPS53681 (Voltage)
        msgs = [I2C.Message([TPS53681_MFR_SPECIFIC_04_ADDR]), I2C.Message([0x00, 0x00], read=True)]
        i2c.transfer(address, msgs)
        vAdc = msgs[1].data[1] * 0x100 + msgs[1].data[0];
#        print("%04x %02x %02x" % (vAdc, msgs[1].data[0], msgs[1].data[1]))
        
        # Read byte at address TPS53681_READ_IOUT_ADDR of TPS53681 (Current)
        msgs = [I2C.Message([TPS53681_READ_IOUT_ADDR]), I2C.Message([0x00, 0x00], read=True)]
        i2c.transfer(address, msgs)
        iAdc = msgs[1].data[1] * 0x100 + msgs[1].data[0];
#        print("%04x %02x %02x" % (vAdc, msgs[1].data[0], msgs[1].data[1]))
    
        # Restore the original channel and sum of current on TPS53681
        msgs = [I2C.Message([TPS53681_PAGE_ADDR]), I2C.Message([page0])]
        i2c.transfer(address, msgs)
        msgs = [I2C.Message([TPS53681_PHASE_ADDR]), I2C.Message([phase0])]
        i2c.transfer(address, msgs)
            
        # Calculate v, i, p    
        v = self.linear11_to_float(vAdc) / 1000
        i = self.linear11_to_float(iAdc) / 1000
        p = v * i
                
        i2c.close()

        return v, i, p

    def getpower(self):
        power = []
        for (b, a, m, f) in zip(self.bus, self.address, self.mOhm, self.flags):
            if f & FLAGS_TPS53681:
                v, i, p = self.tps53681("/dev/i2c-"+str(b), a, m, f)
            else:
                v, i, p = self.ina226("/dev/i2c-"+str(b), a, m, f)
            power.append([v, i, p])
        return power

    def printpower(self):
        power = self.getpower()
        domain = ""
        dtotal = 0
        total = 0
        print("%18s Volts   Amps   Watts" % "")
        for (n, d, p) in zip(self.name, self.domain, power):
            if (domain != "") and (d != domain):
                print("%18s ----- ------- %7.4f" % (domain, dtotal))
                dtotal = 0 
            domain = d
            print("%18s %5.3f %7.4f %7.4f" % (n, p[0], p[1], p[2]))
            dtotal += p[2]
            total += p[2]
        print("%18s ----- ------- %7.4f" % (domain, dtotal))
        print("%18s ----- ------- %7.4f" % ("Total", total))
        return power