if __name__ == "__main__":
    import os, sys
    if 'SUMO_HOME' in os.environ:
        tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
        sys.path.append(tools)
    else:
        sys.exit("please declare environment variable 'SUMO_HOME'")


    import traci
    import traci.constants as tc

    GUI = False
    NET = "3x3grid"
    END = 100000

    sumoBinary = "sumo" + ("-gui" if GUI else "")

    traci.start([sumoBinary, "-c", "nets/{}/{}.sumocfg".format(NET,NET), "--start"])

    for step in range(END):
        print("#### STEP", step)
        print("## Num de Veiculos", traci.vehicle.getIDCount())
        traci.simulationStep()

    traci.close()