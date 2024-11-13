'''
Main for pydanfossair
'''
import argparse
from . import danfossclient
from .commands import UpdateCommand
from .commands import ReadCommand

def main():
    '''
    Main method
    '''
    parser = argparse.ArgumentParser("pydanfossair")
    parser.add_argument("--host", action="store", required=True)
    parser.add_argument("--command", action="store", required=False)

    args = parser.parse_args()

    client = danfossclient.DanfossClient(args.host)

    if args.command is not None:
        if args.command == "boost_on":
            print("Activate boost: {0}".format(client.command(UpdateCommand.boost_activate)))

        elif args.command == "boost_off":
            print("Activate boost: {0}".format(client.command(UpdateCommand.boost_deactivate)))

        elif args.command == "bypass_on":
            print("Activate bypass: {0}".format(client.command(UpdateCommand.bypass_activate)))

        elif args.command == "bypass_off":
            print("Activate bypass: {0}".format(client.command(UpdateCommand.bypass_deactivate)))

        elif args.command == "automatic_bypass_off":
            print("Automatic bypass: {0}"
                  .format(client.command(UpdateCommand.automatic_bypass_deactivate)))

        elif args.command == "automatic_bypass_on":
            print("Automatic bypass: {0}"
                  .format(client.command(UpdateCommand.automatic_bypass_activate)))

        elif args.command == "operation_mode_demand":
            client.command(UpdateCommand.operation_mode_demand)
            print("Operational mode set: {0}"
                  .format(client.command(ReadCommand.operation_mode)))

        elif args.command == "operation_mode_program":
            client.command(UpdateCommand.operation_mode_program)
            print("Operational mode set: {0}"
                  .format(client.command(ReadCommand.operation_mode)))

        elif args.command == "operation_mode_manual":
            client.command(UpdateCommand.operation_mode_manual)
            print("Operational mode set: {0}"
                  .format(client.command(ReadCommand.operation_mode)))

        elif args.command == "set_fan_step_1":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_1)
                print("Fan speed set to 10%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)


        elif args.command == "set_fan_step_2":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_2)
                print("Fan speed set to 20%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)
                    
        elif args.command == "set_fan_step_3":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_3)
                print("Fan speed set to 30%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_4":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_4)
                print("Fan speed set to 40%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_5":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_5)
                print("Fan speed set to 50%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_6":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_6)
                print("Fan speed set to 60%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_7":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_7)
                print("Fan speed set to 70%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_8":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_8)
                print("Fan speed set to 80%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_9":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_9)
                print("Fan speed set to 90%")
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)

        elif args.command == "set_fan_step_10":
            mode = client.command(ReadCommand.operation_mode)
            if mode == "manual":
                client.command(UpdateCommand.set_fan_step_10)
                print("Fan speed set to 100%")    
            elif mode != "manual":
                raise Exception("Operation mode must be to manual before setting fan speed. Current mode is: " + mode)
                
        else:
            raise Exception("Unknown comand: {0}".format(args.command))

    if args.command is None:
        result = client.read_all()
   
        for key, value in result.items():
            print("{0}: {1}".format(key, value))

if __name__ == "__main__":
    main()
