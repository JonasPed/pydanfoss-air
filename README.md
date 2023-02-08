# pydanfossair

Python module and client for Danfoss Air HRV systems.

## Usage

### Read all commands

    python -m pydanfossair --host IP_ADDRESS

### Send update command

    python -m pydanfossair --host IP_ADDRESS --command COMMAND

## Supported commands

- boost_on
- boost_off
- bypass_on
- bypass_off
- automatic_bypass_on
- automatic_bypass_off
- operation_mode_demand
- operation_mode_program
- operation_mode_manual
- set_fan_step_1
- set_fan_step_2
- set_fan_step_3
- set_fan_step_4
- set_fan_step_5
- set_fan_step_6
- set_fan_step_7
- set_fan_step_8
- set_fan_step_9
- set_fan_step_10
